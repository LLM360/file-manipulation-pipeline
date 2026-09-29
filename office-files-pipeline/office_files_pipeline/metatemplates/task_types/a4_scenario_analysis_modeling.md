# Scenario Analysis & Commercial Terms Modeling

**Macro Category:** A — Financial Analysis & Modeling
**Pattern ID:** A4

## 1. Pattern Description

The worker builds a multi-scenario Excel model comparing distinct operational or commercial configurations — lease terms, pricing strategies, production schedules, fill strategies, competitive price benchmarks — and produces a recommendation supported by both quantitative results and written narrative. The cognitive core is constructing structurally parallel scenario blocks (typically three) that vary specific parameters (margin, term, capacity, fill frequency) while holding others constant, then identifying which configuration best satisfies a defined decision criterion (revenue threshold, deadline achievement, margin cap, cost tolerance). What distinguishes this pattern from NPV/IRR evaluation (A3) is that the financial metric is a current-period calculation rather than a discounted future cash flow — the scenarios are compared on margins, costs, revenues, or operational constraints evaluated in the present or near-term. The deliverable is typically an Excel workbook with embedded charts and a written summary, or a comparative table in a PDF report.

## 2. O*NET Grounding

### Occupation Families
- 11-2022 — Sales Managers / Directors — commercial terms scenario modeling (margin, payment terms, allowances)
- 11-3051 — Industrial Production Managers — production capacity scenario planning (catch-up plans, output schedules)
- 11-9141 — Property and Real Estate Managers — lease term scenario comparison
- 29-1051 — Pharmacists — pharmacy cost-effectiveness scenario analysis (fill strategy comparison)
- 19-3021 — Market Research Analysts / 11-2022 — Sales Managers — competitive pricing benchmarking and MSRP recommendation

### Key Work Activities (O*NET vocabulary)
- Analyzing Costs and Benefits
- Making Decisions and Solving Problems
- Scheduling Work and Activities (production scenarios)
- Preparing Financial Models
- Evaluating and Monitoring Operations
- Analyzing Data or Information

### Knowledge Domains (O*NET vocabulary)
- Economics and Accounting
- Mathematics
- Sales and Marketing
- Production and Processing
- Administration and Management
- Medicine and Dentistry (pharmacy context)

### Generalizable Work Context
Operations, sales, or management roles at mid-to-large organizations in manufacturing, real estate, cosmetics/beauty, healthcare, or consumer goods, where a senior individual contributor must evaluate a near-term operational or commercial decision by modeling it under different parameter configurations. The trigger is a specific business problem: a production backlog requiring a recovery plan, a new retail account requiring terms negotiation, an expiring lease requiring renewal options, a fill-strategy change requiring cost justification, or a rebranding requiring competitive price alignment. The audience is a peer review group (operations meeting, account team, medical director) or management.

## 3. Prompt Construction Template

### Persona Pattern
Assign a role with both analytical responsibility and decision accountability: Production Manager, Sales Director, Property Manager, Pharmacist, or Director of Sales. The role should imply direct ownership of the decision being modeled and a specific audience for the recommendation (peer operations meeting, account director, board or medical director). The persona should be knowledgeable about the domain-specific parameters (production capacity rates, retail margin conventions, lease escalators, pharmacy fill economics, fragrance pricing tiers).

### Scenario Pattern
A specific business problem requires choosing among three alternatives (the three-scenario structure is canonical for this pattern). Each scenario varies one or two key parameters while sharing a common baseline. A decision criterion defines when one scenario is preferable (minimum revenue threshold, deadline achievement, margin cap, cost-per-oz tolerance). Reference data provides baseline inputs (historical sales, open POs, current MSRPs, current fill parameters). The output will be used in a formal review or decision meeting.

### Instruction Pattern
Specify each scenario by name and its parameter values. Define the shared calculation framework (what is computed for each scenario). Require a visual comparison (chart) and a written summary (embedded in Excel or as a separate section). The written summary must name the preferred scenario and justify the recommendation. Formatting requirements (color-coding by scenario, editable variable cells, shared column structure) should be specified as closing constraints.

