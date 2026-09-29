# Academic Medical Education Tasks

**Macro Category:** G — Form-Based & Clinical Documentation
**Pattern ID:** G5

## 1. Pattern Description

The worker is a healthcare professional with an academic or teaching role — a medical secretary managing graduate medical education logistics, or a nurse practitioner preparing educational content for nursing students — who must produce materials for a structured medical education program. The cognitive core is multi-constraint academic production: scheduling educational sessions under competing calendar constraints while sourcing appropriate literature, or building a clinically rigorous educational presentation with specific structural pedagogy requirements (pre-test questions, case studies, speaker notes). What distinguishes this pattern from general educational content creation (C4) is the medical education context — literature must meet recency and accessibility standards for GME programs, scheduling must integrate room availability with physician blackout dates, slide content must meet clinical accuracy standards aligned with professional society guidelines (AHA, ACLS, etc.), and the audience is clinical trainees (residents, nursing students) rather than general staff.

## 2. O*NET Grounding

### Occupation Families
- 43-6013 — Medical Secretaries and Administrative Assistants — Manage journal club scheduling, literature sourcing, and academic program logistics for GME departments
- 29-1171 — Nurse Practitioners — Create clinical educational presentations for nursing students; often serve dual clinical-teaching roles in academic medical settings
- 25-1072 — Nursing Instructors and Teachers, Postsecondary — Develop clinical lecture materials, case studies, and assessments for nursing education programs
- 25-1071 — Health Specialties Teachers, Postsecondary — Design medical education curriculum materials across clinical specialties
- 11-9111 — Medical and Health Services Managers — Oversee GME program administration, including scheduling and educational resource coordination

### Key Work Activities (O*NET vocabulary)
- Scheduling Work and Activities
- Documenting/Recording Information
- Searching for Information
- Training and Teaching Others
- Communicating Information and Ideas
- Updating and Using Relevant Knowledge

### Knowledge Domains (O*NET vocabulary)
- Medicine and Dentistry
- Education and Training
- English Language
- Clerical (for scheduling and logistics tasks)
- Biology (for clinical content)

### Generalizable Work Context
This task type arises in academic medical centers, hospital GME programs, nursing schools, and clinical education departments. The trigger is either a program-level scheduling need (setting up a recurring journal club series for a quarter or year) or a content development need (creating a lecture or training module on a specific clinical topic). The audience is clinical trainees — medical residents, nursing students, or continuing education participants. The outputs are used in live educational settings (journal club sessions, classroom lectures) and must meet both operational requirements (room bookings, article accessibility) and pedagogical requirements (pre-tests, case studies, speaker notes).

## 3. Prompt Construction Template

