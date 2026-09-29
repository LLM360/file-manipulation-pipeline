# Peer Feedback & Coaching Documents

**Macro Category:** F — Client Communication & Outreach Materials
**Pattern ID:** F5

## 1. Pattern Description

The worker reviews one or more colleague-produced work artifacts (chat transcripts, investigation reports, field notes) and produces a structured feedback or revision document that identifies specific problems, explains why each is problematic, and provides an improved version or corrected output. The cognitive core is applying professional domain standards — customer service etiquette, investigative report conventions, clinical documentation rules — to evaluate a peer's work product, then synthesizing findings into a coaching document that is both corrective and constructive. This pattern is distinct from performance analysis presentations (B1) because it addresses individual peer output rather than aggregate operational data; and distinct from training materials (C4) because it produces feedback on an existing artifact rather than a general instructional document. The output serves a supervisory or coaching relationship within the same professional domain.

## 2. O*NET Grounding

### Occupation Families
- 43-4051 Customer Service Representatives / 13-1151 Training and Development Specialists — senior CSRs reviewing junior colleague chat transcripts and producing coaching feedback documents
- 33-9021 Private Detectives and Investigators — PI supervisors reviewing and finalizing field investigator reports, correcting structure, verifying timeline accuracy, and aligning with photographic evidence
- 11-9199 Managers, Not Elsewhere Classified — supervisory roles reviewing subordinate work products across various professional domains
- 29-0000 Healthcare Practitioners (various) — clinical supervisors reviewing documentation for accuracy and compliance

### Key Work Activities (O*NET vocabulary)
- Coaching and Developing Others
- Evaluating Information to Determine Compliance with Standards
- Communicating with Supervisors, Peers, or Subordinates
- Training and Teaching Others
- Judging the Qualities of Objects, Services, or People
- Reviewing, Inspecting, or Examining Documents
- Making Decisions and Solving Problems
- Writing Reports or Other Documents

### Knowledge Domains (O*NET vocabulary)
- Customer and Personal Service (chat etiquette, empathy, tone)
- English Language (grammar, sentence structure, punctuation)
- Communications and Media (communication channel conventions)
- Law, Government, and Jurisprudence (investigation documentation standards)
- Public Safety and Security (PI report conventions, evidence alignment)
- Psychology (coaching tone, constructive feedback framing)

### Generalizable Work Context
A senior or supervisory professional receives one or more work artifacts from a junior colleague or field agent and is tasked with providing structured feedback or producing a finalized, corrected version of the artifact. The trigger is a quality control checkpoint, a training initiative, or a required review step before client delivery. The feedback document is delivered internally to the peer or their manager. The worker must balance correctness (identifying real problems against a professional standard) with coaching tone (constructive, not punitive). Reference to external standards (etiquette guides, report conventions, photographic evidence) is frequently required.

## 3. Prompt Construction Template

### Persona Pattern
Assign a senior professional in a supervisory or coaching capacity: Senior Customer Service Representative, PI Supervisor, Clinical Supervisor, Senior Investigator. Include the organization type (bank contact center, PI firm, healthcare system). The persona's seniority signals authority to evaluate the peer's work and the obligation to provide constructive guidance rather than just criticism.

### Scenario Pattern
The trigger is receipt of a peer's work artifact that, despite following technical policy, produced a poor outcome (poor CSAT scores, format violations, timeline inconsistencies, photographic misalignment). Introduce: (1) the peer's role and the artifact they produced (chat logs, draft report, field notes), (2) the quality problem that triggered the review, (3) the specific professional standards the feedback should be grounded in (etiquette guide URL, report conventions, photographic evidence). The scenario frames the task as a coaching opportunity rather than a disciplinary one.

### Instruction Pattern
Instructions specify the per-item structure of the feedback document: (1) identify the problematic statement or section, (2) explain why it is problematic (1-3 sentences), (3) provide an improved alternative. This three-part structure repeats for each problem found. Instructions also specify the document formatting rules (title, bold headers, line spacing, page limit) and the number of source artifacts to review. For report revision tasks, instructions may combine the feedback function with a finalization function (produce the corrected report as the deliverable, not just a list of problems).

