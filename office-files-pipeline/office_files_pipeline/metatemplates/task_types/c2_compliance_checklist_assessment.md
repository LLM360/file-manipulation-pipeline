# Compliance Checklist / Assessment Tool Design

**Macro Category:** C — Policy, Procedure & Standards Authoring
**Pattern ID:** C2

## 1. Pattern Description

The worker creates a structured document — checklist, audit tool, or assessment form — that operationalizes a regulatory or compliance framework into a series of questions, evaluation criteria, or action items organized by domain. Unlike a narrative policy document (C1), the deliverable here is a formatted instrument designed for repeated use: evaluators fill it out, score it, and act on the results. The cognitive core is regulatory translation: the worker reads source legislation, professional standards, or internal policy, extracts the compliance requirements, and renders them into actionable audit questions with consistent syntax (typically Yes/No/Not Applicable), clear citations, and embedded scoring or escalation logic. The output's defining feature is that it can be used by someone other than the author to evaluate compliance independently.

## 2. O*NET Grounding

### Occupation Families
- 13-1041 Compliance Officers — Design audit test question sets, regulatory checklists, and compliance assessment tools derived from statute or regulation
- 13-2061 Financial Examiners — Create regulatory examination tools for mortgage servicing, banking compliance (SCRA, VA loan servicing programs, CFPB)
- 29-9011 Occupational Health and Safety Specialists — Develop multi-domain store or facility safety checklists with scoring and escalation
- 13-1041 Compliance Officers (Government Grants) — Build pre-award risk assessment tools grounded in Uniform Guidance (2 CFR Part 200)
- 33-1012 First-Line Supervisors of Police and Detectives — Design behavioral threat assessment and intake screening forms for operational units
- 29-1051 Pharmacists — Create pharmacy compliance checklists derived from state board of pharmacy regulations

### Key Work Activities (O*NET vocabulary)
- Evaluating Compliance with Laws, Regulations, or Standards
- Interpreting and Applying Laws, Regulations, and Rules
- Documenting/Recording Information
- Analyzing Data or Information
- Developing Objectives, Policies, and Procedures
- Communicating Information to Others

### Knowledge Domains (O*NET vocabulary)
- Law and Government
- English Language
- Economics and Accounting (for financial regulatory compliance)
- Public Safety and Security (for safety/law enforcement checklists)
- Medicine and Dentistry (for pharmacy/clinical compliance tools)
- Administration and Management

### Generalizable Work Context
A compliance function, regulatory affairs team, or operations leadership needs a reusable audit instrument to systematically evaluate whether a process, entity, or practice meets regulatory or organizational requirements. The trigger is often a regulatory requirement to conduct periodic assessments, a new regulation requiring operationalized testing, a recent audit finding, or a new organizational function standing up its compliance program. The resulting tool will be used by staff other than the creator — often frontline supervisors, auditors, or safety coordinators — on a recurring basis.

## 3. Prompt Construction Template

### Persona Pattern
Assign a regulatory, compliance, or operational role with direct accountability to a regulatory body or organizational standards function: Grants Management Specialist, Regulatory Affairs Specialist, Safety Coordinator, Pharmacist-owner, Unit Commander. The persona should have access to or familiarity with the regulatory source material. The organizational context should explain the compliance need: a federal grant agency requiring pre-award vetting tools, a mortgage servicer conducting monthly regulatory testing, a police unit implementing threat assessment protocols, a pharmacy subject to state board inspections.

### Scenario Pattern
A regulatory mandate, leadership request, or audit gap creates the need for a standardized assessment instrument. Name the specific regulation or framework that grounds the tool (2 CFR Part 200, SCRA, an agency servicing handbook, a state pharmacy lawbook, OSHA standards). Specify the intended user (frontline supervisor, compliance analyst, safety coordinator) and the cadence of use (monthly, quarterly, pre-award, per-incident). Include a URL to the regulatory source when web research is required.

