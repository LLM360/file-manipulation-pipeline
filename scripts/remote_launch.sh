#!/usr/bin/env bash
# Worker VM bootstrap + launcher for the office-files-pipeline worker.
#
# Usage (as root on the worker VM, from a checkout of this repository):
#   bash -l scripts/remote_launch.sh
#
# Expects the step's rendered config at /root/ofpipe.toml (see
# docs/operations.md). Run it through a login shell (`bash -l`) so
# /etc/profile chains to ~/.profile and ~/.bashrc, where fnm's hook puts
# node/npm/fnm on PATH.
#
# Idempotent. Wipes process state (Phase 1) but preserves caches:
# /root/.cache/uv, /root/.local/share/fnm, /root/.npm, /root/.cache/cargo-forgecode.
# First run on a cold VM is slow (cargo build ~5-10 min); subsequent runs
# are seconds.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FORGECODE_REPO=https://github.com/llm360/forgecode.git
# Last fork commit whose trace format (one `context` event with top-level
# `messages`) matches rollout_cycle._validate_byte_equality.
FORGECODE_COMMIT=981e7ac35d31d03690156d76a3850f526e75a737
CARGO_TARGET_DIR=/root/.cache/cargo-forgecode

# ── Phase 1: wipe ────────────────────────────────────────────────────
# Kill any prior worker procs and free the reverse-tunnel listeners.
#
# CAUTION: the pkill patterns must NOT match this script's own argv
# (`bash -l <repo>/scripts/remote_launch.sh`). A broad pattern such as
# `[p]ipeline` would kill this script, because the repository path
# contains "pipeline". Patterns below target the actual worker
# entrypoints + agent processes only.
pkill -f 'office-files-pipeline'  || true
pkill -f 'pipeline-coordinator'   || true
pkill -x 'forge'                  || true
pkill -x 'cowbox'                 || true
fuser -k 8000/tcp 8100/tcp 8873/tcp || true
rm -f /root/*-failures.jsonl
rm -rf /tmp/sandbox_*
rm -rf /root/instantiate-output/task_*
rm -rf /root/rollout-output/task_*
rm -rf /root/download-output/task_*
rm -rf /root/classify-output/task_*
rm -rf /root/forgecode

# ── Phase 2: system (idempotent) ─────────────────────────────────────
apt-get update
apt-get install -y \
  build-essential cmake nasm perl pkg-config \
  protobuf-compiler libprotobuf-dev libsqlite3-dev libssl-dev \
  pandoc poppler-utils libreoffice-core-nogui \
  unzip
[[ -x "$HOME/.cargo/bin/cargo" ]] || \
  curl --proto "=https" --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
[[ -x "$HOME/.local/bin/uv" ]] || \
  curl -LsSf https://astral.sh/uv/install.sh | sh
if [[ ! -f /swapfile ]]; then
  fallocate -l 10G /swapfile && chmod 600 /swapfile && mkswap /swapfile
fi
swapon /swapfile 2>/dev/null || true

# ── Phase 2b: node 24 via fnm ────────────────────────────────────────
[[ -x "$HOME/.local/share/fnm/fnm" ]] || \
  curl -fsSL https://fnm.vercel.app/install | bash

# Re-source bashrc to pick up the fnm hook that `fnm install` just appended.
# On a fresh VM, the hook wasn't present when `bash -l` fired at script start.
# On warm VMs, this is a redundant no-op (fnm-hook is already in PATH).
# The `uv` install script also typically appends a `~/.local/bin` PATH
# export to bashrc; sourcing here picks that up too.
#
# We must temporarily relax `set -u` here: Ubuntu's default /root/.bashrc
# references `$debian_chroot` without first defaulting it, and strict
# unbound-var mode would crash the script. Restore strict mode after.
set +u
# shellcheck disable=SC1091
source /root/.bashrc
set -u

fnm install 24
fnm default 24

# Symlink stable paths for AGENT-SIDE discovery inside cowbox. NOT cowbox
# itself — it lives in the activated venv's bin/ on PATH.
# `readlink -f` resolves through fnm's per-shell tmpfs shim
# (/run/user/0/fnm_multishells/...) to the canonical
# /root/.local/share/fnm/node-versions/<v>/installation/bin/<bin> path.
ln -sf "$(readlink -f "$(which node)")"  /usr/local/bin/node
ln -sf "$(readlink -f "$(which npm)")"   /usr/local/bin/npm
ln -sf "$HOME/.local/bin/uv"             /usr/local/bin/uv

# ── Phase 3: forge build ─────────────────────────────────────────────
# Cargo target dir is preserved across launcher invocations so warm
# builds are seconds.
git clone "$FORGECODE_REPO" /root/forgecode
git -C /root/forgecode checkout --quiet "$FORGECODE_COMMIT"
(cd /root/forgecode && \
  CARGO_TARGET_DIR="$CARGO_TARGET_DIR" \
  CARGO_PROFILE_RELEASE_LTO=off \
  CARGO_PROFILE_RELEASE_CODEGEN_UNITS=16 \
  cargo build --release && \
  ln -sf "$CARGO_TARGET_DIR/release/forge" /usr/local/bin/forge)

# ── Phase 4: workspace sync ──────────────────────────────────────────
# Sync the workspace venv (cowbox + office libraries + office-files-pipeline
# + pipeline-coordinator). `--all-packages` is required: the workspace
# root has no project deps, so plain `uv sync` installs nothing.
cd "$REPO_DIR"
"$HOME/.local/bin/uv" sync --all-packages

# ── Phase 5: configure ───────────────────────────────────────────────
mkdir -p /root/forge /root/instantiate-output /root/rollout-output /root/download-output /root/classify-output
cat > /root/forge/.credentials.json <<EOF
[{"id":"openai_compatible","auth_details":{"api_key":"dummy"},"url_params":{"OPENAI_URL":"http://localhost:8000/v1"}}]
EOF

# ── Phase 6: launch ──────────────────────────────────────────────────
# Activate the workspace venv so `office-files-pipeline` is on PATH, and run
# from /root so ``ofpipe.toml`` resolves from cwd. The TOML's `step` field
# drives dispatch.
# shellcheck disable=SC1091
source "$REPO_DIR/.venv/bin/activate"
cd /root
nohup office-files-pipeline > /root/pipeline.log 2>&1 &
disown
