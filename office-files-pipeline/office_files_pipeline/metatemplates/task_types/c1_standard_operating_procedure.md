# Standard Operating Procedure / General Order

**Macro Category:** C — Policy, Procedure & Standards Authoring
**Pattern ID:** C1

## 1. Pattern Description

The worker designs and writes a formal step-by-step procedural document that governs how a specific organizational process should be executed from start to finish. Unlike a policy (which states rules) or a guideline (which offers recommendations), an SOP or general order defines the exact sequence of actions, assigns roles and responsibilities to named parties, and establishes accountability mechanisms. The cognitive core is process design: the worker must decompose an operational workflow into discrete, sequenced steps, anticipate exceptions and failure modes, and communicate clearly to a field-level audience that will rely on the document during active work. What distinguishes this pattern is the operational specificity — each step names a responsible party, includes timing constraints or thresholds, and connects to a broader compliance or quality standard.

## 2. O*NET Grounding

### Occupation Families
- 11-3011 Administrative Services Managers — Write departmental SOPs for attendance, facilities, administrative workflows
- 33-1012 First-Line Supervisors of Police and Detectives — Draft general orders and training procedures for law enforcement units
- 11-9111 Medical and Health Services Managers — Create clinical workflow SOPs for staff handoff, telehealth intake, receiving procedures
- 13-1082 Project Management Specialists — Author change control SOPs for biotech/pharma quality management systems
- 11-2022 Sales Managers — Design return authorization and account operations procedures
- 11-3071 Transportation, Storage, and Distribution Managers — Write receiving, storage, and ESD handling procedures for warehouse operations

### Key Work Activities (O*NET vocabulary)
- Documenting/Recording Information
- Developing Procedures, Policies, and Objectives
- Communicating with Supervisors, Peers, or Subordinates
- Training and Teaching Others
- Coordinating Work and Activities
- Evaluating Information to Determine Compliance with Standards

### Knowledge Domains (O*NET vocabulary)
- Administration and Management
- English Language
- Public Safety and Security (for law enforcement and safety SOPs)
- Medicine and Dentistry (for clinical SOPs)
- Production and Processing (for warehouse/manufacturing SOPs)
- Law and Government (for regulatory compliance SOPs)

### Generalizable Work Context
A department head, operations manager, or senior practitioner is tasked with formalizing an informal or broken process. The trigger is typically an identified gap: complaints from staff, regulatory audit findings, inconsistent execution across locations or staff members, or an organizational change (new system, new regulation, new team). The document will be routed for sign-off by named approving officials, then distributed to frontline staff as a binding reference.

## 3. Prompt Construction Template

### Persona Pattern
Assign a mid-to-senior operations role with domain ownership of the process: department manager, unit commander, district parts manager, senior clerk (training role), warehouse manager. The persona should have authority over the staff who will execute the procedure and be accountable to a named approving authority above them. Include the organizational type (government agency, police department, biotech company, warehouse, dealership network).

### Scenario Pattern
The trigger is a named problem: inconsistent execution across staff or locations, a compliance gap identified by a forum/audit/leadership, a new system rollout requiring documentation, or an organizational change. Name 3–6 specific failure modes or pain points that the SOP must address. Include the stakeholder audience (frontline staff who will use it, approving officials who must sign off, compliance reviewers who may audit it).

### Instruction Pattern
Frame as a deliverable specification: "Create a [page-constrained] Word/PDF document that establishes the procedure for [process name]." Then enumerate structural section requirements (purpose, scope, responsibilities, definitions, procedures). Optionally add a secondary deliverable (companion tracking spreadsheet, visual flowchart, email to staff). Use numbered or bulleted requirements for each section's content.

### Constraint Injection Points
- **Length constraint**: varies from 1 page (concise government policy) to 3–5 pages (detailed technical SOP); hard page limits are common
- **Section headers**: prescribed or partially prescribed (purpose, scope, responsibilities, definitions, procedures is standard; some add references, record retention, escalation)
- **Named stakeholders**: specific approving officials (Chief, Compliance Officer, QA Director) or role titles must appear
- **Compliance alignment**: must reference a named standard (an industry-specific quality standard, GMP, state training mandates, FDA regulations)
- **Secondary deliverable**: companion form, Excel tracking log, visual flowchart, or staff notification email
- **Audience register**: frontline field staff (plain language) vs. regulatory reviewers (formal procedural language)
- **Failure mode coverage**: must explicitly address named exception scenarios (damaged items, missed deadlines, discrepancies)

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE]. [CONTEXT: a gap/problem has been identified in the [PROCESS_NAME] process].

[TRIGGER]: [SPECIFIC_PROBLEM or FORUM/AUDIT/LEADERSHIP_REQUEST]. The following issues have been identified:
a) [FAILURE_MODE_1]
b) [FAILURE_MODE_2]
c) [FAILURE_MODE_3]
[...]

[TASK]: Create a [PAGE_LIMIT]-page [WORD/PDF] document establishing a formal [DOCUMENT_TYPE — SOP/General Order/Policy] for [PROCESS_NAME].

[SECTION_REQUIREMENTS]:
The document must include the following sections:
1. Purpose — [what the procedure accomplishes]
2. Scope — [who and what it applies to]
3. Responsibilities — [named roles and their duties]
4. Definitions — [key terms specific to the process]
5. Procedures — [step-by-step workflow with [TIMING_CONSTRAINTS] and [RESPONSIBLE_PARTIES]]
[6. References — applicable regulations or standards]