### Instruction Pattern
Specify the exact structure of the output: number of questions per section, response format (Yes/No/NA), citation requirement per question, scoring rules, threshold triggers, and escalation protocols. Name any special formatting conventions (unique question identifiers, page limits, separate sections by domain). Distinguish the primary deliverable (the assessment tool) from any secondary outputs (exception statement templates, corrective action plan triggers).

### Constraint Injection Points
- **Response format**: Yes/No only vs. Yes/No/Not Applicable vs. two-part (closed + open-ended follow-up)
- **Citation requirement**: Whether each question must cite its regulatory source (section/paragraph number, CFR citation)
- **Question count constraints**: Exact number of questions per section, per regulatory provision, or per domain area
- **Identifier naming convention**: Unique ID scheme per question (e.g., REG-01a, DOM-Q1)
- **Scoring/threshold logic**: Number of missed items that triggers escalation; pass/fail threshold; scoring rubric
- **Escalation workflow**: Who receives the completed form, what action is triggered by threshold breach, what exception statement format to use
- **Page limit**: Maximum document length (e.g., 1–2 pages for a concise intake or risk-assessment tool; 2–4 pages for a more detailed multi-section form)
- **Temporal coverage**: Daily/weekly/monthly/quarterly/annual scope of the checklist items
- **Format**: Excel (tabular) vs. Word (paragraph or table) vs. PDF (printer-friendly checklist)

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE]. [CONTEXT: regulatory mandate or compliance gap requiring a new assessment instrument].

[TRIGGER]: [REGULATORY_MANDATE or LEADERSHIP_REQUEST]. Your task is to create a [DOCUMENT_TYPE — checklist/assessment tool/audit question set] to [PURPOSE].

[REGULATORY_SOURCE]:
The tool must be grounded in [REGULATION_NAME] ([CITATION]). Reference materials are available at: [URL_IF_WEB_RESEARCH_REQUIRED].

[DELIVERABLE_SPECIFICATION]:
Create a [FORMAT — PDF/Word/Excel] document titled "[EXACT_TITLE]" (max [N] pages) that covers [DOMAIN_COUNT] compliance domains.

[STRUCTURAL_REQUIREMENTS]:
1. Section: [DOMAIN_1] — [N] questions, each with [RESPONSE_FORMAT], citation to [REGULATORY_SECTION]
2. Section: [DOMAIN_2] — [N] questions, each with [RESPONSE_FORMAT]
[...]

[QUESTION_FORMAT]:
- First part: [Yes/No/NA] response prompt
- Second part (if applicable): Open-ended detail request
- Each question must include: [CITATION] / [UNIQUE_IDENTIFIER]

[SCORING_AND_ESCALATION]:
- Threshold: [N] missed items triggers [ESCALATION_ACTION]
- Distribution: Completed forms routed to [STAKEHOLDER_LIST]

[EXCEPTION_STATEMENTS (if applicable)]:
Each question must include a corresponding exception statement formatted as: [FORMAT_DESCRIPTION].

