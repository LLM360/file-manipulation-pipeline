# Architecture

One coordinator hands out work and many worker VMs do it. Every unit of work has the same shape: run one agent in a sandbox on one item, check what it wrote, and push the result into a shared folder tree. The folder tree, not a database, is the record of what is done.

**Code:** `pipeline_coordinator/__main__.py::main`, `pipeline_coordinator/api.py::create_app`, `pipeline_coordinator/reconciler.py::TunnelReconciler`, `office_files_pipeline/cli.py::run_pipeline`, `office_files_pipeline/expand.py::expand_cmd`

## Coordinator

The coordinator runs on the host that holds the artifact tree. At startup it reads the input parquet once and scans the tree to work out, for each step, which items are ready and not yet done (`pipeline_coordinator/rebuild.py::rebuild_download` and its siblings; the rules are in [artifacts.md](artifacts.md)). Only then does it open its HTTP port.

| Endpoint | Returns |
|---|---|
| `POST /claim/download` | `{"task": {"idx", "row"}}`: one input row |
| `POST /claim/classify` | `{"task": {"task_hash"}}`: one downloaded file |
| `POST /claim/instantiate` | `{"task": {"template_id", "classify_task_hash", "instantiate_hash"}}`: the next (file, template) pair from the balanced queue |
| `POST /claim/rollout` | `{"task": {"instantiate_hash"}}`: one finished task package |
| `POST /rebuild/{step}` | rescans the tree for one step, replaces its queue and returns the queue size |
| `POST /workers` | registers a worker IP and opens the tunnels to it |
| `GET /health` | liveness |

An empty queue returns `{"task": null}`. Claims are not leased: an item that is claimed but never finished stays unfinished in the tree, so the next rebuild queues it again. Instantiate and rollout claims also skip items whose output folder already exists.

The coordinator also runs an rsync daemon: module `artifacts`, rooted at `--base-dir`, listening on 127.0.0.1 (`pipeline_coordinator/__main__.py::_generate_rsyncd_conf`). Workers reach it and the HTTP API only through SSH tunnels. When a worker registers, `TunnelReconciler` keeps an `autossh -R …` session open to `root@<worker>`, so that on the worker:

- `127.0.0.1:8100` is the coordinator's HTTP API;
- `127.0.0.1:8873` is the rsync daemon;
- `localhost:8000` is the model endpoint, if the coordinator was started with `--router-url`.

## Worker

A worker VM runs one process, `office-files-pipeline` (`office_files_pipeline/cli.py::main`), for one step. It reads `./ofpipe.toml`, and the `step` field picks the config class and the entry point (`office_files_pipeline/config.py::load_config_from_toml`):

| `step` | Config class | Entry point |
|---|---|---|
| `download` | `DownloadConfig` | `office_files_pipeline/download_cycle.py::run_download` |
| `classify` | `ClassifyConfig` | `office_files_pipeline/classify_cycle.py::run_classify` |
| `instantiate` | `InstantiateConfig` | `office_files_pipeline/instantiate_cycle.py::run_instantiate` |
| `rollout` | `RolloutConfig` | `office_files_pipeline/rollout_cycle.py::run_rollout` |

Each entry point runs a few local checks, empties its `output_dir` and starts `concurrency` coroutines. Every coroutine loops forever. It claims an item, sleeping 1–60 s when the queue is empty or the coordinator can't be reached, then makes attempts until one succeeds or `max_retries` is reached. An attempt is pull → run the agent → validate → push. Any exception ends the attempt and appends one JSON line, with the full error output, to `failure_log_path` (`office_files_pipeline/failures.py::dump_failure`); the next attempt starts after a random 1–180 s wait (`office_files_pipeline/retry.py::retry_with`). Outputs are pushed only after they pass validation, and each step pushes its completion marker last.

## Agents: forge inside cowbox

Each stage's agent starts from a shell-command template, the `cmd` field of the step's TOML. The worker fills in `{work_dir}`, `{stage_dir}`, `{output_dir}` and `{prompt}`, shell-quoted, with `office_files_pipeline/expand.py::expand_cmd`, and runs the result. A typical template:

```
env FORGE_SESSION__PROVIDER_ID=openai_compatible \
    FORGE_SESSION__MODEL_ID=${MODEL_ID} \
    FORGE_SESSION__PROVIDER__URL=http://localhost:8000/v1 \
cowbox --hide {output_dir} --rw {stage_dir} --rw /root/.cache/uv --rw /root/.npm --rw /root/forge -- \
  forge -C {stage_dir} -p {prompt}
```

- **forge** is the agent CLI: our fork of forgecode, talking to the model through an OpenAI-compatible API. [operations.md](operations.md) gives the pinned build and the fork features the pipeline relies on.
- **cowbox** ([github.com/LLM360/cowbox](https://github.com/LLM360/cowbox)) sandboxes each run. The agent can read the machine, but `--hide {output_dir}` hides every task's working folder, and each `--rw` makes one path writable: this task's folders and the package caches. An agent can install whatever it needs, but it can't see or change other tasks.
- **The model** is any OpenAI-compatible server. `${MODEL_ID}` is filled in when the config is deployed; see [operations.md](operations.md).
