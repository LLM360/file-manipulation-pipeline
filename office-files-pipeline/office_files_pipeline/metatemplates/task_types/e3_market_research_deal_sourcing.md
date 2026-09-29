# Market Research & Deal Sourcing

**Macro Category:** E — Research-to-Document Tasks
**Pattern ID:** E3

## 1. Pattern Description

The worker researches publicly available market data from specialized platforms (financial data sites, commercial real estate deal platforms, retail pricing aggregators, regulatory data portals) and compiles the results into a structured quantitative output — most commonly an Excel workbook or a multi-property report — that enables a downstream analytical or transactional decision. The defining feature of this pattern is large-scale, criteria-driven data collection: the worker must apply explicit filters (geography, time period, financial thresholds, concentration type, active status) to identify a qualifying population, then extract a consistent set of metrics per entry. This differs from general research because the output is not a narrative synthesis but a populated data structure ready for analysis, underwriting, or decision-making. The cognitive core is matching real-world data against a multi-dimensional criteria set, then organizing findings into a format that enables direct comparison.

## 2. O*NET Grounding

### Occupation Families
- 13-2051 Financial Analysts — equity market research, equity index screening, valuation multiples
- 41-9021 Real Estate Brokers — commercial deal sourcing, CMA report preparation, property shortlists
- 41-9022 Real Estate Sales Agents — buyer-facing listing reports, comparative market analysis
- 19-3021 Market Research Analysts — competitive pricing benchmarking, MSRP modeling
- 11-2022 Sales Managers — pricing strategy and competitive positioning models
- 13-1022 Wholesale and Retail Buyers — competitive pricing analysis across distribution channels
- 13-1082 Project Management Specialists — regulatory data extraction for site selection decisions

### Key Work Activities (O*NET vocabulary)
- Analyzing Data or Information
- Getting Information
- Documenting Information
- Making Decisions and Solving Problems
- Preparing Reports
- Researching and Documenting Information

### Knowledge Domains (O*NET vocabulary)
- Economics and Accounting
- Mathematics
- Sales and Marketing
- Geography
- English Language
- Law, Government and Jurisprudence (for regulatory portals)
- Engineering and Technology (for site selection contexts)

### Generalizable Work Context
A professional with deal-making, investment, or pricing authority needs a structured data set to support a specific decision: a shopping list for acquisitions, a price-setting model, a valuation for a client, a site selection ranking. The trigger is a business mandate with a defined criteria set — the worker's job is to translate that criteria set into a web research protocol, execute it across one or more platforms, and deliver the result in a structured format. The criteria set arrives either from a stakeholder brief, an attached document, or inline in the task prompt. The output enables others (investors, executives, clients) to make decisions without having to perform the research themselves.

## 3. Prompt Construction Template

### Persona Pattern
Assign a role with deal-sourcing or market intelligence responsibility: investment banking analyst, commercial real estate broker, buyer's agent, pricing strategist, market research analyst. The persona should have a defined client or stakeholder whose mandate drives the research. Seniority level: analyst-to-associate (executes the research) or mid-level professional (owns the analysis and recommendation).

### Scenario Pattern
A client, investment group, or leadership team has a specific acquisition, pricing, or market positioning mandate. The worker must translate the mandate into a research protocol, execute it against named platforms, and compile the results. Provide the criteria set explicitly — this is the filter the worker must apply. The research has a temporal anchor (current as of a specific date or date range).

### Instruction Pattern
State the research mandate first (what is being sought and why), then provide the criteria as a structured list (financial thresholds, geographic bounds, property types, concentration categories, etc.). Then specify the output format with explicit field/column requirements. Specify acceptable data sources by name. Add any exclusion rules. Note the volume target (number of properties, companies, SKUs, wells). Include any downstream purpose statement to anchor the analytical depth required.