### Constraint Injection Points
- **Scenario parameter ranges:** margin range (e.g., a percentage band spanning several points), term options (e.g., a short/medium/long set of lease durations), production rates (e.g., a base rate and one or more higher-capacity tiers), fill periods (e.g., two differing fill-cycle lengths), MSRP tolerance (e.g., a percentage band around a competitor average)
- **Decision threshold:** revenue difference cap (e.g., a small percentage of total revenue), deadline (e.g., a fixed calendar date), margin floor, cost-per-oz tolerance band
- **Shared calculation structure:** same metrics computed for every scenario (revenue, cash flow, margin, annualized cost)
- **Visual requirement:** chart type and what it should illustrate (scenario favorability, percentage OOS, cost comparison)
- **Written summary:** length (a short paragraph of several sentences, or 1–2 pages), content requirements (name preferred scenario, justify with profitability + relationship balance)
- **Operational constraints:** financial constraints (no overtime), labor constraints, stat holidays, customer deadlines

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_NAME/TYPE]. [INSTITUTIONAL_CONTEXT — e.g., evaluating commercial terms for a new retail account; planning production recovery].

[SCENARIO]: [PROBLEM_STATEMENT — e.g., You need to recover from a X-unit backlog by [DEADLINE]; you are proposing commercial terms for a new [N]-door account; you are comparing fill strategies for your pharmacy's top medications].

[TASK_DESCRIPTION]: Build an Excel [workbook / comparative table] modeling three scenarios and recommend the best approach.

[SCENARIOS]:
- Scenario 1 ([NAME]): [PARAMETER_1 = VALUE], [PARAMETER_2 = VALUE], ...
- Scenario 2 ([NAME]): [PARAMETER_1 = VALUE], [PARAMETER_2 = VALUE], ...
- Scenario 3 ([NAME]): [PARAMETER_1 = VALUE], [PARAMETER_2 = VALUE], ...

[SHARED_CALCULATION_STRUCTURE]: For each scenario, calculate:
- [METRIC_1]: [DEFINITION]
- [METRIC_2]: [DEFINITION]
- [METRIC_3]: [DEFINITION]

[DECISION_CRITERION]: Prefer the scenario that [ACHIEVES_DEADLINE / MAXIMIZES_MARGIN / STAYS_WITHIN_THRESHOLD / MINIMIZES_COST].

[CONSTRAINTS]:
- [OPERATIONAL_CONSTRAINT: e.g., no overtime, no second shift]
- [FINANCIAL_CONSTRAINT: e.g., budget cap, COGS proportionality]
- [TIMING_CONSTRAINT: e.g., advance-notice lead time required for a schedule change]

[OUTPUT_REQUIREMENTS]:
1. Scenario comparison [tab / table] with all calculated metrics side-by-side
2. Visual chart comparing [METRIC — e.g., scenario favorability, cost comparison]
3. Written summary ([N] sentences / [N] pages): name preferred scenario and justify with [QUANTITATIVE] and [QUALITATIVE] reasoning
```

## 4. Reference File Requirements

### File Types Needed
- **Baseline data file (xlsx):** Contains the historical or current figures that scenarios will be built from — open purchase orders, quarterly sales and shipment projections, current MSRPs and COGS, reimbursement values, or production capacity data.
- **Price/parameter reference (pdf, optional):** Wholesale price lists, reimbursement schedules, competitor pricing data (for pricing benchmark scenarios), or freight/lease parameter documents.
- **No reference file (inline parameters):** For lease scenario modeling and some pricing models, all scenario parameters are provided directly in the prompt, with no reference file needed.

### Data Characteristics
For production scenarios: weekly time-series data with demand hours, capacity, and balance columns; purchase order tables with product SKU, quantities, and dates. For commercial terms scenarios: quarterly sales and shipment projections for a new account, with revenue and volume figures. For pharmacy scenarios: per-medication reimbursement values and wholesale drug/supply costs from two separate PDFs. For pricing scenarios: SKU-level current MSRP and COGS data with product attributes (concentration, bottle size). Reference data is typically compact (10–100 rows) and directly drives scenario parameter values.

### File Complexity Spectrum
- **Minimal:** All parameters provided inline (no reference file). Three scenarios with 2–3 parameters each. Simple revenue or cost calculation. 1-page PDF output.
- **Moderate:** Single xlsx with quarterly projections or weekly production data. Three scenarios with 3–5 variable parameters. Excel output with comparison tab and embedded chart.
- **Complex:** Two PDFs (reimbursement + wholesale price) plus a SKU list xlsx, or a PO log plus a capacity sheet. Three scenarios requiring multi-step calculation chains. Excel with color-coded scenario tabs, dynamic formula design, and editable variable cells, plus an embedded written summary.

## 5. Output Specification

### Primary Deliverable
- **Format:** xlsx (Excel workbook) for quantitative scenario models; pdf (1–2 pages) for simpler cost-effectiveness analyses
- **Structure (Excel):** Either three scenario tabs (each with per-scenario calculations) plus a comparison/summary tab, OR a single-tab design with three parallel column groups representing each scenario, plus a chart and written summary section in the same workbook
- **Structure (PDF):** Comparative table showing all scenarios side-by-side with a calculated metric for each, plus a narrative recommendation section
- **Key quality signals:** Three structurally parallel scenario blocks with correct parameter application; shared calculation structure applied consistently across all scenarios; decision criterion correctly evaluated; chart present and labeled; written summary names the preferred scenario with explicit justification

### Secondary Deliverables (if any)
- Per-scenario written narrative explaining actions, implications, and on-time delivery assessment (embedded in spreadsheet, for production planning variants)
- Assumption list or decision-criterion definition in a separate section

### Gold Output Characteristics
All three scenarios use identical calculation structure with scenario-specific parameter values correctly substituted. The decision criterion is applied correctly (right threshold, right metric). The chart accurately represents the comparison metric across scenarios. The written summary is the specified length, names the preferred scenario by name, and provides a justification that references both quantitative results (which scenario optimizes the metric) and qualitative considerations (relationship value, operational feasibility, financial constraints). Color-coding or variable-cell formatting is applied as specified.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of parameters varied | 1 parameter per scenario | 2–3 parameters per scenario | 3+ parameters + operational constraint layers |
| Calculation chain length | Direct computation (1 step) | 2–3 step calculation chain | Multi-step sequential (daily scheduling, fill frequency, tiered pricing) |
| Reference files | No reference files (inline parameters) | Single xlsx | Two PDFs + one xlsx |
| Decision criterion | Simple (highest margin wins) | Threshold comparison (revenue diff < X) | Multi-criteria (deadline + cost + relationship) |
| Visual requirement | No chart | One chart in Excel | Multiple charts + color-coded scenario design + editable variables |
| Written output | 1–2 sentences | several-sentence summary embedded in Excel | 1–2 page PDF narrative with table + recommendation |
| Domain-specific constraints | None | One constraint (budget cap, no overtime) | Multiple layered constraints (timing, labor, financial, statutory holidays) |

## 7. Boundary Cases & Adjacent Patterns

**Most similar patterns:**
- **A3 (NPV/IRR Investment Evaluation):** The most structurally similar pattern. A3 evaluates options using time-value-of-money calculations (DCF, NPV, IRR) over a multi-year horizon. A4 compares scenarios on current-period metrics (revenue, margin, cost, operational feasibility) without discounting. If the key calculation involves a discount rate applied to future cash flows, use A3; if all calculations are at current or single-period values, use A4.
- **A6 (Retail Planning & Forecasting):** Both involve projections and constraint satisfaction in Excel. A6 is specifically about open-to-buy, store-level sales forecasts, and inventory planning with retail-specific constraints (turn targets, EOM caps, week-weighting). A4 is broader — it covers any multi-scenario commercial or operational comparison. If the task is retail merchandise planning with OTB budgets and turn rate targets, use A6; for general multi-scenario commercial or operational modeling, use A4.
- **A5 (Operational Metrics Dashboard):** A5 produces a dashboard from historical/operational data; A4 models forward-looking scenarios. If the task requires PivotTables and charts summarizing what happened, use A5. If the task models what would happen under different parameter choices, use A4.

**Key distinguishing signal:** A4 always has three or more named scenarios with explicitly varied parameters, a shared calculation structure applied to each, and a written recommendation. If there is only one scenario being constructed (even if complex), or if the comparison is backward-looking (analyzing what happened), the task belongs to a different pattern.
