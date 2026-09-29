# Data Entry with Protocol-Driven Decision Making

**Macro Category:** B — Data-Driven Document Authoring
**Pattern ID:** B5

## 1. Pattern Description

The worker populates a partially pre-built template or blank form by extracting specific values from multiple source documents and applying embedded rules, conditional logic, or domain protocols to determine what should be entered in each field. The data entry is not mechanical transcription — it requires active decision-making at each step: which source document provides this value, which rule governs this field, what does the protocol require given the observed input value? The cognitive core is cross-referencing — the worker must simultaneously consult 3-5 reference files to resolve each field in the target template. What makes B5 distinct from adjacent B-category patterns is that the primary deliverable is a completed spreadsheet or form (not a narrative document), the decision logic is embedded in or attached to the target template (rather than in the analyst's own judgment), and the task is sequential month-over-month or item-by-item rather than a single aggregated analysis.

## 2. O*NET Grounding

### Occupation Families
- 51-1011 First-Line Supervisors of Production and Operating Workers — production supervisors populating a test plan template by cross-referencing BOM, tooling changeover, and roster files
- 29-2072 Medical Records Specialists — administrative assistants organizing patient records into EMR transfer workbooks and drafting HIPAA-compliant correspondence
- 43-5071 Shipping, Receiving, and Inventory Clerks — shipping clerks populating a daily manifest from WMS pick tickets using weight-based shipping method selection rules
- 29-1141 Registered Nurses — dialysis nurses entering monthly patient lab results into a tracker and applying medication protocols to determine monthly treatment adjustments
- 43-6013 Medical Secretaries and Administrative Assistants — medical administrative assistants organizing patient data from multiple PDFs into structured Excel workbooks with compliance correspondence

### Key Work Activities (O*NET vocabulary)
- Processing Information
- Documenting Information
- Evaluating Information to Determine Compliance with Standards
- Making Decisions and Solving Problems
- Organizing, Planning, and Prioritizing Work
- Communicating with Persons Outside Organization (for correspondence variants)

### Knowledge Domains (O*NET vocabulary)
- Clerical
- Medicine and Dentistry (for clinical variants)
- Transportation (for logistics variants)
- Production and Processing (for manufacturing variants)
- Law, Government and Jurisprudence (for HIPAA/compliance variants)
- Mathematics

### Generalizable Work Context
A frontline operations or administrative worker receives a template or blank form that must be completed using data pulled from multiple source documents. The target template defines the structure of the output — which cells to fill, what values are valid, what rules govern each field. The source documents provide the raw materials: patient records, pick tickets, BOM files, roster data, lab results, shipping parameters. The worker must consult each source document in turn, apply any embedded decision logic (protocol-based medication decisions, weight-threshold shipping selection, alive/deceased filtering), and enter the resolved values into the target template. The completed template will be used by downstream teams (maintenance, clinical staff, shipping department, medical records) who depend on it being accurate.

## 3. Prompt Construction Template

### Persona Pattern
Assign a frontline operational or administrative role whose daily work involves managing structured information across systems or documents — production supervisor, shipping clerk, medical administrative assistant, dialysis nurse. The role should be organizationally responsible for the accuracy of the completed template and should have a defined downstream recipient (plant manager, sales department, QA team, physician). Keep the seniority level mid-to-frontline — this is an execution task, not a strategic one.

### Scenario Pattern
A manager or supervisor has assigned the worker to complete a specific template or form that is needed for an upcoming process — a first-press validation run, a monthly clinical review, a daily shipment reporting cycle, an EMR transition. The trigger is an operational deadline (template must be ready by end of shift, sent to manager, used by team). Specify the scope: how many entities (patients, orders, machines, items) must be populated, what time period is covered, and what the template will be used for once completed.

### Instruction Pattern
Provide a list of the attached source documents and describe what each one contains. Specify which cells in the target template must be populated (yellow cells, blank cells in specified columns) and which must be left alone (pre-populated fields, cells outside scope). Describe the decision logic for any fields requiring conditional judgment (if lab value X, apply protocol Y; if weight exceeds threshold T, use shipping method M). Note any sequential constraint — that decisions for month N depend on the state established in month N-1.

### Constraint Injection Points
- **Target cells definition:** only specified cells should be populated (yellow-highlighted, named columns, blank rows only)
- **Source-to-field mapping:** which source file provides each category of data (BOM file provides material quantities; roster provides labor assignments; pick tickets provide order weights)
- **Protocol-based decision logic:** conditional rules determining what value to enter (if a lab value falls below a defined threshold, start the indicated medication; if weight > X lbs, use carrier method Y)
- **Filtering constraint:** subset of source data to include in template (deceased patients only in one tab; orders from current day's pick tickets only; items meeting all three criteria)
- **Sequential dependency:** current month's entries depend on prior month's state (medication dose titration across months)
- **Scope exclusions:** fields not to populate, data types not in scope (no post-production, no breakdown crew, no patients not in the EMR system)
- **Naming and formatting conventions:** specific workbook names, tab names, file names required

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE]. [BRIEF_CONTEXT — your role in the workflow].

[SCENARIO]: [MANAGER/SUPERVISOR] has asked you to complete [TEMPLATE_NAME] using data from the attached reference files. [PURPOSE — e.g., "The completed template will be used by [DOWNSTREAM_TEAM] to [PURPOSE]."]

[REFERENCE_FILES]:
- File 1 — [FILENAME/TYPE]: [DESCRIPTION — what data it contains and its role in the task]
- File 2 — [FILENAME/TYPE]: [DESCRIPTION]
- File 3 — [FILENAME/TYPE]: [DESCRIPTION — the target template to be populated]
- File 4 — [FILENAME/TYPE]: [DESCRIPTION — protocol or decision rules]
- [Additional files as needed]

[DATA_ENTRY_TASK]:
Populate [TARGET_TEMPLATE] by:
1. [STEP_1 — e.g., "For each [ENTITY], extract [DATA_FIELDS] from File 1 and enter into [COLUMN_SET]"]
2. [STEP_2 — e.g., "Determine [DECISION_FIELD] for each [ENTITY] using the following rule from File 4: [RULE_STATEMENT]"]
3. [STEP_3 — e.g., "For [ENTITY_SUBSET meeting CRITERION], complete [ADDITIONAL_TAB or ADDITIONAL_COLUMN]"]

[DECISION_RULES]:
- [RULE_1 — e.g., "If [FIELD] [CONDITION], then [ACTION] (e.g., use shipping method X)"]
- [RULE_2 — e.g., "Apply [PROTOCOL] for patients assigned to [PHYSICIAN_GROUP]; apply [ALTERNATE_PROTOCOL] for patients assigned to [OTHER_PHYSICIAN_GROUP]"]
- [SEQUENTIAL_RULE if applicable — e.g., "Month N medication dose is based on Month N-1 dose and current month lab values"]

[CONSTRAINTS]:
- Only populate [SPECIFIED_CELLS — e.g., "yellow-highlighted cells" or "blank fields in columns A-G"]
- Leave [EXCLUDED_FIELDS] unchanged
- [NAMING_CONVENTION — e.g., "Save workbook as [FILENAME.xlsx] with tabs named [TAB_1] and [TAB_2]"]
- [SIGNATURE_REQUIREMENT if applicable]

[OUTPUT_SPECIFICATION]: Completed [TEMPLATE_NAME] with all specified cells populated per the rules above. [SECONDARY_DELIVERABLE if applicable — e.g., "Plus two correspondence letters following the provided template with HIPAA clauses from the Clauses Sheet"].
```

## 4. Reference File Requirements

### File Types Needed
- **Target template (xlsx):** The partially pre-built or blank spreadsheet that must be completed. Defines the structure, required fields, tabs, and any embedded rules or color-coded indicators (yellow cells, named ranges). This is the primary output once populated.
- **Source data document (xlsx, pdf, or docx):** The raw data source from which values are extracted — patient records, WMS pick tickets, monthly lab results, team roster. May be structured (tabular) or semi-structured (PDF with tabular content).
- **Protocol or rules document (docx or additional xlsx):** Contains the conditional decision logic applied to determine what values to enter — clinical protocols with medication decision trees, shipping parameter tables with weight thresholds, BOM requirement files with material specifications.
- **Supporting reference files (xlsx or pdf, optional):** Additional lookup tables — tooling changeover times, skill rankings, HIPAA clauses, letter templates, employee identity credentials — that provide specific values needed for individual fields.

### Data Characteristics
The source data document should contain 5-30 entities (patients, orders, items, workers) with enough field diversity to produce meaningful variation across the target template. At least one field should require a protocol-driven decision rather than simple transcription (a lab value that triggers a medication protocol; a shipment weight that selects a carrier; a vital status flag that routes a record to a second tab). Where sequential logic applies, the source data should cover multiple time periods (an extended run of monthly lab results; a week of daily orders) so that earlier-period decisions propagate into later-period fields. The template should have clear cell scope indicators so the worker knows exactly which cells to populate.

### File Complexity Spectrum
- **Minimal:** 2 source files (template + 1 data source), 5-10 entities, 3-5 fields per entity, no conditional logic beyond a simple filter. Output: single populated Excel tab.
- **Moderate:** 3-4 source files (template + data + protocol + lookup table), 10-20 entities, 6-10 fields per entity, 1-2 conditional rules, 1 additional tab for filtered subset. Secondary deliverable: 1 correspondence document.
- **Complex:** 5 source files (template + multi-patient data source + 2-3 protocol documents + employee credential file), a handful of entities each tracked across many time periods, yielding dozens of individual decision points, multiple conditional protocols differentiated by entity group (physician-specific binder protocols), sequential dependency across time periods (dose titration), 2 correspondence letters with HIPAA clauses, named workbook with specific tab naming conventions.

## 5. Output Specification

### Primary Deliverable
- **Format:** Excel workbook (.xlsx) — the populated template file
- **Structure:** One or more tabs with the completed data grid; possible filtered subset tab; each row representing one entity across populated columns; conditional formatting or cell values reflecting applied decision logic
- **Key quality signals:** All specified fields are populated with values derived from the correct source document; conditional rules are applied correctly (correct shipping method for each weight; correct medication per protocol and physician assignment; correct tab for each patient vital status); no out-of-scope cells are modified; tab and file naming conventions are followed; where sequential dependency applies, earlier months correctly inform later months

### Secondary Deliverables (if any)
- Correspondence letters (Word or PDF) drafted using the provided template structure with regulatory clauses (HIPAA) and entity-specific details
- Email to manager or supervisor (brief, a few sentences) confirming completion and noting any exceptions or anomalies
- Conditional formatting or cell highlighting in the completed template marking decision outcomes

### Gold Output Characteristics
A gold output is complete — every specified cell is populated, no required field is left blank, and no out-of-scope field is modified. All conditional decisions are correctly resolved: the right rule was applied, the right source document was consulted, and the right value was entered. Sequential dependencies are correctly chained — a month 3 medication dose correctly reflects the month 2 starting dose and the month 3 lab value. Filtering logic is correctly applied — the right entities appear in the right tabs. File and tab names match the specified naming convention exactly. Any secondary correspondence is factually consistent with the primary data file and includes all required regulatory or compliance elements.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of source files | 2 | 3-4 | 5 with distinct roles (data, protocol, lookup, template, credential) |
| Number of entities | 3-5 | 8-15 | 20-30 or a handful of entities tracked across many time periods |
| Conditional decision logic | Simple filter (include/exclude based on one flag) | 2-3 rules from a protocol document | Multiple protocols differentiated by entity group, with dose titration |
| Sequential dependency | None | Month-over-month with 1 decision variable | Month-over-month with 3-4 interdependent medication state variables |
| Tab / deliverable count | 1 tab | 2 tabs (all entities + filtered subset) | 2 tabs + 2 correspondence letters + named workbook |
| Field scope definition | Color-coded cells (yellow) | Named columns only | Rules embedded within the template with conditional-fill logic |
| Secondary correspondence | None | 1 email body | 2 formal letters with regulatory clauses and identity signing |

## 7. Boundary Cases & Adjacent Patterns

**A1 (Audit Sampling & Compliance Testing):** A1 applies multi-criteria filters to a data population and produces a flagged/filtered Excel output. B5 populates a structured template using cross-referenced source files and embedded decision logic. The key difference is that A1 is a filtering/screening task (which records pass or fail a criterion), while B5 is a population task (what value should go in each field of a template). If the task is about deciding what goes in each cell rather than which rows to include, use B5.

**B3 (Compliance Report from Transaction Data):** B3 produces a written compliance narrative document as the primary deliverable. B5 produces a populated spreadsheet or form. Both involve applying rules to data, but B3's output is a formal written report, while B5's output is a completed data template. If the deliverable is a Word compliance narrative, use B3.

**A5 (Operational Metrics Dashboard / KPI Reporting):** A5 builds analytical infrastructure from scratch — PivotTables, calculated metrics, charts — in a new Excel workbook. B5 populates a pre-existing template following embedded rules. If the analyst is building the structure rather than filling a given structure, use A5.

**B2 (HR & Workforce Decision Reports):** B2 produces written HR documents (PIPs, selection rationale) informed by workforce data analysis. B5 produces completed data templates or forms. If the output is a formal personnel document with narrative content, use B2. If the output is a populated Excel tracker or clinical form, use B5.
