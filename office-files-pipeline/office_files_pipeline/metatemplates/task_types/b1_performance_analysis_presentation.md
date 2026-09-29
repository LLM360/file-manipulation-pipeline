# Performance Analysis Presentation (PowerPoint/PDF from Data)

**Macro Category:** B — Data-Driven Document Authoring
**Pattern ID:** B1

## 1. Pattern Description

The worker analyzes one or more structured data files — operational metrics, financial returns, process performance records, or sales figures — and produces a slide-based presentation that communicates findings to a leadership or stakeholder audience. The core cognitive work is a two-phase sequence: quantitative analysis (aggregating, comparing, or computing statistics from the data) followed by authorial synthesis (translating findings into narrative slides with charts, tables, and interpretive commentary). What makes this pattern distinct from pure dashboard tasks (A5) is that the presentation format and audience-facing framing are central deliverables, not incidental outputs. The deliverable must convey not just what the data shows but what it means and what should be done next.

## 2. O*NET Grounding

### Occupation Families
- 13-2051 Financial Analysts — analyzing portfolio/investment data and presenting findings to CIO or portfolio committees
- 17-2112 Industrial Engineers — process capability and SPC studies presented at tollgate or leadership reviews
- 11-2022 Sales Managers — regional sell-in performance decks for merchandising and planning teams
- 13-1082 Project Management Specialists — grant/funder monthly status reports with spend, risk, and progress
- 13-1031 Claims Adjusters, Examiners, and Investigators — policy compliance review decks for executive approval

### Key Work Activities (O*NET vocabulary)
- Analyzing Data or Information
- Preparing Presentations or Reports
- Communicating with Supervisors, Peers, or Subordinates
- Evaluating Information to Determine Compliance with Standards
- Making Decisions and Solving Problems
- Documenting Information

### Knowledge Domains (O*NET vocabulary)
- Mathematics
- Economics and Accounting
- English Language
- Administration and Management
- Engineering and Technology (for SPC/statistical variants)

### Generalizable Work Context
A professional individual contributor or manager receives a directive — from a CEO, department head, grant assessor, or client — to surface findings from operational or financial data and present them at a defined meeting or submission deadline. The audience is typically more senior than the analyst. The trigger is a periodic reporting cycle (monthly, quarterly, or phase-gate) or an ad hoc analytical request responding to a business concern. The analyst owns both the quantitative work and the narrative construction.

## 3. Prompt Construction Template

### Persona Pattern
Assign a mid-to-senior individual contributor role within a specific organizational context. The role should have analytical responsibility over the data domain being analyzed — e.g., Industrial Engineer at a processing center, Financial Analyst at an asset management firm, Sales Manager for a wholesale brand, Project Manager on a grant-funded project. Specify the organization type (institutional, startup, manufacturing facility, apparel brand) to ground the domain vocabulary.

### Scenario Pattern
A leadership figure or funder has requested a presentation summarizing performance findings for a defined period, project phase, or operational scope. The trigger is either a periodic reporting event (end of month, phase-gate, funding assessment) or a business concern (rising costs, process variance, regional performance gaps). Stakeholders who will receive the deck should be named or characterized (leadership team, grant assessor, merchandising and planning teams, senior management for approval).

### Instruction Pattern
Structure instructions as a required slide list (a fixed slide count, or "N slides covering X, Y, Z") or as a set of analytical deliverables that must be translated into slide content. Specify which data file maps to which slide. Describe both the analytical task (compute capability indices, calculate regional totals, build correlation matrix) and the presentation task (summarize findings, call out risks, provide recommendations). Include chart/visualization requirements where applicable.

### Constraint Injection Points
- **Slide count / format:** fixed slide count (e.g., an exact number), minimum/maximum, or content-per-slide structure
- **Data-to-slide mapping:** which input file governs which slide (e.g., one reference file feeds two consecutive slides)
- **Statistical method:** named method required (ANOVA, Cp/Cpk, I-MR, Pearson correlation)
- **Audience type:** external funder vs. internal leadership vs. peer colleague — changes tone and detail level
- **Output format:** PowerPoint vs. PowerPoint-saved-as-PDF vs. standalone PDF
- **Time window:** fixed date range or reporting period that anchors all analysis
- **Recommendation requirement:** findings alone vs. findings plus prioritized action items

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE]. [BRIEF_CONTEXT_SENTENCE].

[SCENARIO]: [TRIGGER_EVENT — e.g., end of month, phase review, leadership request]. [STAKEHOLDER_AUDIENCE] needs a presentation by [DATE/DEADLINE] covering [SCOPE_OF_ANALYSIS].

[DATA_SOURCE]: Attached is [FILE_DESCRIPTION — e.g., "an Excel file with monthly performance data for [METRIC_A], [METRIC_B], and [METRIC_C] from [DATE_RANGE]"].

[TASK]: Using the attached data, build a [FORMAT] presentation with the following slides:
1. [SLIDE_1_CONTENT]
2. [SLIDE_2_CONTENT]
...
N. [SLIDE_N_CONTENT]

[ANALYTICAL_REQUIREMENTS]:
- [SPECIFIC_ANALYSIS_1 — e.g., "For [METRIC], compute [STATISTIC] and assess [CRITERION]"]
- [SPECIFIC_ANALYSIS_2]
- [EXTENDED_ANALYSIS_IF_APPLICABLE — e.g., "The metric with greatest variability requires..."]

