# Deliverable shape — Batch HA-2024-047 MIxS curation

## Primary deliverable
**Format:** Excel workbook (.xlsx), single sheet named `HumanAssociated`
**Required filename:** `HA-2024-047_MIxS_HumanAssociated.xlsx`

### Sheet structure
- Row 1: the existing 53-column MIxS header row (`samp_name` through `misc_param`). Must remain unchanged.
- Rows 2–16: one data row per sample (H-047-01 through H-047-15, in ascending order).
- No additional sheets, no renamed tabs, no inserted summary rows above the header.

### Mandatory-field coverage
Every row must contain non-blank values for the MIxS HumanAssociated mandatory set:
- `samp_name`
- `project_name`
- `host_subject_id`
- `host_age`
- `host_sex`
- `host_body_site`
- `host_body_product`
- `temp`
- `samp_store_temp`
- `samp_store_dur`
- `host_disease_stat`

### Absence-vocabulary discipline
Where a field was not collected by the study, the cell must contain `not collected`. Where a field is biologically inapplicable to the general adult cohort (the four pregnancy-related columns), the cell must contain `not applicable`. Blanks are not acceptable anywhere in the data rows; they will be rejected by downstream NCBI validation. The only legitimate blank cells are those beyond row 16 or outside column BA.

### Data-validation compliance
Two columns carry baked-in Excel dropdowns in the template:
- `urine_collect_meth` (column AP) — valid values: `catheter`, `clean catch`
- `oxy_stat_samp` (column AS) — valid values: `aerobic`, `anaerobic`, `other`

The worker must enter values that match these lists exactly (lower case, single space). For non-urine samples, `urine_collect_meth` must still be set to `not applicable` even though the dropdown does not offer it; this is an accepted override per MIxS curation protocol.

### Derived-field requirements
- `host_body_mass_index`: computed from `host_tot_mass` (kg) and `host_height` (cm) using standard BMI formula, rounded to one decimal place. The chart-recorded BMI must be treated as a cross-check, not a primary source, when log biometrics are present.
- `temp`: expressed in Celsius. Where the genotyping report provides Fahrenheit, the worker must convert using the standard formula and round to one decimal. Where sources conflict, the worker must apply the resolution rationale given in the prompt.

### Ontology mapping
`host_body_site` and `host_body_product` must reflect ENVO/UBERON-aligned terms derived from the technician shorthand and genotyping report abbreviations, not the raw abbreviations themselves.

### Cross-row consistency
- `samp_name` must follow the exact pattern `H-047-NN` (zero-padded).
- `host_subject_id` must use the `MORRIS-047-NN` hash from the clinical chart, not the `PID-HA47-NN` hash from the collection log.
- `project_name` must be `MORRIS-1` for all rows.
- Dates, numeric values, and spelled entity names must be internally consistent with the source documents and with the field-mapping readme.

## Secondary deliverable
**Format:** Markdown file
**Required filename:** `field_mapping_notes_HA047.md`

### Required sections
1. **Source hierarchy** — a brief statement of which source document is primary for which category of data.
2. **Per-sample mapping decisions** — one subsection per sample (H-047-01 through H-047-15). Each subsection must state:
   - which source was primary for that row;
   - any inference steps taken (abbreviation resolution, unit conversion, conflict resolution);
   - any instance where the source conflicted with the template expectation and how it was resolved.
3. **Global decisions** — any row-agnostic rules applied (absence-vocabulary convention, unit policy, mandatory-field scope).

The readme must be written in plain English professional register, not as a machine checklist. A curator should be able to read it and understand why any given cell contains its value without reopening the source documents.
