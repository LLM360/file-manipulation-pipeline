# Clinical Documentation (SOAP Notes, Care Plans)

**Macro Category:** G — Form-Based & Clinical Documentation
**Pattern ID:** G1

## 1. Pattern Description

The worker is a licensed clinical practitioner (nurse practitioner, PACU nurse, or equivalent) who must produce structured clinical documentation — either a SOAP note or a nursing care plan — from a fully specified patient scenario provided in the prompt. The cognitive core is clinical reasoning: synthesizing a patient's presenting history, objective findings, comorbidities, and medication profile into a correctly formatted clinical document. What distinguishes this pattern from adjacent ones is that all clinical data is given inline (no reference files needed) and the output must follow a rigid documentation schema (SOAP format, or a precise diagnosis/outcome/intervention count structure). The challenge is the intersection of clinical domain knowledge, documentation convention mastery, and embedded constraint satisfaction (e.g., allergy-constrained antibiotic selection, pediatric-specific risk stratification, exact nursing diagnosis counts).

## 2. O*NET Grounding

### Occupation Families
- 29-1171 — Nurse Practitioners — Primary producers of SOAP notes in outpatient, urgent care, and specialty settings
- 29-1141 — Registered Nurses — Produce nursing care plans in inpatient, post-surgical, and PACU settings
- 29-1171.01 — Acute Care Nurse Practitioners — Document SOAP notes for complex, multi-comorbidity presentations
- 29-1141.02 — Pediatric Nurses — Author pediatric-specific care plans with age-appropriate diagnoses and interventions

### Key Work Activities (O*NET vocabulary)
- Documenting/Recording Information
- Diagnosing Medical Conditions
- Providing Medical Care or Treatment
- Evaluating Patient Condition
- Developing Treatment Plans
- Assessing Patient Risk Factors

### Knowledge Domains (O*NET vocabulary)
- Medicine and Dentistry
- Biology
- Psychology
- Customer and Personal Service
- English Language

### Generalizable Work Context
This task type arises in any clinical setting (outpatient primary care, specialty clinic, hospital inpatient, post-anesthesia care) where practitioners must document patient encounters or develop care continuity plans. The trigger is a completed patient encounter or clinical handoff scenario. The audience is other clinical staff (care team, consulting specialists) or regulatory/quality reviewers. Organizations that generate this task type include physician practices, hospital departments, ambulatory clinics, and academic medical centers.

## 3. Prompt Construction Template

### Persona Pattern
Assign a licensed clinical practitioner role with specialty context: pediatric NP, outpatient NP, PACU RN, emergency NP, etc. Specify the practice setting (primary care clinic, pediatric hospital, outpatient specialty clinic). Seniority is intermediate to senior — the practitioner should be independently competent to document without supervision. Include the date of the encounter.

### Scenario Pattern
Provide a complete patient encounter scenario as narrative prose: HPI, PMH, family history, social history, current medications, known allergies, vital signs, and physical exam findings (including any diagnostic results like imaging or labs). The scenario should embed clinical complexity signals — subtle abnormal findings, allergy constraints, pediatric-specific considerations, psychosocial complicating factors, or multi-system involvement. The scenario is fully self-contained in the prompt; no reference files are attached.

### Instruction Pattern
Single deliverable instruction: "Create a [SOAP note / nursing care plan] for this patient." For care plans, specify the exact structural counts (e.g., a fixed number of nursing diagnoses, each with a set number of outcomes, assessments, and interventions). For SOAP notes, the format is implied by the SOAP convention but may include a reminder to use standard SOAP sections. Include output format (PDF or Word) and any page/length constraints.

