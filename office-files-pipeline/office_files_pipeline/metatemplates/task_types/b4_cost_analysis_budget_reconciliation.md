# Cost Analysis & Budget Reconciliation Reports

**Macro Category:** B — Data-Driven Document Authoring
**Pattern ID:** B4

## 1. Pattern Description

The worker analyzes cost, rate, or budget data from reference files to produce a quantitative cost breakdown, budget variance analysis, or cost-effectiveness comparison, accompanied by a written summary or recommendation. The core cognitive sequence is: read rate or cost data from an attached file, apply defined calculation logic (rate × quantity, cost sharing formula, projected escalation factor), and synthesize findings into a structured document that supports a business or operational decision. What distinguishes B4 from pure financial modeling (Macro A) is that the output always includes a narrative document or written summary — not just an Excel model — and the analytical work is grounded in operational or programmatic cost data (production capacity, production rate, service rate cards, carrier pricing) rather than financial statements. The written component communicates not just what the numbers are but what they mean for planning, budgeting, or program viability.

## 2. O*NET Grounding

### Occupation Families
- 51-1011 First-Line Supervisors of Production and Operating Workers — production supervisors analyzing weekly capacity data to build a catch-up plan with written email summary
- 11-9111 Medical and Health Services Managers — health managers building cost-sharing proposals with embedded cost savings graphs for inter-departmental programs
- 27-2012 Producers and Directors — video producers building crew and equipment cost estimates from service rate cards for client proposals
- 11-3071 Transportation, Storage, and Distribution Managers — shipping managers projecting carrier costs using historical rate escalation data and volume projections
- 13-2031 Budget Analysts — analysts reconciling updated cost figures against budgeted amounts and drafting variance explanations

### Key Work Activities (O*NET vocabulary)
- Analyzing Costs and Expenditures
- Preparing Budgets and Cost Estimates
- Analyzing Data or Information
- Making Decisions and Solving Problems
- Communicating with Supervisors, Peers, or Subordinates
- Documenting Information
- Developing Objectives and Strategies

### Knowledge Domains (O*NET vocabulary)
- Mathematics
- Administration and Management
- Economics and Accounting
- Production and Processing (for manufacturing variants)
- Transportation (for logistics/carrier variants)
- Communications and Media (for production/entertainment variants)
- Medicine and Dentistry (for healthcare program variants)

### Generalizable Work Context
A manager, analyst, or coordinator receives a directive — from a department head, client, or CEO — to evaluate the cost implications of a specific operational or programmatic decision. A reference file provides the raw cost inputs (rate cards, budget line items, historical rate increase data). The worker must apply the correct calculation chain and produce both a quantitative output (cost breakdown table or spreadsheet) and a written explanation that makes the findings actionable for the decision-maker. Typical triggers: a catch-up plan for an overloaded operation, a cost-sharing proposal for a new program, a vendor selection decision, or a budget cycle update.

## 3. Prompt Construction Template

### Persona Pattern
Assign a managerial or analytical role with budget or cost authority within the relevant operational domain. The role should be plausibly the one who both runs the numbers and communicates them upward — a production supervisor writing to their manager, a health manager preparing a departmental proposal, a producer quoting a client, a shipping manager presenting to leadership. The org type grounds the cost vocabulary: manufacturing plant, hospital department, entertainment/production company, logistics operation.

### Scenario Pattern
The cost analysis is triggered by an operational need: a production shortfall requiring overtime planning, a proposed new inter-departmental program needing cost justification, a client requesting a production budget, or a business planning cycle requiring carrier cost projections. Name the specific cost drivers being modeled (number of participating departments, shoot days, package sizes and volumes, overtime days). Specify what the written output will be used for (email to manager, formal proposal to other departments, client quote, business planning presentation).

### Instruction Pattern
Describe the calculation chain step-by-step: which cost inputs come from the attached file, what formulas apply (rate × quantity, cost divided by participants, projected price = current price × (1 + average annual increase)), and what the output table structure should look like. Specify which findings must be included in the written summary (key cost changes, delta vs. baseline, recommendation for action). Include any visual requirements (embedded graph showing savings vs. number of participants; side-by-side carrier cost table).

