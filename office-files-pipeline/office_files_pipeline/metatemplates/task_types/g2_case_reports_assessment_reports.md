# Case Reports & Assessment Reports

**Macro Category:** G — Form-Based & Clinical Documentation
**Pattern ID:** G2

## 1. Pattern Description

The worker must transform raw source materials — shorthand case notes, multiple legal/administrative documents, tax source documents — into a polished, formally structured professional report by following a provided template or regulatory format. The cognitive core is content transformation and template-guided synthesis: the worker cannot simply copy-paste source material but must rewrite it into professional prose, accurately interpret legal or clinical source documents, apply professional judgment in designated opinion sections, and satisfy structural requirements such as section counts, page ranges, and placeholder conventions. This pattern is distinguished from pure data entry by the requirement for professional narrative writing, from strategic document authoring by the mandatory template adherence, and from clinical SOAP notes by the broader domain context (social work, child support enforcement, tax) and the multi-document source structure.

## 2. O*NET Grounding

### Occupation Families
- 21-1021 — Child, Family, and School Social Workers — Produce developmental history reports, psychosocial assessments, and IEP-supporting documentation
- 21-1093 — Social and Human Service Assistants — Compile case creation reports for government system entry in child support, welfare, and public assistance programs
- 13-2082 — Tax Preparers — Complete statutory tax return forms and supporting schedules from multi-document tax source files
- 13-1041 — Compliance Officers — Prepare case files and structured reports for regulatory review
- 21-1012 — Healthcare Social Workers — Produce psychosocial assessments and care coordination reports

### Key Work Activities (O*NET vocabulary)
- Documenting/Recording Information
- Processing Information
- Evaluating Information to Determine Compliance with Standards
- Assessing Individuals' Characteristics, Needs, or Situations
- Communicating with Supervisors, Peers, or Subordinates

### Knowledge Domains (O*NET vocabulary)
- Psychology
- Law and Government
- Education and Training
- English Language
- Clerical
- Customer and Personal Service
- Economics and Accounting (for tax preparation variant)

### Generalizable Work Context
This task type arises in government human services agencies, public school districts, child support enforcement offices, tax preparation firms, and any organization that must produce formal case documentation from intake materials. The trigger is a case assignment — a new client or case number is handed to the worker along with raw source materials (notes, legal documents, forms). The audience is a review team, a regulatory system (DCS, IRS, IEP team), or a supervising professional. The deliverable is a single finalized PDF document that is complete and ready for submission or filing.

## 3. Prompt Construction Template

### Persona Pattern
Assign a professional role with explicit case-based responsibilities: school social worker assigned to a Child Study Team, child support enforcement investigator, tax preparer at an accounting firm. Specify the organizational context and the regulatory or institutional framework the worker operates within (e.g., IEP process in a named school district, DCS system entry requirements, IRS regulations for a specified tax year). Seniority is mid-level — independently competent but with a supervisor or senior reviewer as the defined audience.

### Scenario Pattern
Describe a case assignment: a specific client or case number has been received. Provide the reference materials as a list of attached files (shorthand notes + template document + recommendation bank; multiple PDFs of legal and case documents; tax source documents + intake questionnaire). Describe the purpose and use context of the final report (multidisciplinary team meeting preparation, DCS system entry, senior accountant review). The scenario should specify any conventions that deviate from defaults (placeholder names, fields to leave blank, compliance year).

### Instruction Pattern
Two-step instruction: (1) review and synthesize the attached source materials; (2) complete the template or form according to specified requirements. Requirements should include: page range or length target, a "no copy-paste" or "rewrite in professional prose" constraint, specific sections that require professional opinion or judgment (Impressions, Recommendations, Assessment sections), quantity constraints (e.g., a required count of numbered recommendations), and output format with filename convention.

### Constraint Injection Points
- **Content transformation constraints:** prohibition on copy-paste from notes; all source material must be rewritten into professional sentences; notes written in shorthand must be rendered in complete professional prose
- **Structural constraints:** page range (e.g., a specified minimum-to-maximum page count), exact section count, number of recommendations, report sections derived from a mandatory template
- **Placeholder/convention constraints:** specific placeholder text for sensitive fields (e.g., "SCHOOL" instead of school name), fields to be left blank per instructions, date of evaluation specified
- **Professional judgment constraints:** impressions narrative requires worker's professional opinion on client needs, not just data summary; recommendations must be drawn from a bank but may be independently drafted; clinical/legal judgment is the differentiating content in designated sections
- **Accuracy constraints:** for legal/regulatory documents, all information must accurately reflect source documents with no omissions (for DCS system entry or IRS e-filing)
- **Compliance constraints:** must satisfy current-year regulatory requirements (e.g., IRS regulations for the applicable tax year), must follow guide layout exactly (Case Creation Guide), must include all required Schedules/Forms

