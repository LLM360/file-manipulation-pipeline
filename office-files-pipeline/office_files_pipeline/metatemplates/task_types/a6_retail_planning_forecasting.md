# Retail Planning & Forecasting Models

**Macro Category:** A — Financial Analysis & Modeling
**Pattern ID:** A6

## 1. Pattern Description

The worker builds a forward-looking Excel model for retail merchandise or inventory planning: open-to-buy receipt distribution, store-level weekly sales forecasts, wholesale order fulfillment analysis, or distributor inventory replenishment. The cognitive core is constraint satisfaction across multiple simultaneous requirements — budget caps, turn rate targets, EOM inventory ceilings, week-weighting allocations, minimum order floors, and active/closed store filters — while applying a defined trending methodology (STD trend, rate-of-sale calculation, prior-year baseline). What distinguishes this pattern from general scenario analysis (A4) is its retail-specific vocabulary and methodology: open-to-buy (OTB), sell-through (ST%), weeks of supply (WOS), inventory turn, comp store vs. total store, and the 4-5-4 retail calendar. The output is always an Excel model with forward projections, calculated aggregations, and usually a brief written commentary explaining key findings.

## 2. O*NET Grounding

### Occupation Families
- 13-1022.01 — Merchandise Planners — open-to-buy models, store-level sales plans, inventory turn optimization
- 13-1022 — Wholesale and Retail Buyers — account-level OTB, seasonal receipt planning
- 41-4012 — Sales Representatives, Wholesale and Manufacturing — wholesale order fulfillment analysis, PO management
- 13-1081 — Logisticians — distributor inventory replenishment and days-of-supply calculations
- 13-2051 — Financial Analysts — inventory sufficiency analysis, gap reporting

### Key Work Activities (O*NET vocabulary)
- Forecasting Sales and Revenues
- Analyzing Sales Data and Market Conditions
- Planning Inventory and Merchandise
- Processing Information
- Analyzing Data or Information
- Making Decisions and Solving Problems

### Knowledge Domains (O*NET vocabulary)
- Sales and Marketing
- Mathematics
- Economics and Accounting
- Transportation (for logistics/replenishment contexts)
- Administration and Management

### Generalizable Work Context
Planning, buying, or sales operations functions at retail or wholesale companies where a merchandise planner, wholesale analyst, or sales rep is responsible for a recurring planning or reporting deliverable. The trigger is a seasonal or periodic planning event: building the season's receipt plan, forecasting next month's store-level sales, reconciling a fiscal month's order fulfillment, or assessing distributor inventory ahead of a critical sales window. Multiple constraint parameters are provided — budget, turn target, EOM cap, minimum floor, week weights — and the planner must satisfy all of them simultaneously while applying a specified forecasting methodology. The audience is a planning director, account manager, or distributor partner.

## 3. Prompt Construction Template

### Persona Pattern
Assign a retail or wholesale planning role: Merchandise Planner (department store or specialty retail), Divisional Merchandise Manager (omnichannel), Wholesale Sales Analyst (apparel or fragrance company), or Sales Representative (beverage or consumer goods distributor). The role should imply access to prior-year sales data, inventory data, and specific planning constraint parameters. The persona should be familiar with retail-specific metrics and calendar conventions.

### Scenario Pattern
The worker is building a forward-looking plan for a defined period (a season, a fiscal month, or through end of a specific date). Multiple reference files provide last year's data, store status information, shipment schedules, and rate-of-sale history. A set of planning constraints is specified (OTB budget, turn rate target, EOM inventory cap, week-weighting percentages, minimum order quantity, rounding rule). A forecasting methodology is defined (apply STD trend to LY sales, compute rate-of-sale from last 4 weeks, project OOS date from current inventory). The output must satisfy all constraints simultaneously.

### Instruction Pattern
Describe the planning methodology first (how to forecast), then the constraints (what limits the forecast), then the output structure (what the Excel should look like). Specify aggregation hierarchy explicitly (by-door detail + Total/Closed/Comp roll-ups; by-SKU summary + OOS chart). Define all derived metrics with formulas. Specify rounding rules and minimums. Require a written commentary (1–2 sentences to a few sentences) in the output.