[CONSTRAINTS]:
- Length: [N] pages max
- Format: [PDF/Word/Excel]
- Response options: [Yes/No/NA] only
- Audience: [EVALUATOR_ROLE]
```

## 4. Reference File Requirements

### File Types Needed
- **Regulatory source document** (pdf/URL): The statute, regulation, or framework that grounds the checklist content — accessed via provided URL for web research tasks; primary content source for question generation (e.g., 2 CFR Part 200, SCRA statute, an agency servicing handbook, a state pharmacy lawbook)
- **Existing template or form** (pdf/URL, optional): A comparable checklist from another jurisdiction, a predecessor version, or an industry reference form to adapt and expand (e.g., a peer agency's intake or assessment form, a state board self-assessment form)
- **Internal policy document** (docx/pdf, optional): Organizational policy that the checklist must reflect or align with (e.g., internal escalation protocols, corrective action procedures)

### Data Characteristics
Regulatory source documents: formal legal text with numbered sections, defined terms, mandatory requirements ("shall"), and condition-based obligations. Existing template references: structured forms with numbered items, categorical sections, and response fields — serve as structural scaffolds. Internal policy documents: prose descriptions of organizational procedures with named roles and escalation chains.

### File Complexity Spectrum
- **Minimal:** Pure knowledge task — no reference files; regulatory framework is named and well-known (e.g., OSHA safety categories); worker generates questions from domain expertise; URL to regulatory source provided but no file
- **Moderate:** One reference file (existing comparable form or regulatory document excerpt); worker must read, interpret, and translate into the required checklist format with correct citations
- **Complex:** Multiple source URLs (two regulatory provisions, each requiring separate question sets with distinct identifiers and item counts); output must cover 3+ temporal frequencies (daily/weekly/monthly/quarterly/annual); companion exception statement template required per question

## 5. Output Specification

### Primary Deliverable
- **Format:** PDF (most common for checklists), Excel (for audit question trackers), or Word (for assessment tools with narrative components)
- **Structure:** Header section (tool title, organization, date, evaluator fields); numbered sections by compliance domain; per-item structure (identifier, question text, response field, citation); scoring summary; escalation instructions
- **Key quality signals:** Every question has an actionable Yes/No framing (evaluable by the named user without additional judgment); citations are accurate and traceable; question count and identifiers match specifications; scoring logic is unambiguous; escalation threshold and consequence are clearly stated; format is printer-friendly and usable by non-expert evaluators

### Secondary Deliverables (if any)
- Exception statement templates (one per question, formal regulatory-tone narrative for non-compliance findings)
- Corrective action plan template (triggered by scoring threshold breach)
- Distribution routing instructions embedded in the footer

### Gold Output Characteristics
A gold-standard compliance checklist contains: questions phrased so that a "Yes" answer always indicates compliance (and "No" indicates a finding); unique identifiers that enable tracking across audit cycles; citations that reference the specific regulatory section (not just the act name); a scoring section that an evaluator can complete without interpretation; an escalation path that is explicit about who receives the completed form and what happens at each threshold; and a page layout that allows a supervisor to complete the form in the field (appropriate spacing, readable font, logical grouping by domain).

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of compliance domains | 2–3 | 5–8 | 10+ (e.g., many operational domains plus a dedicated scoring section) |
| Regulatory sources | Single well-known framework | One specific statute with 2 provisions | Two or more separate statutes each requiring distinct question sets |
| Question format | Yes/No only | Yes/No + citation | Yes/No + open-ended follow-up + citation + exception statement |
| Web research required | None (domain knowledge) | One URL to access | Two+ URLs, must synthesize across multiple regulatory documents |
| Scoring/escalation logic | No scoring required | Simple threshold count | Multi-tier scoring with weighted domains and tiered escalation paths |
| Output format complexity | Simple list of questions | Structured table with identifier column and response column | Multi-document output (separate PDFs by frequency: daily/weekly/quarterly) |
| Page constraint | No limit | 2–4 page limit | 1–2 page limit (forces conciseness across many required items) |

## 7. Boundary Cases & Adjacent Patterns

**C1 (Standard Operating Procedure):** C1 produces a workflow narrative that tells someone how to execute a process. C2 produces an evaluation instrument that enables someone to audit whether a process was executed correctly. If the primary deliverable is a checklist used for auditing or assessment (rather than instruction), classify as C2. SOPs that include embedded checklists as a sub-component remain C1 if the procedure narrative is the primary deliverable.

**C5 (Form/Template Design):** C5 forms are intake or operational templates — they collect information about a subject (patient intake, fax transmission). C2 assessment tools evaluate compliance against standards. When the form is primarily an audit instrument (questions about whether requirements are met, with yes/no responses and scoring), classify as C2. When it's a data-collection or intake form (fields for patient name, subscription type, sender information), classify as C5.

**B3 (Compliance Report from Transaction Data):** B3 produces a written compliance report by cross-referencing transaction data against policy. C2 produces the audit instrument itself (the checklist or question set). If the task is to fill out or complete a checklist using data, it may be B3. If the task is to design the checklist instrument, classify as C2.

**C3 (Clinical Guidelines):** C3 produces evidence-based clinical recommendations. C2 produces compliance evaluation tools. A pharmacy compliance checklist (derived from state pharmacy law) is C2. A clinical care protocol or prescribing guideline is C3.
