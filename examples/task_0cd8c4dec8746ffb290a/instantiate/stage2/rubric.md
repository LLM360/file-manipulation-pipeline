# Rubric — Batch HA-2024-047 MIxS curation review

Reviewer instructions: Open the completed `HA-2024-047_MIxS_HumanAssociated.xlsx` and the accompanying `field_mapping_notes_HA047.md`. Check each criterion against the source documents where indicated. A criterion marked "2 pts" requires a substantive assertion; "1 pt" is a small structural or surface check; "3 pts" is judgment. Penalties appear as negative values.

---

## A. Workbook completeness and scope (15 pts)

1. **File and sheet naming.** The delivered workbook is named `HA-2024-047_MIxS_HumanAssociated.xlsx` (or close variation) and contains exactly one sheet named `HumanAssociated`. (1 pt)

2. **Row count.** Exactly 15 data rows present (rows 2–16), one per sample H-047-01 through H-047-15, in ascending numeric order. (1 pt)

3. **Header preservation.** Row 1 contains all 53 original MIxS headers (`samp_name` through `misc_param`) with no additions, deletions, or reorderings. (1 pt)

4. **Mandatory-field coverage.** Every row contains a non-blank value in: `samp_name`, `project_name`, `host_subject_id`, `host_age`, `host_sex`, `host_body_site`, `host_body_product`, `temp`, `samp_store_temp`, `samp_store_dur`, `host_disease_stat`. (2 pts)

5. **No blank policy.** No blank cells appear in rows 2–16 for any of the 53 columns. Where data were unavailable, `not collected` or `not applicable` is used; where data were missing due to source conflict, `missing` is used with a note. (2 pts)

6. **Pregnancy-field absence vocabulary.** The four pregnancy-related columns (`gestation_state`, `maternal_health_stat`, `foetal_health_stat`, `amniotic_fluid_color`) contain `not applicable` for every row in the general adult cohort. Any other value (including blank or `not collected`) loses points. (2 pts)

7. **Urine-collection non-urine handling.** For all 14 non-urine samples, `urine_collect_meth` is set to `not applicable`. For the single urine sample (H-047-11), it is set to `clean catch`. (2 pts)

8. **Oxygen status consistency.** `oxy_stat_samp` is `aerobic` for all 15 rows. (1 pt)

9. **Project name consistency.** `project_name` is `MORRIS-1` for every row. (1 pt)

10. **Host subject ID source fidelity.** `host_subject_id` uses the `MORRIS-047-NN` hash from the clinical chart PDF, not the `PID-HA47-NN` hash from the collection log. (2 pts)

---

## B. Ontology mapping and controlled vocabulary (18 pts)

11. **Body-site mapping accuracy — NP samples.** For the 7 nasopharyngeal samples (H-047-01, 03, 05, 07, 09, 12, 14), `host_body_site` is `nasopharynx` (not `NP`). (1 pt)

12. **Body-site mapping accuracy — SPT samples.** For the 5 sputum samples (H-047-02, 06, 08, 13, 15), `host_body_site` is `sputum` (not `SPT`). (1 pt)

13. **Body-site mapping accuracy — BL samples.** For the 2 bronchoalveolar lavage samples (H-047-04, 10), `host_body_site` is `bronchoalveolar lavage` (not `BL`). (1 pt)

14. **Body-site mapping accuracy — urine sample.** For H-047-11, `host_body_site` is `urinary tract` (not `urine`). (1 pt)

15. **Body-product mapping accuracy — NP.** For nasopharyngeal samples, `host_body_product` is `nasal mucus`. (1 pt)

16. **Body-product mapping accuracy — SPT.** For sputum samples, `host_body_product` is `sputum`. (1 pt)

17. **Body-product mapping accuracy — BL.** For BAL samples, `host_body_product` is `bronchoalveolar lavage fluid`. (1 pt)

18. **Body-product mapping accuracy — urine.** For H-047-11, `host_body_product` is `urine`. (1 pt)

19. **Medication mapping — no meds.** For samples where the chart lists no medications (H-047-01, 07, 12), `ihmc_medication_code` is `not applicable`. (1 pt)

20. **Medication mapping — known codes.** For samples on albuterol (H-047-06, 13), fluticasone/salmeterol (H-047-02, 10, 15), tiotropium (H-047-03, 06, 10, 15), or budesonide/formoterol (H-047-04, 14), `ihmc_medication_code` contains the exact mapped term(s). Where multiple medications apply (e.g., H-047-06, 10, 15), all applicable terms are present, separated by commas. (2 pts)

21. **Medication mapping — missing codes.** For medications not found in the IHMC ontology (ethinyl estradiol/norethindrone for H-047-05, prenatal multivitamin for H-047-09, ciprofloxacin for H-047-11), `ihmc_medication_code` is set to `missing` rather than the free-text trade name or a fabricated code. (2 pts)

22. **Urogenital disorder appropriateness.** For H-047-11 (UTI), `urogenit_tract_disor` is `urinary tract infection` and `kidney_disord` is `not collected`. For all other samples, `urogenit_tract_disor` and `kidney_disord` are `not applicable`. (2 pts)

23. **Pulmonary disorder assignment.** For COPD samples, `pulmonary_disord` is `COPD`. For asthma samples, it is `asthma`. For healthy samples, it is `none`. (1 pt)

---

## C. Derived fields and unit conversions (15 pts)

24. **BMI computation — standard formula.** `host_body_mass_index` is computed as kg / (m^2), rounded to one decimal place, for every row where log weight and height are present. (2 pts)

25. **BMI computation — specific values.** Sample-specific spot checks:
   - H-047-01 BMI = 22.8
   - H-047-04 BMI = 28.7
   - H-047-10 BMI = 28.1 (computed from 91.0 kg / 180 cm; chart BMI absent in log but present in chart; computed value takes precedence).
   - H-047-11 BMI = 26.7
   - H-047-15 BMI = 28.8 (2 pts)

