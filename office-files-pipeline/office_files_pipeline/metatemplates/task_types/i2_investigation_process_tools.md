# Investigation Process Tools & Guides

**Macro Category:** I — Investigation & Security Reports
**Pattern ID:** I2

## 1. Pattern Description

The worker — a PI, loss prevention professional, or investigation supervisor — must create standardized reusable operational artifacts that other investigators will use in the field: guides, observation forms, flowcharts, or awareness decks. Unlike I1 (which produces a specific completed report), this pattern produces infrastructure: the templates, procedures, and reference tools that enable consistent, professional investigative work across an organization or team. The cognitive core is designing for a future unknown user — the form must be self-explanatory, the guide must establish clear procedure, and the flowchart must correspond structurally to an accompanying awareness presentation. Dual-document deliverables with required structural correspondence between outputs are a hallmark of this pattern.

## 2. O*NET Grounding

### Occupation Families
- **33-9021 Private Detectives and Investigators** — PI practitioners who need standardized tools for their own and their team's use
- **11-9199 Loss Prevention Managers** — corporate LP professionals who create district-wide process documentation and awareness materials
- **33-1099 First-Line Supervisors of Protective Service Workers** — supervisors responsible for establishing and standardizing investigative procedures across a team

### Key Work Activities (O*NET vocabulary)
- Developing procedures for investigation or protective service operations
- Documenting information by creating structured forms and guides
- Training and instructing subordinates through written materials
- Communicating with supervisors, peers, or subordinates via written process documentation
- Organizing information into usable operational format

### Knowledge Domains (O*NET vocabulary)
- Law and Government — investigation procedures, legal constraints on undercover work
- Public Safety and Security — surveillance methodology, loss prevention protocols, evidence standards
- English Language — clear instructional writing, professional document design
- Administration and Management — process documentation, standard operating procedure authoring

### Generalizable Work Context
A small-to-mid-size investigation firm or a multi-store retail chain's loss prevention department needs standardized field tools. The trigger is the establishment or formalization of a workflow that has previously been ad hoc, or the need to train new investigators. The worker is typically the most experienced person on the team and is producing materials that will be used by junior investigators with less experience. Outputs are reusable across many future engagements, so they must be general enough to fit varied cases while specific enough to guide behavior.

## 3. Prompt Construction Template

### Persona Pattern
Assign the worker as a PI, LP professional, or investigation supervisor at a named firm type (new PI firm, multi-store retailer, corporate LP department). Specify that the documents will be used by other investigators or staff — this establishes the purpose of designing for a future user. Include a brief reason for creating the materials (new firm being established, existing process being formalized, regional training initiative).

### Scenario Pattern
The scenario trigger is the need for standardized tools — either because the firm or department is new and is creating foundational templates for the first time, or because a real incident has demonstrated the need for formalized procedure and prompted creation of an awareness tool. The scenario should include: who will use the documents, in what context, and for what purpose. Include any specific incident or operational context that motivates the content.

### Instruction Pattern
Specify each deliverable separately with its own structural requirements. For guides: list required sections (Purpose, Scope, Procedures). For forms: specify the header names and the physical formatting requirements (lines for handwritten notes, checkboxes). For flowcharts: specify that each node corresponds to a section in the accompanying document. For awareness decks: specify that each slide covers one flowchart item. State exact document titles where required.

### Constraint Injection Points
- **Document titles:** often specified exactly and must match precisely
- **Form formatting:** ruled lines for handwritten notes (physical field-use design), checkbox fields, section header counts
- **Structural correspondence:** flowchart nodes must map 1:1 to presentation slides/sections
- **Anonymization:** incident-based tools must redact real names, location or facility identifiers, dates
- **Output format:** PDF for both in most cases; PowerPoint for awareness deck variant
- **Audience:** field investigators (operational language) vs. district managers (awareness/training register)
- **Dual vs. single deliverable:** guide + form vs. flowchart + awareness deck

### Structural Template

```
[PERSONA]: You are a [PI / Loss Prevention professional / Investigation Supervisor] at [ORG_TYPE]. [CONTEXT: You are establishing standardized procedures for your new firm / You are formalizing the response protocol following a recent incident].

[SCENARIO]: [TRIGGER_EVENT: Your firm's founder has asked you to create reusable templates for field investigators / A [INCIDENT_TYPE] incident at one of your stores has prompted the need for an awareness and training document]. [AUDIENCE: These documents will be used by [field investigators in the field / regional LP managers for training / new hires during onboarding]].

[TASK]: Create the following documents:

Document 1: [EXACT_TITLE]
- Type: [Operational guide / Observation form / Process flowchart]
- Required sections/elements: [LIST]
- Formatting requirements: [ruled lines for handwritten notes / checkbox fields / flowchart nodes]
- Purpose statement: [REQUIRED_PURPOSE_LANGUAGE]

Document 2: [EXACT_TITLE]
- Type: [Awareness presentation / Observation form / Supporting guide]
- Structure: [Each [flowchart item / major section] should correspond to one [slide / form section]]
- [ANONYMIZATION: Anonymize all identifying information — no real names, location identifiers, or dates]
- Purpose: [AWARENESS_OR_FIELD_USE_PURPOSE]

[CONSTRAINTS]:
- Document titles must match exactly as specified
- [ANONYMIZATION_RULE if applicable]
- Both documents must be delivered as [PDF / PDF + PowerPoint]
- Structural correspondence must be maintained between documents

[OUTPUT_SPECIFICATION]: [N] PDF documents [+ 1 PowerPoint file], with exact titles as specified above.
```

