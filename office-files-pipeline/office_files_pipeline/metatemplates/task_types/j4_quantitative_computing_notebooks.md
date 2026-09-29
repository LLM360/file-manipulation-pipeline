# Quantitative Computing & Algorithm Notebooks

**Macro Category:** J — Software & Technical Implementation
**Pattern ID:** J4

## 1. Pattern Description

The worker is a quantitative researcher, data scientist, or computational scientist who must implement multiple distinct algorithmic approaches to the same problem within a single Jupyter notebook, compare them empirically through benchmarks and convergence analysis, produce visualizations of each method's behavior, and deliver a written production recommendation. The notebook is simultaneously code, analysis, and report. What makes this pattern distinct from general software development is the comparative analysis layer: the worker must implement N methods, measure them against the same ground truth, and synthesize findings into a judgment about which is best suited for a specific production context. The cognitive core is holding both computational correctness and analytical judgment together — the code must run, the visualizations must illuminate real tradeoffs, and the recommendation must be defensible.

## 2. O*NET Grounding

### Occupation Families
- **15-2099.01 Financial Quantitative Analysts** — quants who implement and evaluate pricing models, risk models, or optimization algorithms for production trading systems
- **15-2021 Mathematicians** — researchers implementing numerical methods with rigorous convergence analysis
- **15-1221 Computer and Information Research Scientists** — computational scientists comparing algorithm performance and making production recommendations
- **19-4099 Life, Physical, and Social Science Technicians** — domain-specific variant for scientific computing applications

### Key Work Activities (O*NET vocabulary)
- Analyzing data or information using quantitative methods
- Developing mathematical or statistical models
- Writing computer programs to implement and test algorithms
- Interpreting data to determine implications for production use
- Preparing documents or presentations to communicate research findings
- Evaluating performance of algorithms using benchmarks and test cases

### Knowledge Domains (O*NET vocabulary)
- Mathematics — numerical methods, convergence theory, stochastic processes, option pricing theory
- Computers and Electronics — Python scientific computing (NumPy, SciPy, Matplotlib), Jupyter notebooks, performance measurement
- Economics and Accounting — financial instrument mechanics (options, early exercise, yield curves)

### Generalizable Work Context
A quantitative research team or individual researcher is evaluating which algorithmic approach to adopt for a production system. The trigger is an expansion of the system's scope (new asset class, new data type, new regulatory requirement) that requires validating multiple algorithmic approaches before committing to one. The worker has domain expertise in both the underlying mathematics and the production system's constraints (latency, accuracy requirements, compute budget). No external data files are needed — the algorithms generate or consume analytically specified inputs.

## 3. Prompt Construction Template

### Persona Pattern
Assign the worker as a quantitative researcher, data scientist, or computational analyst at a specific type of organization (proprietary trading firm, hedge fund, research lab, tech company). Specify the strategic context that motivates the analysis (expanding a trading desk to a new instrument, adopting a new pricing model, evaluating a new algorithm family). The persona should have both coding ability and domain expertise — this is not a pure coding task.

### Scenario Pattern
Describe the production system that the research will inform. What is the current state? What change is being evaluated? Who will act on the recommendation (quant desk manager, engineering team, research director)? What are the production constraints that will inform the recommendation (latency requirements, accuracy tolerance, compute budget, existing infrastructure)? State the recommendation is for production use — this frames the analysis as applied, not academic.

### Instruction Pattern
Provide a bulleted list of three types of deliverables: (1) algorithm implementations, (2) visualizations, and (3) written summary with recommendation. Name each algorithm to be implemented explicitly. Name each visualization type (convergence plot, runtime benchmark chart, accuracy comparison). Require the written summary to include a specific recommendation with justification tied to the production context.

