This file is a blank metadata collection template from the Genomics Standards Consortium (GSC) MIxS (Minimum Information about any (x) Sequence) standard. Specifically, it is the "HumanAssociated" extension template, stored in the `mixs-templates/extensions_only/` directory of the GSC mixs repository.

**Content and structure:** The workbook contains a single sheet ("HumanAssociated") with 53 predefined column headers and zero data rows. The columns define a comprehensive metadata schema spanning multiple domains:

- **Sample and project identifiers:** samp_name, project_name
- **Host subject demographics:** host_subject_id, host_age, host_sex, ethnicity, host_occupation
- **Health and clinical status:** host_disease_stat, ihmc_medication_code, chem_administration, smoker, host_hiv_stat, drug_usage, host_body_mass_index, medic_hist_perform, study_complt_stat, pulmonary_disord, nose_throat_disord, blood_blood_disord, kidney_disord, urogenit_tract_disor
- **Body site and phenotype:** host_body_site, host_body_product, host_genotype, host_phenotype, gestation_state, maternal_health_stat, foetal_health_stat, amniotic_fluid_color
- **Physiological measurements:** host_tot_mass, host_height, host_body_temp, host_pulse
- **Lifestyle and exposure:** host_diet, host_last_meal, host_fam_rel, diet_last_six_month, weight_loss_3_month, pet_farm_animal, travel_out_six_month, twin_sibling, perturbation
- **Sample handling and technical:** salinity, oxy_stat_samp, temp, organism_count, samp_vol_we_dna_ext, samp_store_temp, samp_store_dur, samp_store_loc, urine_collect_meth, host_symbiont, misc_param

**State:** This is a finalized, authoritative community standard template — not a draft or working document. It is intentionally blank (no data rows) so that it can be distributed to researchers and data submitters as the structural scaffold for metadata entry. The repository has 15 associated pull requests, indicating active community maintenance of the standard.

**Tasks supported:**
- **Metadata population / data entry:** A researcher, lab technician, or bioinformatician receives this template alongside source documents (sample collection logs, clinical charts, genotyping reports, lab notebooks) and must populate rows with metadata for each biological sample. Many fields require domain knowledge and protocol application rather than simple transcription (e.g., mapping free-text clinical notes to MIxS-controlled vocabularies for body site or disease status).
- **Template adaptation:** A lab manager or data coordinator may receive this community standard as a baseline reference and modify it to add study-specific fields or remove irrelevant columns for a particular cohort study.
- **Data validation and harmonization:** When integrating metadata from multiple studies, this template serves as the canonical schema against which incoming data must be validated and remapped.

**Non-obvious aspects:** The template mixes clinical/demographic fields with environmental/technical sample handling fields in a flat single-sheet structure. Although the filename suggests a human focus, it includes fields for maternal/fetal health (gestation_state, foetal_health_stat, amniotic_fluid_color), making it suitable for pregnancy-related sample studies without requiring a separate template. The `misc_param` catch-all column at the end allows extension beyond the 52 standard fields. As a GitHub-hosted artifact from an open standards body, this file is designed for broad distribution across research institutions and public databases (e.g., NCBI, EBI) to ensure metadata interoperability.
