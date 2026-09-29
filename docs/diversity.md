# Where diversity comes from

There is no direct way to measure how well the generated tasks cover real office work, so the pipeline controls where variation enters instead. Four mechanisms do this. Each one is cheap and mechanical, so an agent's own preferences can't collapse the distribution.

**Code:** `pipeline_coordinator/rebuild.py::_greedy_marginal_balance`, `office_files_pipeline/instantiate_static/cast.py::sample_cell`, `office_files_pipeline/rollout_static/draw.py::main`, `office_files_pipeline/rollout_cycle.py::_should_skip_stage1`

## 1. A balanced queue over templates and file types

Most input files are PDFs, and some templates match far more files than others. So the instantiate queue isn't first come, first served. `_greedy_marginal_balance` puts the (file type, template, file) items into buckets by (template, file type) and shuffles each bucket. It then repeatedly takes the next item from the bucket whose template and file type have been used least so far, with ties going to the rarer template. Any prefix of the queue is therefore close to even across templates and file types, and when a bucket runs dry the others fill in. The queue is rebuilt at startup and on `POST /rebuild/instantiate`.

## 2. The design space and `cast.py`

In instantiate stage 1 the agent doesn't choose the task directly. It writes a design space: the axes along which a realistic task around this file could differ. It marks each axis *behavioral* (neighbouring values change what the worker has to do) or *cosmetic* (they only change the surface). `cast.py`:
- rejects the space unless the behavioral axes multiply out to at least 100 combinations (`office_files_pipeline/instantiate_static/cast.py::BEHAVIORAL_FLOOR`), and prints per-axis diagnostics so the agent can revise;
- picks one value per axis with a random generator seeded from the task hash (`office_files_pipeline/instantiate_static/cast.py::_seed_to_int`), so the pick is reproducible.

The worker re-runs `cast.sample_cell` on the agent's design space and compares the result with the brief's front matter (`office_files_pipeline/instantiate_cycle.py::validate_stage_outputs`). An agent that swaps in a combination it likes better fails validation.

## 3. Rollout postures and `draw.py`

Before each rollout, a stage-1 agent writes several distinct styles of system prompt ("postures"), and `draw.py` picks one uniformly at random. This draw is deliberately unseeded: the agent can't predict the pick, so there is no gain in writing one favoured posture and several weak ones. A fixed 5% of tasks, chosen by hash, skip this step and keep the default prompt as a baseline arm. The byte-equality gate (`office_files_pipeline/rollout_cycle.py::_validate_byte_equality`) checks that the model saw the prompt that was written.

## 4. The manifolds as fixed anchors

Each instantiate stage reads a fixed manifold, the same for every task: stage 1 reads `THE_REAL_WORK_MANIFOLD.md`, on how real work varies and how to tell variation that changes the work from variation that only changes its surface. Stage 2 reads `THE_ARTIFACT_SHAPE_MANIFOLD.md`, on what real requests, rubrics and reference files look like. Both describe the target distribution in the abstract and offer no examples to copy. What varies from task to task is the source file, the template, stage 1's classify annotation and stage 2's design brief.