### Constraint Injection Points
- **Budget constraint:** total OTB dollar budget or gross receipt cap that receipts must not exceed
- **Turn rate target:** seasonal or monthly inventory turn target the model must achieve or exceed
- **EOM inventory cap:** ending inventory dollar or unit limit for the plan period's last month/week
- **Week-weighting targets:** percentage of monthly sales allocated to each week (ranges per week, e.g., a heavier first week tapering across the remaining weeks)
- **Topside constraint:** total plan must not exceed a percentage of prior year (e.g., a target percentage above or below LY comp)
- **Active/closed filter:** only active stores receive forecasted sales; closed stores are excluded from the plan but shown on aggregate lines
- **Rounding and floor rules:** rounding increment (nearest dollar amount, nearest pallet) and minimum value (a dollar floor, 1 pallet rounded up)
- **Rate-of-sale methodology:** definition of rate of sale (daily sold last 4 weeks × 7), date window, lookback period

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE]. [CONTEXT — e.g., responsible for the season's receipt plan; managing distributor inventory for the [BRAND] account].

[SCENARIO]: It is [DATE/PERIOD_CONTEXT]. You are [PLAN_TRIGGER — e.g., building the by-door weekly sales plan for a peak sales month; analyzing distributor inventory ahead of a critical month-end; forecasting next season's receipts].

[DATA_SOURCES]:
- [FILE_1]: [DESCRIPTION — e.g., LY weekly sales by store and STD sales data; current inventory and rate of sale by SKU]
- [FILE_2]: [DESCRIPTION — e.g., store matrix with active/closed status and anomaly notes; upcoming scheduled shipments]
- [FILE_3 (if applicable)]: [DESCRIPTION — e.g., pallet-to-case conversion ratios]

[FORECAST_METHODOLOGY]:
- Trend calculation: [FORMULA — e.g., TY STD / LY STD = STD trend; then apply to LY weekly sales]
- Rate of sale: [FORMULA — e.g., daily inventory sold (last 4 weeks) × 7]
- Projection basis: [REFERENCE_PERIOD — e.g., use Q3 LY through Q1 LY as projection basis]

[PLANNING_CONSTRAINTS]:
- Budget: [TOTAL_BUDGET or OTB_CAP]
- Turn rate target: [TARGET — e.g., an omni inventory turn rate to reach or exceed]
- EOM [inventory / stock] cap: [LIMIT — e.g., EOM inventory for the plan's final month capped at a set dollar level]
- Week-weighting targets: [W1: X–Y%, W2: X–Y%, W3–W4: X–Y% each]
- Topside: [TOTAL PLAN ≤ X% of LY for [comp / total] stores]
- Active/closed filter: [only active stores receive forecasted sales]
- Rounding: [nearest $X / nearest pallet, minimum $X / 1 pallet rounded up]

[OUTPUT_STRUCTURE]:
- By-[door / SKU / UPC] detail rows for [active / all] entries
- Aggregate rows: [Total, Closed, Comp] OR [SKU summary with OOS flag]
- Calculated columns: [METRIC_1 formula], [METRIC_2 formula], [PERCENT_CHANGE vs. LY]
- Visual: [chart showing METRIC — e.g., % OOS by UPC; OTB allocation by month]
- Written commentary: [N sentences] on [KEY_FINDINGS — e.g., total order value for the period and the impact of orders slipped to the next period]

[ANOMALY_HANDLING]: [Notes in store matrix / Exception items / Partial quantities must be applied as follows: ...]
```

## 4. Reference File Requirements

### File Types Needed
- **Last year (LY) sales file (xlsx):** Store-level or SKU-level weekly or monthly historical sales data, organized by identifier (store ID, UPC, SKU) with prior-year period values and optionally season-to-date (STD) totals.
- **Status/matrix file (xlsx):** Store status table (active/closed/comp flags, anomaly notes, store IDs) or inventory master (current stock, incoming shipments, rate-of-sale by SKU).
- **Conversion/parameter file (xlsx, optional):** Unit conversion reference table (pallets to cases) or shipment schedule (planned delivery dates and quantities by SKU).
- **PO log or shipment export (xlsx):** For order fulfillment analysis, a line-item or order-level file with planned and actual ship dates, order values, and shipped values.

### Data Characteristics
Historical sales files: one row per store or SKU, 4–52 weekly sales columns (or monthly periods), plus STD totals. Store matrix: one row per store with categorical status flags and notes. Inventory/shipment file: one row per SKU with numeric stock quantity, scheduled shipment dates, and rate-of-sale fields. For order fulfillment: one row per PO with start/cancel ship dates, PO value, actual ship date, and shipped value. Reference data typically spans 20–200 stores or 5–20 SKUs. Data must be clean enough to derive all required metrics without additional transformation beyond what is specified.

### File Complexity Spectrum
- **Minimal:** Single xlsx with a handful of SKUs, current inventory and rate-of-sale columns. Simple DOI and OOS-date calculation. Output is a single summary table with highlighted rows.
- **Moderate:** Two xlsx files (LY sales by store + store matrix). 20–50 stores, four weekly columns, STD trend application, week-weighting constraint, three aggregate roll-up lines, rounding rule. Output is a by-door plan with summary.
- **Complex:** Three xlsx files (LY sales, store matrix, shipment schedule) plus a conversion table. 100+ stores or 10+ SKUs. Multiple simultaneous constraints (budget + turn + EOM cap + week-weighting + topside). Omnichannel split (stores vs. e-commerce), anomaly handling, unit conversion, active/closed filtering, chart requirement, written commentary.

## 5. Output Specification

### Primary Deliverable
- **Format:** xlsx (Excel workbook)
- **Structure:** By-entity detail rows (stores, SKUs, or UPCs) plus aggregate roll-up rows (Total, Closed, Comp; or overall total). Calculated columns for all derived metrics (forecasted sales, percent change vs. LY, percent shipped, weeks of supply, percent OOS). At least one chart (OOS by UPC, receipt distribution by month) for inventory health or distribution analysis variants. Written commentary section (1–2 sentences to a short paragraph).
- **Key quality signals:** Constraint satisfaction verifiable — budget total does not exceed cap; turn rate calculated correctly; EOM inventory within limit; week-weighting percentages within specified ranges; topside not exceeded. Rounding applied correctly. Active/closed filter correctly applied. Anomaly notes from store matrix are correctly handled.

### Secondary Deliverables (if any)
- Separate email or commentary cell explaining the key finding from the plan (e.g., "period-to-date shipped orders total $X; orders slipped to the next period represent $Y impact")

### Gold Output Characteristics
All constraints satisfied simultaneously: budget not exceeded, turn target met, EOM cap respected, week weights within their ranges, topside not exceeded, rounding applied to specified increment with correct floor. Active stores only receive forecasted values; closed stores appear only in aggregate. Anomaly handling is applied correctly (e.g., closed stores flagged, partial quantities acknowledged). Aggregate roll-up lines (Total, Closed, Comp) sum correctly. Charts display the correct metric on the correct axis with labels. Written commentary is specific and quantitative (not generic).

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of simultaneous constraints | 1 (budget only) | 2–3 (budget + turn + EOM) | 4–5 (budget + turn + EOM + topside + week-weighting) |
| Number of reference files | 1 xlsx | 2 xlsx files | 3 xlsx files + conversion table |
| Granularity of plan | Total or category level | Store-level (20–50 entities) | Store-level (100+ stores) with active/closed filter and anomaly handling |
| Forecast methodology | Single trend factor | STD trend applied to LY weekly sales | Multi-period projection basis with historical quarterly reference |
| Unit conversion | None | One conversion (e.g., rate of sale from daily to weekly) | Full pallet-to-case conversion with lookup table |
| Omnichannel complexity | Single channel | Two channels with separate plans | Two channels with combined turn and EOM constraint |
| Aggregate hierarchy | Total only | Total + Comp | Total + Closed + Comp with separate calculations |
| Visual requirement | No chart | One chart | Chart + conditional highlighting for risk items |

## 7. Boundary Cases & Adjacent Patterns

**Most similar patterns:**
- **A4 (Scenario Analysis & Commercial Terms Modeling):** Both involve Excel models with constraints and projections. A6 is specifically about retail planning with retail-domain methodology (OTB, turn, STD, WOS, week-weighting, comp store). A4 covers general multi-scenario commercial or operational comparisons. If the task uses retail-specific vocabulary and methodology with OTB budgets and turn rate targets, use A6. If the task compares three named scenarios with varied commercial or operational parameters, use A4.
- **A5 (Operational Metrics Dashboard):** A5 produces a backward-looking summary of what happened (PivotTables, conditional formatting, KPI summaries). A6 produces a forward-looking plan of what will happen (forecasts, receipts, replenishment). If the task is analyzing historical sales data, use A5. If the task is building a forward projection or receipt plan, use A6.
- **A1 (Audit Sampling):** A6 variants involving order fulfillment analysis (which orders shipped within the target window? which slipped to the next period?) can resemble A1's filtering logic. The distinction is purpose: A1 filters to identify compliance anomalies; A6 filters to build a planning or performance summary. If the filtered output feeds a planning decision (replenishment, receipt allocation), use A6; if it flags exceptions for compliance review, use A1.

**Key distinguishing signal:** A6 always involves retail-domain planning vocabulary (OTB, turn, STD, WOS, comp/closed, week-weighting, EOM cap) and produces a forward-looking projection or receipt plan. The simultaneous satisfaction of multiple numerical constraints is the defining cognitive challenge.
