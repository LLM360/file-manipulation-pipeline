# Financial Statement & P&L Construction

**Macro Category:** A — Financial Analysis & Modeling
**Pattern ID:** A2

## 1. Pattern Description

The worker builds a structured financial report — a profit and loss statement, amortization schedule, or multi-tab financial package — by consolidating and classifying data from multiple source files (GL extracts, invoice PDFs, location- or event-based revenue sheets, prior-month template workbooks). The cognitive core is data consolidation across heterogeneous sources combined with accurate financial categorization: every revenue or expense line must be correctly classified, every derived amount must reconcile to a provided target or prior-period figure. What distinguishes this pattern is the presence of explicit reconciliation targets or GL balances that the output must match, multi-source input aggregation requiring judgment about which source is authoritative, and professional formatting conventions (column layouts, header structure, category hierarchies) that mirror real accounting deliverables. The deliverable is almost always a multi-tab Excel workbook.

## 2. O*NET Grounding

### Occupation Families
- 13-2011 — Accountants and Auditors — primary occupation for GL reconciliation, amortization schedules, and financial package assembly
- 13-2051 — Financial Analysts — covers P&L construction, management reporting, multi-branch income statement modeling
- 11-3031 — Financial Managers — covers multi-branch financial package and management accounting
- 13-1111 — Management Analysts — covers consolidation of operational financial data into reporting packages

### Key Work Activities (O*NET vocabulary)
- Analyzing Financial Data
- Preparing Financial Reports
- Processing Information
- Documenting Information
- Organizing and Interpreting Information

### Knowledge Domains (O*NET vocabulary)
- Economics and Accounting
- Mathematics
- English Language
- Clerical (record management and filing)
- Administration and Management

### Generalizable Work Context
Finance or accounting teams at professional services firms, entertainment/media companies, cosmetics brands, or multi-branch corporations where a staff accountant or finance manager is responsible for a periodic financial close deliverable. The trigger is a recurring calendar event: month-end close, quarter-end, tour settlement, or fiscal year rollover. The audience is a CFO, external auditor, or senior leadership who expects a specific format with reconciled totals and professional presentation. Multiple source files representing different cost/revenue streams must be aggregated into a single coherent workbook.

## 3. Prompt Construction Template

### Persona Pattern
Assign an accounting or finance role with clear institutional context: Senior Staff Accountant (at a professional services firm), Finance Lead (at an entertainment/management company), Finance Manager (at a multi-branch corporation), or Planning Manager (at a cosmetics brand). The role should imply ongoing responsibility for a monthly or quarterly deliverable, access to multiple internal data sources, and a specific supervisor or external stakeholder who will review the output.

### Scenario Pattern
The worker is building or updating a financial report for a defined period (month-end, quarter, fiscal year, tour settlement). Multiple reference files contain the underlying data (invoices, GL extracts, prior-month templates, location- or event-based revenue tables). A template or prior-period version of the workbook defines the structural format. Explicit reconciliation targets (GL balances, variance thresholds) are provided either inline or embedded in the reference files. The output must be professionally formatted and ready for review.

### Instruction Pattern
Tab-by-tab specification works well. List each tab by name, then bullet-point its required content: header information, section structure, specific line items or categories, formula logic (e.g., amortization rule, withholding rate per country, currency conversion), and reconciliation target. Formatting requirements (sort order, headers, column layout) are specified as closing constraints.