### Constraint Injection Points
- **Artifact type:** chat transcript (text-based, tone/empathy focused) vs. investigation report (structure, timeline, photo alignment) vs. clinical note (protocol compliance, completeness) — drives different evaluation criteria
- **Number of source artifacts:** a single report vs. multiple chat cases — drives document length and section count
- **Feedback vs. revision:** produce a coaching document listing problems and improvements vs. produce the corrected artifact itself as the deliverable — significantly different task structures
- **External standards reference:** URL to etiquette guide vs. photographic archive vs. style guide — the external reference source drives what standards are applied
- **Per-item structure requirements:** fixed 3-part structure (identify + explain + rewrite) vs. more open-ended revision
- **Formatting constraints:** document title, bold section headers, line spacing (1.5), page limit — can be varied independently
- **Domain standards complexity:** basic chat etiquette (accessible) vs. PI surveillance report conventions (specialized) vs. clinical documentation (highly technical)

### Structural Template

```
[PERSONA]: You are a [SENIOR_ROLE] at [ORG_TYPE]. [BRIEF_CONTEXT: your team handles X / you supervise field investigators / you are responsible for quality review].

[SCENARIO]: Your colleague [JUNIOR_ROLE_DESCRIPTION] recently [WORK_ARTIFACT_DESCRIPTION: completed several live chat interactions / submitted a field surveillance report]. Despite [TECHNICAL_COMPLIANCE: following policy / completing the surveillance], [QUALITY_PROBLEM: received poor CSAT scores / the report contains structural issues and timeline gaps].

[REFERENCE_FILES]:
- [FILE_1]: [artifact type and description — e.g., first case docx (live chat transcript, banking customer service)]
- [FILE_2]: [artifact type and description — e.g., second case docx]
- [FILE_3]: [artifact type and description — e.g., third case docx]
[OR for report revision:]
- [FILE_1]: [draft report docx — field investigator's surveillance report with timeline observations]
- [FILE_2]: [photographic archive — zip file with surveillance photographs for cross-referencing]

[EXTERNAL_STANDARDS] (if applicable): Consult [REFERENCE_GUIDE_URL / professional standards document] for best practices to ground your feedback.

[TASK]: Review [the case transcripts / the draft report] and produce a [DELIVERABLE_TYPE]:

Option A — Coaching feedback document:
Create a Word document titled "[DOCUMENT_TITLE]" with:
- Bold section headers for each case: "[CASE_1_HEADER]," "[CASE_2_HEADER]," etc.
- For each problematic statement found in each case:
  1. Identify the problematic statement (quote or describe it)
  2. Explain why it is problematic (1-3 sentences)
  3. Provide an improved alternative statement

Option B — Revised/finalized report:
Produce a corrected [PDF / Word] document structured into [N imposed sections, e.g., an overview, a chronological narrative, and a concluding assessment]:
- Correct grammar, punctuation, and sentence structure
- Verify timeline accuracy [cross-referencing photographic evidence]
- Remove unnecessary information; preserve all relevant timestamped observations
- Align all written claims with photographic evidence

[FORMAT_CONSTRAINTS]:
- Document title: "[TITLE]"
- Section headers: bold
- Line spacing: [1.5 / standard]
- Maximum length: [N pages]
- Output format: [Word / PDF]
```

## 4. Reference File Requirements

