Date: 18 Nov 2024
To: Lab Manager — Microbiome Submission Curation
From: Dr. Elena Voss, Principal Investigator, MORRIS-1 Study
Subject: Batch HA-2024-047 — NCBI SRA/BioSample submission prep, deadline 22 Nov

The October bronchoscopy and respiratory-sampling push for MORRIS-1 is sitting on your bench. We have 15 human-associated specimens (H-047-01 through H-047-15) that need to go into NCBI BioSample by Friday so the SRA accession numbers can hit the consortium quarterly report. The upstream team handed me the attached GSC MIxS HumanAssociated blank template — 53 columns, single sheet, zero rows. Your job is to get every one of those 15 samples into that grid with the fields NCBI actually validates, and to do it in a way that survives a curator audit six months from now.

I have three source documents for you, and they do not agree cleanly. You will need to triangulate.

1. **sample_collection_log_2024-11.xlsx** — The Google Sheets export the field team mailed me last week. It has merged date/time headers, weights and heights in kg/cm, a free-text "Reviewer notes" column that sometimes contradicts the structured fields, and body sites written in technician shorthand (NP, SPT, BL). Temperatures are in Celsius.

2. **clinical_chart_deid_batch-HA047_2024-10-14.pdf** — De-identified chart extracts from our IRB-approved data-use agreement. Patient IDs are hashed as MORRIS-047-XX, which do not match the log's PID-HA47-XX hashes, but the cross-reference to sample IDs is in the document. Demographics (age, sex, ethnicity), disease status, and smoking are here. Medications are listed by trade name (Advair, Spiriva, Symbicort, etc.). Chart-recorded BMIs sometimes differ from what you'd compute from the log's weight and height — I need you to decide which number enters the template and document why.

3. **genotyping_report_batch-HA-2024-047.pdf** — The genotyping lab's handling report. It lists body-site abbreviations again, DNA extraction volumes, and accession temperatures recorded on an IR probe in Fahrenheit. For some specimens the Fahrenheit reading does not round-match the Celsius entry in the collection log. The genotyping report is the more reliable proxy for actual sample temperature at accession, especially for BAL and induced-sputum specimens where the log temperature may be pre-procedure oral rather than aliquot temperature.

**What you need to produce:**

A. The populated workbook. Save it as `HA-2024-047_MIxS_HumanAssociated.xlsx`. Keep the single `HumanAssociated` sheet. You do not need to fill all 53 columns — focus on the MIxS mandatory fields for a HumanAssociated package (identifiers, host demographics, body site, body product, disease status, collection temperature, storage metadata) plus anything you can resolve from the sources. For fields the study genuinely did not collect, use the MIxS absence term `not collected`. For fields that are biologically inapplicable to this cohort (the four pregnancy-related columns — gestation_state, maternal_health_stat, foetal_health_stat, amniotic_fluid_color — for a general adult population), use `not applicable`. Do not leave blanks; NCBI's validator flags blanks as missing rather than inapplicable.

Two columns have Excel data-validation dropdowns baked into the template. `urine_collect_meth` is locked to `catheter` or `clean catch`. `oxy_stat_samp` is locked to `aerobic`, `anaerobic`, or `other`. Only one of the 15 samples is urine; for the rest, set `urine_collect_meth` to `not applicable` even though Excel may grumble. For `oxy_stat_samp`, all specimens were collected in ambient air — use `aerobic`.

For `host_body_site` and `host_body_product`, the template has no dropdown, but MIxS still expects ENVO/UBERON-aligned terms. Map the technician shorthand to real anatomy: `NP` -> `nasopharynx`, `SPT` -> `sputum`, `BL` -> `bronchoalveolar lavage`. Body product follows the same mapping logic (nasal mucus, sputum, bronchoalveolar lavage fluid, urine).

`host_body_mass_index` is present in the template, but if the log lists `host_tot_mass` and `host_height`, compute BMI from those two values rather than copying a conflicting chart BMI blindly. If the log weight/height are missing, use what the chart provides. `temp` should be in Celsius; convert from the genotyping report's Fahrenheit readings where necessary, resolving conflicts using the rationale above.

B. A field-mapping readme named `field_mapping_notes_HA047.md`. This is not boilerplate. For each sample, note: which source was primary for that row, what inference steps you took (e.g., how you resolved the NP abbreviation, why you picked one temperature over another), and any mapping decision where the source conflicted with the template expectation. The consortium's data-access committee reads these; they need to follow your reasoning.

Send both files back by end of day Thursday. If anything in the source documents looks inconsistent in a way that blocks a clean mapping, flag it in the readme rather than guessing.
