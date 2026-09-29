# Audit Sampling & Compliance Testing

**Macro Category:** A — Financial Analysis & Modeling
**Pattern ID:** A1

## 1. Pattern Description

The worker applies formal screening or sampling logic to a structured dataset of records (financial transactions, grant awards, purchase orders, inventory items) to identify a subset that meets defined risk-based or compliance criteria. The cognitive core is simultaneously satisfying multiple independent selection criteria while maintaining full population coverage — each criterion must be satisfied by at least one selected record, and each selected record must satisfy at least one criterion. What distinguishes this pattern from generic filtering is the dual-constraint logic (statistical or regulatory parameter derivation plus multi-criteria coverage requirements) and the requirement to document the methodology alongside the output. The deliverable is always a new Excel workbook containing both the filtered/flagged result set and the calculation workings that justify the selection.

## 2. O*NET Grounding

### Occupation Families
- 13-2011 — Accountants and Auditors — core occupation for financial and compliance audit sampling tasks
- 13-1041 — Compliance Officers / Grants Administrators — applies to regulatory compliance screening of award or transaction data
- 43-5071 — Shipping, Receiving, and Inventory Clerks — applies to operational inventory cross-referencing and location report population
- 13-2031 — Budget Analysts — applies to grant spend rate compliance testing

### Key Work Activities (O*NET vocabulary)
- Analyzing Data or Information
- Evaluating Compliance with Laws, Regulations, or Standards
- Documenting/Recording Information
- Processing Information
- Identifying Objects, Actions, and Events
- Making Decisions and Solving Problems

### Knowledge Domains (O*NET vocabulary)
- Economics and Accounting
- Mathematics
- Law, Government, and Jurisprudence
- English Language
- Clerical (record management and filing)

### Generalizable Work Context
Mid-to-large organizations in regulated industries (financial services, government, wholesale, automotive manufacturing) where a compliance or operations team member performs periodic review of a structured dataset to identify anomalous, non-compliant, or risk-elevated records. The trigger is typically a cyclical reporting requirement (quarterly audit cycle, monthly compliance review, fiscal month close) or an operational exception event (receiving dock activity, daily transaction export). The audience for the output is a senior reviewer (audit manager, CFO, grants officer) who uses the flagged subset to initiate follow-up actions.

## 3. Prompt Construction Template

### Persona Pattern
Assign a compliance-oriented or operations role with institutional context: Auditor (at a bank or government agency), Grants Management Specialist (post-award compliance), Wholesale/Order Analyst (billing/fulfillment audit), or Inventory Clerk (warehouse location reporting). Seniority level is mid-level; the worker is competent with Excel but not a data scientist. The organizational context should imply access to structured data exports from an ERP, WMS, or grants management system.

### Scenario Pattern
The worker receives a structured data export (xlsx) from an internal system. A specific compliance event or cyclical review cycle has triggered the need to identify flagged records. There may be a regulatory framework cited (e.g., 2 CFR Part 200, audit standards) or an operational SOP that specifies the criteria. A fixed reference date or period anchors the analysis. The output will be reviewed by a senior stakeholder (audit manager, CFO, grants officer, operations supervisor).

### Instruction Pattern
Multi-step numbered instructions work best for this pattern. Steps typically follow: (1) calculate a parameter or threshold from provided inputs, (2) add computed columns to the source data, (3) apply filtering or flagging logic using defined criteria, (4) produce a filtered/annotated output workbook with specified column structure. Sub-bullets specify exact column names, label vocabulary, and exception handling rules.

### Constraint Injection Points
- **Numerical parameters:** confidence levels, error rates, percentage thresholds (e.g., a confidence level paired with a tolerable error rate; a spend-percentage threshold paired with a time-elapsed threshold)
- **Multi-criteria selection logic:** number of distinct criteria (3–10), coverage requirements (all criteria satisfied, all named entities included)
- **Column schema:** exact column names and order in the output
- **Label vocabulary:** classification labels must be drawn from a fixed set (e.g., a pair of spend-pace labels; a pair of line-level error-type labels)
- **Exception handling:** half-quantity rules, exclusion conditions (items not yet moved, UOM exemptions)
- **Reference date:** fixed anchor date for all time-based calculations

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE]. [INSTITUTIONAL_CONTEXT].

[SCENARIO]: You have received an Excel export of [DATASET_DESCRIPTION] as of [REFERENCE_DATE]. [TRIGGER_EVENT — e.g., quarterly compliance review, receiving dock activity, end-of-month order reconciliation].

[TASK_DESCRIPTION]: Review the data and produce a [DELIVERABLE_DESCRIPTION] that identifies [FLAG_LOGIC_SUMMARY].

[REQUIREMENTS]:
1. [PARAMETER_CALCULATION — e.g., calculate required sample size using X confidence level and Y error rate; compute % time elapsed as (reference date − start date) / (end date − start date)]
2. [ADD_COMPUTED_COLUMNS — e.g., add a variance column; add a % Funds Spent column]
3. [APPLY_CRITERIA — specify each criterion with its threshold; all criteria must be satisfied by at least one record]
4. [PRODUCE_OUTPUT — filtered/flagged tab with specified columns; calculation workings tab]

[CRITERIA]:
- [CRITERION_1]: [THRESHOLD_AND_CONDITION]
- [CRITERION_2]: [THRESHOLD_AND_CONDITION]
- [CRITERION_N]: [THRESHOLD_AND_CONDITION]
- Coverage requirement: [ALL_NAMED_ENTITIES / ALL_CATEGORIES must appear]

