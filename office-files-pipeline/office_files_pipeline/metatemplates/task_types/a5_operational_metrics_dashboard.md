# Operational Metrics Dashboard / KPI Reporting

**Macro Category:** A — Financial Analysis & Modeling
**Pattern ID:** A5

## 1. Pattern Description

The worker transforms raw operational or transactional data from one or more source files into a structured, multi-tab Excel dashboard (or PowerPoint presentation) featuring aggregated KPI summaries, PivotTables, charts, and conditional formatting. The cognitive core is multi-dimensional aggregation: computing the right metric at the right level of granularity (by category, period, operator, SKU, supplier), then surfacing it in a visual, interactive format that enables management to monitor performance. What distinguishes this pattern from financial statement construction (A2) is its focus on operational metrics — utilization rates, production output, sell-through percentages, incident rates, ADR — rather than accounting categories, and its emphasis on visual and interactive features (PivotTables with dropdown selectors, conditional formatting for top/bottom performers, multi-chart layouts). The deliverable is an Excel workbook with multiple interconnected worksheets, or a PowerPoint with a table-and-chart structure per slide.

## 2. O*NET Grounding

### Occupation Families
- 11-3021 — Computer and Information Systems Managers — IT work-time study analysis and operational reporting
- 41-2021 — Rental Clerks / 11-3071 — Transportation Managers — vehicle rental daily operational reports
- 51-1011 — First-Line Supervisors of Production Workers — manufacturing output dashboards
- 13-1023 — Purchasing Agents / 13-1022 — Merchandise Planners — retail sales performance dashboards
- 11-2022 — Sales Managers / 19-3021 — Market Research Analysts — SKU-level account performance recaps
- 13-1081 — Logisticians / Inventory Analysts — warehouse incident analysis presentations

### Key Work Activities (O*NET vocabulary)
- Analyzing Data or Information
- Presenting Data or Information
- Documenting Information
- Evaluating and Monitoring Operations
- Organizing, Planning, and Prioritizing Work
- Processing Information

### Knowledge Domains (O*NET vocabulary)
- Mathematics
- Computers and Electronics
- Administration and Management
- Transportation (for logistics/rental contexts)
- Sales and Marketing (for retail contexts)
- Production and Processing (for manufacturing contexts)

### Generalizable Work Context
Operations, IT, logistics, retail buying, or account management functions at mid-to-large organizations where a team member is responsible for producing a recurring performance report from a data extract. The trigger is a recurring reporting cycle (end of day, end of week, end of fiscal period) or an ad-hoc analytical request from management. The audience is a direct manager, operations team, or national account team who uses the dashboard to monitor trends, identify outliers, and direct attention. The data comes from a single structured export (ERP, WMS, POS, IT time-tracking system) and is dense enough to require aggregation before it is useful.

## 3. Prompt Construction Template

### Persona Pattern
Assign an operational role responsible for a specific reporting deliverable: IT Manager (work-time analysis), Car Rental Clerk (daily operational report), Production Supervisor (operator output dashboard), Assistant Buyer (sales performance pivot), National Account Director (SKU-level account recap), or Inventory Analyst (incident analysis presentation). The persona should have access to a specific data export and a named audience (manager, operations team, account director) for the deliverable.

### Scenario Pattern
The worker has received a structured data export (one xlsx file, typically) from an operational system. A recurring reporting deadline or a specific management request triggers the need for a formatted dashboard. The source data is transactional (one row per rental agreement, production record, retail transaction, incident) and needs to be aggregated across multiple dimensions (category, period, operator, SKU, supplier) before it is useful. Named worksheet structures, specific metric formulas, and visualization requirements are all specified.

### Instruction Pattern
Specify deliverable structure tab-by-tab (for Excel) or slide-by-slide (for PowerPoint). For each tab/slide, list: name, content type (PivotTable, chart, KPI table, raw data), specific columns or metrics, and any conditional formatting or interactivity rules. Define derived metrics explicitly (formula for LOR, ADR, utilization rate, sell-through, ST%, etc.). Specify chart types by name (pie, bar, multi-chart layout). Close with overall formatting or structural constraints (file naming, sheet naming, column order).