### Structural Template

```
[PERSONA]: You are a [PROFESSIONAL_ROLE] at [ORGANIZATION_TYPE]. [REGULATORY_CONTEXT].

[CASE_SCENARIO]: You have been assigned a new case involving [CLIENT_NAME] ([CASE_ID_OR_CONTEXT]). [BACKGROUND_ON_CASE: referral reason, case type, purpose of report].

[REFERENCE_MATERIALS]:
You have been provided with the following documents:
1. [FILE_1]: [DESCRIPTION — template/guide OR shorthand notes OR source data document]
2. [FILE_2]: [DESCRIPTION]
3. [FILE_3]: [DESCRIPTION]
[... additional files as needed]

[TASK]:
1. Review all attached source materials.
2. Complete the [REPORT_TYPE] using the [TEMPLATE/GUIDE_NAME] as your structural framework.

[REQUIREMENTS]:
- Rewrite all notes/source material in complete, professional [sentences/prose/language]; do not copy-paste directly.
- [STRUCTURAL_REQUIREMENT: e.g., Report must fall within a specified page range / Include a specified count of numbered recommendations]
- [PLACEHOLDER_CONVENTION: e.g., Use "SCHOOL" throughout as the school name placeholder]
- [BLANK_FIELD_CONVENTION: e.g., Leave social worker name/address and student address fields blank]
- [JUDGMENT_SECTION: e.g., Write a School Social Work Impressions narrative reflecting your professional opinion on the supports this student needs]
- [ACCURACY_REQUIREMENT: e.g., All information must accurately reflect source documents; complete and ready for DCS system entry]

[CONSTRAINTS]:
- [COMPLIANCE_CONSTRAINT: e.g., Must comply with IRS regulations for the applicable tax year; include all required Schedules/Forms for e-filing]
- [FORMAT_CONSTRAINT: Output as PDF titled "[FILENAME]"]
- [REVIEWER_CONTEXT: Prepared for senior accountant review / submitted for multidisciplinary team preparation]
```

## 4. Reference File Requirements

### File Types Needed
- **Primary source materials (2–4 files):**
  - Shorthand/unpolished notes document (docx): case notes, clinical notes, or field notes written in abbreviated or informal style; serves as the raw content to be transformed into professional prose
  - Legal/administrative source documents (pdf or docx): court orders, paternity results, case detail summaries, tax forms, intake questionnaires — documents that contain factual information to be accurately extracted and incorporated
  - Template or guide document (docx or pdf): the structural blueprint for the output report; defines required sections, field headings, placeholder conventions, and formatting standards
  - Recommendation or reference bank (optional, docx): a curated pool of pre-written items (recommendations, standard clauses, boilerplate) that the worker selects from or adapts

### Data Characteristics
Source materials for this pattern are heterogeneous in format and polish:
- Notes documents: shorthand, fragmented sentences, informal vocabulary, possibly bullet-pointed; represent the raw material that must be elevated to professional prose
- Legal/official documents: formal register, precise factual content (dates, names, dollar amounts, legal obligations, test results), structured by official format; must be accurately extracted and correctly placed
- Templates: section headers with placeholder fields or blank prompts; define the mandatory structure the output must follow; may include conventions for sensitive data handling (leave blank, use placeholder)
- Tax source documents: official IRS/employer-issued forms (W-2, 1099-INT, 1099-B, 1099-DIV, Schedule K-1) plus a structured client questionnaire; require matching to correct IRS form lines
- Reference/recommendation banks: organized lists of professional recommendations or standard clauses; worker must select contextually appropriate items

