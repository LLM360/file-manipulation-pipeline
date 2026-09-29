# Instantiate

Turns one (file, template) pair into a complete task package in two agent stages. In stage 1 an agent reads the file and the template and defines a design space: the ways a realistic task around this file could vary. A sampler picks one combination, and the agent writes a brief for it. In stage 2 a second agent writes the task itself: an email-style request, reference files, a rubric and the shape of the expected deliverable.

**Code:** `office_files_pipeline/instantiate_cycle.py::attempt_instantiate`. Prompts: `office_files_pipeline/prompts/instantiate_stage1.md`, `office_files_pipeline/prompts/instantiate_stage2.md`. Sampler: `office_files_pipeline/instantiate_static/cast.py::sample_cell`. Config: `office_files_pipeline/configs/instantiate/forge-mini.toml`.

## Setup

1. **Claim.** `POST /claim/instantiate` returns `template_id`, `classify_task_hash` and `instantiate_hash`.
2. **Pull.** `office_files_pipeline/instantiate_cycle.py::pull_source_files` fetches, in one rsync, the file from the dump folder and `annotation.md` from the classify folder into `_pulled/`.
3. **Stage inputs.** `office_files_pipeline/instantiate_cycle.py::prepare_stage_inputs` gives each stage its own folder with `inputs/` and `outputs/`. Inputs are copies, so a stage sees only what it is given:

| Input | Stage 1 | Stage 2 |
|---|---|---|
| `metatemplate.md` (the assigned template) | yes | yes |
| the source file, under its original name | yes | yes |
| manifold | `THE_REAL_WORK_MANIFOLD.md` | `THE_ARTIFACT_SHAPE_MANIFOLD.md` |
| other | `classify_annotation.md`, `cast.py` | stage 1's `design_brief.md` |

`inputs/.venv` links to the worker's environment, so agents can use the office libraries installed there (openpyxl, python-docx, python-pptx, pymupdf, pdfplumber, weasyprint and others). Stage prompts are filled in with `str.format`; stage 1 gets the task hash as `{task_hash}`.

## Stage 1: design

The agent writes `outputs/design_space.json`: named axes, each with a list of `values`, a `behavioral` flag and a one-line `rationale`. It then runs `uv run inputs/cast.py --seed <instantiate_hash> outputs/design_space.json`. `cast.py` rejects the space if its behavioral axes multiply out to fewer than 100 combinations and prints per-axis diagnostics. Otherwise it picks one value per axis, deterministically from the seed, and writes them as the YAML front matter of `outputs/design_brief.md`. The agent then writes the brief's prose (who the worker is, why the work is happening now, which parts of the file matter) and finishes with `outputs/.done`.

`office_files_pipeline/instantiate_cycle.py::validate_stage_outputs` requires `.done`, a parseable `design_space.json`, `design_brief.md`, and front matter identical to what `cast.sample_cell` returns for the same design space and seed. Because the worker re-runs the sampler itself, an agent can't hand-pick its combination.

## Stage 2: task package

The agent reads the brief, the template and the file, and writes to `outputs/`:
- `prompt.md`: the request as the worker would receive it, in a manager's voice;
- `reference_files/`: the source file or a modified copy, plus any other inputs the task needs;
- `modifications.md`: what was changed in the reference files, when the brief calls for it;
- `rubric.md`: weighted criteria a reviewer would check;
- `deliverable_shape.md`: the format and required content of the result;
- `completed_work/`: a reference solution, when the brief calls for one;
- `.done`.

Validation requires `.done`, `prompt.md`, `rubric.md`, `deliverable_shape.md` and a `reference_files/` directory, which may be empty.

## Push

`office_files_pipeline/instantiate_cycle.py::stage_final_and_push` assembles `instantiation.json`, both stages' outputs and both forge traces in `_final/` and pushes it in one rsync. Within one claim, the markers `.source_pulled`, `outputs/.done` (per stage) and `.pushed` let a retry skip what already succeeded; validation always runs again.

Shipped settings: 90 coroutines per worker, up to 3 attempts per item, 60 minutes for stage 1 and 70 for stage 2.
