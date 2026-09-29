# Surveillance & Investigation Report Writing

**Macro Category:** I — Investigation & Security Reports
**Pattern ID:** I1

## 1. Pattern Description

The worker occupies a supervisory or senior investigator role and must transform raw field materials — draft reports, timestamped notes, time logs, and photographic evidence — into a polished, client-facing investigation report. The core cognitive work is multi-source synthesis: pulling observations from two or more input documents, reconstructing a coherent chronological timeline, integrating photographic evidence, and layering a professional assessment with actionable recommendations. This pattern is distinct from generic document editing because it requires domain-specific judgment about what constitutes a significant observation versus peripheral noise, how to handle anonymization, and how to maintain an evidentiary chain suitable for legal or insurance use. The output must be structurally uniform (Summary, Surveillance, Assessment sections), page-constrained, formatted as PDF, and in some variants printed on official company letterhead.

## 2. O*NET Grounding

### Occupation Families
- **33-9021 Private Detectives and Investigators** — primary occupation family; supervisors and senior investigators write these reports as a core duty
- **33-1099 First-Line Supervisors of Protective Service Workers** — supervisory PIs who review field investigators' work and sign off on deliverables
- **13-1031 Claims Adjusters, Examiners, and Investigators** — insurance-side investigators who commission these reports; understanding their standards informs report quality

### Key Work Activities (O*NET vocabulary)
- Writing reports or other production outputs documenting observations and findings
- Reviewing documents or data for accuracy and completeness
- Evaluating information to determine compliance with standards
- Organizing, planning, and prioritizing work
- Analyzing data or information to identify relationships or draw conclusions
- Documenting/recording information for use as formal evidence

### Knowledge Domains (O*NET vocabulary)
- Law and Government — investigative legal standards, chain-of-custody requirements, anonymization obligations
- Public Safety and Security — surveillance tradecraft, observation methodology, evidence documentation
- English Language — professional report writing, grammar and syntax at a legal-document standard
- Clerical — structured document formatting, filing conventions, PDF production

### Generalizable Work Context
A private investigation firm or loss prevention department receives completed field work from one or more investigators and assigns a supervisor or senior investigator to consolidate materials into a deliverable for an external client (insurer, retailer, corporate HR, law firm). The trigger is the conclusion of a surveillance engagement and the need to deliver a formal report that could be used in litigation, insurance decisions, or HR actions. The work is time-sensitive and quality-gated — the supervisor's signature on the report implies professional accountability.

## 3. Prompt Construction Template

### Persona Pattern
Assign the worker as a supervisor or senior investigator at an established private investigation firm. The seniority level matters — senior investigators are expected to exercise judgment, not merely transcribe. Specify the investigative specialty (domestic, corporate/retail, insurance fraud) because each has a slightly different report vocabulary and emphasis. Include that the firm has established professional standards and a named client on this engagement.

### Scenario Pattern
The trigger is always receipt of field materials from one or more subordinate investigators. The scenario should specify: what the investigation was about (subject description without real names), who the client is at a category level (insurance agency, retail chain, individual), and why the senior investigator is involved (quality review, multi-investigator synthesis, or report finalization for legal submission). Include the number of field documents being provided and whether photographs are included.

### Instruction Pattern
Provide a numbered or bulleted list of required tasks: review materials, reconstruct timeline, integrate photographic evidence, write the report. Always specify the mandatory section structure (Summary, Surveillance, Assessment minimum), page limit, and output format (PDF). Add specific quality requirements: grammar correction, removal of irrelevant details, consistency between written narrative and photographic evidence, professional tone.

### Constraint Injection Points
- **Page limit:** varies from 2 pages (tight, forces aggressive editing) to 5+ pages (multi-investigator compilation)
- **Section structure:** three-section minimum (Summary/Surveillance/Assessment); can add sub-sections for multi-investigator reports
- **Letterhead requirement:** present/absent; when present, the firm's company letterhead template is a reference file
- **Anonymization scope:** none vs. partial (no store number) vs. full (no names, locations, or identifying details)
- **Source material complexity:** single draft from one investigator vs. two sequential investigators with overlapping/contradictory observations
- **Evidence integration:** photographs only vs. photographs + time log vs. photographs + CCTV cross-reference instructions
- **Client deliverable purpose:** internal HR action vs. insurance claim processing vs. potential litigation

### Structural Template

```
[PERSONA]: You are a [Senior Investigator / Claims Investigation Supervisor / PI Supervisor] at [FIRM_TYPE] private investigation firm with [N] years of experience handling [SPECIALTY: domestic surveillance / corporate retail / insurance fraud] cases.

[SCENARIO]: Your client, [CLIENT_TYPE: a regional insurance agency / a multi-location retail chain / a private individual], retained your firm to investigate [SUBJECT_SITUATION: a reported workplace injury claim / suspected employee theft / a domestic matter]. [FIELD_CONTEXT: Field Investigator [A] conducted surveillance on [DATE_1]; Investigator [B] continued on [DATE_2].] You have received the following materials:
- [FILE_1]: [DESCRIPTION]
- [FILE_2]: [DESCRIPTION]
- [FILE_3 (if applicable)]: [DESCRIPTION]

[TASK]: Review all submitted materials and produce a finalized professional investigation report suitable for delivery to the client. Specifically:
1. Organize and reconstruct the surveillance timeline from the field notes and time logs.
2. Integrate photographic evidence by referencing specific photographs at relevant narrative points.
3. Correct grammar, punctuation, and sentence structure throughout.
4. Remove peripheral or irrelevant observations; retain all significant findings.
5. Apply [ANONYMIZATION_RULE: no real names or store numbers / full anonymization].
6. Structure the report into three sections: Summary, Surveillance, Assessment.
7. Include client-facing recommendations in the Assessment section.

[CONSTRAINTS]:
- Maximum [N] pages
- PDF format
- [LETTERHEAD: Print on company letterhead / Standard firm formatting]
- All key observations must be preserved — do not omit significant findings
- Report must be consistent with photographic evidence

[OUTPUT_SPECIFICATION]: Single PDF document, max [N] pages, [on provided company letterhead / standard formatting], sections: Summary, Surveillance, Assessment.
```

