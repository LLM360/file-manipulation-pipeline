# Worked example: one file through every step

This folder follows one input file through the pipeline. It holds the text each step produced; binary files are listed by name only, and agent traces are not included.

**Source file:** `HumanAssociated.xlsx`, a blank sample-metadata template ("HumanAssociated") from the Genomics Standards Consortium's MIxS repository, licensed CC0-1.0:
https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs/b0b1e03b705cb432d08914c686ea820985b9cb20/mixs-templates/extensions_only/HumanAssociated.xlsx
It is the `xlsx` row of [`../input_rows.csv`](../input_rows.csv).

| Step | Task hash | Files here |
|---|---|---|
| download, classify | `52d452206a917e7b817f` | `classify/assignments.json`, `classify/annotation.md` |
| instantiate | `0cd8c4dec8746ffb290a` | `instantiate/stage1/`, `instantiate/stage2/` |
| rollout | `0cd8c4dec8746ffb290a` | `rollout/` |

**Classify** assigned one template, `task_types/b5_protocol_driven_data_entry.md` (data entry with protocol-driven decisions), and described the file in `annotation.md`.

**Instantiate, stage 1.** The agent wrote the design space in `design_space.json`. `cast.py` picked one value per axis into the front matter of `design_brief.md`, and the agent wrote the brief's prose below it.

**Instantiate, stage 2.** The agent wrote the task. `prompt.md` asks a lab manager to fill in the template for a batch of specimens from three sources that don't fully agree, `rubric.md` lists what a reviewer would check, `deliverable_shape.md` describes the expected workbook and notes, and `modifications.md` explains that the blank template was used unchanged. It also produced these binary files, not included here:
- reference files: `MIxS_HumanAssociated_blank.xlsx`, `clinical_chart_deid_batch-HA047_2024-10-14.pdf`, `genotyping_report_batch-HA-2024-047.pdf`, `sample_collection_log_2024-11.xlsx`
- completed work: `HA-2024-047_MIxS_HumanAssociated_populated.xlsx`, `field_mapping_notes_HA047.md`

**Rollout, stage 1.** The agent wrote several system-prompt styles in `postures.json`, `draw.py` picked the one in `posture.txt`, and the agent wrote `system_prompt.md` in that style.

**Rollout, stage 2.** Another agent did the task with that system prompt and delivered `HA-2024-047_MIxS_HumanAssociated.xlsx` and `field_mapping_notes_HA047.md` (not included).

Every person, organization and record in the task is fictional; the agents made them up.