### Constraint Injection Points
- **Volume target:** number of entries required (e.g., all constituents of a broad market index, 5–10 properties, all wells across several named systems)
- **Geographic constraint:** state, metro, zip code, radius, county
- **Temporal constraint:** active listings as of a date, data currency requirement, lookback period for comparables
- **Financial thresholds:** price range, cap rate minimum, NOI floor, P/E benchmark range, MSRP tolerance band
- **Property/asset type filter:** property class, product concentration, aquifer type
- **Source platform constraint:** named platforms only (e.g., a financial data site, a commercial real estate deal platform, a retail pricing aggregator, a state regulatory data portal)
- **Field schema:** exact column names required in output
- **Aggregation requirement:** individual-level AND summary/roll-up level in same workbook
- **Valuation methodology:** cost-per-ounce calculation, cap rate formula, LTM vs. NTM P/E
- **Exclusion rules:** gift sets, seasonal products, inactive/abandoned wells, non-standard formulations

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE]. It is [DATE_CONTEXT].

[SCENARIO]: Your [CLIENT/LEADERSHIP] has asked you to [RESEARCH_MANDATE — e.g., "source acquisition opportunities" / "benchmark competitor pricing" / "compile a market valuation screen"].

[CRITERIA SET]:
Research must identify [ASSET_TYPE / DATA_CATEGORY] meeting ALL of the following criteria:
- [CRITERION_1: e.g., geographic scope]
- [CRITERION_2: e.g., financial threshold]
- [CRITERION_3: e.g., asset class / type filter]
- [CRITERION_4: e.g., active/current status]
- Exclude: [EXCLUSION_RULE_1], [EXCLUSION_RULE_2]

[DATA SOURCES]: Research using the following platforms: [PLATFORM_1], [PLATFORM_2]. Use [PRIORITY_SOURCE] when multiple sources are available.

[OUTPUT REQUIREMENTS]:
Produce an Excel workbook with the following structure:
- Tab 1 — [ALL_ENTRIES / FULL_DATASET]: Include the following columns:
  [COLUMN_1], [COLUMN_2], [COLUMN_3], [COLUMN_4], [COLUMN_5], [COLUMN_6], [COLUMN_7]
- Tab 2 (if applicable) — [FILTERED_SUBSET / SUMMARY / AGGREGATED_VIEW]

[ANALYTICAL LAYER]:
[CALCULATION_REQUIREMENT — e.g., "Calculate average cost-per-ounce by size bracket" / "Add filter flag columns for each criterion" / "Include a valuation range summary"]