## 4. Reference File Requirements

### File Types Needed
- **Field investigator report draft (docx):** A timestamped narrative account of a surveillance session written by a field investigator — may have grammar errors, informal language, and extraneous detail. Should be 2–4 pages of raw prose with timestamped activity entries.
- **Surveillance photograph archive (zip):** A set of 5–20 photographs taken during surveillance with filenames that include timestamps or sequential numbering. Images should depict subject activity relevant to the investigation claim (e.g., physical activity inconsistent with an injury claim, employee behavior near cash registers).
- **Time log / company template (docx):** A standardized form used by the firm to record investigator check-in/check-out times and contact notes; may have pre-filled sections.
- **Company letterhead template (pdf):** Firm's official letterhead with logo, address, and contact information — used as the formatting template for client-deliverable reports.
- **Second investigator's report (docx)** (multi-investigator variant): A second field investigator's narrative covering a different date or time window, potentially contradicting or complementing the first.

### Data Characteristics
The field report draft should contain 15–30 timestamped activity entries, some significant and some routine (e.g., "Subject entered vehicle" is significant; "Cloud cover at 10 AM" is peripheral). Photographs should be referenced by filename in the report narrative. The time log should have fields for investigator name, case number, date, start/end times, and location notes. Multi-investigator variants need enough overlap (or deliberate gap) in the surveillance timeline to require synthesis judgment.

### File Complexity Spectrum
- **Minimal:** One investigator's draft report (2 pages) + 5 photographs (no time log, no letterhead). Single-session domestic surveillance.
- **Moderate:** One investigator's draft + time log + 12 photographs + letterhead. Corporate retail investigation, one week of embedded observation.
- **Complex:** Two investigators' reports + time log + 20+ photographs + letterhead. Insurance fraud case with sequential surveillance days, potentially contradictory observations, embedded photograph evidence required.

## 5. Output Specification

### Primary Deliverable
- **Format:** PDF
- **Structure:** Three mandatory sections — Summary (case background, subject, dates, client), Surveillance (chronological timeline of significant observations), Assessment (professional conclusions and recommendations)
- **Key quality signals:** Coherent timeline with no gaps or contradictions, photograph references integrated at appropriate narrative points, professional prose free of grammar errors, page limit observed, anonymization rules applied consistently, client-actionable recommendations present

### Secondary Deliverables (if any)
- None standard; occasionally a cover letter or transmittal email draft

### Gold Output Characteristics
A gold output reads as a document a senior investigator would actually submit to an attorney or insurance adjuster. It opens with a concise Summary (1–2 paragraphs) that establishes who was investigated, why, and when. The Surveillance section is a clean chronological narrative where each entry adds to the evidentiary picture — routine non-events are omitted. Photographs are referenced by number or filename at the relevant narrative moment. The Assessment closes with specific, defensible conclusions and concrete recommendations (e.g., "Claimant's observed physical activity is inconsistent with the claimed injury; recommend denial of claim pending further investigation"). Page count falls at or within the specified limit.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of source investigators | 1 | 2 | 3 (sequential + concurrent) |
| Source material quality | Well-organized draft, minor grammar fixes | Unstructured notes with interspersed irrelevant details | Raw shorthand notes plus contradictions between investigators |
| Photograph integration | 5 photos, no embedding required | 12 photos, referenced by filename in narrative | 20+ photos, some must be selected as exhibits, some excluded |
| Page limit | 3–4 pages (comfortable) | 2 pages (tight) | 1.5 pages (extreme compression required) |
| Anonymization requirement | None | Partial (no store number, no names) | Full (no names, locations, dates in prose — coded references only) |
| Letterhead requirement | Absent | Simple header | Full letterhead template supplied as reference file |
| Investigation specialty | Domestic surveillance (simpler vocabulary) | Corporate retail (behavioral judgment layer) | Insurance fraud (legal evidentiary standard, claim denial recommendation) |

## 7. Boundary Cases & Adjacent Patterns

**I2 (Investigation Process Tools & Guides):** I2 produces the forms and guides that field investigators use; I1 produces the actual report that results from using those forms. The same engagement can span both patterns when it creates an operational guide or template (I2) and also produces the observation forms later used in I1 workflows. Choose I2 when the deliverable is a reusable template or guide; choose I1 when the deliverable is a specific completed report.

**F5 (Peer Feedback & Coaching Documents):** F5 includes reviewing a colleague's work and providing annotated corrections. This pattern can carry an F5 dimension whenever finalizing the report involves correcting grammar and structure in a field investigator's draft. The distinction is purpose: F5 is about coaching the investigator; I1 is about producing a client-deliverable report. If the output goes to the field investigator as feedback, it is F5. If it goes to the client, it is I1.

**B3 (Compliance Report from Transaction Data):** B3 also cross-references sources against criteria to produce a findings narrative. The key distinction is domain and evidence type: B3 uses financial transaction data and regulatory rules; I1 uses surveillance observations and photographic evidence. If the task involves financial data, choose B3. If the task involves surveillance field notes and photographs, choose I1.
