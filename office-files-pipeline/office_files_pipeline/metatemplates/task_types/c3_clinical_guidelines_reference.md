# Clinical Guidelines & Reference Guides

**Macro Category:** C — Policy, Procedure & Standards Authoring
**Pattern ID:** C3

## 1. Pattern Description

The worker produces a formal clinical document — prescribing guideline, formulary, care plan, SOAP note, or reference guide — grounded in evidence-based medicine, professional society standards, or pharmacological knowledge. The deliverable serves as an authoritative clinical reference that will guide clinical decisions made by the practitioner or by other clinicians following the author's recommendations. The cognitive core is clinical synthesis: the worker must integrate domain expertise (anatomy, pharmacology, diagnostic criteria, treatment protocols) with applicable professional standards (AHA guidelines, NANDA nursing diagnoses, specialty-society prescribing guidance) to produce a document that is both clinically accurate and structurally formatted for its intended use context. What distinguishes this pattern from general document authoring is the dual accountability to clinical accuracy and document structure — a SOAP note must follow the precise S/O/A/P format with clinically defensible content; a prescribing guideline must be evidence-grounded and cite its sources.

## 2. O*NET Grounding

### Occupation Families
- 29-1060s Physicians and Surgeons (Medical Directors) — Write prescribing guidelines and clinical standards for practice-wide implementation
- 29-1051 Pharmacists — Compile drug formularies, create days' supply reference guides, design pharmacy compliance references
- 29-1171 Nurse Practitioners — Produce SOAP notes, clinical care plans, educational health posters, and clinical lectures
- 29-1141 Registered Nurses — Create SBAR communication templates, nursing care plans, clinical handover tools
- 11-9111 Medical and Health Services Managers — Develop clinical protocols and reference documents for care coordination functions

### Key Work Activities (O*NET vocabulary)
- Documenting Medical Information
- Analyzing Data or Information
- Making Decisions and Solving Problems
- Providing Medical Care (when clinical judgment is the core)
- Developing and Delivering Educational Programs (for clinical education materials)
- Processing Information

### Knowledge Domains (O*NET vocabulary)
- Medicine and Dentistry
- Biology
- English Language
- Customer and Personal Service (for patient-facing materials)
- Law and Government (for regulatory formulary compliance)
- Education and Training (for clinical education documents)

### Generalizable Work Context
A senior clinician, pharmacist, or medical director is creating a clinical document for one of three purposes: (1) a practice-wide standard to ensure consistency across providers (prescribing guidelines, formularies), (2) patient-specific documentation for a clinical encounter (SOAP note, care plan), or (3) a reference or educational resource for clinical staff or patients (poster, reference guide, SBAR template). The trigger is organizational (new practice launch, staff training need, audit compliance) or patient-driven (active clinical encounter requiring documentation). Evidence-based sourcing from professional society guidelines is required for categories 1 and 3; patient-specific clinical data drives categories 2.

## 3. Prompt Construction Template

### Persona Pattern
Assign a licensed clinical role with appropriate specialty: Medical Director (prescribing guidelines), Pharmacist (formulary, reference guide), Nurse Practitioner (SOAP note, educational lecture), PACU Nurse (care plan), ED Nurse (communication template). The organizational context should explain the clinical practice setting: telemedicine startup, outpatient clinic, hospital department, community pharmacy, pediatric hospital. For prescribing guidelines and formularies, the persona is usually setting organizational standards for other clinicians; for SOAP notes and care plans, they are documenting a specific patient encounter.

### Scenario Pattern
For practice-wide standards: name the clinical area (hormone therapy, hypertension, pharmacy billing compliance) and explain the organizational trigger (new practice launch, provider inconsistency, audit risk). For patient encounter documentation: provide the full clinical vignette including HPI, PMH, relevant history, vital signs, and physical exam findings inline. For reference/education materials: name the target audience (nursing students, pharmacy technicians, general public at health fair) and specify the delivery context (lecture, poster, quick-reference card).

### Instruction Pattern
Prescribing guidelines: "Research current evidence-based standards from [named societies/sources] and create a comprehensive [document type] with citations." Formularies: "Identify [drug categories], research pricing from [named sources], and organize using the provided template." SOAP notes: "Create a SOAP note for [patient identifier] using the clinical information provided." Care plans: "Develop a care plan with exactly [N] nursing diagnoses, [N] outcomes per diagnosis, [N] assessments per diagnosis, and [N] interventions per diagnosis." Reference guides: "Create a [format] reference guide covering [content areas] for [audience]."

