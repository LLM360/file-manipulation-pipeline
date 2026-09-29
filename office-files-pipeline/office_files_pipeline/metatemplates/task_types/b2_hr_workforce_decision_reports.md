# HR & Workforce Decision Reports

**Macro Category:** B — Data-Driven Document Authoring
**Pattern ID:** B2

## 1. Pattern Description

The worker analyzes structured employee or workforce data — performance metrics, timekeeping records, work order logs, case logs, or evaluation scores — and produces a written document that communicates a personnel decision, flags a workforce risk, or formalizes a corrective action plan. The defining characteristic is that a human judgment about people (a hiring decision, a performance improvement plan, a utilization flag) is grounded in and justified by the analyzed data. The document is typically a formal HR artifact — a written selection rationale, a Performance Improvement Plan (PIP), a workforce utilization tracker with written findings — rather than a pure dashboard. What distinguishes B2 from adjacent patterns is the integration of both quantitative benchmarking (mean, standard deviation, thresholds) and qualitative judgment (prioritization criteria, leadership potential, training fit) in producing a document with HR or personnel consequences.

## 2. O*NET Grounding

### Occupation Families
- 11-9111 Medical and Health Services Managers — residency program coordinator analyzing surgical case log benchmarks and flagging residents at risk of missing graduation requirements
- 41-1011 First-Line Supervisors of Retail Sales Workers — grocery manager evaluating employee performance data to select an overnight manager candidate
- 13-1082 Project Management Specialists — project manager building a workload utilization tracker and answering analytical questions about burnout and budget overrun risk
- 11-9141 Property, Real Estate, and Community Association Managers — property manager analyzing maintenance KPIs and writing a formal PIP for a superintendent
- 13-1071 Human Resources Specialists — HR analyst generating flag-and-notify reports on employee performance anomalies

### Key Work Activities (O*NET vocabulary)
- Evaluating Personnel Performance
- Analyzing Data or Information
- Documenting Information
- Making Decisions and Solving Problems
- Staffing Organizational Units
- Developing Objectives and Strategies
- Communicating with Supervisors, Peers, or Subordinates

### Knowledge Domains (O*NET vocabulary)
- Personnel and Human Resources
- Administration and Management
- Mathematics
- English Language
- Medicine and Dentistry (for clinical education variants)
- Customer and Personal Service

### Generalizable Work Context
A manager or coordinator is asked by a senior stakeholder to evaluate a specific workforce situation — a hiring decision, a flagged performance gap, a utilization imbalance, or a residency program compliance issue — using available operational data. The trigger is usually a defined review period (end of month, quarterly review, program year) or an observed problem (a superintendent's redo rate is too high, a department is consistently overutilized). The worker must both compute the relevant metrics from the data and produce a formal document that will be used in a consequential personnel process.

## 3. Prompt Construction Template

### Persona Pattern
Assign a managerial or coordinator role with direct or advisory authority over the personnel being evaluated. The role should be organizationally credible for producing the deliverable — e.g., a Program Coordinator is credible for a residency benchmarking report; a Grocery Manager is credible for selecting an overnight manager; a Property Manager is credible for writing a superintendent PIP. Specify the organization size and type to set the scale of the workforce being analyzed.

### Scenario Pattern
A senior stakeholder (department chair, CEO, regional director) has requested an analysis and formal document addressing a specific personnel situation. The scenario should name the time period, the number of employees or candidates involved, and the specific question being answered (Who should be promoted? Who is at risk? Which department is overloaded?). The request should be framed as coming from a defined authority figure who will act on the output.

### Instruction Pattern
Provide numbered or bulleted analytical steps, specifying what to calculate (utilization rate, mean/SD benchmark, KPI threshold comparison, priority-weighted score), and what to include in the written document (required sections, page limits, mandatory signature blocks). For PIP tasks, enumerate the required sections precisely. For selection tasks, specify the priority ordering of criteria. For utilization trackers, specify the threshold definitions and question prompts that must be answered in writing.

### Constraint Injection Points
- **Evaluation criteria priority ordering:** explicit weighting or ranking of criteria (e.g., a top-priority qualitative trait outranking a lower-priority output metric)
- **Statistical thresholds:** specific flagging thresholds (e.g., a standard-deviation-based outlier cutoff; a low-utilization percentage cutoff; a high-utilization percentage cutoff)
- **Required document sections:** named sections (performance gap summary, measurable objectives, support/resources, consequences, signatures)
- **Page/length limits:** a PIP is capped at a small number of pages; a selection rationale is capped at a short sentence count; written answers are brief
- **Regulatory or standards context:** ACGME graduation requirements, HIPAA, a fixed-length PIP review period, CMS standard of care
- **Output format:** Excel tracker with embedded written answers vs. Word document vs. email draft

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE] ([ORG_SIZE/CONTEXT]).

