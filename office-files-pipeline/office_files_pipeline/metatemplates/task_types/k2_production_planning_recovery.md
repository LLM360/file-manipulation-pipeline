# Production Planning & Recovery Scheduling

**Macro Category:** K — Scheduling, Space Planning & Logistics
**Pattern ID:** K2

## 1. Pattern Description

The worker builds a forward-looking production plan that sequences operations, manages capacity constraints, and projects when a backlog or set of open orders will be fulfilled. The trigger is typically a demand-supply gap — the operation is behind on orders, a new product trial is being launched, or capacity is changing — and the task is to produce an explicit day-by-day or week-by-week plan showing how output ramps up, when targets are met, and what conditions govern each phase. The cognitive core is sequential constraint reasoning: daily output rates, priority ordering of orders, financial constraints (e.g., no overtime), holiday exclusions, capacity change milestones, and catch-up thresholds must all be integrated into a coherent timeline. This pattern is distinct from K1 (Workforce Scheduling) in that the scarce resource is production capacity (machine hours, output units) rather than human coverage; and distinct from A4 (Scenario Analysis) in that the scenarios are operationally grounded in real manufacturing constraints rather than commercial or financial parameters.

## 2. O*NET Grounding

### Occupation Families
- 11-3051 Industrial Production Managers — own the production planning process; responsible for capacity, output targets, and delivery commitments
- 51-1011 First-Line Supervisors of Production and Operating Workers — translate production plans into daily assignments; often the direct author of catch-up plans
- 43-5061 Production, Planning, and Expediting Clerks — maintain production schedules, track open orders, and update plans as capacity changes
- 17-2112 Industrial Engineers — design and analyze production flow, capacity models, and scheduling systems

### Key Work Activities (O*NET vocabulary)
- Scheduling Work and Activities
- Analyzing Data or Information
- Making Decisions and Solving Problems
- Coordinating Work and Activities of Others
- Monitoring Processes, Materials, or Surroundings
- Estimating the Quantifiable Characteristics of Products, Events, or Information

### Knowledge Domains (O*NET vocabulary)
- Production and Processing
- Mathematics
- Administration and Management
- Engineering and Technology
- Personnel and Human Resources (for labor-constrained scenarios)

### Generalizable Work Context
A manufacturing or production operation facing a demand-supply mismatch: either accumulated backlog from a capacity shortfall, a new product introduction requiring validation runs, or a capacity change (new equipment, extended shifts, product transfers) that must be sequenced correctly. The task is triggered by a manager's request for a formal plan before an operations review meeting, a customer deadline, or a trial launch date. Stakeholders include production managers, plant managers, quality/engineering teams (for validation runs), and customer-facing logistics or sales teams who need shipping date commitments.

## 3. Prompt Construction Template

### Persona Pattern
Assign a production supervisor, production manager, or first-line operations lead with direct knowledge of the operation's daily output rates and order backlog. The persona should be the person accountable for both the plan and communicating it to management. Seniority: supervisor to manager level. The role should imply familiarity with the specific manufacturing process (welding, extrusion, automotive parts assembly, food processing, etc.) to ground domain authenticity.

### Scenario Pattern
The scenario establishes: (1) the current production state (backlog size, current capacity, reason for gap), (2) one or more capacity milestones that will occur during the planning horizon (e.g., equipment upgrades, shift changes, product cell transfers), (3) business constraints that cannot be violated (no overtime, customer deadline, financial restriction), and (4) priority ordering if multiple products or order types are involved. The task is to produce the plan before an operations meeting or before communicating a commitment to a customer.

### Instruction Pattern
Instructions specify the output structure (Excel with one or more scenario tabs), the time granularity (daily or weekly), the metrics to track per row (planned output, cumulative output, open orders remaining, catch-up flag), and any written narrative to accompany the plan (scenario summaries, email body). For multi-scenario tasks, each scenario is defined with its specific parameters. Instructions are most effective as a numbered list of constraints followed by numbered scenario definitions.