## 4. Reference File Requirements

### File Types Needed
- **None (primary modality):** This pattern typically requires no reference files — the content comes from domain knowledge. The worker must know investigation procedures, LP workflow standards, or undercover observation methodology.
- **Optional: Incident description or case brief (inline text):** When grounded in a specific real incident, the prompt itself contains the incident narrative that the flowchart and awareness deck must be based on.

### Data Characteristics
No structured reference data required. The input is domain knowledge about investigative or LP procedures. For incident-based variants, the incident description should be 200–400 words describing the sequence of events, roles involved, and outcome — detailed enough to derive flowchart nodes from it.

### File Complexity Spectrum
- **Minimal:** Single document — a standardized observation form with 5–8 section headers and ruled lines. No incident context required.
- **Moderate:** Two documents with no structural correspondence — a procedural guide (3–4 sections) and a blank observation form. Domain knowledge only.
- **Complex:** Two structurally-linked documents — a process flowchart (6–10 nodes) and a corresponding awareness presentation (one slide per flowchart item), both derived from a real anonymized incident narrative provided in the prompt.

## 5. Output Specification

### Primary Deliverable
- **Format:** PDF (always); PowerPoint added for awareness deck variant
- **Structure:** Dual deliverable — guide/flowchart + form/deck, with structural correspondence when required
- **Key quality signals:** Document titles match exactly, section headers are professional and descriptive, forms are designed for physical field use (lines long enough for handwritten entries, headers clearly labeled), structural correspondence maintained between paired documents, anonymization complete when required

### Secondary Deliverables (if any)
- PowerPoint awareness presentation (in the flowchart + awareness deck variant)

### Gold Output Characteristics
A gold output produces documents that could actually be printed and distributed to field investigators without modification. The guide uses professional PI or LP vocabulary and covers the full operational lifecycle (purpose, scope, when to use, step-by-step procedure, documentation requirements). The form has enough structure to guide an investigator's observations without being so prescriptive that it excludes relevant information. In the awareness deck variant, each slide contains the same information as the corresponding flowchart node — no additional content, no omissions. Where anonymization is required, zero identifying details remain.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of documents | 1 (single guide or form) | 2 (guide + form) | 2 with required structural correspondence (flowchart + deck) |
| Content grounding | Pure domain knowledge | Domain knowledge + named procedure | Incident-derived content requiring anonymization |
| Form design specificity | Simple headers with blank space | Section headers with ruled lines and character guidance | Multi-column form with conditional fields and checkboxes |
| Structural correspondence requirement | None | Loose (same sections in both docs) | Strict 1:1 (each flowchart node = one presentation item) |
| Anonymization scope | None | Partial (no location or facility identifiers) | Full (no names, dates, locations, or implicit identifiers) |
| Output format complexity | Single PDF | Two PDFs | PDF + PowerPoint |
| Document length | 1 page each | 2–3 pages each | 4–6 pages (guide) + 8–12 slides (deck) |

## 7. Boundary Cases & Adjacent Patterns

**I1 (Surveillance & Investigation Report Writing):** I1 and I2 can arise from the same underlying scenario. The distinction is deliverable type: I2 creates tools that enable future investigations; I1 produces a specific completed report for a specific case. If the output is a template, guide, form, or flowchart used by other investigators, it is I2. If the output is a client-deliverable report about a specific subject, it is I1.

**C1 (Standard Operating Procedure / General Order):** C1 also produces procedural documents, but for general organizational operations (administrative processes, police department procedures). The distinction is domain specificity: C1 applies to any organizational operation; I2 is specific to surveillance and investigation tradecraft. If the SOP is about cash handling or HR processes, use C1. If it explicitly requires PI or LP operational knowledge, use I2.

**C2 (Compliance Checklist / Assessment Tool Design):** C2 creates scoring-based assessment tools grounded in regulatory text. I2 creates field-use forms designed for observation and documentation. The distinction is grounding: C2 references specific regulations; I2 references investigative procedures and operational workflows.