### Constraint Injection Points
- **Number of methods to implement:** 2 (easy) to 5+ (complex)
- **Named chart types required:** convergence plot, pricing comparison chart, runtime benchmark bar chart — vary which are required
- **Production context constraints:** high-frequency (latency), batch overnight (throughput), real-time risk (accuracy), GPU-accelerated vs. CPU
- **Mathematical specificity:** generic "implement the algorithm" vs. specific parameter values (N steps, M paths, tolerance threshold)
- **Early exercise / complex features:** American vs. European options, barrier features, path-dependence, stochastic volatility
- **Written summary depth:** brief recommendation (1 paragraph) vs. full analysis (methodology, limitations, conditions for switching)
- **Language/library constraints:** specific Python version, required libraries (NumPy/SciPy/Matplotlib), prohibited libraries (no QuantLib)

### Structural Template

```
[PERSONA]: You are a [ROLE: Quantitative Researcher / Data Scientist] at [ORG_TYPE: a proprietary trading firm / a hedge fund / a research laboratory]. [STRATEGIC_CONTEXT: Your [TEAM] is expanding into [NEW_AREA] and needs to evaluate which [ALGORITHM_TYPE] best suits production use.]

[PRODUCTION_CONTEXT]: Your firm's [SYSTEM_NAME] must [PRIMARY_FUNCTION: price / value / optimize / simulate] [INSTRUMENT_OR_PROBLEM] [OPERATIONAL_CONSTRAINT: in under N milliseconds / at M instruments per second / with accuracy to K decimal places].

[DELIVERABLE_REQUIREMENTS]:
Develop a comprehensive Python notebook (.ipynb) that:
- Implements and compares the following [N] methods:
  1. [METHOD_1_NAME] — [BRIEF_DESCRIPTION]
  2. [METHOD_2_NAME] — [BRIEF_DESCRIPTION]
  3. [METHOD_3_NAME] — [BRIEF_DESCRIPTION]
  [additional methods...]

- Produces the following visualizations:
  - [VISUALIZATION_1: Convergence plot of METRIC vs. PARAMETER]
  - [VISUALIZATION_2: METRIC comparison across methods]
  - [VISUALIZATION_3: Runtime benchmark bar chart]
  [additional visualizations...]

- Includes a written summary section with:
  - Comparison of methods across [ACCURACY / SPEED / SCALABILITY / EASE_OF_IMPLEMENTATION]
  - A specific recommendation for which method to use in production, with justification tied to [PRODUCTION_CONSTRAINT]

[CONSTRAINTS]:
- [LIBRARY_CONSTRAINT: Use NumPy, SciPy, Matplotlib — do not use QuantLib or other pricing libraries]
- [PARAMETER_SPECIFICATION: Use the following parameters: PARAM_1 = VALUE_1, PARAM_2 = VALUE_2...]
- [BENCHMARK_METHODOLOGY: Measure runtime using timeit over N repetitions]
- [SPECIFICITY_REQUIREMENT: Address [SPECIFIC_FEATURE: American early exercise / path-dependence / stochastic vol]]

[OUTPUT_SPECIFICATION]: Clean, well-documented Python notebook (.ipynb) with markdown cells explaining each section, code cells implementing each method, visualization cells for each required chart, and a final markdown summary cell with the production recommendation.
```

## 4. Reference File Requirements

### File Types Needed
- **None (primary modality):** This pattern typically requires no reference files — algorithms generate their own test cases from analytical parameters specified in the prompt.
- **Optional: Market data CSV (for calibration variant):** A variant could provide a CSV of historical prices or yield curve data that the algorithms must be calibrated to, adding a data ingestion step before the algorithm comparison.
- **Optional: Benchmark output file (for validation variant):** A reference output CSV showing "correct" values computed by a trusted external system, against which the worker's implementations must be validated.

### Data Characteristics
No reference files required. All parameters needed for the algorithms (spot price, strike price, volatility, interest rate, time to expiration, number of steps, number of paths) are provided inline in the prompt. If market data files are used in variants, they should be standard financial time series: date, open, high, low, close, volume for equities; date, maturity, yield for fixed income; date, strike, expiration, bid, ask for options.