### Constraint Injection Points
- **Metric definitions:** explicit formulas for derived metrics (LOR = average rental days; ADR = total revenue / total rental days; ST% = Sales / Stock On Hand; utilization rate = rented units / available units)
- **Aggregation dimensions:** which categorical breakdowns are required (by vehicle category, by supplier, by operator and machine, by brand and store)
- **Tab/slide structure:** named tabs or slides, content type per tab, ordering
- **PivotTable + dropdown interactivity:** data validation week selectors, branch/aggregate dropdowns
- **Conditional formatting rules:** top/bottom performers highlighted in specific colors; threshold-based cell coloring
- **Chart requirements:** chart type (pie, bar), data mapped to chart, one chart per slide or arranged in a compact grid
- **Classification/mapping schemes:** pre-assigned activity-to-segment mappings (e.g., a set of granular activities mapped to a smaller number of higher-level segments); material status code filters (e.g., one range of codes flagged as ongoing, another range flagged as discontinued)

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE]. [REPORTING_CONTEXT — e.g., responsible for producing the daily operational report; managing national account performance].

[SCENARIO]: You have received [SOURCE_DATA_DESCRIPTION] for [PERIOD] from [SYSTEM/SOURCE]. [MANAGEMENT_OR_REPORTING_TRIGGER].

[TASK_DESCRIPTION]: Produce a [DELIVERABLE_TYPE — Excel workbook / PowerPoint presentation] [FILENAME] with [N] [tabs / slides] as specified below.

[DELIVERABLE_SPECIFICATION]:

[Tab/Slide N]: "[TAB_NAME]" — [CONTENT_TYPE]
- Metrics / columns: [METRIC_LIST]
- Aggregation: by [DIMENSION_1], broken out by [DIMENSION_2]
- Derived formulas: [METRIC_NAME] = [FORMULA]
- Visualization: [CHART_TYPE showing METRIC vs. DIMENSION]
- Interactivity: [DROPDOWN for SELECTOR; DATA_VALIDATION list of values]
- Conditional formatting: [RULE — e.g., top 3 operators highlighted green; bottom 3 red]

[METRIC_DEFINITIONS]:
- [METRIC_1]: [FORMULA]
- [METRIC_2]: [FORMULA]

[CLASSIFICATION_MAPPING (if applicable)]:
- [CATEGORY_1]: includes [ITEM_A, ITEM_B, ITEM_C]
- [CATEGORY_2]: includes [ITEM_D, ITEM_E]

