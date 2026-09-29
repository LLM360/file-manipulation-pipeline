# Form & Template Design

**Macro Category:** C — Policy, Procedure & Standards Authoring
**Pattern ID:** C5

## 1. Pattern Description

The worker designs or redesigns a fillable form, intake questionnaire, tracking spreadsheet, or operational template for recurring organizational use. Unlike a one-time analytical deliverable, the output is a reusable tool — it will be completed by other people on an ongoing basis, stored in a system, and may need to be compatible with downstream digital platforms (CRM systems, Google Forms, helpdesk macro tools). The cognitive core is information architecture for operational contexts: the worker must determine what data needs to be collected, how to structure the collection for usability by the intended user (often non-expert), what field types are appropriate (text, Yes/No, dropdown, checkbox, date), and how to organize sections logically for the workflow it supports. What distinguishes this pattern is the emphasis on the template's reusability, usability, and operational context — the form is a tool designed to be used repeatedly by someone other than the creator.

## 2. O*NET Grounding

### Occupation Families
- 43-6013 Medical Secretaries and Administrative Assistants — Design clinical workflow forms (payment decline tracking spreadsheets, patient intake checklists, fax cover sheets)
- 11-9141 Property, Real Estate, and Community Association Managers — Create violation inspection questionnaires and operational templates for inspection companies and sub-associations
- 13-1111 Management Analysts / Consultants — Revise and improve existing organizational forms (student evaluation forms, client intake questionnaires) for better information capture
- 29-1141 Registered Nurses (Administrative context) — Design clinical administrative forms (intake documentation, escalation cover sheets) for facility operational compliance
- 11-3011 Administrative Services Managers — Create tracking templates and operational forms for department-level use

### Key Work Activities (O*NET vocabulary)
- Documenting/Recording Information
- Developing Procedures, Policies, and Forms
- Organizing, Planning, and Prioritizing Work
- Communicating with Customers or Patients (form-design determines what they experience)
- Evaluating Information to Determine Compliance with Standards

### Knowledge Domains (O*NET vocabulary)
- Clerical
- Administration and Management
- Customer and Personal Service
- English Language
- Medicine and Dentistry (for clinical forms)
- Law and Government (for forms with compliance requirements)

### Generalizable Work Context
A department or organization needs a new form to standardize data collection for a recurring process — or has an existing form that is disorganized, incomplete, or not compatible with its current workflow or systems. The trigger is operational: a new process is being established (patient transfer requests, declined payment outreach), an existing form is generating poor-quality data or causing downstream errors, or a system migration requires form redesign (moving to Google Forms, adding to CRM as macros). The resulting form will be used by administrative staff, field operators, or clients on a recurring basis.

## 3. Prompt Construction Template

### Persona Pattern
Assign an administrative, operational, or coordinative role with ownership of the process the form supports: Medical Secretary (billing and patient management), Community Association Manager (property inspection coordination), Client Services Consultant (improving client feedback collection), Registered Nurse (clinical administrative workflow design). The organizational type should explain the operational context: healthcare clinic, homeowners association, small business, outpatient care facility. The persona has enough domain knowledge to know what data needs to be captured but may benefit from design best practices.

### Scenario Pattern
Describe the operational workflow that the form supports: processing inter-facility patient transfer requests; tracking patients with declined subscription payments; conducting property violation inspections; collecting student feedback after class. Identify who will fill out the form (field supervisors, administrative staff, patients, students) and how it will be used downstream (routing to other parties, entering into a system, triggering actions). If redesigning an existing form, describe the problems with the current version (disorganized, missing key fields, redundant questions, not digital-compatible).

### Instruction Pattern
For new form creation: "Create a [FORMAT] form for [PURPOSE] that includes [SECTION_LIST] with [FIELD_TYPE_REQUIREMENTS]." For redesign: "Revise the attached form to [IMPROVEMENT_OBJECTIVES]. Organize it into [SECTIONS] and ensure compatibility with [PLATFORM]." Specify exact field requirements, dropdown option values, page limits, mandatory vs. optional distinctions, and any compliance elements (confidentiality statement, HIPAA notation, branding).

