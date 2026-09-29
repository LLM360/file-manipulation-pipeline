# Engineering Analysis & Simulation Reports

**Macro Category:** J — Software & Technical Implementation
**Pattern ID:** J6

## 1. Pattern Description

The worker is an engineer (mechanical, aerospace, civil, or chemical) who must perform a numerical simulation or engineering analysis on a specified physical system, produce multiple types of visualizations from the computational results, evaluate those results against pass/fail criteria or engineering margins, and deliver a technical report documenting the methodology, findings, and design recommendations. The cognitive core combines three distinct skills: numerical computation (executing the finite-difference, FEA, or CFD calculation correctly), technical judgment (interpreting results against engineering acceptance criteria), and technical communication (presenting findings in a concise, professional report suitable for a design review). Conditional logic is characteristic — recommendations are only issued when results fail or approach threshold limits.

## 2. O*NET Grounding

### Occupation Families
- **17-2011 Aerospace Engineers** — primary occupation for thermal/structural analysis of aerospace components
- **17-2141 Mechanical Engineers** — general-purpose engineering analysis across thermal, structural, and fluid domains
- **17-2131 Materials Engineers** — materials-specific analysis (thermal properties, composite behavior, creep, fatigue)
- **17-2051 Transportation Engineers** — domain-specific variant for structural analysis of transportation infrastructure
- **17-2199 Engineers, All Other** — civil and structural variants

### Key Work Activities (O*NET vocabulary)
- Analyzing data or information from engineering simulations and tests
- Evaluating information to determine compliance with engineering standards and acceptance criteria
- Documenting results in technical reports
- Designing or recommending engineering solutions to identified problems
- Using numerical methods and computational tools to solve engineering problems
- Interpreting scientific data to draw engineering conclusions

### Knowledge Domains (O*NET vocabulary)
- Engineering and Technology — finite difference methods, heat transfer theory, structural mechanics, materials behavior
- Physics — thermodynamics, fluid mechanics, continuum mechanics
- Mathematics — numerical analysis, matrix methods, differential equations
- Design — engineering drawing interpretation, component geometry, tolerance analysis

### Generalizable Work Context
An engineering team at an aerospace firm, manufacturing company, or infrastructure project needs a formal numerical analysis of a specific component or system. The trigger is a design review milestone, a safety margin verification, or a failure investigation. A formal analysis request (work order or technical specification) defines the component geometry, material properties, boundary conditions, and acceptance criteria. The worker performs the computation, generates required visualizations, evaluates results against margins, and produces a report that the design team and customer will review. If margins are tight or violated, design recommendations must be generated.

## 3. Prompt Construction Template