[CONSTRAINTS]:
- File named: [FILENAME]
- Observations section: [BRIEF / MANAGEMENT-FACING / ACTIONABLE]
- Data range: [WEEK_RANGE, OPERATOR_RANGE, PERIOD]
```

## 4. Reference File Requirements

### File Types Needed
- **Primary transactional data file (xlsx):** One row per operational event (rental agreement, production shift record, weekly sales transaction, incident event, IT activity log entry). Must contain categorical fields for all required aggregation dimensions, numeric fields for all KPI metrics, and optionally temporal fields for period-based breakdowns.
- **Classification mapping reference (embedded in prompt or separate file, optional):** A lookup table or inline mapping that assigns each record's category to a higher-level segment (e.g., a set of granular activity categories mapped to a smaller number of analytical dimensions; SKU material status codes mapped to lifecycle stages).

### Data Characteristics
Transactional data with 30–500 rows, 8–20 columns. Must include: a primary categorical dimension (vehicle category, operator name, brand, supplier), at least one numeric metric column (revenue, units, time duration, cost), optionally a secondary categorical dimension for cross-tab analysis (booking source, payment method, machine line, shift), and a period or date field for time-based filtering. Some derived metrics must be computable from the available columns (LOR from date fields; ST% from sales and inventory; utilization from rented vs. available). Enough categorical variety to produce meaningful breakdowns (at minimum 3–5 distinct values per dimension).

### File Complexity Spectrum
- **Minimal:** Single xlsx with 30–80 rows, one categorical dimension, two numeric columns. Two-tab output: raw data tab and a simple KPI summary tab. No PivotTables or charts required.
- **Moderate:** Single xlsx with 100–300 rows, 2–3 categorical dimensions, 5–8 numeric columns. Three-to-five-tab output with a dashboard tab containing PivotTables, 2 charts, and a KPI summary table.
- **Complex:** Single xlsx with 300–500 rows across a full year or multiple periods. Five-to-seven-tab output: raw data tab, multiple PivotTable tabs with data validation dropdown selectors, conditional formatting with threshold-based coloring, several charts arranged in a compact grid layout, and a KPI summary table with several computed metrics.

## 5. Output Specification

### Primary Deliverable
- **Format:** xlsx (Excel workbook); occasionally pptx (PowerPoint) when the audience is management and the data dimensions map neatly to one-slide-per-dimension
- **Structure (Excel):** 2–7 tabs. Typical structure: Tab 1 — raw data (possibly as a structured table or pivot source); Tab 2 — KPI summary table with aggregate metrics; Tab 3+ — dimensional breakdown tabs with PivotTables or structured tables; Final tab — dashboard with charts, KPI cards, and conditional formatting
- **Structure (PowerPoint):** Title slide + one slide per analytical dimension (each with a table and a chart). 4–6 slides total.
- **Key quality signals:** Derived metrics are computed correctly from available data; PivotTables aggregate to correct totals; conditional formatting highlights correct rows/cells; charts are labeled and match specified type; observations section is brief and actionable; all specified tabs/slides are present with correct naming

### Secondary Deliverables (if any)
- Brief narrative observations section (2–5 sentences) embedded within the Excel file or at the end of the PowerPoint, synthesizing trends and flagging anomalies for management attention

### Gold Output Characteristics
All specified aggregation dimensions are present. Derived metric formulas are correctly applied (no off-by-one in LOR, correct sell-through denominator, correct utilization rate base). PivotTables produce totals that match the raw data sum. Conditional formatting fires on the correct cells based on the specified threshold. Charts show the correct metric vs. the correct dimension and use the specified chart type. The observations section identifies 2–3 genuine patterns in the data (top performer, highest-revenue category, anomalous trend) rather than restating column headers. Tab and file names match specifications exactly.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of output tabs / slides | 2 tabs | 3–4 tabs | 5–7 tabs with interconnected PivotTables |
| Number of aggregation dimensions | 1 dimension | 2 dimensions | 3+ dimensions with cross-tab analysis |
| Derived metric complexity | Direct sum | 1–2 derived formulas | 5+ derived metrics with different denominators |
| Interactivity | No interactivity | One dropdown filter | Multiple data-validation dropdowns with week/range selectors |
| Chart requirements | No charts | 1–2 charts | Multiple charts arranged in a grid layout, one per dimension |
| Conditional formatting | None | One formatting rule | Multi-rule formatting (top/bottom N + threshold-based) |
| Classification mapping | No mapping needed | One pre-assigned mapping (inline) | Multi-dimensional mapping scheme (many categories collapsed into a handful of higher-level segments) |
| Row count in source data | 30–80 rows | 100–200 rows | 300–500 rows (full year, spanning many entities and weekly periods) |

## 7. Boundary Cases & Adjacent Patterns

**Most similar patterns:**
- **A2 (Financial Statement Construction):** Both produce multi-tab Excel workbooks from source data. A2 follows accounting report conventions with GL reconciliation and category classification; A5 emphasizes operational KPIs, PivotTables, and visual/interactive features. Choose A2 when reconciliation targets and accounting categories drive the structure; choose A5 when the task is building an interactive performance monitoring tool.
- **A1 (Audit Sampling):** Both process tabular source data. A1 filters/flags qualifying rows; A5 aggregates all rows into dimensional summaries. Choose A1 when the output is a filtered subset; choose A5 when the output is a summary dashboard representing the full dataset.
- **B1 (Performance Analysis Presentation):** B1 also produces presentation-format output from data, but the emphasis in B1 is on narrative interpretation and stakeholder communication (charts with commentary, insights for leadership). A5 is more mechanically specified: named tabs, exact metric formulas, specific chart types per slide. Choose A5 when the instructions enumerate specific KPI formulas and chart requirements; choose B1 when the task emphasizes analytical narrative and strategic insight.

**Key distinguishing signal:** A5 always involves transforming a raw operational data file into a structured summary format with at least one of: PivotTable, conditional formatting, multi-dimensional KPI table, or chart with specific type requirements. If the source data is financial (GL, P&L) rather than operational (transactions, output logs), prefer A2.
