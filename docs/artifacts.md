# Artifacts

The steps talk to each other only through one folder tree: the coordinator's `--base-dir`, served over rsync as the module `artifacts`. Each task is a folder `<tree>/<shard>/task_<hash>/`, where `<shard>` is the first three hex characters of the hash. Marker files record what is done, and the coordinator rebuilds every queue from them.

**Code:** `pipeline_coordinator/rebuild.py::rebuild_download`, `pipeline_coordinator/rebuild.py::rebuild_classify`, `pipeline_coordinator/rebuild.py::rebuild_instantiate`, `pipeline_coordinator/rebuild.py::rebuild_rollout`, `office_files_pipeline/download_cycle.py::push_download`, `office_files_pipeline/classify_cycle.py::push_classify`, `office_files_pipeline/instantiate_cycle.py::stage_final_and_push`, `office_files_pipeline/rollout_cycle.py::push_rollout`

## Trees and hashes

| Tree | Written by | Task hash |
|---|---|---|
| `office-files-dump/` | download | `sha256(raw_url)[:20]` (`pipeline_coordinator/rebuild.py::_row_task_hash`) |
| `office-files-classify/` | classify | the dump folder's hash |
| `office-files-instantiate/` | instantiate | `sha256(template_id + ":" + classify_hash)[:20]` (`pipeline_coordinator/rebuild.py::instantiate_hash_for`) |
| `office-files-rollout/` | rollout | the instantiate folder's hash |

A `template_id` is a template's path relative to `metatemplates/`, for example `task_types/a1_audit_sampling.md`. A file assigned three templates gets three instantiate folders.

## What each step writes

**download:** `office-files-dump/<shard>/task_<hash>/`
- `task.json`: the full input row, written by the worker before the agent runs.
- The downloaded file under its original name, plus `.done` holding the file's absolute path.
- Or, instead of both: `.no_file`, meaning the file was too large, gone, or couldn't be fetched.

The whole folder is pushed in one rsync.

**classify:** `office-files-classify/<shard>/task_<hash>/`
- `assignments.json`: `{"assignments": [{"template_id": …, "rationale": …}, …]}`, checked against `office_files_pipeline/schemas/assignments.schema.json`. The list may be empty.
- `annotation.md`: free-form notes on what the file contains.
- Or only `.no_file`, when the file couldn't be read at all.

`assignments.json` is pushed first and `annotation.md` last, so a scan never mistakes a half-finished push for a result. The agent's own `.done_classify` marker stays on the worker.

**instantiate:** `office-files-instantiate/<shard>/task_<hash>/`
- `instantiation.json`: the task hash, the template id, the classify hash, the source file's path in the dump tree, and a fingerprint of the stage commands.
- `stage1/`: `design_space.json`, `design_brief.md`, `.done`.
- `stage2/`: `prompt.md`, `rubric.md`, `deliverable_shape.md`, `reference_files/`, optionally `modifications.md` and `completed_work/`, and `.done`.
- `trace_stage1.jsonl`, `trace_stage2.jsonl`: forge traces of the two agent runs.

The worker assembles all of this in a local `_final/` folder and pushes it in one rsync. On the worker, the markers `.source_pulled` and `.pushed` let a retry skip work that already succeeded.

**rollout:** `office-files-rollout/<shard>/task_<hash>/`, pushed in this order:
1. `trace.jsonl`: the forge trace of the run.
2. `deliveries/`: what the agent produced, minus cache folders and files over 100 MB.
3. `system_prompt.md`: the system prompt the agent ran with.
4. `postures.json` and `posture.txt`: only when the system prompt was rewritten.
5. `rollout.json`: start time, duration, attempt count and `stage1_skipped`.
6. `.done`: last, so its presence means everything above is there.

## When an item is queued

| Step | Queued when |
|---|---|
| download | the row's dump folder has neither `.done` with a file nor `.no_file` |
| classify | the dump folder has `.done` and a file, and the classify folder is not finished (finished means `assignments.json` and `annotation.md`, or `.no_file`) |
| instantiate | a finished classify folder lists the template and the dump folder has the file; the claim skips it if the instantiate folder exists |
| rollout | the instantiate folder has `stage2/.done` and there is no rollout folder |

Download and classify redo any item whose folder is incomplete. Instantiate and rollout skip an item once its output folder exists at all, so an item whose push died halfway is not retried; the missing `stage2/.done` or `.done` keeps it out of later steps and away from consumers.