### Persona Pattern
Assign either an administrative role with academic medical program responsibilities (medical secretary for a hospital department's GME program) or a clinical practitioner with a teaching role (nurse practitioner preparing a student lecture). Specify the academic program context ([DEPARTMENT] residency journal club, undergraduate nursing course on [TOPIC], GME program for [SPECIALTY] residents). The seniority level implies independent responsibility for program logistics or content quality.

### Scenario Pattern
**For scheduling variants:** The worker is responsible for a recurring educational program (journal club, grand rounds, case conference) and must select dates for an upcoming series, avoiding institutional blackout dates and satisfying room availability constraints. The scenario provides access to a room booking system (reference file) and a blackout dates document (reference file). The scenario specifies the number of sessions, the time period, the required spacing between sessions, and a weekday preference hierarchy.

**For content creation variants:** The worker must create an educational presentation or lecture on a specific clinical topic for a defined learner audience. The scenario specifies the audience (nursing students, medical residents, continuing education participants), the clinical topic (a chronic condition, an acute condition, a pediatric-specific condition), any professional society guidelines that must be referenced (AHA, ACLS, IDSA), and specific structural pedagogical requirements (pre-test question, case study, speaker notes, references slide).

### Instruction Pattern
**Scheduling variant:** Multi-part instruction: (1) select dates from room availability file, avoiding blackout dates, applying weekday hierarchy and minimum spacing rule; (2) source literature for each session on assigned topics, applying recency and accessibility criteria; (3) produce multiple deliverables — updated scheduling file, article PDFs with naming convention, draft email to supervisor. Each constraint is explicitly enumerated.

**Content creation variant:** Single deliverable with detailed structural requirements listed as a bulleted or numbered list of required sections, pedagogical elements, and slide count ceiling. Speaker notes and illustration requirements are explicit. Clinical accuracy to named professional society guidelines is specified.

### Constraint Injection Points
- **Scheduling constraints:** Weekday preference hierarchy (ordered from most to least preferred); minimum inter-session gap (e.g., a minimum number of weeks between sessions); must not conflict with blackout dates from provided document; must use available rooms from booking file
- **Literature sourcing constraints:** Publication recency (within last 5–10 years); accessibility (no paywall, no login required, fully free to access); discipline match (articles must be on the assigned topic, not adjacent topics); file naming convention (month must appear in PDF file names)
- **Structural pedagogical constraints:** Pre-test question must appear first (before content slides); clinical case study must appear with specified patient characteristics; speaker notes required on specified slides; references slide formatted in a specified citation style; slide count ceiling
- **Clinical accuracy constraints:** Staging or classification criteria must follow named professional society guidelines (e.g., AHA, ACLS, IDSA); illustrations of clinical concepts (e.g., a diagnostic technique, a medication's mechanism of action) must be included; clinical case study must include realistic risk factors
- **Communication constraints:** Draft email to supervising physician must be addressed correctly, must attach all produced files, and must summarize the scheduled sessions

### Structural Template

```
[PERSONA]: You are a [ROLE] for the [DEPARTMENT_NAME] at [INSTITUTION_TYPE].

[SCENARIO]: You are responsible for [managing the annual journal club / developing educational content] for [PROGRAM_DESCRIPTION]. [OPERATIONAL_CONTEXT].

[REFERENCE_MATERIALS if scheduling variant]:
- [FILE_1]: Room availability calendar (xlsx) — contains room booking availability for [TIME_PERIOD]
- [FILE_2]: Holiday/conference/blackout dates document (docx) — lists dates when [AUDIENCE] are unavailable

[TASK — SCHEDULING VARIANT]:
1. Schedule [NUMBER] [PROGRAM_TYPE] sessions for [MONTHS/PERIOD]:
   - Use only available dates from the room booking file
   - Avoid all blackout dates listed in [FILE_2]
   - Apply weekday preference hierarchy: [DAY_1] > [DAY_2] > [DAY_3] > [DAY_4] > [DAY_5]
   - Sessions must be at least [N] weeks apart

2. For each session, source [N] peer-reviewed articles on the topic: [TOPIC_1 (Session 1)], [TOPIC_2 (Session 2)], [TOPIC_3 (Session 3)]
   - Articles must be published within the last [N] years
   - Articles must be fully accessible without paywall or login
   - Save each article as a PDF with the month in the file name

3. Update the room booking file to reflect the scheduled sessions; save as "[SCHEDULE_FILENAME]"

4. Draft an email to [SUPERVISOR_NAME] attaching the schedule and all [N × NUMBER_OF_SESSIONS] article PDFs

[TASK — CONTENT CREATION VARIANT]:
Create a [FORMAT: PowerPoint presentation / PDF lecture / Word study guide] on [CLINICAL_TOPIC] for [AUDIENCE: nursing students / medical residents / CME participants].

Required content areas:
- [CONTENT_AREA_1]
- [CONTENT_AREA_2]
- [CONTENT_AREA_3]
[... enumerate all required clinical topics]

Structural requirements:
- [PRE-TEST_REQUIREMENT: include one pre-test multiple-choice question on [SLIDE_NUMBER]/first slide]
- [CASE_STUDY_REQUIREMENT: include one clinical case study involving a patient with [RISK_FACTORS]]
- [ILLUSTRATION_REQUIREMENT: include a visual illustration of [CLINICAL_CONCEPT]]
- Speaker notes where necessary throughout
- References slide as the final slide, properly formatted
- Maximum [N] slides

[CLINICAL_ACCURACY_REQUIREMENT]: Must align with [AHA / ACLS / IDSA / other named guidelines]

[OUTPUT_SPECIFICATION]: [FORMAT], [NAMING], [DELIVERABLES_LIST]
```

## 4. Reference File Requirements

### File Types Needed
- **Room availability calendar (xlsx) — for scheduling variants:** A spreadsheet showing a booking calendar for a shared room or conference room across a time period (quarter, semester, year). Availability is indicated by open vs. booked status for each date/time slot. May be organized by month-column or date-row structure with status flags.
- **Blackout dates document (docx) — for scheduling variants:** A list of dates when the target audience is unavailable due to institutional events (holidays, conferences, academic events, grand rounds, training days). Structured as a simple list or table with date and event name.
- **No reference files required for content creation variants:** Clinical content is generated from the practitioner's domain knowledge and professional society guidelines (accessed via web or implicit in the knowledge base). The prompt provides the clinical topic and structural requirements; all content is produced from expertise.

### Data Characteristics
Room availability data for this pattern is calendar-structured:
- Date dimension: spanning 3–12 months of the academic or fiscal year
- Room dimension: one or more named rooms with independent availability status
- Status values: binary (available/booked) or more granular (available, booked, maintenance, etc.)
- Time dimension (optional): may specify time-of-day availability if scheduling includes start time requirements

Blackout dates data is list-structured:
- Date: specific date or date range
- Event type: holiday, conference, clinical training day, institutional event
- Applicability: which audience group is affected (all physicians, residents only, etc.)

Literature requirements for sourced articles:
- Recency: published within a specified lookback window (5 years, 10 years) from the task date
- Accessibility: freely accessible without institutional login, paywall, or subscription
- Topic alignment: clearly relevant to the specified topic (not adjacent or tangentially related)
- Source quality: peer-reviewed journal publication (not news articles, blog posts, or non-reviewed content)

### File Complexity Spectrum
- **Minimal:** Single scheduling session — one available date to find from a simple room calendar with five blackout dates; source two articles on one topic; no email draft required; presentation with 10 slides and minimal structural requirements
- **Moderate:** Three scheduling sessions across one quarter with weekday preference hierarchy and minimum spacing; source six articles across two topics with accessibility screening; update room booking file and draft email; presentation with 15 slides covering six clinical content areas with speaker notes
- **Complex:** Multiple scheduling sessions spanning several months with competing room availability constraints, a full academic calendar of blackout dates, and a weekday preference hierarchy ranking every weekday; source articles across three or more distinct medical topics (all must be paywall-free, recency-checked, and topic-verified); produce several deliverables (updated Excel, one article PDF per required article with naming convention, draft email attaching every file); separately, a long-form presentation (20+ slides) with pre-test, illustration, case study, speaker notes throughout, and staging or classification content that complies with a named professional society's guidelines — across different specialties

## 5. Output Specification

### Primary Deliverable
- **Format:** Excel (schedule file) + PDF (article files) + draft email text — for scheduling tasks; PowerPoint (.pptx) — for content creation tasks
- **Structure:**
  - Scheduling output: Updated room booking Excel file with new bookings entered for the scheduled sessions; individual article PDF files for every required article, following a standardized naming convention (month in file name); draft email text addressed to named supervisor, summarizing scheduled dates and listing all attachments
  - Content creation output: PowerPoint presentation with: Slide 1 (pre-test multiple-choice question), clinical content slides covering all specified areas in logical order, clinical case study slide with specified patient characteristics, the required clinical illustration, speaker notes on applicable slides, final references slide with citations
- **Key quality signals:** All scheduled dates pass all constraint checks (available in room file, not on blackout list, correct weekday preference, minimum spacing satisfied); all articles are genuinely accessible without paywall; article PDFs have month in file name; email draft lists every attachment correctly. For presentation: pre-test question appears before content slides; case study patient has specified risk factors; staging or classification criteria are used with the correct values from the cited guideline; speaker notes are substantive (not just repeated slide text)

### Secondary Deliverables (if any)
- For scheduling tasks: the draft email itself functions as a secondary coordination deliverable, transmitting the schedule and all article PDFs to the supervising physician in a professional tone
- In some variants: a summary handout or study guide may accompany the lecture presentation

### Gold Output Characteristics
A gold scheduling output selects dates that satisfy all constraints simultaneously — not just most of them. If the third preferred weekday is not available without violating spacing or blackout constraints, the gold output correctly falls back to the fourth preferred weekday rather than violating the spacing constraint. All sourced articles are genuinely peer-reviewed and accessible (no ResearchGate previews that require login, no articles behind institutional subscriptions). The email draft is addressed to the correct person, uses a professional tone appropriate for clinical academic communication, and lists every attachment by file name.

A gold presentation produces a pre-test question that is relevant and moderately challenging for the audience level — it tests knowledge that will be taught in the presentation. The case study patient reflects the specified risk factors and the clinical decisions in the case study are consistent with the content covered in the presentation. Condition staging or classification criteria are presented with the exact values from the cited professional guideline, not approximated. Speaker notes provide substantive additional information or teaching points rather than restating the slide text verbatim.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Scheduling constraint density | 5 blackout dates, simple room availability, no weekday preference | 10–15 blackout dates, two rooms with different availability, 3-level weekday preference | Full academic calendar of blackout dates, limited room availability, a full weekday preference hierarchy ranking every weekday, a minimum weeks-between-sessions spacing rule |
| Number of sessions to schedule | 1 session | 2 sessions | 3+ sessions across different months |
| Literature sourcing scope | 2 articles on 1 topic | 6 articles across 2 topics | Articles across three or more distinct clinical topics, several per topic, with full accessibility verification |
| Multi-deliverable complexity | 2 deliverables (schedule + email) | 3 deliverables (schedule + PDFs + email) | 4+ deliverables (updated Excel + one PDF per required article + draft email listing every attached file) |
| Presentation clinical depth | 10 slides, 4 content areas, no professional society guideline alignment required | 15 slides, 6 content areas, one guideline reference required | 20+ slides, many content areas, full named-guideline alignment, pre-test + illustration + case study + speaker notes |
| Audience clinical sophistication | Layperson-facing health education | Nursing students (clinical but pre-clinical) | Medical residents or post-graduate clinicians (full clinical sophistication expected) |

## 7. Boundary Cases & Adjacent Patterns

**Most similar patterns:**
- **C4 (Training Materials & Educational Presentations):** C4 produces training documents and educational presentations for general staff audiences across many industries. G5 is specifically medical education for clinical trainees, with the added requirements of professional society guideline alignment, medical literature sourcing with accessibility constraints, and GME scheduling against clinical calendar constraints. If the audience is clinical trainees and the content requires medical professional society guideline accuracy, it is G5; if the audience is general staff and the content is a workplace skill or process, it is C4.
- **G1 (Clinical Documentation — SOAP Notes, Care Plans):** G1 produces patient-specific clinical documentation; G5 produces educational materials about clinical topics. If the deliverable teaches clinicians about a condition or procedure, it is G5; if it documents a specific patient encounter, it is G1.
- **E1 (Literature Review & Evidence Synthesis):** E1 produces comprehensive academic literature reviews with search methodology and synthesis. G5 includes literature sourcing as a supporting activity for scheduling (selecting articles for journal club sessions) rather than producing a standalone evidence synthesis. If the deliverable IS the literature review, it is E1; if literature is sourced to support a scheduling or educational deliverable, it is G5.
- **G3 (Healthcare Administrative Forms & Correspondence):** G3 produces administrative workflow tools (tracking spreadsheets, fax forms); G5 produces academic program deliverables (lecture materials, journal club schedules). Both involve healthcare administrative workers, but G3 outputs are operational tools for daily workflow; G5 outputs are educational program materials for academic events.