### Constraint Injection Points
- **Evidence source requirements**: Named professional societies (e.g., AHA or other relevant specialty associations), specific databases, named URLs (an online drug-pricing lookup tool, professional society websites for guidelines)
- **Citation requirement**: Whether citations are required per recommendation, per section, or as a reference list; specific citation format
- **Clinical content scope**: Named diagnoses, patient populations, medication classes, or clinical scenarios that must be covered
- **Structural template**: SOAP format (Subjective/Objective/Assessment/Plan); SBAR (Situation/Background/Assessment/Recommendation); care plan (diagnosis/outcome/assessment/intervention counts per diagnosis)
- **Patient-specific constraints**: Named drug allergies that restrict treatment choices; specific vital signs or lab values that must be incorporated and addressed; comorbidities that affect clinical reasoning
- **Page/format constraints**: One-page care plan; 1–2 page reference guide; large-format poster (specified print dimensions); slide-count-limited lecture
- **Audience register**: Patient-facing (plain language); clinician-facing (clinical terminology acceptable); mixed audience (dual-register content)
- **Formulary rules**: FDA-approved vs. off-label tiers; brand deduplication when formulations are identical; pricing source specified

### Structural Template

```
[PERSONA]: You are a [CLINICAL_ROLE] at [CLINICAL_SETTING]. [CONTEXT: organizational or clinical trigger].

[TASK_TYPE — choose one]:

A) PRACTICE-WIDE STANDARD (prescribing guideline / formulary):
"Your CMO has asked you to [create/compile] a [DOCUMENT_TYPE] for [CLINICAL_AREA] to serve as the clinical standard for all [PROVIDER_TYPE] at [ORG_NAME]."
Source requirements: Research current standards from [NAMED_SOCIETIES/DATABASES]. Include citations for each recommendation.
Scope: [PATIENT_POPULATION / DRUG_CLASSES / CLINICAL_SCENARIOS]

B) PATIENT ENCOUNTER DOCUMENTATION (SOAP note / care plan):
"Create a [SOAP note / nursing care plan] for [PATIENT_IDENTIFIER] using the clinical information below."
[PATIENT_VIGNETTE: Date, Chief Complaint, HPI narrative, PMH, medications, allergies, social history, family history, vital signs, physical exam findings, relevant lab/imaging results]
Structural requirements: [SOAP format / N diagnoses × N outcomes × N assessments × N interventions]
Constraints: [ALLERGY_RESTRICTIONS / CLINICAL_FLAGS that must be addressed in the plan]

C) REFERENCE / EDUCATION DOCUMENT (poster / reference guide / template):
"Create a [FORMAT/SIZE] [DOCUMENT_TYPE] for [AUDIENCE] covering [N] content areas: [CONTENT_AREA_LIST]."
Visual requirements: [tables / icons / product comparisons / image sourcing]
Source requirements: [KNOWLEDGE_BASED / specific URL sources]
Page/size constraints: [N pages / large-format print dimensions / 1-page limit]

[OUTPUT_SPECIFICATION]: [FORMAT], [FILE_NAME], [STRUCTURE]
```

## 4. Reference File Requirements

### File Types Needed
- **Formulary template** (xlsx, optional): Pre-defined column structure for organizing drug formulary data — no medication data pre-populated; defines the schema the output must follow (medication name, NDC, strength, dose form, route, price, tier)
- **Patient chart** (docx, optional): For care plan and appeal letter tasks — contains full clinical history, diagnosis, medication list, prior treatment trials; primary content source for patient-specific documents
- **Clinical scenario inline** (no file): For SOAP notes — the complete clinical vignette is embedded in the prompt text (HPI, PMH, vitals, exam findings); no reference file needed
- **URL to professional society guidelines** (web research): Named URLs to relevant specialty societies, AHA, FDA, or pharmacy board websites providing the evidence base for guidelines and formularies
- **Regulatory source** (pdf/URL): For pharmacy compliance documents — state board of pharmacy lawbook, FDA drug approval database

### Data Characteristics
For formulary templates: column headers define the schema; 0 data rows; typically 5–10 columns covering drug identification, dosing, route, pricing, and tier classification. For patient charts: semi-structured clinical narrative with discrete data points (lab values, vital signs, medication names and doses) embedded in prose; may include prior treatment response assessments. For clinical vignettes: highly structured inline data with named fields (DOB, CC, HPI, PMH, FH, SH, Allergies, Medications, VS, PE findings).

### File Complexity Spectrum
- **Minimal:** Pure knowledge task — clinical vignette provided inline (SOAP note or care plan); no reference files; clinical data is complete and unambiguous
- **Moderate:** Formulary template provided defining schema; worker researches drug list and pricing using named web sources; brand deduplication and FDA approval tier rules apply
- **Complex:** Prescribing guideline requiring synthesis from multiple named professional societies (national and international specialty associations) plus textbooks and peer-reviewed literature; citations required per recommendation; must cover full prescribing workflow (evaluation, indication, contraindication, regimen selection, monitoring, follow-up)

## 5. Output Specification

