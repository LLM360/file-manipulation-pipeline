# NPV/IRR & Investment Evaluation

**Macro Category:** A — Financial Analysis & Modeling
**Pattern ID:** A3

## 1. Pattern Description

The worker builds a financial model comparing two or more discrete investment options (vendors, capital projects, product lines, partnership tiers) using discounted cash flow frameworks — NPV, IRR, or gross margin projection — and concludes with a recommendation that cites both quantitative results and qualitative considerations. The cognitive core is correctly structuring the financial model for each option: applying discount rates, amortizing upfront costs over the right period, splitting volume across variants or tiers, and then presenting results in a side-by-side comparison. What distinguishes this pattern from general financial statement construction is the evaluation-and-recommendation structure: the analysis is explicitly comparative, each option gets its own calculation block, and the output always includes a summary with a stated preference. The deliverable ranges from a pure Excel workbook with per-option tabs to a board-level PDF report drafted in Word.

## 2. O*NET Grounding

### Occupation Families
- 11-3061 — Purchasing Managers / Category Buyers — vendor NPV evaluation for sourcing decisions
- 13-2051 — Financial Analysts — capital investment analysis, NPV/IRR modeling
- 11-3031 — Financial Managers — board-level capital allocation and investment recommendation
- 11-2022 — Sales Managers / Enterprise Sales Directors — partnership revenue and margin projection models
- 11-9141 — Property and Real Estate Managers — leasing scenario evaluation (adjacent to A4)

### Key Work Activities (O*NET vocabulary)
- Analyzing Costs and Benefits
- Making Investment Decisions
- Preparing Financial Reports for Management
- Evaluating Suppliers or Partners
- Developing Financial Models
- Analyzing Data or Information

### Knowledge Domains (O*NET vocabulary)
- Economics and Accounting
- Mathematics
- Administration and Management
- Production and Processing (for manufacturing/procurement contexts)
- Sales and Marketing (for partnership/revenue projection contexts)

### Generalizable Work Context
Finance, procurement, or sales functions at established corporations (automotive, technology, real estate, B2B product companies) where a senior individual contributor or manager must evaluate a capital commitment or strategic partnership decision. The trigger is a specific business event: a new vehicle program requiring supplier nomination, an annual capital budgeting cycle, or a proposed distribution partnership. The audience is leadership (a finance controller, CFO, or Board of Directors) who needs a recommendation with documented assumptions. The analysis is forward-looking over a defined horizon (typically 1–10 years).

## 3. Prompt Construction Template

### Persona Pattern
Assign a senior individual contributor with decision-support responsibility: Senior Category Buyer (procurement), Senior Finance Manager (corporate finance), or Enterprise Sales Director (B2B partnerships). The role should imply access to cost/volume reference data and accountability for providing a structured recommendation to a named senior reviewer (finance controller, Board of Directors, VP of Sales). Seniority is mid-to-senior; the worker is expected to apply standard financial modeling conventions independently.

### Scenario Pattern
The organization is evaluating a specific decision that requires choosing among two or more alternatives. A reference document provides the financial parameters for each option (cost quotes, volume projections, pricing tiers, cash flow estimates). A defined evaluation framework is specified (NPV at a given discount rate, IRR compared to WACC, gross margin at a volume threshold). The output will be presented to a named senior audience as the basis for a formal decision.

### Instruction Pattern
For Excel-based outputs: specify a per-option calculation tab structure plus a comparison/summary tab. List the financial parameters for each option inline or reference the parameter document. State the modeling rules (discount rate, amortization logic, volume split, tier threshold) explicitly. Require that assumptions be listed. For document-based outputs (PDF board report): specify sections in order (analysis, recommendation, risk, allocation scenario), page limit, and addressee. In both cases, always require a stated recommendation with supporting rationale.

