# Classify

Assigns each downloaded file to zero or more of the 57 metatemplates, with a rationale for each, and writes a free-form annotation of what the file contains.

**Code:** `office_files_pipeline/classify_cycle.py::attempt_classify`. Prompt: `office_files_pipeline/prompts/classify_prompt.md`. Schema: `office_files_pipeline/schemas/assignments.schema.json`. Config: `office_files_pipeline/configs/classify/forge-mini.toml`.

1. **Claim.** `POST /claim/classify` returns a dump task hash.
2. **Pull.** `office_files_pipeline/classify_cycle.py::pull_source_dir` copies the dump folder without its metadata, so the agent's folder holds exactly `task.json` and the file.
3. **Prompt.** `office_files_pipeline/classify_cycle.py::build_prompt` fills in `{schema_json}`, `{templates_dir}` (the installed `metatemplates/task_types/`) and `{task_filename}` with `str.replace`. The prompt has the agent read `taxonomy_overview.md` first, shortlist templates, and only then read the shortlisted template files. Most of it is guidance on what counts as a reference input: a file qualifies when a worker doing one of the template's tasks would plausibly attach it, and long per-template notes settle recurring borderline cases.
4. **Agent.** It writes `assignments.json`, `annotation.md` and an empty `.done_classify`. If the file can't be read at all, it writes only `.no_file`.
5. **Validate.** `office_files_pipeline/classify_cycle.py::validate_classify` accepts `.no_file` as is. Otherwise it requires `.done_classify`, an `assignments.json` that parses and matches the schema, and `annotation.md`. Every `template_id` must name a real template; other spellings of a real one, such as a bare file name, are normalized to `task_types/<name>.md` (`office_files_pipeline/classify_cycle.py::_normalize_template_id`) and written back.
6. **Push.** `office_files_pipeline/classify_cycle.py::push_classify` sends `assignments.json` and then `annotation.md`, or only `.no_file`.

Shipped settings: 175 coroutines per worker, up to 10 attempts per item, one hour per agent run.