### Constraint Injection Points
- **Named sections**: Required content areas by exact name specified in the prompt (e.g., a respondent or demographic-info section, a feedback or evaluation section, a follow-up-interest section, a referral-source section, a section for shareable comments or testimonials)
- **Field types**: Dropdowns with specified option values (subscription plans, urgency levels, Yes/No with circle option); checkboxes; date fields; text fields with blank lines
- **Page limits**: Maximum document length per deliverable type (e.g., a short cover document capped at one page; a checklist capped at a low page count; a longer document left open-ended but expected to stay concise)
- **Branding/compliance elements**: Company logo placement; HIPAA confidentiality statement from a provided file; an internal-use-only notation; page numbers
- **Platform compatibility**: Google Forms structure; CRM macro copy-paste compatible; digital fillable vs. print-and-write
- **Tracking columns**: For data collection forms — date sent, date received, staff initials; status dropdowns; outreach tracking columns
- **Optional field designation**: Demographic questions marked as optional; flexibility for community-specific additions
- **Source document requirements**: All questions from an attached reference document must be incorporated; existing form fields must be restructured but retained

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE]. [CONTEXT: new process requiring standardized data collection OR existing form needing redesign].

[TRIGGER]: [OPERATIONAL_PROBLEM or NEW_PROCESS_LAUNCH]. You need to create [N] form(s) for use by [USER_AUDIENCE] to [PURPOSE].

[DELIVERABLE_SPECIFICATION]:
Create a [FORMAT — Word/Excel/PDF] [DOCUMENT_TYPE — form/template/checklist/spreadsheet] with the following:

[SECTION_REQUIREMENTS]:
Section 1: [SECTION_NAME] — Fields: [FIELD_1 (type)], [FIELD_2 (dropdown: option_A | option_B | option_C)], [FIELD_3 (required/optional)]
Section 2: [SECTION_NAME] — Fields: [...]
[...]

[FIELD_TYPE_REQUIREMENTS]:
- Dropdowns: [FIELD_NAME] with options [OPTION_LIST]
- Checkboxes: [FIELD_NAME] (check all that apply / select one)
- Y/N fields: Use circle-one format: Y / N
- Free text: [N] blank lines per item
- Date fields: [FIELD_NAME] (MM/DD/YYYY format)

[COMPLIANCE_ELEMENTS]:
- Include [LOGO] from attached file
- Embed [CONFIDENTIALITY_STATEMENT] from attached file
- Add [HIPAA_NOTATION / INTERNAL_STAFF_ONLY marker]
- Page numbers: [YES/NO]

[PLATFORM_COMPATIBILITY]:
This form will be used in [GOOGLE_FORMS / CRM_MACRO / PRINT / SHAREPOINT].
Design for [DIGITAL_FILLABLE / PRINT_AND_WRITE].

[OPTIONAL_ADDITIONS]:
Include blank lines after each [CATEGORY] for [PURPOSE — community-specific additions, custom items].