### File Complexity Spectrum
- **Minimal:** Two algorithm implementations (e.g., two numerical solvers), one convergence plot, one runtime comparison, one-paragraph summary. Pure knowledge, simple parameter set.
- **Moderate:** Three algorithm implementations with domain-specific complexity (e.g., binomial tree + finite differences + Monte Carlo for European options), two visualizations (convergence + benchmark), structured written summary. Named parameters in prompt.
- **Complex:** Four or five algorithm implementations requiring advanced domain knowledge (e.g., American options with early exercise, stochastic volatility, or path-dependence, addressed through a mix of simulation-based, PDE-based, lattice-based, and transform-based methods), three visualization types, production recommendation with comparative analysis across accuracy, speed, and implementation complexity. Named chart types required.

## 5. Output Specification

### Primary Deliverable
- **Format:** Python notebook (.ipynb)
- **Structure:** Organized sections with markdown headers: introduction/context, algorithm implementations (one section per method), visualization section, comparative analysis, production recommendation
- **Key quality signals:** All named algorithms implemented correctly (not stub implementations), visualizations clearly labeled with axes, legend, and title, runtime benchmarks measured with a controlled methodology (timeit or equivalent), written summary addresses each specified comparison dimension, production recommendation explicitly names the recommended method and explains why in the context of the stated production constraints

### Secondary Deliverables (if any)
- None standard; occasionally a separate requirements.txt file

### Gold Output Characteristics
A gold output notebook runs top-to-bottom without errors. Each algorithm section is preceded by a markdown cell explaining the method's mathematical basis at a level appropriate for a quantitative audience. Convergence plots show the relationship between a tuning parameter (number of steps, number of paths) and accuracy relative to a known reference value or analytical solution. Runtime benchmarks are measured consistently using the same hardware-agnostic methodology. The pricing comparison chart shows all methods on the same axes with clear differentiation. The written summary section reads as a professional memo to a quant desk manager — it names tradeoffs explicitly ("Method X is 5x faster but converges only to 3 decimal places at typical step counts"), states the recommendation clearly, and includes a caveat for when a different method might be preferred.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of algorithmic methods | 2 | 3 | 5+ |
| Domain complexity | Standard numerical methods (sorting, root-finding) | Financial options pricing (European, closed-form reference) | American options with early exercise, stochastic volatility, and advanced simulation-based methods |
| Number of required visualizations | 1 | 2 | 3+ (convergence + accuracy + runtime + parameter sensitivity) |
| Benchmark methodology specificity | Informal timing | timeit with N repetitions | Full profiling with warm-up runs, cache effects, multi-parameter sweeps |
| Written summary depth | One recommendation sentence | One paragraph per method + recommendation | Full comparative table + recommendation + switching conditions |
| Parameter specification | Provided inline in prompt | Partially provided (some to be chosen by worker) | Not provided (worker must select realistic parameters with justification) |
| Library constraints | None | Core scientific Python only (NumPy, SciPy) | Specific versions, prohibited libraries named |

## 7. Boundary Cases & Adjacent Patterns

**J1 (Full-Stack Application Development):** J1 produces a production-deployable codebase (ZIP file). J4 produces an analysis notebook (.ipynb) that documents a research process and supports a recommendation. The notebook is not intended to be deployed — it is a research artifact. If the code is meant to be a standalone deployable system, use J1.

**J2 (Component/Utility Development with Tests):** J2 produces a focused, tested software component. J4 produces a research notebook comparing multiple approaches. If the output is a single implementation with tests (no comparison, no recommendation), use J2. If the output compares multiple implementations and recommends one, use J4.

**A3 (NPV/IRR & Investment Evaluation):** A3 involves evaluating multiple options using financial models, but the deliverable is an Excel workbook with financial calculations, not a Python notebook with algorithm implementations. The distinction is the medium: Excel for business-facing financial modeling (A3), Python notebook for computational algorithm research (J4).

**B1 (Performance Analysis Presentation):** B1 analyzes data and produces a presentation. J4 implements algorithms and analyzes them. If the core deliverable is a slide deck or Word document, use B1. If the core deliverable is a Jupyter notebook with executable code, use J4.