### Constraint Injection Points
- **Daily/weekly output rate:** single fixed rate vs. rate that changes at a milestone date vs. multiple rates across scenarios
- **Priority ordering:** single product (simple) vs. two products with sequencing rules (moderate) vs. three+ products with interdependencies (complex)
- **Financial constraints:** no overtime allowed, no second shift, budget cap on additional labor
- **Date constraints:** customer shipping deadline, stat/federal holiday exclusions, capacity upgrade date, material arrival date
- **Catch-up definition:** varies from "no remaining backlog" to "completable within current week" to "all orders shipped before deadline"
- **Scenario count:** single plan (easy), two scenarios (moderate), three scenarios with comparative narrative (hard)
- **Input file complexity:** one file with a simple capacity table vs. five files cross-referencing BOM, tooling times, labor roster, and raw materials

### Structural Template

```
[PERSONA]: You are a [ROLE] at [FACILITY_TYPE] in [LOCATION]. Your operation produces [PRODUCT] and is currently [PROBLEM_STATE: e.g., X hours/units behind on open orders].

[SCENARIO]: [MANAGER/TRIGGER] has asked you to create a [PLAN_TYPE] starting [START_DATE]. The operation currently runs [CURRENT_CAPACITY] and has the following constraints:
- [CONSTRAINT_1: e.g., financial — no overtime pay authorized]
- [CONSTRAINT_2: e.g., capacity milestone — upgrade to X units/day on DATE]
- [CONSTRAINT_3: e.g., product priority — complete Product A backlog before Product B]
- [CONSTRAINT_4: e.g., date exclusions — exclude stat holidays and weekends]
- [CONSTRAINT_5: e.g., customer deadline — all POs must ship by DATE]

[DELIVERABLE]: Create an Excel workbook with [N] scenario tabs. Each tab must show:
- Date (excluding weekends and [HOLIDAY_LIST])
- Planned production per day ([PRODUCT_LINE breakdown if applicable])
- Cumulative production to date
- Open purchase orders remaining
- Catch-up status flag (yes/no or date achieved)

[SCENARIO DEFINITIONS]:
Scenario 1 — [NAME]: [SPECIFIC PARAMETERS — daily rate, constraints active]
Scenario 2 — [NAME]: [SPECIFIC PARAMETERS — daily rate, constraints active]
Scenario 3 — [NAME]: [SPECIFIC PARAMETERS — daily rate, constraints active]

[WRITTEN SUMMARY]: For each scenario, provide [2–4 sentences] explaining the approach, implications for each product line, and whether the scenario achieves [DEADLINE/TARGET] on time.

[REFERENCE FILES]: [LIST of attached files with descriptions]

[OUTPUT SPECIFICATION]: Excel workbook with [N] tabs (one per scenario), plus [optional summary/email] as [format].
```

## 4. Reference File Requirements

### File Types Needed
- **Capacity/demand time-series file (xlsx):** Weekly or daily columns with demand hours/units, current capacity, weekly balance, and cumulative balance; the primary data source for understanding the gap and extending the plan forward
- **Open purchase orders listing (xlsx):** Per-order rows with product SKU, order quantity, and required ship date; used to establish priority and calculate when each order will be fulfilled
- **Bill of Materials / FG BOM (xlsx):** Finished goods components and quantities; used in validation-run planning to determine what materials are needed per production batch
- **Labor/team roster (xlsx):** Names, skill levels, or rankings for allocation to specific machines or tasks; relevant when the plan involves assigning operators to specific press runs or production stages
- **Tooling changeover times (xlsx):** Time required to switch between product configurations; affects daily effective output and sequencing decisions
- **Product specification document (docx):** Batch sizes, output yields, process parameters for a specific product; used in food/chemical/extrusion manufacturing to anchor the throughput calculation

### Data Characteristics
The core quantitative structure is a time-series table: rows are days or weeks, columns are metrics (demand, capacity, balance, open orders). The planning horizon is typically 4–20 weeks (daily) or 6–52 weeks (weekly). Open order datasets are typically 5–50 rows with 3–5 attributes per order (SKU, quantity, date, priority). BOM files are 5–30 rows. Tooling changeover tables are matrices of product-to-product transition times (5×5 to 20×20). All numeric values should be realistic for the industry: welding output measured in standard hours per day; automotive or parts assembly measured in units per day; food processing in pounds per batch.