[SCENARIO]: [SENIOR_STAKEHOLDER] has asked you to [ANALYTICAL_TASK] using [DATA_SOURCE] as of [DATE/PERIOD]. [BACKGROUND_SENTENCE about why this matters].

[DATA_SOURCE]: Attached is [FILE_DESCRIPTION — e.g., "an Excel file containing [METRIC_A], [METRIC_B], and [METRIC_C] for [N] employees/candidates/residents"].

[TASK]:
1. Using the attached data, [ANALYTICAL_STEP_1 — e.g., "calculate [STATISTIC] for each [ENTITY] and compare against [BENCHMARK]"].
2. [ANALYTICAL_STEP_2 — e.g., "identify [ENTITIES] that fall below [THRESHOLD] on [CRITERION]"].
3. Produce a [DOCUMENT_TYPE] with the following sections:
   - [SECTION_1]
   - [SECTION_2]
   - [SECTION_3]

[CRITERIA/THRESHOLDS]:
- [CRITERION_1]: [DEFINITION or THRESHOLD]
- [CRITERION_2]: [DEFINITION or THRESHOLD]
- Priority ordering: [HIGHEST] > [MEDIUM] > [LOWEST]

[CONSTRAINTS]:
- Document length: [PAGE_LIMIT or SENTENCE_COUNT]
- [REGULATORY_GROUNDING if applicable]
- [SIGNATURE_BLOCK_REQUIREMENT if PIP]
- [TRAINING_OPTIONS_LIST if recommending resources]