### Constraint Injection Points
- **Discount rate:** specific percentage applied to years 2+ (Year 1 is present value); WACC for IRR comparison
- **Amortization rule:** upfront tooling/R&D cost amortized over first N units, or split evenly between variants
- **Volume parameters:** total volume, variant split ratios (e.g., a base vs. premium variant split), annual projections over product life
- **Tier thresholds:** pricing changes above/below a unit volume threshold (e.g., sub-1,000 vs. over-1,000 units)
- **Recommendation requirement:** must name the preferred option and justify with both quantitative and qualitative reasoning
- **Page limit (document outputs):** maximum page count for board-level reports
- **Risk requirement:** top N risks with mitigation strategies required for recommended option

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_NAME/TYPE]. [INSTITUTIONAL_CONTEXT — e.g., responsible for supplier nominations for a new vehicle program; presenting to the Board of Directors].

[SCENARIO]: [ORG] is evaluating [N] [OPTION_TYPE — e.g., shortlisted suppliers, capital projects, partnership tiers] for [DECISION_CONTEXT]. [REFERENCE_DOCUMENT] provides the financial parameters for each option.

[TASK_DESCRIPTION]: Build an Excel workbook / draft a [DOCUMENT_TYPE] that:
1. Calculates [NPV/IRR/GROSS_MARGIN] for each option using the parameters below
2. Presents a side-by-side comparison [on a summary tab / in a comparison section]
3. Recommends [one option / capital allocation] with [quantitative + qualitative] justification
[4. Identifies the top [N] risks for the recommended option with mitigation strategies]
[5. Proposes a dual-investment scenario allocating $[AMOUNT] across both options]

[MODELING_RULES]:
- Discount rate: [X]% applied to [years 2–N]; Year 1 costs are at present value
- [AMORTIZATION_RULE]: [e.g., tooling cost amortized over a fixed unit volume regardless of variant]
- [VOLUME_RULE]: [e.g., a base/premium variant split and a total unit volume]
- [TIER_RULE]: [e.g., pricing tier applies above 1,000 units per fiscal year]
- Ignore inflation in all calculations
- List all assumptions explicitly [on the summary tab / in an appendix]

[OPTION_PARAMETERS]: [Reference the attached document OR provide inline as a table]

