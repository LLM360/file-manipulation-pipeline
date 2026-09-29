# Technical Design & Architecture Documents

**Macro Category:** D — Strategic & Advisory Document Authoring
**Pattern ID:** D1

## 1. Pattern Description

The worker authors a formal technical document that specifies or proposes an architecture, design, engineering analysis, or set of technical standards — then delivers it to engineers, executives, or both. The cognitive core is justified technical decision-making: selecting among options, explaining trade-offs, and documenting design rationale in a form that others can act on (build from, review, or approve). What distinguishes this pattern from generic report writing is that the deliverable IS the engineering artifact — it drives downstream action (ticket decomposition, cloud migration, design review, code review). Reference files, when present, are either existing architecture documents to mirror/extend or simulation data to interpret; in many cases no reference files exist and the worker must draw entirely on domain knowledge.

## 2. O*NET Grounding

### Occupation Families
- 11-3021 Computer and Information Systems Managers — produces technical standards and architecture decisions that govern engineering teams
- 15-1241 Computer Network Architects — produces cloud migration proposals, infrastructure design documents
- 15-1252 Software Developers, Applications — produces feature design documents and coding standards
- 17-2011 Aerospace Engineers — produces CFD/simulation engineering reports for design review
- 13-1111 Management Analysts — produces process/workflow specification documents in technical contexts

### Key Work Activities (O*NET vocabulary)
- Developing and Building Systems
- Analyzing Data or Information
- Making Decisions and Solving Problems
- Documenting Information
- Communicating Technical Information to Non-Technical Audiences
- Evaluating Information to Determine Compliance with Standards

### Knowledge Domains (O*NET vocabulary)
- Computers and Electronics
- Engineering and Technology
- Telecommunications
- Administration and Management
- English Language
- Physics (for simulation/aerodynamic subtypes)

### Generalizable Work Context
A technical individual contributor or manager at a software company, consulting firm, engineering firm, or internal IT organization is tasked with documenting a proposed or existing system — either because a new system is being built, an existing system is being migrated/replaced, or because fragmented team practices need to be codified. The trigger is typically a new project kickoff, a migration decision, a design review gate, or an internal audit/standardization initiative. Stakeholders include senior engineers who will implement the design, executives who will approve it, or cross-functional teams (IT, QA, Product) who need authoritative reference.

## 3. Prompt Construction Template

### Persona Pattern
Assign a technical leadership or senior engineering role: CTO, Engineering Manager, Solutions Architect, Mechanical/Aerospace Engineer. Include organizational context — company type (startup, product agency, consulting firm, aerospace firm), team structure (number of teams, tech stack), and the scope of authority (owns the decision, is proposing for approval). Seniority should be senior enough that the person is expected to make defensible technical choices rather than present options to someone else.

### Scenario Pattern
A concrete technical trigger requires a design artifact: a new system needs to be built before a deadline; a cloud migration proposal is needed for a customer's review; engineering teams are producing inconsistent code; a simulation study needs to be written up for a design review. Provide the business context that explains why this document matters — the downstream consequence (ticket decomposition, customer approval, team rollout, design team decision). Include any technology constraints (existing stack, required services, budget/timeline).

### Instruction Pattern
Specify the deliverable format (Word, PDF), length constraint (page limit), and required sections. For design documents: purpose, goals, scope, functional requirements, technical decisions with justifications, constraints, risks/open questions. For standards documents: technology-area coverage with specific named sections. For engineering reports: a prescribed section sequence (e.g., objective, setup/environment, boundary conditions or inputs, results, discussion, conclusion). For migration proposals: multi-deliverable packages (architecture summary + diagram + POC instructions). Use a numbered or bulleted section list to make sections explicit.

### Constraint Injection Points
- **Page/length limit:** short (a few pages) for decision documents; moderate (several pages) for standards; long-form for comprehensive reports; single-paragraph to multi-page per section
- **Technology specificity:** fixed tech stack (React/Next.js/TypeScript, PostgreSQL, GitHub Actions; or services from a specific cloud provider; or specific CFD solver outputs)
- **Audience calibration:** engineers who don't need hand-holding vs. executives who need strategic framing vs. mixed audience requiring both layers
- **Deliverable count:** single document vs. multi-document package (architecture summary + diagram + POC steps)
- **Reference style:** mirror the format of an existing document; use official vendor icons; cite named external style guides
- **Timeline constraint:** a short, fixed launch window, design review gate date, staged rollout before team distribution
- **Section prescription:** required section headers that must appear verbatim; required tables or figures

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE]. [TECH_STACK_CONTEXT]. [TEAM_STRUCTURE_OR_CLIENT_CONTEXT].

[SCENARIO]: [TRIGGER_EVENT — new system/migration/standardization need]. [BUSINESS_CONSEQUENCE — what downstream action this document enables]. [DEADLINE_OR_GATE].

[DELIVERABLE_SPEC]:
Produce [FORMAT] ([PAGE_LIMIT]) covering:
1. [SECTION_1]
2. [SECTION_2]
3. [SECTION_3]
...

[TECHNICAL_REQUIREMENTS]:
- [TECH_CONSTRAINT_1 — specific services, tools, or standards that must be used]
- [TECH_CONSTRAINT_2]
- ...

