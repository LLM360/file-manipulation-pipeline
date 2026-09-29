# Rollout

Has an agent carry out a finished task in a sandbox and records its trace. First, another agent rewrites the agent's default system prompt in a randomly drawn style, so the recorded runs don't all share one system prompt.

**Code:** `office_files_pipeline/rollout_cycle.py::attempt_rollout`. Prompt for stage 1: `office_files_pipeline/prompts/rollout_prompt_customize.md`. Assets: `office_files_pipeline/rollout_static/AGENTS.md`, `office_files_pipeline/rollout_static/draw.py`. Config: `office_files_pipeline/configs/rollout/forge-mini.toml`.

## Setup

1. **Claim.** `POST /claim/rollout` returns an `instantiate_hash`.
2. **Prepare.** `office_files_pipeline/rollout_cycle.py::prepare_rollout` starts every attempt from an empty task folder:
   - `work/`: the agent's working folder, with `reference_files/` (pulled from the instantiate task and made read-only), an empty `deliveries/`, and `AGENTS.md`, which forge adds to the system prompt;
   - `rollout_stage2_prompt.md`: the instantiate task's `prompt.md` plus a one-line pointer to `AGENTS.md`;
   - `prompt_customize/`: stage 1's folder, with `draw.py`;
   - `prompt_customize/system_prompt_original.md`: forge's default system prompt for `work/`, printed by `forge prompt render` without calling a model (`office_files_pipeline/rollout_cycle.py::render_system_prompt`; this command runs outside the sandbox).

## Two arms

`office_files_pipeline/rollout_cycle.py::_should_skip_stage1` maps the first 32 bits of the task hash to [0, 1) and skips stage 1 when the value is below `skip_stage1_prob` (0.05). The baseline arm is therefore fixed by the hash: those tasks run with forge's default prompt, copied to `system_prompt.md` unchanged.

## Stage 1: system prompt

The agent reads the original prompt and writes `postures.json`: distinct styles ("postures") in which an organization might write such a prompt. The prompt asks for at least five; `draw.py` rejects fewer than three. It runs `uv run draw.py postures.json`, which picks one uniformly at random into `posture.txt`. It then writes `system_prompt.md` in that posture, keeping the operational facts of the environment, and finishes with `.done`.

`office_files_pipeline/rollout_cycle.py::validate_stage1_basic` requires a non-empty `system_prompt.md` and `.done`. In the modify arm, `office_files_pipeline/rollout_cycle.py::validate_stage1_tool_use` also requires `postures.json` and `posture.txt`, so an agent can't skip the draw.

## Stage 2: the run

forge runs in `work/` with `FORGE_SYSTEM_PROMPT_FILE` pointing at `system_prompt.md` and `FORGE_TRACE_FILE` recording the session. The agent must put its results in `deliveries/` and create `.done`.

`office_files_pipeline/rollout_cycle.py::validate_rollout` requires `.done` and at least one file in `deliveries/` outside cache folders. It then applies the byte-equality gate (`office_files_pipeline/rollout_cycle.py::_validate_byte_equality`): the SHA-256 of `system_prompt.md` must equal the SHA-256 of the single system message in the trace's `context` event. That proves the model saw exactly the prompt stage 1 wrote.

## Push

`office_files_pipeline/rollout_cycle.py::push_rollout` sends, in order: `trace.jsonl`, `deliveries/`, `system_prompt.md`, `postures.json` and `posture.txt` (modify arm only), `rollout.json`, and `.done` last.

Shipped settings: 125 coroutines per worker, up to 3 attempts per item, 60 minutes for stage 1 and 90 for stage 2.