[CONSTRAINTS]:
- [STATISTICAL_CONSTRAINT — e.g., "Do not assume thresholds — derive from provided data only"]
- [FORMAT_CONSTRAINT — e.g., "Save as PDF"]
- [DATA_RANGE_CONSTRAINT]
- [AUDIENCE_CONSTRAINT]

[OUTPUT_SPECIFICATION]: [N]-slide [FORMAT] deck. Each slide should include [CHART_OR_TABLE_REQUIREMENT]. Final slide must include [RECOMMENDATION/NEXT_STEPS].
```

## 4. Reference File Requirements

### File Types Needed
- **Primary data file (xlsx):** Tabular time-series or cross-sectional data containing the performance metrics to be analyzed. Must have clear dimension columns (date, region, entity name) and measure columns (units, revenue, error counts, processing rates, return percentages).
- **Secondary context files (xlsx or docx, optional):** Risk registers, spend profiles, project logs, or policy documents that inform specific slides but are not the primary analytical input.
- **Template file (xlsx, optional):** Pre-structured workbook defining the expected analytical layout — used in variant where analyst populates a given framework rather than building from scratch.

### Data Characteristics
The primary data file should contain at minimum 3-12 months of observations or a sufficient cross-sectional population (8-20 entities, regions, or indices). Numerical measures should be raw rather than pre-aggregated, requiring the analyst to compute summaries. Multiple metrics per row (e.g., a rate metric and day-of-week context; units and revenue by region) support multi-dimensional analysis. Sufficient variance across entities or time periods is essential to generate meaningful findings and recommendations.

### File Complexity Spectrum
- **Minimal:** Single Excel tab, one primary metric, one time dimension, 6-12 rows of data. Single analytical dimension (e.g., monthly trend only).
- **Moderate:** Single Excel tab with 3 metrics, cross-sectional by region or entity, 20-50 rows. Requires pivot-style aggregation and one comparison dimension.
- **Complex:** Multiple tabs or multiple input files (e.g., financial, risk, and status-tracking sources), 3-5 metrics requiring different statistical treatments, 50-200 rows, with a data-to-slide mapping constraint that forces the analyst to route specific content to specific presentation sections.

## 5. Output Specification

### Primary Deliverable
- **Format:** PowerPoint (.pptx) or PDF; sometimes specified as PowerPoint saved as PDF
- **Structure:** Ordered slides with prescribed sections — title, executive summary or overview, metric-level analysis slides (one per metric or region), risk or exception highlights, recommendations/next steps
- **Key quality signals:** Charts and tables accurately derived from provided data; findings are interpreted (not just described); recommendations are logically grounded in the analysis; slide structure follows the prescribed mapping; no fabricated data points; appropriate level of statistical rigor for the method named

### Secondary Deliverables (if any)
- Excel workbook with the underlying analysis or data tabs (e.g., correlation matrix, regional pivot, or capability calculation) — serves as an appendix or supporting document
- Written PDF narrative (separate from slides) summarizing findings and implications in prose form

### Gold Output Characteristics
A gold output correctly computes all required statistics from the provided data, maps findings to the correct slides, generates visualizations that accurately represent the computations, interprets results in business-relevant language appropriate for the named audience, and closes with actionable recommendations. The slide narrative neither over-claims beyond what the data supports nor under-describes the significance of findings. Section headers match the prescribed structure, and the total slide count matches the specified constraint.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of metrics analyzed | 1 | 3 | 5+ with different statistical treatments per metric |
| Statistical depth | Simple aggregation (sum, average) | Multi-dimensional pivot with comparison | Full SPC analysis (Cp, Cpk, ANOVA, I-MR, regression) |
| Number of input files | 1 | 2-3 | 4+ with explicit data-to-slide mapping |
| Slide count | 4-6 | 8-10 | 12-18 with strict per-slide content rules |
| Audience formality | Internal peer review | Internal leadership | External grant assessor or regulator |
| Recommendation requirement | None | General next steps | Prioritized action items with risk-tiering |
| Visualization requirement | Tables only | Charts or tables | Named chart types (ANOVA interval plot, I-MR, capability histogram) |

## 7. Boundary Cases & Adjacent Patterns

**B4 (Cost Analysis & Budget Reconciliation Reports):** B4 produces a written summary or Excel cost breakdown rather than a slide deck. Choose B1 when the deliverable is a presentation for an audience, and B4 when it is a cost document for management review.

**A5 (Operational Metrics Dashboard / KPI Reporting):** A5 focuses on building the analytical infrastructure (PivotTables, dashboards, conditional formatting) in Excel, where the Excel workbook IS the deliverable. B1 uses Excel as input and produces a slide presentation as the deliverable. If a task requires both, classify by the primary deliverable.

**B3 (Compliance Report from Transaction Data):** B3 produces a Word narrative report citing regulatory frameworks, not a slide deck. The investigation and exception-identification work differs from the performance-trend analysis typical of B1. If the output is a SAR narrative or compliance findings document rather than slides, use B3.

**C5 (Market Research & Competitive Intelligence Report):** C5 involves web research as the primary information-gathering mode. B1 is driven by attached data files — the analysis is quantitative and file-grounded, not research-driven. If the task requires fetching external data (web scraping, index downloads) to build the analysis from scratch rather than working from attached files, consider whether C5 is a better fit.