[OUTPUT_SPECIFICATION]: [FORMAT], named [FILENAME if specified], with [STRUCTURE].
```

## 4. Reference File Requirements

### File Types Needed
- **Primary employee data file (xlsx):** Structured personnel data with rows per employee and columns for performance dimensions (KPIs, metrics, attendance, productivity scores, timekeeping hours). Must include identifiers (employee name, department, employment status) and the specific measures being evaluated.
- **Secondary operational log or case log (docx or xlsx, optional):** Timestamped activity records (work orders, complaint logs, surgical case counts) from which KPIs must be computed rather than read directly. Adds a calculation step before the analytical work.
- **Budget or allocation file (xlsx, optional):** Project-level or department-level hour allocations used for variance calculations in utilization tasks.
- **Standards reference (URL or docx, optional):** External or internal benchmark document defining required thresholds (ACGME graduation requirements, KPI standards, training protocol list).

### Data Characteristics
The primary data file typically covers 5-30 employees or candidates. Each row represents one employee across one time period, or multiple rows represent monthly observations per employee. Quantitative columns (hours worked, cases completed, redo count, productivity rate) should contain raw values that require summary computation (mean, SD, ratio). At least one qualitative or categorical column (interview notes, evaluation narrative, employment status) should be present to support the multi-criteria judgment task. Variance across the employee population should be sufficient to produce meaningful flags — not all employees should be at the same performance level.

### File Complexity Spectrum
- **Minimal:** Single Excel tab, 5-8 employees, 2-3 quantitative metrics already in comparable units, straightforward selection task (choose best candidate from N).
- **Moderate:** Single Excel tab, 10-20 employees, 3-5 metrics requiring calculation from raw timestamps or counts, explicit threshold-based flagging, one written document deliverable.
- **Complex:** 3 input files (roster + timekeeping log + budget), 20-30 employees across multiple departments, FTE/PTE differentiation, overhead reserve exclusion, multi-level analysis (department aggregate + individual), plus written responses to named analytical questions; or multi-year surgical case log requiring benchmark construction and cross-cohort comparison.

## 5. Output Specification

### Primary Deliverable
- **Format:** Word document (PIP, selection rationale, email draft) or Excel workbook (utilization tracker with embedded written answers)
- **Structure:** Named sections matching HR document conventions — performance gap summary, measurable objectives, consequences statement, signature block (for PIPs); department-level and individual-level tabs with flag columns (for trackers); selection justification paragraph (for hiring decisions)
- **Key quality signals:** Findings are grounded in computed metrics (no assertion without a number); thresholds are correctly applied to generate flags; written narrative is factual, fair, and appropriately formal for HR use; document structure matches the prescribed section list; output length is within specified limits

### Secondary Deliverables (if any)
- Excel workbook companion to a Word PIP (e.g., a benchmarking tracker with highlighted flag cells)
- Email draft to a supervisor or medical director summarizing flagged items
- Conditional formatting or cell highlighting in Excel output marking at-risk employees

### Gold Output Characteristics
A gold output correctly computes all required statistics (mean, SD, utilization rates, KPI ratios) from the provided data, applies the specified thresholds to generate accurate flags, produces a written document whose claims are directly traceable to the data, uses appropriate formal HR or clinical language, and conforms to all structural constraints (page limit, section headings, signature block, file naming). The written justification for personnel decisions is specific and evidence-based — naming the employee, the relevant data points, and the criteria used — rather than generic. If a PIP, it includes all five mandatory sections with measurable objectives and a timeline.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of employees analyzed | 3-5 | 10-20 | 20-30 across multiple departments |
| Data computation required | Metrics provided directly | Simple ratio calculation (redo rate from timestamps) | Multi-step: compute utilization → apply FTE/PTE split → subtract overhead reserve |
| Number of input files | 1 | 2 | 3 (roster + timekeeping + budget) |
| Statistical benchmarking | Threshold comparison only | Mean and SD calculation per metric | SD-based flagging across 5+ metrics with cross-cohort comparison |
| Written document type | Short selection paragraph (a few sentences) | Formal email to department head | Formal PIP with 5 required sections, page limit, and signature block |
| Regulatory grounding | None | Internal KPI standards | External standards (ACGME requirements, CMS, HR compliance) |
| Multi-criteria prioritization | Single criterion | 2-3 weighted criteria | Explicit priority hierarchy with override logic |

## 7. Boundary Cases & Adjacent Patterns

**B1 (Performance Analysis Presentation):** B1 produces slides for leadership, while B2 produces Word documents or Excel trackers used in HR processes. If the output is a presentation deck rather than a formal personnel document, use B1.

**A5 (Operational Metrics Dashboard / KPI Reporting):** A5 focuses on building dashboard infrastructure (PivotTables, charts, conditional formatting) in Excel where the Excel workbook itself is the analytical deliverable. B2 uses metrics computation as a step toward a written HR document or personnel decision. If there is no personnel decision or formal HR document, use A5.

**B3 (Compliance Report from Transaction Data):** B3 involves regulatory compliance screening of transaction data with findings documented in a Word report — typically financial, operational, or healthcare billing data. B2 is specifically about personnel data (employee performance, workforce utilization, candidate evaluation). The population being evaluated in B2 is always employees or trainees, not transactions.

**C1 (Standard Operating Procedure / General Order):** C1 is about writing procedural documents from domain knowledge. B2 requires reading and analyzing a specific data file to produce the document. If the task requires no data analysis and is purely about authoring an HR policy from domain knowledge, use C1 instead.