26. **BMI conflict resolution.** For rows where the chart BMI differs from the computed BMI by more than 0.2 (H-047-02: chart 25.9 vs computed 25.6; H-047-06: chart 28.1 vs computed 28.4; H-047-08: chart 26.0 vs computed 25.7; H-047-12: chart 26.5 vs computed 26.8), the workbook contains the computed value, not the chart value. (2 pts)

27. **Temperature conversion — Fahrenheit to Celsius.** For specimens where the genotyping report is the primary temperature source (H-047-04: 99.1 F -> 37.3 C; H-047-06: 99.3 F -> 37.4 C; H-047-08: 98.6 F -> 37.0 C; H-047-10: 99.1 F -> 37.3 C), the `temp` value reflects the correctly converted Celsius reading, rounded to one decimal. (2 pts)

28. **Temperature conflict resolution.** For H-047-04, H-047-06, and H-047-08, the `temp` value in the workbook matches the converted genotyping report temperature, not the collection-log temperature, per the rationale that genotyping accession temperature is the more reliable proxy for sample temperature at collection for BAL and sputum. (2 pts)

29. **Temperature inference — missing log value.** H-047-10 has no collection-log temperature; the workbook `temp` is 37.3 C derived from the genotyping report's 99.1 F. (1 pt)

30. **Storage parameters.** `samp_store_temp` is -80 for all 15 rows. `samp_store_dur` uses the exact day count from the collection log (e.g., H-047-01 = "45 days", H-047-04 = "50 days") and includes the unit string "days". (2 pts)

31. **Sample volume fidelity.** `samp_vol_we_dna_ext` matches the extraction volume from the genotyping report / log (e.g., H-047-04 = 300, H-047-10 = 280). (1 pt)

32. **Weight and height units.** `host_tot_mass` is in kilograms and `host_height` is in centimeters for every row, matching the log without unit conversion. (1 pt)

---

## D. Source triangulation and provenance documentation (12 pts)

33. **Readme existence and sections.** The secondary deliverable `field_mapping_notes_HA047.md` is present and contains the three required sections: Source hierarchy, Per-sample mapping decisions, Global decisions. (1 pt)

34. **Per-sample coverage.** The readme contains a distinct subsection for every sample H-047-01 through H-047-15. (1 pt)

35. **Primary source attribution.** Each per-sample subsection names which source document was primary for identifiers / biometrics versus demographics / disease versus extraction metadata. (2 pts)

36. **Inference documentation — body site.** The readme documents the abbreviation-to-ontology mapping (NP -> nasopharynx, SPT -> sputum, BL -> bronchoalveolar lavage) for at least one sample where the mapping required inference. (2 pts)

37. **Inference documentation — BMI conflict.** The readme explicitly notes the BMI conflict for at least one sample where the chart BMI differed from the computed BMI, states which source was chosen, and gives a rationale. (2 pts)

38. **Inference documentation — temperature conflict.** The readme explains the temperature conflict resolution for at least one BAL or sputum sample where the genotyping report was chosen over the collection log, with rationale. (2 pts)

39. **Inference documentation — medication mapping.** The readme documents at least one medication mapping decision where a trade name had to be mapped to an IHMC term or declared missing. (2 pts)

---

## E. Consistency and accuracy (12 pts)

40. **Demographic fidelity.** `host_age`, `host_sex`, and `ethnicity` match the clinical chart extract for every row. (2 pts)

41. **Disease status fidelity.** `host_disease_stat` matches the chart diagnosis for every row (e.g., H-047-04 = "COPD Gold III", H-047-11 = "UTI"). (2 pts)

42. **Smoking status fidelity.** `smoker` matches the chart for every row. (1 pt)

43. **`chem_administration` parity.** `chem_administration` matches `ihmc_medication_code` in every row. (1 pt)

44. **`not collected` discipline.** Fields not gathered by the study (e.g., `host_diet`, `host_last_meal`, `host_genotype`, `host_phenotype`, `host_body_temp`, `host_hiv_stat`, `drug_usage`, `host_occupation`, `pet_farm_animal`, `travel_out_six_month`, `twin_sibling`, `medic_hist_perform`, `nose_throat_disord`, `host_pulse`, `organism_count`, `host_symbiont`, `samp_store_loc`) contain `not collected` rather than blanks, `N/A`, or fabricated values. (3 pts)

45. **Cross-artifact consistency.** Entity names, sample IDs, patient hashes, numeric values, and dates that appear in both the workbook and the readme are identical; no internal contradictions exist between the two deliverables. (2 pts)

46. **No extraneous cells modified.** Cells in row 1 (headers) and any cells beyond row 16 remain unchanged from the original template. (1 pt)

---

## F. Penalties

47. **Fabricated or hallucinated values.** Any cell contains a value not traceable to one of the three source documents, a legitimate computation from source values, or the specified MIxS absence vocabulary. (-3 pts per instance, cap -9)

48. **Blank cells in data rows.** Any blank cell in rows 2–16 where a value, `not collected`, `not applicable`, or `missing` should appear. (-2 pts per instance, cap -6)

49. **Wrong patient hash used.** Any row uses `PID-HA47-NN` instead of `MORRIS-047-NN` in `host_subject_id`. (-2 pts per instance, cap -6)

---

## G. Holistic round-up (3 pts)

50. **Overall professional coherence.** The deliverable reads as the product of someone who opened all three sources, understood the MIxS schema, and made reasoned choices — not a mechanical dump of one source into the template. (3 pts)

---

**Total possible score: 75 pts**  
**Penalty floor: -21 pts**