### File Complexity Spectrum
- **Minimal:** Two files — a partially completed template and a single source document with all facts clearly stated; no judgment sections, no page-range constraints, no placeholder conventions; output is 2–4 pages
- **Moderate:** Three files — shorthand notes (content to transform), a multi-section template, and one legal or reference document; one professional judgment section (Impressions); page range of 5–10 pages; one placeholder convention
- **Complex:** Four-plus files — shorthand notes requiring full prose rewriting, multiple legal documents requiring accurate extraction (court order + paternity results + case summary), template with all sections, and a recommendation bank; professional judgment narrative plus a substantial set of individually crafted numbered recommendations; a long, tightly bounded page range; multiple placeholder and blank-field conventions; no direct copy-paste allowed; output ready for regulatory system entry

## 5. Output Specification

### Primary Deliverable
- **Format:** PDF (the dominant output format for this pattern)
- **Structure:** Follows the provided template structure exactly — section headers as defined in the guide or template; all sections completed with no placeholder text remaining; professional prose throughout; judgment/impressions section containing worker's synthesized professional opinion; recommendations or conclusions section meeting the specified count requirement
- **Key quality signals:** No shorthand or informal language surviving from source notes; all factual data from source documents accurately placed in correct sections; professional opinion sections contain substantive analysis rather than data restatement; all required template sections present; page range satisfied; filename conventions followed

### Secondary Deliverables (if any)
- None in most cases — the PDF is the single deliverable
- For the tax preparation variant: the "PDF" IS the completed IRS tax return form and its supporting schedules — all required schedules must be included and complete for e-filing

### Gold Output Characteristics
A gold case report transforms every piece of shorthand source material into polished professional language appropriate to the discipline (social work, child support enforcement, tax preparation). For social work/case reports: the Impressions section demonstrates actual clinical/professional judgment — it does not merely summarize the notes but synthesizes them into a coherent professional opinion about client needs and recommended supports. For legal/government reports: every field in the template is completed, every factual item from source documents is accurately reflected, and the document is indistinguishable from one produced by an experienced professional in that field. For tax returns: all applicable Schedules are identified and completed, income from all source documents is correctly categorized and placed on the correct form lines, and the return is compliant with current-year regulations.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Source material polish | Source document is clean prose or a structured form | Source document is semi-structured with some informal language | Shorthand, fragmented, abbreviated case notes requiring complete rewriting |
| Number of source files | 2 files | 3 files | 4–14 files of varying types (notes + template + legal docs + recommendation bank) |
| Professional judgment requirement | All content is factual extraction only | One impressions or conclusions section with brief professional comment | Full narrative impressions section plus a substantial set of individually crafted recommendations |
| Page range constraint | Short (2–4 pages) | Moderate (5–8 pages) | Long, with a tight page-count range, or a strict page limit |
| Placeholder/convention complexity | No placeholder conventions | One placeholder convention (e.g., use "SCHOOL") | Multiple conventions: placeholder text + blank fields + naming conventions + date specification |
| Compliance specificity | General professional standards | Organizational template compliance | Multi-schedule regulatory compliance (IRS current-year rules, DCS system entry requirements) |

## 7. Boundary Cases & Adjacent Patterns

**Most similar patterns:**
- **G1 (Clinical Documentation — SOAP Notes, Care Plans):** Both produce structured professional documents from provided information. G2 is distinguished by multi-document source consolidation (2–14 files), multi-domain applicability (social work, legal, tax — not just clinical), and the transformation of informal/shorthand source material into professional prose. G1 uses a single inline clinical scenario and produces a medically standardized format (SOAP/NANDA). Choose G2 when the source material requires prose rewriting and the output format is a case-specific report or statutory form.
- **B5 (Data Entry with Protocol-Driven Decision Making):** Both involve populating a template from multiple source files. B5 produces structured Excel data with decision logic applied; G2 produces polished narrative prose in a PDF report. The key differentiator is prose quality and professional judgment: G2 requires writing, B5 requires data placement and rule application.
- **G4 (Medical Necessity & Insurance Documentation):** G4 produces documents for insurance or financial assistance purposes using a patient chart as primary input. G2 uses broader case source materials (not necessarily clinical) and produces reports for professional review or regulatory system entry. If the output is addressed to an insurance payer, it is G4.
- **C1 (Standard Operating Procedure / General Order):** C1 produces organizational policy documents authored from domain knowledge; G2 produces case-specific reports from provided source materials about a specific client or case. C1 documents organizational processes; G2 documents individual cases.