[AUDIENCE_GUIDANCE]: The document will be reviewed by [AUDIENCE_1] and [AUDIENCE_2]. [TONE_CALIBRATION — engineers don't need hand-holding / executives need executive summary layer].

[REFERENCE_FILES]: [ATTACHED_FILE_DESCRIPTION — existing architecture doc to mirror / simulation results to interpret / style guides to reference]. [STYLE_MATCHING_INSTRUCTION if applicable].

[OPEN_QUESTIONS_PROMPT if applicable]: Surface any open questions not addressed in the requirements.
```

## 4. Reference File Requirements

### File Types Needed
- **Existing architecture summary (DOCX):** Bulleted or narrative description of current system components, data flows, and integrations — serves as style template for the proposed architecture document
- **Architecture diagram (PDF):** Visual topology diagram of existing system using vendor or generic icons — serves as visual style template for the proposed diagram
- **Simulation/post-processing results (PDF):** Numerical output tables from engineering simulation software (CFD solver, FEA, etc.) — serves as source data for engineering reports
- **CAD/geometry file (STEP or similar):** 3D model of the artifact being analyzed — supplementary to simulation results
- **External style guide URLs:** Named coding/engineering standards documents (e.g., a language style guide or a cloud platform's best-practices guide) — cited rather than attached

### Data Characteristics
For architecture documents: system component names, interaction verbs (calls, writes to, serves, proxies), service names from a specific cloud provider or technology ecosystem. For simulation reports: tabular numerical values (field variable min/max, global goal values) with physical units; boundary condition parameters (inlet velocity, material properties). For coding standards: technology vocabulary specific to the stack (ORM names, test framework names, branch naming conventions). All reference data should be self-consistent and internally coherent — no contradictions between diagram and narrative.

### File Complexity Spectrum
- **Minimal:** Single existing architecture summary (DOCX) to mirror, no diagram; pure knowledge task with one style reference
- **Moderate:** Existing architecture summary + diagram (PDF); requires style matching across text and visual; one or two supplementary external reference URLs
- **Complex:** Full multi-file package — architecture diagram + summary + simulation data + CAD geometry; requires multi-deliverable output (architecture doc + visual diagram + step-by-step POC); web research for vendor documentation URLs

## 5. Output Specification

### Primary Deliverable
- **Format:** Word document (.docx) or PDF
- **Structure:** Numbered sections with prescribed headers; may include tables (e.g., requirements matrix, field variable summary), bullet lists for decision rationale, and clearly labeled open questions or risk items
- **Key quality signals:** Decisions are justified (not just listed); trade-offs are named; technical choices are grounded in the specific constraints given; the document could be handed to a team to execute without clarifying questions on the core design

### Secondary Deliverables (if any)
- PDF architecture diagram using official vendor icons (for cloud migration proposals)
- Proof of Concept (POC) step-by-step implementation document (for migration proposals)
- Separate linked supporting files (coding standards may be versioned/extended over time)

### Gold Output Characteristics
A gold output presents a specific, defensible recommendation for each major technical decision — not a list of options left open. It names the chosen approach and explains why in 1–3 sentences grounded in the stated constraints (timeline, team size, tech stack compatibility). Sections flow logically: requirements → decisions → constraints/risks → open questions. Page limits are respected. If style matching is required, the structure and formatting conventions of the reference document are visibly mirrored. Tables are accurate and internally consistent with the narrative.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Deliverable count | Single document | Two documents (e.g., summary + POC) | Three documents (summary + diagram + POC) |
| Reference files | No reference files (pure knowledge) | One reference file (existing architecture to mirror) | Two reference files of different types (diagram + summary) + web documentation URLs |
| Section prescription | 3–4 named sections | 5–6 named sections with defined content per section | 6+ sections with prescribed tables, required figures, and per-step annotation requirements |
| Technical depth | High-level design only | Design + justified decisions + named risks | Design + justifications + quantitative data interpretation (simulation results) + actionable recommendations |
| Audience complexity | Single technical audience | Dual audience (engineers + executives) requiring different framing per section | Multi-stakeholder package with separate deliverables for different audience roles |
| Timeline/constraint tightness | No hard deadline, exploratory | Staged rollout with named review gate | Short, fixed hard deadline affecting which architectural choices are viable |

## 7. Boundary Cases & Adjacent Patterns

- **vs. C1 (Standard Operating Procedure):** SOPs define how a process is executed by operators; technical design documents define what a system should be and why. SOPs are procedural and role-facing; design documents are architectural and engineer-facing. If the output is a step-by-step checklist for staff to follow, it is C1; if it is a specification for engineers to build from, it is D1.
- **vs. D4 (Program & Evaluation Plans):** D4 documents define objectives, methodologies, and accountability structures for organizational programs; D1 documents specify technical system designs. D4 operates at the organizational program level; D1 operates at the system architecture level. If the document contains data collection instruments, evaluation frameworks, or inter-organizational agreements, it is D4.
- **vs. C4 (Training Materials):** If the purpose of the document is to teach someone how to use or understand something (rather than to specify what should be built), it is C4. Coding standards documents (D1) are normative ("do this") and enforceable; training guides (C4) are educational ("here is how this works").
- **Choose D1 when:** The deliverable is intended to drive a build, migration, or review decision; technical choices are made and justified; the primary audience is engineers or technical leads; reference files (if any) are existing technical artifacts to mirror or data outputs to interpret.