### Constraint Injection Points
- **Reconciliation targets:** specific GL balance amounts or month-end totals the output must match
- **Classification schema:** defined expense categories, account numbers from a chart of accounts, or revenue line groupings
- **Multi-source handling:** which source file is authoritative for which data element; two-entity column structure (e.g., Entity A | Entity B | Combined)
- **Calculation rules:** amortization period defaults, withholding tax rates per country, currency conversion basis, period mapping
- **Scope exclusions:** specific tabs or sections explicitly out of scope (e.g., CFO tabs excluded from update)
- **Output naming and header conventions:** exact file name, "As of [date]" header, company name in header

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_NAME/TYPE]. [INSTITUTIONAL_CONTEXT — e.g., responsible for monthly close, advising an external client's management].

[SCENARIO]: [TRIGGER_EVENT — e.g., a month-end close, a tour settlement]. You have received [N] source files: [FILE_LIST_WITH_DESCRIPTIONS].

[TASK_DESCRIPTION]: Prepare [DELIVERABLE_NAME] — a [TAB_COUNT]-tab Excel workbook named [FILENAME] — using the provided source files and the [TEMPLATE/PRIOR_PERIOD_FILE] as your structural reference.

[DELIVERABLE_SPECIFICATION]:

Tab [N]: "[TAB_NAME]"
- Header: [COMPANY_NAME], [REPORT_PERIOD], [AS_OF_DATE]
- Sections: [SECTION_LIST]
- Line items: [ITEM_DESCRIPTION]
- Formulas / calculation rules: [CALCULATION_RULE]
- Reconciliation target: [GL_BALANCE or VARIANCE_TARGET]

[CLASSIFICATION_RULES]:
- [CATEGORY_1]: [DEFINITION_AND_SOURCE]
- [CATEGORY_2]: [DEFINITION_AND_SOURCE]

[CONSTRAINTS]:
- [CURRENCY_OR_CONVERSION_RULE]
- [SORTING_RULE]
- [SCOPE_EXCLUSION]
- Output file named exactly: [FILENAME]

[ESCALATION_OR_QUALITY_REQUIREMENT]: [FLAG_INCONSISTENCIES / DOCUMENT_CHANGES / REVIEW_READY]
```

## 4. Reference File Requirements

### File Types Needed
- **Prior-month or template workbook (xlsx):** Defines the structural format the new output must follow. Contains existing tabs (some in scope, some excluded), table of contents, and sample formatting conventions.
- **Transaction/GL source files (xlsx, txt, pdf):** Raw financial data — invoice-level expense detail, trial balance, accrual schedules, payroll registers, location- or event-based revenue tables. May be multiple files covering different cost categories.
- **Policy/parameter files (xlsx, pdf):** Chart of accounts for account number application; withholding tax rate tables by country; amortization policy documents; insurance schedule PDFs with policy periods and payment dates.

### Data Characteristics
Source files collectively contain all financial figures needed to construct the report. Transaction files have one row per invoice, GL entry, or individual revenue line; they contain date, vendor/entity name, amount, and category fields. Template files are multi-tab with defined column structures and placeholder values. Policy files contain structured parameter tables (account codes, rates, periods). The total input volume is typically 3–18 files covering 50–500 transaction rows across all sources.

### File Complexity Spectrum
- **Minimal:** Single xlsx source file + simple two-tab output structure. One classification dimension (5–7 expense categories), no reconciliation target, single currency.
- **Moderate:** 3–6 source files (mix of xlsx and pdf), 3-tab output with summary and two detail tabs, GL reconciliation targets for 3–5 months, amortization logic, one currency conversion.
- **Complex:** 15–20 source files of mixed types (xlsx, pdf, txt), template-driven update workflow with 10+ existing tabs, table of contents management, multiple account hierarchies, multi-entity columns, CFO-level escalation protocol, scope exclusions.

## 5. Output Specification

### Primary Deliverable
- **Format:** xlsx (Excel workbook)
- **Structure:** 2–10 tabs depending on complexity. Always includes: summary/header tab (overview with totals), one or more detail tabs (line-item breakdowns by category or time period), optionally a calculation/workings tab (amortization schedule, sample size)
- **Key quality signals:** All line items sum correctly to section totals; all section totals reconcile to provided GL targets; expense categories match defined schema; multi-entity columns are correctly attributed; professional formatting (borders, headers, sort order) matches template conventions

### Secondary Deliverables (if any)
- Table of Contents tab update when adding new tabs to a prior-period template
- CFO notification memo or email stub when flagging inconsistencies

### Gold Output Characteristics
A gold output reconciles exactly to all provided GL targets (within rounding). Every line item is correctly classified into the defined expense or revenue category. Multi-source data is correctly attributed to the right column or entity. Amortization calculations use the correct default rule when policy is silent. Formatting mirrors the provided template: headers, column widths, sort order, and section separators. Any new tabs are documented in the table of contents. Inconsistencies are flagged with comments rather than silently resolved.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of source files | 1 xlsx | 3–6 mixed files | 15–20 files (xlsx + pdf + txt) |
| Number of output tabs | 2 tabs | 3–5 tabs | 8–12 tabs with TOC management |
| Reconciliation requirement | None | Targets for 1–2 periods | Targets for 4–6 periods across multiple accounts |
| Calculation complexity | Direct summation | Amortization over defined period | Amortization + currency conversion + country-specific tax rates |
| Multi-entity structure | Single column | Two entities with separate columns | Two entities + combined column + sub-division breakdowns |
| Template fidelity | No template provided | Prior-period template as structural guide | Prior-period template with excluded tabs, TOC, and escalation rules |
| Classification depth | 3–5 flat categories | 2-level hierarchy (category + subcategory) | 3-level (division → category → vendor) |

## 7. Boundary Cases & Adjacent Patterns

**Most similar patterns:**
- **A1 (Audit Sampling):** Also produces Excel from tabular source data, but A1 selects a qualifying subset using defined criteria. Choose A2 when ALL source rows are included and must be classified/aggregated into a structured financial report; choose A1 when the task is to identify and extract a specific qualifying subset.
- **A5 (Operational Metrics Dashboard):** Both produce multi-tab Excel workbooks from reference data. A5 emphasizes PivotTables, charts, conditional formatting, and KPI summaries for operational data; A2 emphasizes financial accounting structure (GL reconciliation, amortization schedules, P&L category hierarchies). Choose A2 when the output follows accounting report conventions with reconciliation targets; choose A5 when the output is an interactive operational dashboard.
- **A3 (NPV/IRR Investment Evaluation):** Both involve financial modeling in Excel, but A3 evaluates discrete investment options using DCF/NPV/IRR frameworks with a recommendation. A2 constructs a complete historical or period-to-date financial statement from source data. Choose A2 when building a backward-looking accounting report; choose A3 when evaluating forward-looking investment alternatives.

**Key distinguishing signal:** A2 always involves consolidating multiple source files into a structured accounting report that reconciles to a provided target or template. If there is no reconciliation requirement and no multi-source consolidation, the task likely belongs to A5 (dashboard) or A4 (scenario model).
