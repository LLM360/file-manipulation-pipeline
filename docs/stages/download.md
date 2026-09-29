# Download

Fetches the file behind each input row. An agent downloads the file the row names, or declares it unusable; the worker checks which of the two the agent reported and pushes the folder into the dump tree.

**Code:** `office_files_pipeline/download_cycle.py::attempt_download`. Prompt: `office_files_pipeline/prompts/download_prompt.md`. Config: `office_files_pipeline/configs/download/forge-mini.toml`.

1. **Claim.** `POST /claim/download` returns a row index and the full row.
2. **Prepare.** `office_files_pipeline/download_cycle.py::prepare_download` creates the task folder and writes the row to `task.json`; classify later reads `file_path` from it.
3. **Prompt.** `office_files_pipeline/download_cycle.py::build_prompt` fills in `{raw_url}`, `{file_path}` and `{max_size_mb}` (100) with `str.replace`, so any other braces in the prompt are left alone.
4. **Agent.** It saves the file under its original name at the top of its folder and writes `.done` containing the file's absolute path. If the file is over the size limit or can't be fetched, it writes only `.no_file`.
5. **Validate.** `office_files_pipeline/download_cycle.py::validate_download` accepts `.no_file` on its own, or `.done` next to at least one real file. Both markers, neither marker, or `.done` without a file make the attempt invalid; it is retried from an empty folder.
6. **Push.** `office_files_pipeline/download_cycle.py::push_download` copies the whole folder to `office-files-dump/<shard>/task_<hash>/`.

Shipped settings: 175 coroutines per worker, up to 10 attempts per item, one hour per agent run.