### File Types Needed
- **Chat transcript files (docx, 1-3 files):** Text-based records of live customer service interactions. Each file contains: agent greeting, customer query, agent responses, resolution or close. Structured as a dialogue with labeled speakers. 10-30 exchanges per transcript is typical. The transcripts should contain identifiable problems (tone gaps, empathy failures, jargon, premature closure) while also containing correct elements that should not be flagged.
- **Draft investigation report (docx):** A field investigator's prose narrative of surveillance activities with timestamped observations. Should contain deliberate grammar/punctuation issues, minor timeline inconsistencies, extraneous detail, and a lack of clear section structure. 2-4 pages in draft form.
- **Photographic archive (zip):** A set of surveillance photographs with filenames or embedded timestamps. Used for cross-referencing against the written report narrative. The photographs may reveal minor discrepancies with the draft report (e.g., subject's clothing description inconsistent, timestamp gap not accounted for).
- **External etiquette guide or standards document (web URL):** Referenced but not downloaded — the agent retrieves relevant standards during task execution (e.g., live chat best practices, PI report formatting conventions).

### Data Characteristics
Chat transcripts should be realistic customer service interactions in a specific industry (banking, insurance, retail) with realistic customer personas (elderly, frustrated, confused) and at least 2-3 identifiable coaching opportunities per case. Investigation reports should contain realistic surveillance language (subject observed, timestamp, activity description) with plausible but improvable structure. Photographs in zip archives should be representable as a description (file list with timestamps) since the pipeline works with document data rather than actual images. External URLs should point to publicly accessible professional standards resources.

### File Complexity Spectrum
- **Minimal:** Single chat transcript (1 docx) with 2-3 identifiable problems; produce coaching document with bold headers and per-item 3-part structure; no external reference required; 1-2 pages
- **Moderate:** Multiple chat transcripts (several docx files) each with 2-4 identifiable problems; consult external etiquette guide URL; produce consolidated coaching document with one section per case; 1.5 spacing; max 5 pages
- **Complex:** Draft surveillance report (docx) + photographic archive (zip); produce a finalized and corrected, page-limited PDF report with several imposed sections (e.g., an overview section, a chronological narrative section, and a concluding assessment section); correct grammar/timeline/extraneous content; verify all claims against photographic evidence; hard page limit requiring editorial compression

## 5. Output Specification

### Primary Deliverable
- **Format:** Word document (.docx) or PDF
- **Structure:**
  - Coaching document: one section per source artifact (bold case header), each section containing per-problem subsections with (1) problem identification, (2) explanation, (3) improved alternative
  - Revised report: final polished document with imposed section structure (e.g., an overview section, a chronological narrative section, and a concluding assessment section) — the feedback is implicit in the corrections rather than explicitly listed
- **Key quality signals:** All genuine problems identified (no false negatives); no correct elements unfairly flagged (no false positives); explanation of each problem grounded in professional standards or external reference; improved alternatives are clearly superior and professionally appropriate; formatting constraints (bold headers, line spacing, page limit) exactly met; revised report is internally consistent and timeline-accurate

### Secondary Deliverables (if any)
- None typical for this pattern. The feedback document or revised report is the sole deliverable.

### Gold Output Characteristics
A gold output: (1) identifies all genuine problems in the source artifacts without omission; (2) provides explanations that are specific and grounded (citing the external standard or professional convention being violated, not just asserting the statement was "bad"); (3) provides improved alternatives that are genuinely better — not just rephrased versions of the same mistake; (4) maintains a coaching tone throughout (constructive, not critical or punitive); (5) correctly applies all formatting constraints (document title, bold headers, spacing, page limit); (6) for report revision tasks, produces a polished professional document that is internally consistent, timeline-accurate, and properly cross-referenced with the photographic evidence.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of source artifacts | 1 transcript or report | 2-3 transcripts | 3+ artifacts across different types (report + photo archive) |
| Problem density per artifact | 2 clear, obvious problems | 3-4 problems ranging from obvious to subtle | 4-6 problems including subtle tone issues, implicit timeline gaps, photographic inconsistencies |
| Task type | Pure feedback listing (identify + explain + rewrite) | Feedback + partial revision | Full revision/finalization of artifact (corrected output is the deliverable, not a list of problems) |
| External standards grounding | No external reference required | URL to etiquette guide provided for reference | Multiple standards sources (etiquette guide + professional conventions + photographic evidence) must be integrated |
| Domain complexity | Chat etiquette (broadly accessible) | Investigation report structure (moderately specialized) | Clinical documentation compliance (highly specialized, terminology-sensitive) |
| Formatting constraints | Basic (title + sections) | Moderate (bold headers + line spacing + page limit) | Strict (hard page limit requiring editorial compression of a longer draft + imposed section structure) |
| Coaching tone complexity | Direct and collegial | Professionally balanced (critical but constructive) | Diplomatically sensitive (subject is a long-tenured employee with authority in other contexts) |

## 7. Boundary Cases & Adjacent Patterns

**C4 — Training Materials & Educational Presentations:** Both C4 and F5 have an educational intent, but they differ in what triggers the task and who the audience is. C4 produces general instructional materials for a class of learners (new hires, staff group). F5 produces specific feedback on a specific individual's work product in a coaching relationship. If the deliverable is a training deck, a guide for new hires, or a set of case studies for group use, it is C4. If the deliverable is feedback on a named colleague's specific transcript or report, it is F5.

**B1 — Performance Analysis Presentation:** B1 analyzes aggregate operational data to produce leadership-facing performance presentations (CSAT trends, quality metrics dashboards). F5 analyzes individual work artifacts to produce peer coaching documents. The distinction is: aggregate data analysis → leadership presentation (B1) vs. individual artifact review → peer coaching document (F5).

**G3 — Medical Records Review & Summarization (if in the taxonomy):** Report revision tasks in F5 share structural similarities with any document review/correction pattern. The key differentiator is the coaching relationship: F5 always has a peer-to-peer or supervisor-to-subordinate coaching frame, whereas pure document revision tasks (copy-editing, medical record summarization) lack the corrective feedback and improved-alternative structure that defines F5.