### Constraint Injection Points
- **Rate card scope:** which cost items come from the attached file vs. which are given in the prompt parameters
- **Calculation parameters:** numerical constants provided (hours/day, overage percentage, volume projections, historical rate increase years)
- **Cost exclusions:** items to exclude from the calculation (e.g., a specific production phase, a pay category, or particular budget line items excluded from scope)
- **Scenario count:** single scenario vs. multiple scenarios to compare (e.g., varying counts of participants, or several size/category tiers)
- **Visual requirement:** whether a chart or graph must be embedded in the document
- **Written output type:** email body vs. formal proposal section vs. executive summary

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE]. [BRIEF_CONTEXT — role authority over the cost domain].

[SCENARIO]: [TRIGGER_EVENT — e.g., "Your manager has asked you to build a cost analysis for [PROGRAM/OPERATION]" or "You have been asked to propose [COST_SHARING_ARRANGEMENT] to [PARTNER_DEPARTMENTS]"].

[DATA_SOURCE]:
- Attached file: [FILE_DESCRIPTION — e.g., "an Excel rate card containing [ROLE/EQUIPMENT] fees per [TIME_UNIT]" or "a budget spreadsheet with [COST_LINE_ITEMS] for [PROGRAM]"]

[CALCULATION_TASK]:
Using the attached data:
1. [STEP_1 — e.g., "Calculate the total cost for [SCOPE] using the rate card, with the following crew configuration: [SPECIFICATION]"]
2. [STEP_2 — e.g., "Apply [FORMULA] to project [COST_DIMENSION] across [SCENARIOS]"]
3. [STEP_3 — e.g., "Compare total cost under each scenario against [BASELINE or ALTERNATIVE]"]

[PARAMETERS]:
- [PARAM_1 — e.g., "Crew: [ROLES], no [EXCLUDED_ROLES]"]
- [PARAM_2 — e.g., "Setup time: [N] hours per shoot day"]
- [PARAM_3 — e.g., "Volume projections: [SIZE_A]: [N] units, [SIZE_B]: [N] units"]
- [EXCLUSION_RULE]

[OUTPUT_SPECIFICATIONS]:
1. [QUANTITATIVE_OUTPUT — e.g., "Excel spreadsheet with line-item cost breakdown including [COLUMNS]"]
2. [WRITTEN_OUTPUT — e.g., "Brief written summary / email body / proposal section (a few sentences) explaining the [RECOMMENDATION or KEY_FINDING]"]
3. [VISUAL_OUTPUT if applicable — e.g., "Graph showing [SAVINGS or COST_COMPARISON] by [DIMENSION]"]