### Primary Deliverable
- **Format:** Word (.docx) for guidelines, appeals, and care plans; Excel (.xlsx) for formularies; PDF for posters, reference guides, and SBAR templates
- **Structure:** Varies by sub-type:
  - Prescribing guideline: sections for background, indications, contraindications, regimen options, monitoring, special populations, references
  - Formulary: tabular rows per medication with schema from template; organized by drug class or approval tier
  - SOAP note: S / O / A / P sections in exact order; each section labeled
  - Care plan: three-column or four-column table (diagnosis | outcome | assessments | interventions); prescribed item counts per diagnosis
  - Reference guide: section-based layout with labeled headers; tables, icons, or product comparison visuals as specified
  - SBAR template: table with one row per SBAR block and separate columns for guidance versus fill-in prompts

- **Key quality signals:** Clinical accuracy (drug names, dosing parameters, diagnostic criteria match current standards); structural adherence (correct section order, prescribed item counts); citation quality (named society guidelines cited correctly); clinical constraints addressed (allergies, comorbidities, vital sign abnormalities integrated into the plan); language register appropriate to audience (plain language for patient-facing, clinical terminology for provider-facing)

### Secondary Deliverables (if any)
- Patient counseling handout (plain language version of clinical guidelines)
- Speaker notes alongside clinical lecture slides
- Exception handling sections for edge cases in clinical workflows

### Gold Output Characteristics
For SOAP notes: gold output integrates all provided clinical data without omission, constructs an assessment with appropriate differential diagnosis considerations, and builds a plan that addresses each clinical abnormality (including allergy-appropriate drug selection, specific lab follow-up, and safety considerations). For prescribing guidelines: gold output cites named professional societies per recommendation, distinguishes evidence-based from consensus recommendations, covers the full prescribing workflow, and limits scope to the defined patient population. For formularies: gold output includes correct medication names (no trade/generic confusion), covers both FDA-approved and off-label tiers as specified, provides accurate pricing from the named source, and applies deduplication rules correctly.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Clinical knowledge breadth | Single condition, straightforward management | Multiple comorbidities or differential diagnosis required | Rare clinical scenario with evidence-based synthesis from multiple societies across countries |
| Source research requirement | Pure domain knowledge (no web research) | One named professional society URL | Multiple named specialty societies (national and international) + textbooks + peer-reviewed literature |
| Clinical constraint complexity | No drug allergies, no comorbidities | One relevant allergy restricting treatment | Multiple allergies + drug interactions + comorbidity-specific considerations |
| Structural prescription | Open format | Named sections with content requirements | Exact item counts per section (e.g., a fixed number of diagnoses, each with a fixed number of assessments and interventions) |
| Audience register | Single audience (clinician or patient) | Dual audience requiring separate sections | Mixed audience with simultaneous accessibility requirements (plain language + clinical depth) |
| Format complexity | Prose document | Structured table or template-constrained | Large-format design with spatial layout (e.g., a large-format poster with multiple content sections and visual elements) |
| Citation requirement | No citations needed | Reference list at end | Per-recommendation citations throughout the document |

## 7. Boundary Cases & Adjacent Patterns

**C1 (Standard Operating Procedure):** C1 covers operational procedures (how to run a process, receive a shipment, handle a return). C3 covers clinical content (how to treat a condition, what to prescribe, how to document a patient encounter). An SOP for telehealth intake workflow is C1; prescribing guidelines for a telehealth practice are C3. Nursing care plans and SOAP notes are always C3 (clinical documentation requiring clinical expertise), not C1 (operational procedure documents).

**C2 (Compliance Checklist):** A pharmacy compliance checklist derived from a state Board of Pharmacy lawbook is C2 (it evaluates whether the pharmacy meets regulatory requirements). A pharmacy days' supply reference guide that teaches technicians to calculate billing correctly is C3 (it conveys clinical/technical knowledge, not audit criteria). The distinguishing question: is the document an audit instrument (C2) or a clinical reference/guideline (C3)?

**C4 (Training Materials):** Clinical lecture slides and educational posters straddle C3/C4. When the primary deliverable is a clinical reference document (even if it will be used to educate), classify as C3. When the deliverable is a full instructional package with pedagogical scaffolding (pre-test questions, case studies for role-play, speaker notes, exercises, quizzes), classify as C4. A hypertension lecture for nursing students that includes a pre-test, case study, and speaker notes is C4. An SBAR template or clinical education poster is C3.

**D3 (Investment/Financial Advisory Reports):** No overlap. C3 is specifically clinical/pharmacological domain knowledge. D3 covers financial advisory documents. The only confusion risk is if a "formulary" is misread as financial — it is not; clinical formularies are drug lists, not financial instruments.

**B5 (Data Entry with Protocol-Driven Decision Making):** When a nurse fills out a tracking spreadsheet using patient lab values and applies protocol-defined medication decision rules, that is B5. When a nurse practitioner creates the protocol or guideline document that specifies those rules, that is C3. The distinction is authoring the standard (C3) vs. applying it to specific data (B5).