### Persona Pattern
Assign the worker as an engineer with a relevant specialization (mechanical engineer at an aerospace firm's materials lab, structural engineer at a civil infrastructure firm, process engineer at a chemical plant). Specify the organizational context (small aerospace firm, government lab, engineering consultancy) because this affects report formality and audience. State that the analysis will be used for a formal design review or safety verification.

### Scenario Pattern
Describe the physical component being analyzed (a heat shield, a structural bracket, a pressure vessel, a beam) and why the analysis is being performed (design verification, margin check, failure investigation, regulatory submission). Provide the reference file context (a formal analysis request document containing the boundary conditions and acceptance criteria). State the downstream use of the analysis (design review, customer deliverable, regulatory submission).

### Instruction Pattern
Provide the numerical parameters explicitly in the prompt (not hidden in reference files): number of nodes, node spacing, material properties (k, ρ, cp, E, ν), boundary conditions (temperatures, pressures, fluxes, heat transfer coefficients), time steps or load cases. List required visualizations explicitly by type (profile plots, contour plots, time-trace plots, summary tables). Specify pass/fail thresholds or acceptance criteria. State the conditional recommendation requirement: if margin < X, provide mitigation recommendations.

### Constraint Injection Points
- **Problem dimensionality:** 1D vs. 2D vs. 3D analysis
- **Number of nodes/elements:** 10–30 nodes (tractable by hand or simple code) vs. 100+ (requires computational tool)
- **Number of required time steps or load cases:** 2–4 vs. 8–12
- **Number of visualization types required:** 1 (table only) vs. 4 (profile + contour + time-trace + table)
- **Named nodes/locations to track:** 3 nodes vs. 10+ specific locations
- **Margin threshold and conditional logic:** fixed threshold (e.g., a maximum allowable temperature) vs. percentage margin (e.g., a percent-of-limit margin)
- **Reference file:** analysis request PDF provided vs. all parameters in prompt
- **Report formality:** internal memo vs. formal report with sections and referenced standard

### Structural Template

```
[PERSONA]: You are a [SPECIALIZATION: Mechanical Engineer / Structural Engineer / Process Engineer] at [ORG_TYPE: a small aerospace firm's materials lab / a civil engineering consultancy / a manufacturing facility's reliability department]. You are conducting [ANALYSIS_TYPE: thermal analysis / structural analysis / fluid-thermal coupling] for a [COMPONENT_NAME] component.

[ANALYSIS_CONTEXT]: [CLIENT_OR_PROJECT_NAME] requires a [ANALYSIS_PURPOSE: thermal protection component qualification / pressure vessel certification / bridge deck verification] for [END_USE: an aircraft program / regulatory submission / a capital project design review]. A formal analysis request is attached.

[REFERENCE_FILE]: [FILENAME] — [DESCRIPTION: Analysis request with geometry, boundary conditions, material properties, and acceptance criteria]

[NUMERICAL MODEL PARAMETERS]:
- Domain: [GEOMETRY: 1D linear / 2D planar / composite layered]
- Nodes: [N] nodes, spacing: [DELTA_X] m
- Material properties: [k = VALUE W/m·K], [ρ = VALUE kg/m³], [cp = VALUE J/kg·K]
- Boundary conditions:
  - [BOUNDARY_1: External face: T = X°C, h = Y W/m²·K]
  - [BOUNDARY_2: Internal face: T = X°C, h = Y W/m²·K]
- Analysis duration: [DURATION], time steps: [T_1, T_2, T_3, T_4]

[DELIVERABLE — Technical Report containing]:
- [VISUALIZATION_1: Node temperature profiles vs. node index at each time step]
- [VISUALIZATION_2: Isotherm contour plot at t = T_MAX]
- [VISUALIZATION_3: Time-trace plots for nodes [NODE_1, NODE_2, NODE_3]]
- [SUMMARY_TABLE: Back-face temperatures at each time step with margin vs. [LIMIT]°C limit]
- [CONDITIONAL: If margin < [MARGIN_THRESHOLD], provide mitigation recommendations]

[CONSTRAINTS]:
- Report must be concise and suitable for a design review audience
- Margins must be stated explicitly as [ABSOLUTE / PERCENTAGE] values
- [SPECIFIC_NODE_TRACKING: Named nodes must be clearly identified in all relevant visualizations]
- [REPORT_FORMAT: PDF / Word document]
```

## 4. Reference File Requirements

### File Types Needed
- **Formal analysis request (PDF):** A 1–3 page engineering work order or analysis brief containing the component description, geometry specification, material properties, boundary conditions, and acceptance criteria. This is the primary reference file for this pattern — it formalizes the problem statement and parameters that the worker must apply.

### Data Characteristics
The analysis request PDF should contain: a named component description, a schematic or textual geometry specification (dimensions, node count, node spacing), material properties as a table (thermal: k/ρ/cp; or structural: E/ν/yield strength), boundary conditions as a table or prose (temperatures, pressures, heat fluxes, heat transfer coefficients), time points or load cases to evaluate, and acceptance criteria (temperature limits, stress limits, deflection limits, safety factors).

### File Complexity Spectrum
- **Minimal:** Analysis request with 5–10 nodes, 2 boundary conditions, 2 time points, one acceptance criterion, and one required visualization (summary table). All parameters directly stated.
- **Moderate:** Analysis request with 15–25 nodes, composite material (two layers), 3–4 time points, one pass/fail threshold, and three required visualizations (profile, time-trace, table).
- **Complex:** Analysis request with 20–30 nodes in a 2D domain, multiple material layers, 4+ time points, two acceptance criteria (temperature limit + gradient limit), four visualization types, and a conditional recommendation requirement triggered by margin proximity.

## 5. Output Specification

### Primary Deliverable
- **Format:** PDF or Word document (technical report)
- **Structure:** Title/scope section, methodology description, results section (with embedded visualizations), summary table of key metrics vs. acceptance criteria, conditional recommendations section
- **Key quality signals:** Numerical results are self-consistent (temperatures increase monotonically toward steady-state, boundary nodes match boundary conditions), all required visualization types present and clearly labeled (axis labels, units, node identifiers), summary table explicitly states margin values (not just temperatures), conditional recommendations triggered only when the margin threshold is met, technical prose is concise and uses appropriate engineering vocabulary

### Secondary Deliverables (if any)
- None standard; occasionally the raw computation output (CSV of node temperatures at each time step) accompanies the report

### Gold Output Characteristics
A gold output technical report reads as a document that a design review panel would accept as a formal engineering deliverable. The methodology section briefly describes the numerical method used (e.g., explicit finite-difference scheme) and notes its stability condition. The results section presents temperature profiles at each required time step with clearly identified node indices. The contour plot (for 2D problems) uses appropriate color scales and clearly indicates the acceptance criterion level as a contour line. Time-trace plots track exactly the named nodes from the prompt and are clearly differentiated by color or line style. The summary table includes: time step, back-face temperature, margin (absolute and/or percentage), and pass/fail status. If conditional recommendations are triggered, they are specific and actionable (increase insulation layer thickness by X mm, add active cooling at node N, reduce exposure duration by Y minutes) — not generic.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Problem dimensionality | 1D (single row of nodes) | 1D composite (two material layers) | 2D spatial domain |
| Number of nodes | 5–10 | 15–25 | 30+ |
| Number of time steps / load cases | 2 | 4 | 8+ |
| Number of visualization types | 1 (summary table) | 2–3 (profile + table) | 4+ (profile + contour + time-trace + table) |
| Acceptance criteria | Single temperature limit | Temperature limit + margin percentage | Multiple criteria (temperature, gradient, stress) |
| Conditional recommendation trigger | None | One threshold | Two thresholds (warning + fail) |
| Reference file complexity | All parameters in prompt | Short analysis request PDF | Multi-page analysis brief with attached drawings |

## 7. Boundary Cases & Adjacent Patterns

**D1 (Technical Design & Architecture Documents):** D1 produces design documents that recommend an approach without performing the numerical analysis. J6 performs the numerical computation and reports results. If the deliverable describes what analysis should be done (without doing it), use D1. If the deliverable reports the results of actually performing the analysis, use J6.

**B1 (Performance Analysis Presentation):** B1 analyzes performance data from reference files (operational data) and produces a presentation. J6 performs a numerical simulation and produces a technical report. The distinction is whether the analysis involves a physical model (simulation/computation) or descriptive statistics on existing data. If the worker must run equations and compute numerical results, use J6.

**J4 (Quantitative Computing & Algorithm Notebooks):** J4 compares multiple algorithmic approaches in a notebook. J6 applies a single specified numerical method and reports engineering results in a formal report format. If the task is to compare several methods and recommend one, use J4. If the task is to apply a specified method and evaluate results against engineering criteria, use J6.

**A5 (Operational Metrics Dashboard / KPI Reporting):** A5 transforms operational data into dashboards. J6 computes physical simulation results and reports findings with engineering margin analysis. Both can produce charts and tables, but A5 is always data-driven (Excel, PivotTables) and business-facing, while J6 is computation-driven and technically facing.