[CONSTRAINTS]:
- Output columns (in order): [COL_1], [COL_2], ..., [COL_N]
- Classification labels: [LABEL_A] or [LABEL_B]
- Exception: [SPECIFIC_EXCEPTION_RULE]

[OUTPUT_SPECIFICATION]: Excel workbook with Tab 1 "[POPULATION_TAB_NAME]" and Tab 2 "[CALCULATION_TAB_NAME]". Tab 2 must show all workings for [PARAMETER_DERIVATION].
```

## 4. Reference File Requirements

### File Types Needed
- **Primary data file (xlsx):** Population-level tabular data with one row per entity (grant award, transaction, PO line, inventory item). Must contain numeric fields for threshold calculations, date fields for time-based criteria, categorical fields for coverage requirements, and identifier fields (SKU, award number, metric ID).
- **Lookup/master file (xlsx, optional):** A secondary reference mapping entities to locations, expected values, or classification codes (e.g., a location/item master list, an expected unit price table, a case pack reference).
- **Template file (xlsx, optional):** A blank structured output template with predefined column headers that the worker must populate.

### Data Characteristics
Tabular data with 50–500 rows, 8–20 columns. Must include: one or more numeric metric columns (amounts, quantities, rates), at least one date column pair (start/end, or period-over-period), categorical grouping columns (division, supplier, product line, geography), and a unique identifier column. Numeric values should span a wide enough range that multi-criteria filtering selects 5–25% of the population. Some records should naturally satisfy multiple criteria; some should be edge cases (zero values, exactly at threshold).

### File Complexity Spectrum
- **Minimal:** Single xlsx with 30–60 rows, two numeric columns for threshold calculation, one date pair, one categorical grouping. Filtering produces 5–10 flagged rows.
- **Moderate:** Single xlsx with 100–200 rows, 3–5 numeric metrics, a date column pair, 3–4 categorical grouping columns (hierarchy), 5–7 selection criteria producing 15–30 flagged rows.
- **Complex:** Primary data file plus a lookup/master file. 300–500 rows in primary file, 10–15 columns, 7+ selection criteria with coverage requirements across all named sub-categories, plus a blank template file to populate. Exception handling rules for specific records.

## 5. Output Specification

### Primary Deliverable
- **Format:** xlsx (Excel workbook)
- **Structure:** Tab 1 — original population data with added computed columns (variance, %, flag indicator) and all rows present; Tab 2 — filtered/flagged subset with exact column schema; Tab 3 (optional) — calculation workings (parameter derivation, formula documentation)
- **Key quality signals:** Correct statistical/threshold calculation; all criteria satisfied by at least one row; all coverage requirements met; exact column names and label vocabulary used; no extraneous rows in filtered output

### Secondary Deliverables (if any)
- Brief Word document or email summarizing findings and error frequency (audit + summary report variant)

### Gold Output Characteristics
A gold output populates the filtered tab with exactly the rows that satisfy the defined criteria — no more, no fewer. The computation tab shows the full derivation of any numerical parameters (sample size formula, threshold calculation). Column headers match the specified schema exactly. Label vocabulary is drawn strictly from the defined set. Any coverage requirements (all named entities, all categories) are demonstrably satisfied. Exception rules (half-quantity, UOM exemptions) are applied correctly to specific records.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Population size | 30–60 rows | 100–200 rows | 300–500 rows |
| Number of selection criteria | 2–3 criteria | 5–7 criteria | 8–10 criteria with coverage requirements |
| Criterion type | Single threshold on one column | Dual threshold (two columns) | Multi-column criteria with named entity coverage |
| Reference files | Single xlsx | Two xlsx files | Two xlsx + blank template to populate |
| Exception handling | None | One exception rule | Multiple exception rules with partial-quantity logic |
| Parameter derivation | Parameters given directly | One derived parameter (e.g., sample size) | Multiple derived parameters with formula documentation required |
| Output schema | Flexible (any reasonable columns) | Named columns (6–8) | Exact column list with exact label vocabulary |

## 7. Boundary Cases & Adjacent Patterns

**Most similar patterns:**
- **A5 (Operational Metrics Dashboard):** Also transforms raw tabular data in Excel, but A5 produces a multi-tab dashboard with aggregations, PivotTables, and charts — not a filtered/flagged subset. Choose A1 when the deliverable is a record-level filtered output with selection justification; choose A5 when the deliverable is a summary dashboard.
- **A2 (Financial Statement Construction):** Both work from Excel source data, but A2 consolidates and classifies financial transactions into a structured report (P&L, amortization schedule), while A1 selects a qualifying subset from a population using explicit criteria. Choose A1 when there is a binary inclusion/exclusion decision per row; choose A2 when every row is included but needs to be classified and aggregated.
- **B3 (Compliance Report from Data):** B3 also involves compliance criteria applied to data, but the primary deliverable is a narrative Word document (e.g., SAR narrative, compliance memo) with the Excel as a supporting file. Choose A1 when the Excel filtered output IS the deliverable; choose B3 when a prose narrative is the primary output.

**Key distinguishing signal:** A1 always produces a filtered/flagged row-level subset of a source population, plus documented calculation workings. If the task's primary output is a summary dashboard, a narrative document, or a full-population financial report, it belongs to a different pattern.