### Constraint Injection Points
- **Clinical constraints:** allergy restrictions (drug class X contraindicated — must select alternative), pediatric age-specific requirements (age-appropriate dosing, return-to-sport protocols, FACES pain scale), comorbidity interactions (existing medications + new treatment plan), vital sign abnormalities that must be addressed in the plan
- **Structural constraints:** exact nursing diagnosis count, exact intervention/assessment count per diagnosis, one-page limit for care plans, all provided clinical data must be incorporated into the SOAP note
- **Diagnostic constraints:** embedded subtle findings (e.g., a symptom with a benign-seeming explanation that could also signal a more serious concern, an abnormal oxygen saturation reading that must be addressed in the plan, a subtle gait or coordination deficit on exam)
- **Documentation convention constraints:** standard SOAP sections (S/O/A/P), NANDA-compliant nursing diagnoses, proper formatting of differentials in Assessment section

### Structural Template

```
[PERSONA]: You are a [SPECIALTY] Nurse Practitioner / Registered Nurse at [SETTING_TYPE]. Today's date is [DATE].

[PATIENT_SCENARIO]:
Patient: [AGE]-year-old [SEX] presenting with [CHIEF_COMPLAINT].

HPI: [DETAILED_HPI_NARRATIVE including onset, duration, character, aggravating/relieving factors, associated symptoms, mechanism if applicable]

PMH: [PAST_MEDICAL_HISTORY]
Family History: [FAMILY_HISTORY]
Social History: [SOCIAL_HISTORY]
Allergies: [ALLERGY_1] ([REACTION_TYPE]), [ALLERGY_2] ([REACTION_TYPE])
Current Medications: [MED_LIST]

Vital Signs: T [TEMP], BP [BP], HR [HR], RR [RR], O2 Sat [SAT]
Physical Exam: [SYSTEM_EXAM_FINDINGS with normal and abnormal results mixed]
[DIAGNOSTIC_RESULTS if applicable, e.g., CXR, labs]

[TASK]: Create a [SOAP note / nursing care plan] for this patient.

[CONSTRAINTS]:
- Use standard [SOAP / care plan] format
- [STRUCTURAL_CONSTRAINT: e.g., Include an exact number of nursing diagnoses, each with a set number of outcomes, assessments, and interventions]
- [PAGE_CONSTRAINT: e.g., Fit on one page]
- All provided clinical data must be incorporated accurately
- [ALLERGY/DRUG_CONSTRAINT if applicable]

[OUTPUT_SPECIFICATION]: [PDF / Word document], [page limit]
```

## 4. Reference File Requirements

### File Types Needed
- None — all patient data is provided inline in the prompt text. The clinical scenario IS the reference material.

### Data Characteristics
The clinical scenario functions as structured data delivered as narrative prose. It must include:
- Demographics: age, sex, date of encounter
- Chief complaint and HPI: mechanism, timeline, symptom characterization, severity rating (0-10 or FACES scale for pediatric)
- Medical/surgical history: prior diagnoses, prior procedures relevant to current presentation
- Family history: relevant heritable conditions
- Social history: occupation, habits, living situation, relevant risk exposures
- Allergy list: drug name + reaction type (allergy vs. intolerance)
- Current medications: name, dose, frequency, indication
- Vital signs: complete set (T, BP, HR, RR, O2 sat, pain score, weight/height for pediatric)
- Physical exam: system-by-system with mix of normal and abnormal findings; embedded subtle findings that require clinical judgment
- Diagnostic results (optional): imaging findings (CXR consolidation, head CT), lab values, or clinical tool scores

### File Complexity Spectrum
- **Minimal:** Single chief complaint, no allergies, single comorbidity, normal vitals except presenting symptom, straightforward diagnosis (e.g., uncomplicated URI with clear diagnosis implied)
- **Moderate:** Two to three comorbidities, one drug allergy that restricts standard treatment choice, one abnormal vital sign requiring plan address, two differential diagnoses in Assessment, one subtle embedded finding
- **Complex:** Multiple significant drug allergies that jointly restrict the standard first-line treatment options, three-plus comorbidities with medication interactions, pediatric patient with age-specific protocol requirements, subtle embedded findings that create safety concerns (e.g., a risk-bearing activity continued despite a possible undiagnosed injury), multi-system abnormalities, an abnormal oxygen saturation requiring a treatment decision, need for specialist referral alongside primary treatment plan

## 5. Output Specification