[DOWNSTREAM PURPOSE]: This output will be used to [DECISION — e.g., "support LOI submission" / "set new MSRPs" / "identify viable production sites"].
```

## 4. Reference File Requirements

### File Types Needed
- **Criteria document (PDF or DOCX):** Investor acquisition criteria outlining target property types, price ranges, cap rate expectations, geographic markets, and investment strategy (value-add vs. stabilized). This is the "screening brief" attached by the stakeholder.
- **CMA template (DOCX):** Pre-structured report template for comparative market analysis reports, defining section layout and required elements.
- **SKU/asset master list (XLSX):** Current product list with existing prices, cost figures, and attribute data (concentration, size, category) used as the starting point for competitive benchmarking.
- **None (web-research-only):** Many tasks in this pattern require no reference files — all data is sourced from named platforms.

### Data Characteristics
**Reference file (when present):** Tabular product/asset master data with 5–20 columns including identifiers (SKU, property ID), financial metrics (current price, COGS, cap rate), categorical attributes (concentration, property type, asset class), and dimensional data (size, square footage). Typically 20–500 rows.

**Output data:** Each row represents one deal, property, company, or product. Required fields per row typically include: unique identifier, geographic identifier, 4–8 financial/metric columns, categorical classification columns, and optionally one or more calculated/derived columns (filter flag, cost-per-ounce, recommended value). Aggregation rows or summary tabs collect roll-up statistics.

### File Complexity Spectrum
- **Minimal:** No reference files; 5–10 entries; 6 columns; single tab; data sourced from one platform; no calculations.
- **Moderate:** One reference file (criteria PDF or template); 15–50 entries; 8–10 columns; two-tab structure (all entries + filtered subset); one derived column (filter flag or simple calculation).
- **Complex:** Reference file (SKU master with pricing and COGS); 500+ entries across multiple aggregation levels; separate benchmarking calculation sheet; multi-dimensional filtering; cost-per-ounce or P/E aggregation by subgroup; rationale column requiring written justification per entry.

## 5. Output Specification

### Primary Deliverable
- **Format:** Excel workbook (.xlsx) — most common; sometimes a PDF or Word report for real estate deal summaries
- **Structure:** Single tab (small datasets) or multi-tab (all data + filtered subset + aggregation summary); consistent column schema; sortable; filter flags or derived columns where specified
- **Key quality signals:** All entries meet the stated criteria (geographic, financial, temporal, type); excluded entries absent; required field count consistent per row; derived calculations (cost-per-ounce, cap rate) correctly applied; aggregation correctly grouped; filter flag logic consistent with stated exclusion criteria

### Secondary Deliverables (if any)
- Written recommendation memo or email (e.g., recommending top wells to manager, justifying MSRP choices)
- Individual property report pages (for deal sourcing — one section per shortlisted property with photos and narrative)
- Charts or graphs embedded in Excel (valuation comparisons, price benchmarking)

### Gold Output Characteristics
A gold output applies all stated criteria without gaps (no missing entries from the target population, no non-qualifying entries included), maintains a consistent column schema across all rows, calculates derived metrics correctly (cost-per-ounce, cap rate, P/E ratio), uses correct aggregation grouping (sub-sector, size bracket, concentration tier), and — where a recommendation or narrative is required — provides specific, reasoned justification tied directly to the data. Output is formatted for professional delivery, not raw data dump.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Entry volume | 5–15 entries | 50–100 entries | 500+ entries (e.g., all constituents of a broad market index) |
| Criteria complexity | 1–2 filters | 3–4 filters with numerical thresholds | 5+ interdependent filters with exclusion rules and tolerance bands |
| Source platform count | 1 named platform | 2 platforms with priority rules | 3+ platforms with deduplication logic |
| Calculation depth | No derived columns | One filter flag or simple calculation | Multi-dimensional aggregation (cost-per-ounce by size × concentration) |
| Output structure | Single-tab flat table | Two-tab (all data + filtered subset) | Multi-tab with roll-ups, charts, and written rationale per entry |
| Temporal constraint | Current data, no date specificity | Specific date cutoff (active as of date X) | Historical lookback with recency weighting |
| Recommendation layer | Data only | Brief email/summary | Written per-entry rationale with multi-component justification |

## 7. Boundary Cases & Adjacent Patterns

**E4 (Regulatory Data Extraction & Comparison):** Both patterns involve extracting structured data from web sources into comparison tables. E4 focuses specifically on government/regulatory/compliance portals (state boards, CMS, EPA) and produces outputs organized for regulatory comparison. E3 involves commercial market platforms (deal platforms, pricing sites, financial data services) for investment or business decisions. When the source is a government portal and the output is a regulatory comparison with compliance implications, use E4.

**A5 (Operational Metrics Dashboard / KPI Reporting):** A5 transforms already-collected data from reference files into dashboards and KPI summaries; the data collection is complete before the task begins. E3 requires the worker to collect the data through web research as the primary work activity. If the data must be actively sourced from the web, use E3; if it arrives pre-attached, use A5.

**E2 (Curated Local Resource Guides):** E2 aggregates service-directory information (contact details, hours, descriptions) for operational reference. E3 aggregates quantitative market/financial data (prices, metrics, financial ratios) for analytical or transactional decisions. When the output is a navigational reference for service use rather than a quantitative model for decision-making, use E2.

**B4 (Cost Analysis & Budget Reconciliation Reports):** B4 analyzes cost data from attached reference files to identify variances or cost-effectiveness. E3 requires collecting benchmark data from external web platforms before analysis can begin. If the cost data is pre-provided in reference files, use B4; if it must be sourced through web research, use E3.
