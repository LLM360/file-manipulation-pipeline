# Operations

How we ran the pipeline: one coordinator, an OpenAI-compatible model endpoint, and a fleet of worker VMs, each fleet working on one step at a time. None of this is packaged for general use; read it as a description of a setup that worked.

**Code:** `pipeline_coordinator/config.py::CoordinatorConfig`, `office_files_pipeline/config.py::load_config_from_toml`, `scripts/remote_launch.sh`

## Input

The coordinator reads one parquet file with one row per candidate file. The code needs three columns:

| Column | Used for |
|---|---|
| `raw_url` | the URL the download agent fetches, and every task hash (`sha256(raw_url)[:20]`) |
| `file_path` | the name the downloaded file is saved under (its last path component) |
| `file_ext` | balancing the instantiate queue across file types |

Each row is copied whole into `task.json`, so any extra columns (repository, commit, how the file was found) reach the classify agent as context. `examples/input_rows.csv` shows seven rows with the columns we used.

## Coordinator

```
uv sync --all-packages
uv run pipeline-coordinator \
  --repo-root <folder for .state/ and logs/> \
  --parquet-path <input.parquet> \
  --base-dir <artifact tree root> \
  [--router-url http://<model host>:<port>] \
  [--http-host 0.0.0.0] [--http-port 8100] [--rsync-daemon-port 8873]
```

Run it on the host that holds the artifact tree: it scans the tree with `find` and serves it with `rsync --daemon` on 127.0.0.1. It also needs passwordless SSH as root to the workers. Registering a worker (`curl -X POST http://<coordinator>:8100/workers -H 'content-type: application/json' -d '{"ip": "<worker ip>"}'`) makes the coordinator start `autossh` with reverse forwards for ports 8100 and 8873, and 8000 when `--router-url` is set. After changing the tree by hand, `POST /rebuild/<step>` recomputes that step's queue.

## Workers

Each worker VM runs one step. On each VM, as root:

1. Clone this repository.
2. Render the step's config and install it as `/root/ofpipe.toml`. The `cmd` templates contain a `${MODEL_ID}` placeholder that the worker does not fill in: expanding an unrendered template raises `KeyError`. Substitute the model name the endpoint serves (`curl <endpoint>/v1/models` lists it):
   ```
   MODEL_ID=<served model id> envsubst '${MODEL_ID}' \
     < office-files-pipeline/office_files_pipeline/configs/<step>/forge-mini.toml > /root/ofpipe.toml
   ```
   Any field can also be overridden with an `OFPIPE_`-prefixed environment variable, for example `OFPIPE_CONCURRENCY=50`.
3. Run `bash -l scripts/remote_launch.sh`. It installs system packages (LibreOffice, pandoc, poppler, build tools), Rust, uv and Node 24; builds forge at the pinned commit; runs `uv sync --all-packages`; writes forge's provider settings (an OpenAI-compatible provider at `http://localhost:8000/v1` with a placeholder key); and starts `office-files-pipeline` from `/root` in the background. The log goes to `/root/pipeline.log` and one line per failed attempt to `/root/pipeline-failures.jsonl`.
4. Register the VM with the coordinator (`POST /workers`, above).

A worker reaches the coordinator, the rsync daemon and the model only through the tunnels: `127.0.0.1:8100`, `127.0.0.1:8873` and `localhost:8000`.

## The forge build

The agent CLI is our fork of forgecode, [github.com/llm360/forgecode](https://github.com/llm360/forgecode), pinned at commit `981e7ac35d31d03690156d76a3850f526e75a737`. The pipeline relies on four features of the fork:

| Feature | Used for |
|---|---|
| `FORGE_TRACE_FILE` | a JSONL trace of each run: the instantiate traces and the rollout trace |
| merged system messages for OpenAI-compatible providers | exactly one system message in each model request |
| `FORGE_SYSTEM_PROMPT_FILE` | running rollout stage 2 with the stage-1 prompt |
| `forge prompt render` | printing the default system prompt without calling a model |

At the pinned commit, the trace holds one `context` event, written on the first turn, with the messages exactly as sent to the model. `office_files_pipeline/rollout_cycle.py::_validate_byte_equality` reads that event. Later commits on the fork replaced it with a per-turn `request` event that nests the messages under `body`, which the check doesn't read; that is why the build is pinned.

cowbox comes from [github.com/LLM360/cowbox](https://github.com/LLM360/cowbox) as a Python dependency, pinned at commit `a032d7f683bbddf4809ac257d9d4dac5c931e01a` in `office-files-pipeline/pyproject.toml`.
