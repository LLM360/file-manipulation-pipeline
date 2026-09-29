# Documentation

Start here. Each document opens with a short summary and a **Code:** line that points at the relevant modules.

- [architecture.md](architecture.md): the coordinator, the workers, the sandbox, the agent CLI and the model endpoint, and how they connect.
- [artifacts.md](artifacts.md): the on-disk contract. Folder layout, hash rules, marker files, what each step pulls and pushes, and when an item is eligible.
- [stages/download.md](stages/download.md): fetching the file for each input row.
- [stages/classify.md](stages/classify.md): assigning each file to zero or more metatemplates.
- [stages/instantiate.md](stages/instantiate.md): designing (stage 1) and writing (stage 2) a task for one file and one template.
- [stages/rollout.md](stages/rollout.md): rewriting the system prompt (stage 1) and doing the task (stage 2).
- [diversity.md](diversity.md): the mechanisms that spread tasks across patterns, file types and styles.
- [metatemplates.md](metatemplates.md): the taxonomy, the template format, which step reads which section, and where the templates came from.
- [operations.md](operations.md): how we ran it. Coordinator flags, the input format, worker setup, config rendering and the pinned forge build.

Code pointers name a module and a function or class, for example `office_files_pipeline/rollout_cycle.py::validate_rollout`. Paths starting `pipeline_coordinator/` live under `pipeline-coordinator/`, and paths starting `office_files_pipeline/` under `office-files-pipeline/`.