### Primary Deliverable
- **Format:** PDF or Word document (SOAP note); PDF (care plan)
- **Structure:**
  - SOAP note: Four clearly labeled sections — Subjective (CC, HPI, PMH, SH, FH, medications, allergies), Objective (vitals, PE, diagnostic results), Assessment (working diagnosis with differential), Plan (treatment, follow-up, patient education, referrals)
  - Care plan: Tabular structure with header (patient ID, date, setting), then three nursing diagnosis blocks each containing: diagnosis statement, measurable outcome, four assessments, four interventions
- **Key quality signals:** All provided clinical data accurately placed in correct SOAP section; drug allergies respected in treatment plan; clinical reasoning explicit in Assessment/Plan; care plan diagnoses are NANDA-appropriate; interventions are specific and measurable; abnormal vitals addressed in plan

### Secondary Deliverables (if any)
None in most cases, though this pattern can pair with a medical necessity appeal letter as a secondary deliverable when the encounter also motivates an insurance request (see G4).

### Gold Output Characteristics
A gold SOAP note will correctly organize every piece of provided clinical data into the appropriate section (no HPI details buried in Objective, no exam findings in Subjective). The Assessment will name a primary diagnosis with ICD-10 code, list differentials with brief justification for why each was considered/excluded, and incorporate subtle embedded findings. The Plan will reflect allergy-conscious drug selection (no PCN for PCN-allergic patients), age-appropriate protocols, and address every abnormal finding in the Objective. A gold care plan will use valid NANDA nursing diagnosis language, produce outcomes that are measurable (SMART format), and generate assessments and interventions that are clinically specific to the patient's scenario rather than generic.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Allergy constraints | No allergies | One allergy to common first-line drug | Two or more significant drug allergies restricting standard treatment; potential interaction with existing medications |
| Patient age/population | Adult, typical presentation | Pediatric patient (age-appropriate dosing, FACES pain scale) | Neonate or elderly patient with unique pharmacokinetics, fall risk, cognitive considerations |
| Clinical complexity | Single diagnosis, straightforward plan | Two to three comorbidities, one abnormal vital requiring plan response | Multi-system involvement, embedded safety concern (driving/return-to-sport risk stratification), specialist referral decision required |
| Embedded subtle findings | All findings clearly abnormal or normal | One subtle finding present | Two or more subtle findings (e.g., a symptom with a benign explanation that could also signal a more serious condition; a subtle coordination or gait deficit) |
| Structural constraint | Standard SOAP format, no count constraints | Care plan with a fixed number of diagnoses and general structure | Care plan with exact counts (e.g., a fixed number of diagnoses, each with a fixed number of outcomes, assessments, and interventions), one-page constraint |
| Documentation format | SOAP note | Nursing care plan | Both SOAP note and discharge summary required |

## 7. Boundary Cases & Adjacent Patterns

**Most similar patterns:**
- **G4 (Medical Necessity & Insurance Documentation):** The two patterns can overlap when a task requires a SOAP-like clinical summary as the basis for an insurance appeal letter. The distinction: G1 produces the clinical note itself; G4 uses clinical documentation as input to produce an insurance-facing document. Choose G1 when the deliverable IS the clinical note; choose G4 when the deliverable is an insurance or administrative document that references clinical data.
- **G2 (Case Reports & Assessment Reports):** Both involve structured document completion from provided information. G1 is healthcare-specific with standardized clinical formats (SOAP, NANDA); G2 is broader (social work, legal, tax) and produces free-form or agency-specific reports rather than medically standardized formats.
- **C3 (Clinical Guidelines & Reference Guides):** C3 produces population-level clinical guidelines for practitioner reference; G1 produces patient-specific clinical documentation. If the deliverable describes what to do for a patient type, it is C3; if it documents what was done (or planned) for a specific patient encounter, it is G1.
- **G5 (Academic Medical Education):** G5 produces educational materials about clinical topics (lectures, journal schedules); G1 produces active clinical documentation. If the output is meant to teach clinicians, it is G5; if it is meant to document or plan care, it is G1.