[CONSTRAINTS]:
- Page limit: [N] pages maximum
- Format: [Word/Excel/PDF]
- Audience: [DESCRIPTION — frontline staff / patients / field inspectors]
```

## 4. Reference File Requirements

### File Types Needed
- **Existing form to revise** (docx): Current version of the form being improved — provides baseline structure, existing fields, and the gaps/problems to be addressed; worker must retain useful elements and restructure/add per the new specifications
- **Patient information list or violation categories** (pdf/docx): Reference document listing all data elements or violation types that must be included in the new form — ensures exhaustive coverage without requiring the worker to generate the item list from scratch
- **Branding and compliance assets** (docx/pdf): Company logo file (embedded in a Word document); pre-written HIPAA or confidentiality statement text that must be incorporated verbatim; defines the visual and legal elements to include
- **No reference file (pure design)**: Some form design tasks require no reference files — the worker designs from scratch based on domain knowledge of the process and standard form design practices (e.g., designing a payment decline tracking spreadsheet with standard CRM compatibility)

### Data Characteristics
Existing form documents: consumer-facing or administrative questionnaire with current field structure, often with identified gaps (redundant questions, missing sections, poor organization). Violation or data element reference lists: structured enumeration of categories and sub-items, organized by domain (architectural regulations, landscaping, food safety, etc.) — each item must appear in the output form. Branding assets: typically a small image or short text block embedded in a document, not a complex data source.

### File Complexity Spectrum
- **Minimal:** No reference files; pure design task from operational requirements stated in the prompt; single deliverable (one Excel tracking spreadsheet or one Word template); no compliance elements beyond standard formatting
- **Moderate:** One reference file (existing form to revise, or a data element list to incorporate); dual deliverable (tracking spreadsheet + email template); dropdown and checkbox formatting required; platform compatibility constraint (e.g., Google Forms or a CRM macro tool)
- **Complex:** Multiple reference files (e.g., a logo, a compliance statement, and a detailed data element list); two or more separate form deliverables with different purposes (e.g., a short cover document plus a detailed checklist); regulatory compliance requirements (e.g., HIPAA or other applicable clinical/facility standards); precise page limits and exact field requirements for each document; specific notation requirements (e.g., an internal-use-only marker, page numbers, contact instruction footer)

## 5. Output Specification

### Primary Deliverable
- **Format:** Word (.docx) for fax cover sheets, checklists, and intake questionnaires; Excel (.xlsx) for tracking spreadsheets with data validation features; PDF for printed inspection forms
- **Structure:** Header block (organization name/logo, form title, date, ID fields) → labeled sections with field-level content → footer (contact information, compliance notices, page count)
- **Key quality signals:** All specified fields present with correct field types (dropdown with specified options, not free text); sections are named and ordered logically relative to the workflow they support; field labels use the correct terminology for the audience; optional fields are clearly marked as optional; compliance elements (logo, confidentiality statement) are placed correctly; page limit is respected; form can be completed by its intended user without additional guidance

### Secondary Deliverables (if any)
- Companion email template (Word): notification message to send along with the form (e.g., a payment or account-status alert to affected customers; a notice accompanying the rollout of a new operational process)
- Test user example row: one sample completed row in a tracking spreadsheet showing how fields should be populated

### Gold Output Characteristics
A gold-standard form output is immediately usable by its intended audience without explanation: field labels are unambiguous; field types match the data being collected (dropdowns where finite option sets exist; free text where narrative is expected; yes/no circles where binary evaluations are needed); sections flow in the same order as the real-world workflow they support; compliance elements are embedded correctly (confidentiality statement is complete and placed in the right position; logo appears on all pages as specified); page constraint is respected without truncating required content; and platform compatibility is demonstrated by design choices (avoiding complex formatting incompatible with Google Forms; keeping table structures that CRM macros can paste cleanly).

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of form deliverables | Single form | Two forms with different purposes and formats | Three or more separate documents (e.g., a cover document, a checklist, and a companion email template) |
| Reference file inputs | None — designed from scratch | One reference (existing form to revise OR data element list) | Three or more reference files (e.g., a logo, a compliance statement, and a data element list) |
| Field type complexity | Simple text fields only | Mix of text, dropdown, and checkbox fields | Named dropdown options specified, Y/N circle fields, date fields with tracking columns, internal-use-only annotations |
| Compliance/branding elements | None required | Company logo included | Logo + HIPAA confidentiality statement + page numbers + specific footer content with contact details |
| Platform compatibility | Print-only (no digital requirements) | Google Forms-compatible structure | CRM macro compatible (copy-paste format) with data validation features |
| Page constraints | No page limit | A page limit on a single deliverable | Simultaneous page limits across multiple deliverables of different lengths |
| Source coverage requirement | Fields designed from domain knowledge | Must include all items from a reference list | Must incorporate all reference-list items with their sub-questions, each on its own line, with blank lines for open-ended or category-specific additions |

## 7. Boundary Cases & Adjacent Patterns

**C1 (Standard Operating Procedure):** An SOP governs how a process is executed (narrative workflow). A form is the data-collection instrument used within or alongside a process. SOPs often include a companion form as a secondary deliverable — but if the primary deliverable is the operational template or fillable form rather than the procedure narrative, classify as C5. A Change Request Form designed to mirror an SOP's process steps is a C5 secondary deliverable; the SOP is C1.

**C2 (Compliance Checklist/Assessment Tool):** C2 assessment tools are audit instruments designed to evaluate compliance (questions answered Yes/No, scored against a threshold, triggering escalation). C5 forms collect operational data for a process (patient admission data, student feedback, property inspection details). The distinguishing question: is the form evaluating compliance or collecting data for an operational workflow? A safety audit checklist with scoring is C2; a patient intake checklist that collects clinical information is C5.

**B5 (Data Entry with Protocol-Driven Decision Making):** B5 involves populating an existing template with data from source documents, applying embedded rules to determine values. C5 involves designing the template itself. When the task is to create the form (choose fields, structure sections, design layout), classify as C5. When the task is to fill out a pre-existing template with data from other files, classify as B5.

**B3 (Compliance Report from Transaction Data):** B3 produces narrative compliance findings by analyzing transaction data. C5 designs the form or template that would be used to collect data in the first place. No meaningful overlap — the only edge case is a form that is designed to serve as a compliance report template (rare; classify as C5 since the primary task is design, not analysis).