[CONSTRAINTS]:
- [FORMAT_CONSTRAINT]
- [EXCLUSION_CONSTRAINT]
- [SCOPE_BOUNDARY]
```

## 4. Reference File Requirements

### File Types Needed
- **Rate card or cost schedule (xlsx or pdf):** The primary cost input — a table of rates by role, equipment, package size, or service type. Must contain enough specificity for the worker to compute a line-item budget (e.g., hourly or daily rates by crew role; shipping costs by carrier and package size; shared-program cost line items with per-unit and recurring fees).
- **Operational parameters file (xlsx, optional):** Contains the volume or quantity inputs to be applied against the rate card (weekly demand/capacity hours; video series list; annual shipment volumes by package size; historical rate increase percentages by year and carrier).
- **Background context document (docx or email thread, optional):** Contains program narrative, prior cost estimates, or email thread with relevant cost parameters — provides context for which costs are in scope and what the baseline is for comparison.

### Data Characteristics
The rate card should contain 5-20 line items organized by a cost driver dimension (crew role, equipment type, carrier, package size, program participant count). Each line item should have a unit rate and optionally a multiplier field (hours, days, units). The operational parameters provide the multiplicands — volume, days, participants — that convert unit rates into total costs. When a multi-scenario comparison is required, the parameter file or prompt should provide 2-5 scenario configurations to compute. Data should be internally consistent but require calculation (not pre-totaled).

### File Complexity Spectrum
- **Minimal:** Single rate card with 5-8 line items, single scenario, fixed quantity parameters provided in the prompt. Written output is 2-3 sentences. No graph required.
- **Moderate:** Rate card with 10-20 line items, 2-3 scenarios, quantity parameters from a secondary file. Written summary is a formal email or proposal section (1 paragraph). One simple comparison table in the output.
- **Complex:** Rate card plus historical time-series data requiring averaging and projection, 4-5 carrier/scenario combinations with exclusion logic, volume-weighted total cost calculation, visual chart required in document, multi-component written proposal with a structured section on cost savings vs. a baseline.

## 5. Output Specification

### Primary Deliverable
- **Format:** Excel spreadsheet (cost breakdown table) plus Word document (written summary, email, or proposal section); sometimes a Word or PDF document with an embedded graph
- **Structure:** Line-item cost table (crew role / equipment / package size × rate × quantity = subtotal; total row at bottom); written component covering key findings, cost change narrative, and recommendation; optional chart showing cost comparison across scenarios or savings vs. number of participants
- **Key quality signals:** All rate inputs traced back to the attached file (no fabricated rates); calculation chain is correct (rate × quantity, no double-counting, correct exclusions applied); written summary accurately describes the quantitative findings and makes a clear recommendation; visual element (if required) correctly represents the data in the table

### Secondary Deliverables (if any)
- Email draft to manager or partner departments (typically 2-5 sentences or a short paragraph summarizing plan and rationale)
- Separate scenario tabs in Excel for each planning scenario (e.g., one tab per participating department count; one column set per carrier)

### Gold Output Characteristics
A gold output applies the rate card correctly to all in-scope line items, excludes all items explicitly out of scope, produces totals that are arithmetically correct, presents the cost breakdown in a clear structured format, and writes a summary that accurately reflects the numbers without adding unsupported claims. For multi-scenario tasks, all scenarios are computed and the comparison is presented in a way that makes the recommendation obvious. The written component is concise and appropriate in register for its intended audience (manager email vs. departmental proposal vs. executive summary). If a graph is required, it correctly visualizes the relevant cost dimension.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Rate card line items | 5-8 | 10-15 | 20+ with tiered pricing or exclusion logic |
| Number of scenarios | 1 | 2-3 | 4-5 with different configurations and availability constraints |
| Quantity inputs | Given directly in prompt | Provided in secondary file | Computed from historical data (e.g., average rate increase from a multi-year time series) |
| Calculation complexity | Rate × quantity per line | Multi-step (hours × days × rate + setup time) | Volume-weighted projection with availability exclusion per scenario |
| Written output length | 2-4 sentences (email body) | 1-2 paragraph summary | Multi-section proposal with embedded graph and narrative per section |
| Visual requirement | None | Simple comparison table | Chart embedded in Word document (savings by participant count) |
| Cost exclusions | None | 1-2 specified exclusions | Multiple explicit exclusions with scope boundary definition |

## 7. Boundary Cases & Adjacent Patterns

**A4 (Scenario Analysis & Commercial Terms Modeling):** A4 is a pure Excel financial model comparing multiple commercial or operational scenarios, where the model itself is the deliverable. B4 always includes a written summary or proposal document as a required output alongside the quantitative file. If there is no narrative document and the deliverable is purely an Excel model, use A4.

**A3 (NPV/IRR & Investment Evaluation):** A3 uses DCF methodology and financial investment frameworks (NPV, IRR, payback period). B4 uses operational cost analysis — rate cards, production rates, carrier pricing, program cost sharing — without discounted cash flow mechanics. If the task involves investment appraisal techniques, use A3.

**B3 (Compliance Report from Transaction Data):** B3 cross-references data against regulatory criteria to identify violations. B4 applies rate cards or cost parameters to compute a budget or cost estimate. Both produce written documents alongside data files, but B3 is about compliance violations while B4 is about cost planning and reconciliation.

**B1 (Performance Analysis Presentation):** B1 translates analysis into a slide presentation. B4 produces Excel cost breakdowns and Word documents or email summaries. If the deliverable is a presentation deck rather than a cost analysis document, use B1. Some tasks may blend the two (a cost proposal with an embedded graph in Word) — classify by the primary document type.