[NAMED_STAKEHOLDERS]:
The following parties must be named as required approvers/participants: [ROLE_1], [ROLE_2], [ROLE_3].

[COMPLIANCE]:
The procedure must align with [REGULATORY_STANDARD/POLICY].

[SECONDARY_DELIVERABLE (if any)]:
Additionally, create [COMPANION_FORM or TRACKING_TOOL or STAFF_EMAIL].

[CONSTRAINTS]:
- Length: [N] pages maximum
- Format: [Word/PDF]
- Audience: [FRONTLINE_STAFF / COMPLIANCE_REVIEWERS]
```

## 4. Reference File Requirements

### File Types Needed
- **Working session summary or issue log** (docx): Structured input from stakeholders capturing process gaps, pain points, failure modes, and design decisions — serves as the content scaffold for the SOP; may be formatted as meeting notes, enumerated issues, or multi-stakeholder input summary
- **Existing reference documentation** (docx/pdf, optional): Prior version of the procedure, related policy framework, or platform/system documentation that the SOP must align with (e.g., a telehealth platform's documentation, return process guidelines)
- **Industry standard or regulatory document** (pdf, optional): External standard that the SOP must reference (e.g., an industry-specific quality standard, GMP change control guidelines, state training mandates)

### Data Characteristics
For the issue log: qualitative enumeration of 4–10 named failure modes organized by category; may include named responsible parties, timeline violations, system references. For the reference documentation: existing procedural steps or system workflow descriptions in prose or outline form. For the regulatory document: formal technical standard with numbered requirements clauses.

### File Complexity Spectrum
- **Minimal:** No reference files — SOP authored entirely from domain knowledge; problem is stated inline with 3–5 named failure modes
- **Moderate:** One reference file (working session notes or existing process document) that provides the raw content to be formalized into SOP structure
- **Complex:** Reference file plus external standard URL; multi-stakeholder input summary that must be synthesized across QA, operations, finance, and regulatory voices; secondary deliverable (form or tracking tool) that must mirror the SOP logic

## 5. Output Specification

### Primary Deliverable
- **Format:** Word (.docx) or PDF
- **Structure:** Sections in order — Purpose, Scope, Responsibilities, Definitions, Procedures (numbered steps), References (optional), Appendices (optional)
- **Key quality signals:** Each procedure step names a responsible party; timing constraints are explicit (e.g., "within 3 business days"); exception handling is addressed; all named failure modes from the trigger scenario are resolved by a procedure step; document fits within page limit; professional language appropriate to the audience

### Secondary Deliverables (if any)
- Companion Excel tracking log (with named columns and data validation features)
- One-page visual flowchart (in Word using SmartArt, or described as a Visio-style diagram)
- Staff notification email (100–200 words, directing staff to the new documents and inviting feedback)
- Companion intake form or request form that mirrors the SOP's process steps

### Gold Output Characteristics
A gold-standard SOP output contains: a purpose statement that explains why the procedure exists (not just what it does); a scope that explicitly names who is included and excluded; a responsibilities section that maps each named role to specific duties in the process; step-by-step procedures where each step is a complete sentence beginning with an action verb, names the responsible party, and specifies any timing constraint; exception handling embedded within the relevant procedure step (not as a separate section unless the document specifies otherwise); and a page length that matches the constraint. The document reads as if a competent frontline employee with no prior knowledge of the process could execute the procedure correctly on first reading.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Process complexity | Linear sequence, single responsible party, no branches | Multi-step workflow with 2–3 responsible roles and one exception scenario | Multi-branch process with 4+ roles, conditional logic, multiple exception types |
| Number of named failure modes to address | 2–3 | 4–5 | 6+ |
| Reference file inputs | None (pure domain knowledge) | One working session document | Two+ files (notes + external standard + existing policy) |
| Page/length constraint | No constraint | 3–5 page limit | 1–2 page constraint (requires extreme conciseness) |
| Secondary deliverable | None | One companion form or email | Companion form + visual flowchart + staff communication |
| Regulatory alignment | General best practice | Named internal policy | Named external standard with specific clause references |
| Named approving officials | Generic role titles | 2–3 named roles with specific sign-off duties | 4+ named stakeholders with tiered approval authority |

## 7. Boundary Cases & Adjacent Patterns

**C2 (Compliance Checklist/Assessment Tool):** C1 produces a narrative procedural document; C2 produces a structured form with yes/no items, scoring, and escalation logic. When the output is a checklist used to evaluate compliance rather than a workflow to execute, choose C2. When the output instructs how to do the work (rather than auditing whether it was done), choose C1.

**C4 (Training Materials):** C1 SOPs may be used for training, but they are authoritative operational documents — not pedagogical materials. Training materials in C4 have learning objectives, exercises, case studies, and audience-calibrated language. An SOP optimized to train a new hire (with tips, common mistakes, "why" explanations per step) sits at the boundary; if it has explicit instructional scaffolding (icebreakers, quizzes, practice exercises), classify as C4.

**C5 (Form/Template Design):** When the output is primarily a fillable form (fields, dropdowns, checkboxes) rather than a procedural narrative, classify as C5. SOPs sometimes include a companion form as a secondary deliverable; that secondary form may be a C5 artifact but the primary deliverable remains C1.

**D1 (Technical Design Documents):** SOPs for highly technical processes (software deployment, engineering procedures) may resemble technical design documents. The distinguishing feature is audience: C1 SOPs are for operators/practitioners executing a process; D1 technical documents are for architects/engineers evaluating and deciding on system design approaches.
