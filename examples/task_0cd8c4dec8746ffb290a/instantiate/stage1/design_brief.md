---
source_to_field_mapping_complexity:
  value: "source_gaps_with_inference"
  behavioral: true
controlled_vocabulary_fidelity:
  value: "standard_term_mapping"
  behavioral: true
pregnancy_subcohort_logic:
  value: "n_a_general_cohort"
  behavioral: true
missing_data_semantics:
  value: "mixs_na_vocabulary"
  behavioral: true
validation_and_derived_fields_scope:
  value: "compute_derived_fields"
  behavioral: true
deliverable_completeness_scope:
  value: "minimal_mandatory"
  behavioral: true
secondary_documentation:
  value: "field_mapping_readme"
  behavioral: true
persona_role:
  value: "lab_manager"
  behavioral: false
---

This task lands on the desk of a lab manager who is shepherding a batch of human-microbiome study samples through NCBI SRA/BioSample submission. The upstream team has handed over a Genomics Standards Consortium (GSC) MIxS `HumanAssociated` blank template—a single-sheet, 53-column workbook with zero data rows and a header row that runs from `samp_name` through `misc_param`. The manager's job is not rubber-stamping numbers into a grid; it is deciding, for each of roughly 12–20 samples, what actually belongs in this schema when the source documents are fragmentary and contradictory.

The source material is deliberately messy. You have a primary sample collection log (a shared Google Sheets export re-saved as `.xlsx` with merged date columns and free-text reviewer notes in row margins), a de-identified clinical chart PDF where patient IDs are hashed differently than the log, and a genotyping lab report that lists body sites in its own abbreviations (e.g., "NP" for nasopharynx, "SPT" for sputum). There is no one-to-one mapping: the log lists a sample weight in grams, the template wants `host_tot_mass` but the units are ambiguous in the MIxS spec; the PDF lists current medications by trade name, but the template column is `ihmc_medication_code`, which expects International Human Microbiome Consortium ontology terms, not free text. The runner has to open all three sources, triangulate, and occasionally make an evidence-based inference with a note. This is the core of the job.

The template itself carries its own odd texture. It is flat—one sheet, no grouping—yet the columns span clinical demographics (`host_age`, `host_sex`, `ethnicity`), disease and medication status (`pulmonary_disord`, `blood_blood_disord`, `ihmc_medication_code`), lifestyle (`pet_farm_animal`, `travel_out_six_month`), maternal/fetal health (`gestation_state`, `foetal_health_stat`, `amniotic_fluid_color`), and technical sample handling (`samp_store_temp`, `samp_vol_we_dna_ext`, `urine_collect_meth`). In this sampled cell, the cohort is a general adult population, so the four pregnancy fields are expected to be marked `not applicable` using MIxS absence vocabulary, but the runner still has to *notice* them, rule on them, and enter the controlled absence term rather than leaving blanks. Blanks are not acceptable in MIxS because downstream validators flag them as missing rather than inapplicable.

Two fields—`urine_collect_meth` and `oxy_stat_samp`—have Excel data-validation dropdowns baked into the template (`catheter` / `clean catch` for the former; `aerobic` / `anaerobic` / `other` for the latter). These are not decorative; if the runner types a non-matching string, Excel will reject it or downstream curators will. The runner must read the log, infer the collection method from the technician's shorthand, and pick the dropdown value that fits. In other cases (`host_body_site`, `host_body_product`), there is no dropdown in the template, but MIxS still expects values from the ENVO or UBERON ontologies. The runner must map free-text source entries to standard terms—`nasopharynx` rather than `NP`, `sputum` rather than `SPT`—without being handed a lookup table. This is professional judgment, not transcription.

For the fields that *can* be derived, the runner is expected to compute rather than copy blindly when sources conflict. `host_body_mass_index` is explicitly present in the template, but if the log lists `host_tot_mass` and `host_height`, the BMI column must be calculated and cross-checked. If the log *also* lists a BMI that differs from the computed value (common when a clinical chart uses a different formula or an outdated measurement), the runner must decide which source wins and document the choice in the field-mapping readme. Similarly, `temp` (sample temperature at collection) may be recorded in the log in Celsius while the lab report uses Fahrenheit; the runner must convert and enter the correct unit implied by the MIxS standard.

The scope of this cell is *minimal mandatory*—the runner does not need to populate all 53 columns. Instead, they should identify the MIxS mandatory fields for human-associated packages (typically identifiers, host basics, body site, and collection metadata) and fill those completely, marking the rest as `not applicable` or `missing` where appropriate. This means the runner must know (or infer from context) which columns are required for submission versus which are optional extensions, and they must do this without an explicit checklist being provided.

Finally, the secondary deliverable is a field-mapping readme (plain text or markdown) that accompanies the populated workbook. For each sample, the readme should note: which source document was primary for that row, any inference steps taken (e.g., "Sample H-14 NP location inferred as nasopharynx per collection protocol v3.2; genotyping report lists 'SPT' but log confirms nasopharyngeal swab"), and any mapping decisions where the source conflicted with the template expectation. This document is what makes the workbook auditable six months later when a curator asks why a cell contains what it does.

The test of whether the runner has done real work, rather than generic data entry, is whether the output reflects grappling with the specific friction points of this file: the ontology remapping, the unit conversions, the pregnancy-field N/A handling, the derived-field computation, the dropdown-bound validation fields, and the provenance readme. A runner who simply dumps the log into the template row-for-row will fail the specificity test.