### File Complexity Spectrum
- **Minimal:** Single xlsx with weekly demand vs. capacity columns and a cumulative balance; one product; one scenario; no holiday exclusions
- **Moderate:** Open PO listing with 10–20 orders across two product lines; single capacity milestone date; two scenarios; Canadian or US statutory holidays to exclude; written summary required
- **Complex:** Five cross-referenced files (BOM, tooling times, labor roster, raw materials inventory, partially completed plan template); two parallel machines to be sequenced; three scenarios with distinct capacity and labor assumptions; detailed per-scenario narrative required; validation quantities only (no buffer)

## 5. Output Specification

### Primary Deliverable
- **Format:** Excel workbook (.xlsx)
- **Structure:** One tab per scenario (if multi-scenario) or one main planning tab; rows = time periods; columns = production metrics; catch-up milestone row or flag column visible inline
- **Key quality signals:** Daily output totals are arithmetically correct and respect capacity constraints; cumulative totals agree with daily rollup; open orders decrease correctly as production progresses; catch-up date is accurately identified; holiday/weekend exclusions are applied correctly; scenario differences are clearly delineated

### Secondary Deliverables (if any)
- Written scenario summaries embedded in the workbook or in a companion email/memo (2–4 sentences per scenario): explains approach, product-line implications, and on-time delivery assessment
- Brief email body to plant manager summarizing the recommended plan and key risks

### Gold Output Characteristics
A gold output produces a day-by-day (or week-by-week) plan where every numerical cell is arithmetically verifiable: planned production × active days = cumulative increase, open POs decrease by exactly the planned production each period, capacity constraints are never violated. The catch-up date is pinpointed accurately. Holiday and weekend exclusions are applied correctly to the calendar. In multi-scenario outputs, the scenarios differ exactly as specified (different daily rates, different constraints active) and the narrative accurately describes what each scenario achieves relative to the deadline.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of scenarios | 1 | 2 | 3+ with full comparative narrative |
| Number of product lines | 1 | 2 with priority ordering | 3+ with interdependencies |
| Capacity changes during horizon | None (fixed rate) | One milestone (rate change on date X) | Multiple milestones with different triggers |
| Input file count | 1 (demand/capacity table) | 2–3 (PO list + capacity + one constraint file) | 5 cross-referenced files (BOM, tooling, roster, materials, template) |
| Date constraints | No holidays | US/Canadian stat holidays excluded | Multiple constraint types (holidays + material arrival + notification lead times) |
| Financial constraints | None | No overtime | No overtime + no second shift + specific capacity ceiling |
| Written narrative requirement | None | 2-sentence summary | Per-scenario narrative covering actions, product-line implications, and delivery assessment |

## 7. Boundary Cases & Adjacent Patterns

**K1 (Workforce Scheduling with Constraint Satisfaction):** The boundary is the primary resource. K2 schedules production output volume (units, hours, batches); K1 schedules personnel coverage (who works which day). A borderline case may combine workforce scheduling (staff allocated across roles) with production sequencing (equipment cycle scheduling). The deciding factor is whether the dominant output is a staffing calendar or a production output timeline — if the latter, classify as K2.

**A4 (Scenario Analysis & Commercial Terms Modeling):** Both K2 and A4 can produce multi-scenario Excel outputs. The distinction is operational vs. commercial grounding. K2 scenarios vary daily output rates, capacity milestones, and physical constraints; A4 scenarios vary pricing terms, margin thresholds, or commercial structures. If the scenarios are driven by machine capacity and production sequencing, use K2. If they are driven by financial terms and business decisions, use A4.

**B5 (Data Entry with Protocol-Driven Decision Making):** A closely related boundary case is populating a pre-built template by reading rules embedded in the file and cross-referencing several other reference documents. When the task is primarily "populate a given template from multiple reference files using embedded rules," it belongs in B5 regardless of the manufacturing context. When the task requires designing the schedule logic from scratch, it is K2.

**A5 (Operational Metrics Dashboard / KPI Reporting):** If the production data is being aggregated into a dashboard to report on past performance (PivotTables, charts, KPIs), use A5. K2 is forward-looking: the plan projects what will happen, not what did happen.
