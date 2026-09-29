# Metatemplates and manifolds

A metatemplate describes one pattern of professional office work: who does it, what they receive, what they produce, and how the task can be made harder. There are 57, grouped into 11 categories. Classify decides which templates fit a file; instantiate builds a task from one template and one file.

**Code:** `office_files_pipeline/classify_cycle.py::KNOWN_TEMPLATE_IDS`, `office_files_pipeline/instantiate_cycle.py::prepare_stage_inputs`. Files: `office_files_pipeline/metatemplates/`, `office_files_pipeline/instantiate_static/`.

## Taxonomy

| Category | Patterns |
|---|---|
| A. Financial Analysis & Modeling | A1–A6 |
| B. Data-Driven Document Authoring | B1–B5 |
| C. Policy, Procedure & Standards Authoring | C1–C5 |
| D. Strategic & Advisory Document Authoring | D1–D6 |
| E. Research-to-Document Tasks | E1–E6 |
| F. Client Communication & Outreach Materials | F1–F5 |
| G. Form-Based & Clinical Documentation | G1–G5 |
| H. Creative & Media Production | H1–H7 |
| I. Investigation & Security Reports | I1–I2 |
| J. Software & Technical Implementation | J1–J6 |
| K. Scheduling, Space Planning & Logistics | K1–K4 |

`metatemplates/taxonomy_overview.md` summarizes every pattern (roles, inputs, outputs, complexity signals) and adds statistics across the whole set. Each pattern has one file in `metatemplates/task_types/`, named `<id>_<slug>.md`, for example `a1_audit_sampling.md`. Its path relative to `metatemplates/`, `task_types/a1_audit_sampling.md`, is the `template_id` used everywhere else, so the file names are stable identifiers.

## Template format

Each template has a title, its **Macro Category** and **Pattern ID**, and seven sections:

1. **Pattern Description**: the work, the worker and what triggers it.
2. **O\*NET Grounding**: the occupations that do this work.
3. **Prompt Construction Template**: persona, scenario, instruction patterns, where constraints go, and a skeleton request.
4. **Reference File Requirements**: what inputs the task needs, including a "File Types Needed" list.
5. **Output Specification**: what the deliverable looks like and what a strong one gets right.
6. **Complexity Knobs**: a table of knobs with Easy, Medium and Hard settings.
7. **Boundary Cases & Adjacent Patterns**: how to tell this pattern from its neighbours.

## Who reads what

| Reader | Reads | For |
|---|---|---|
| classify agent | `taxonomy_overview.md`, then the shortlisted templates | matching the file against §4, Reference File Requirements |
| instantiate stage 1 | the assigned template (`inputs/metatemplate.md`) | axes for the design space, notably §6, Complexity Knobs |
| instantiate stage 2 | the same template | the request, reference files and deliverable shape (§3–§5) |

## Manifolds

`office_files_pipeline/instantiate_static/THE_REAL_WORK_MANIFOLD.md`, read in instantiate stage 1, describes how real professional work varies and how to tell variation that changes the work from variation that only changes its wording. `office_files_pipeline/instantiate_static/THE_ARTIFACT_SHAPE_MANIFOLD.md`, read in stage 2, describes how real requests, rubrics, reference files and finished work tend to look. Both are descriptive and abstract, with no examples to copy.

## Provenance

The taxonomy and metatemplates were derived from the public GDPval tasks; the released templates omit per-task sample IDs and task-level examples. The manifold documents summarize population-level observations.