[OUTPUT_SPECIFICATION]:
- [Excel: One calculation tab per option named "[OPTION_NAME]"; one summary/comparison tab with recommendation and comments]
- [PDF: Maximum [N]-page report addressed to [AUDIENCE]; sections: [SECTION_LIST]]
```

## 4. Reference File Requirements

### File Types Needed
- **Cost/volume parameter document (docx or pdf):** Vendor quotation or investment proposal document containing per-option financial parameters: unit prices (by variant if applicable), upfront tooling or R&D costs, volume projections by year over the product lifecycle, or cash flow estimates.
- **Email correspondence (docx, optional):** For partnership/B2B scenarios, pricing and tier structure communicated via email format, including tiered cost schedules and product line breakdowns.
- **Inline parameters (no reference file):** For simpler variants, all financial parameters can be provided directly in the prompt (especially for 2-option models with straightforward cash flows).

### Data Characteristics
Reference documents contain structured cost data organized by option (vendor, project, product line): per-unit prices for one or more product variants, upfront capital costs (tooling, R&D, integration), annual volume projections over a 1–10 year horizon, and optionally a tiered pricing structure with a threshold. For board-report variants, the reference document describes two distinct investment opportunities with narrative context and financial parameters. The total parameter set is compact — typically 3–5 options × 5–10 financial parameters each.

### File Complexity Spectrum
- **Minimal:** Inline parameters for 2 options, single product variant, 3-year horizon, simple gross margin calculation. No reference file needed.
- **Moderate:** Single docx with vendor quotation data for 3 options, 2 variants each, multi-year volume projections, tooling amortization rule. Output is a multi-tab Excel workbook.
- **Complex:** PDF investment opportunity document for 2 capital projects requiring NPV and IRR, plus a dual-investment scenario allocating a defined capital amount across both projects. Output is a PDF board report, within a defined page limit, with risk analysis.

## 5. Output Specification

### Primary Deliverable
- **Format:** xlsx (Excel workbook) for quantitative vendor/project evaluation; pdf (Word converted to PDF) for board-level investment reports
- **Structure (Excel):** One calculation tab per option (named by option name), one summary/comparison tab with side-by-side NPV/IRR/margin values, stated recommendation, and assumption list
- **Structure (PDF):** Sections in order — executive summary, per-option analysis (NPV/IRR with direction estimates), recommendation with quantitative and qualitative justification, risk analysis (top N risks + mitigation), and optionally a dual-investment allocation scenario
- **Key quality signals:** Correct discount rate application (Year 1 at present value, Years 2+ discounted); correct amortization of upfront costs; correct volume splits applied to per-variant unit costs; stated recommendation names a specific option with both quantitative and qualitative reasoning

### Secondary Deliverables (if any)
- Assumption list embedded in summary tab or report appendix
- Risk register with mitigation strategies (for board-level variants)

### Gold Output Characteristics
NPV/IRR calculations correctly apply the specified discount rate to the correct cash flow timing. Upfront costs are correctly amortized (over first N units or as a lump sum in Year 1). Volume projections match the reference document exactly. For multi-variant models, variant volume splits are applied correctly to per-variant unit prices. The summary/comparison tab shows all options side-by-side with a clear recommendation naming the preferred option. Assumptions are all listed explicitly. For document outputs, the page limit is respected, the board is addressed directly, and risks are specific and actionable (not generic).

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of options | 2 options | 3 options | 3 options + dual-investment allocation scenario |
| Product variants | Single variant | 2 variants with volume split | 2 variants with split + tiered pricing threshold |
| Evaluation framework | Gross margin projection | NPV with given discount rate | NPV + IRR + WACC comparison |
| Amortization complexity | No upfront costs | Tooling amortized over first N units | Tooling + R&D with separate treatments, split by variant |
| Output format | Excel workbook only | Excel workbook with per-option tabs + summary | PDF board report with executive summary, risk analysis, and allocation scenario |
| Recommendation depth | Recommend one option with summary | Recommend with quantitative + qualitative justification | Recommend + top N risks with mitigation + dual-investment alternative |
| Reference file format | Inline parameters | Single docx/pdf with structured data | Multiple documents (pricing email + investment proposals) |

## 7. Boundary Cases & Adjacent Patterns

**Most similar patterns:**
- **A4 (Scenario Analysis & Commercial Terms Modeling):** Both involve multi-scenario Excel models with a recommendation. The distinction is analytical framework: A3 uses DCF/NPV/IRR or a defined investment return metric as the evaluation criterion; A4 compares scenarios on operational or commercial terms (margins, lease terms, production plans) without requiring a time-value-of-money calculation. Choose A3 when the core computation involves discounting cash flows over a multi-year horizon; choose A4 when the scenarios vary commercial parameters and the comparison is based on current-period metrics.
- **A2 (Financial Statement Construction):** A2 builds a historical or period-to-date financial report from source data; A3 builds a forward-looking model evaluating discrete alternatives. If the task involves reconciling to a GL balance or assembling actuals, it's A2; if it involves projecting future cash flows to compare options, it's A3.
- **B2 (Research-Based Report / Memo):** When the NPV/IRR analysis is embedded in a longer narrative document without a structured Excel model (e.g., a strategic memo), it may blur into B2. Choose A3 when a structured financial model with per-option calculations is the primary deliverable; choose B2 when the deliverable is primarily a narrative document that cites financial estimates without building a full model.

**Key distinguishing signal:** A3 always has (a) two or more discrete options being evaluated, (b) a defined financial metric (NPV, IRR, gross margin) computed for each, and (c) a stated recommendation. If any of these three elements is missing, the task belongs to a different pattern.
