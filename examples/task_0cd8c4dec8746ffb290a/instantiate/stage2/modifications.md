# Modifications record — Batch HA-2024-047

**Source file:** `inputs/HumanAssociated.xlsx` (GSC MIxS HumanAssociated v6.0 blank template)
**Reference file shipped to runner:** `reference_files/MIxS_HumanAssociated_blank.xlsx`
**Gold file:** `completed_work/HA-2024-047_MIxS_HumanAssociated_populated.xlsx`

## Modification description

No artificial modifications were applied to the source file. The upstream team delivered the GSC MIxS `HumanAssociated` blank template exactly as received from the Genomics Standards Consortium: a single-sheet workbook (`HumanAssociated`) containing only the header row (53 columns, `samp_name` through `misc_param`) and zero data rows. The template retains its original Excel data-validation dropdowns on columns `urine_collect_meth` (`catheter` / `clean catch`) and `oxy_stat_samp` (`aerobic` / `anaerobic` / `other`). No cells were blanked, removed, or scrambled; the workbook was delivered in its native blank state.

## What the runner must do

The runner's task is to populate rows 2–16 with 15 sample records by cross-referencing the three source documents and applying the decision logic described in `prompt.md`. The blank template is therefore the natural starting point for a template-fill task rather than a manually modified one.

## Auditable diff

Because the reference file is the unmodified source, the diff between `inputs/HumanAssociated.xlsx` and `reference_files/MIxS_HumanAssociated_blank.xlsx` is empty. The substantive transformation is the population of 15 data rows, which is captured in the gold file and graded by the rubric.
