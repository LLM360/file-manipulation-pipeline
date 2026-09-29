# Tenant/Customer Communications & Tracking

**Macro Category:** F — Client Communication & Outreach Materials
**Pattern ID:** F3

## 1. Pattern Description

The worker drafts one or more client-facing communications (emails, letters, memos, talking points) and often a paired internal tracking document, by analyzing reference data from a tabular log or feedback dataset. The cognitive core is dual-purpose synthesis: extracting structured information from source data to generate personalized or grouped communications for tenants/customers/constituents, while simultaneously organizing that same data into an operational tracking or summary document for internal use. This pattern is distinct from generic email drafting because the communications are grounded in specific reference data (move-out dates, feedback logs, fund details) that must be cross-referenced and applied; and because most tasks in this pattern produce two distinct deliverables targeted at different audiences (the external party and an internal manager or board).

## 2. O*NET Grounding

### Occupation Families
- 11-9141 Property, Real Estate, and Community Association Managers — leasing agents and property managers sending tenant communications with scheduling/tracking documents
- 43-4051 Customer Service Representatives — government service reps drafting informational email responses; financial services reps responding to client benefit inquiries
- 43-4031 Municipal Clerks — government CSRs summarizing constituent feedback for board presentations
- 43-4171 Receptionists and Information Clerks — administrative staff coordinating inspection scheduling and resident notifications

### Key Work Activities (O*NET vocabulary)
- Communicating with the Public
- Documenting or Recording Information
- Scheduling Work and Activities
- Providing Information to Others
- Analyzing Data or Information (feedback categorization, eligibility cross-referencing)
- Resolving Conflicts and Negotiating with Others (tenant exception handling)
- Getting Information (researching fund details, regulatory content)
- Organizing, Planning, and Prioritizing Work

### Knowledge Domains (O*NET vocabulary)
- Customer and Personal Service
- English Language
- Administration and Management
- Law, Government, and Jurisprudence (retirement-benefit program rules, government district administration)
- Economics and Accounting (retirement-fund structures, retirement benefits)
- Sales and Marketing (tenant retention strategy framing)

### Generalizable Work Context
A customer-facing role (leasing agent, government service rep, property manager, or CSR) receives either a reference data file or a direct client inquiry, and must produce: (1) communications addressed to the external party (tenants, constituents, clients), and (2) an internal document that organizes the same underlying data for manager or board use. The trigger is an operational event (move-outs at month end, a board meeting, a client service inquiry, a retention problem). The source data is typically a tabular log, feedback form, or known regulatory structure. Exception handling — applying a default rule while accommodating individually noted departures — is common.

## 3. Prompt Construction Template

### Persona Pattern
Assign a front-line to mid-level client-facing role: Leasing Agent, Government Service Representative, Property Manager, or Customer Service Representative. Include the organization type and, for property management tasks, the community name and size (e.g., a mid-size or large residential community, given as a unit count). The persona establishes the professional register for communications (formal government tone vs. warm residential landlord tone).

### Scenario Pattern
For tenant communication tasks: specify the operational event (move-out period, lease renewal cycle, vendor turn scheduling), the default rule (default inspection date, default renewal terms), and the exception mechanism (individual tenant notes or feedback requiring date/term adjustments). For constituent/customer service tasks: specify the inquiry type (fund information request, board meeting preparation), the client profile (military-to-civilian transition, long-tenured resident), and the information domain to be addressed.

### Instruction Pattern
Instructions specify the dual-deliverable structure: (1) external-facing communication(s) — format, tone, content, subject line or header — and (2) internal document — columns, format, audience. Numbered requirements work well. Default-plus-exception logic is best expressed as a rule statement ("default date X; apply alternate dates from the notes file for residents who requested them").

### Constraint Injection Points
- **Default rule + exception handling:** a baseline date, term, or value applies to all cases unless a specific exception is noted in a source file; the exception detection is part of the task
- **Dual audience:** external communication (tenants, constituents, clients) vs. internal document (manager tracker, board summary, talking points); each has different format and register
- **Data source cross-referencing:** one source provides the population (who to communicate with), another provides the exception data (individual preferences or notes) — both must be used
- **Tracking document column schema:** fixed columns prescribed in the prompt (e.g., a unit or account identifier, the person's name, and one or more key dates); can be varied in number and type
- **Feedback categorization:** qualitative data (exit surveys, constituent comments) must be categorized before being synthesized; number of categories and their labels can be varied
- **Communication register:** formal government language vs. warm property management tone vs. informational financial services tone
- **Page/length constraint:** one-page summary vs. 1-2 page memo vs. comprehensive email response

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE — residential community name / government district / government agency / financial services firm].

[SCENARIO]: [OPERATIONAL_TRIGGER: end-of-month move-outs / board meeting preparation / client inquiry / tenant retention problem]. [DATA_CONTEXT: N residents moving out / constituent feedback received / client transitioning between roles].

[REFERENCE_FILES]:
- [FILE_1]: [file type and description — e.g., move-out report with resident names, unit numbers, and move-out dates]
- [FILE_2]: [file type and description — e.g., tenant notes with individual scheduling preferences]

[TASK]: Produce two deliverables:

Deliverable 1 — [EXTERNAL_COMMUNICATION_TYPE: email / letter / comprehensive email response]:
- Addressed to: [tenants / constituent / client]
- Subject/header: [SUBJECT_IF_SPECIFIED]
- Content: [COMMUNICATION_CONTENT_REQUIREMENTS]
- Default rule: [DEFAULT_DATE/TERM/CONTENT]; apply exceptions where [EXCEPTION_CONDITION] is noted in [FILE_2]

Deliverable 2 — [INTERNAL_DOCUMENT_TYPE: tracking table / summary document / talking points / strategic memo]:
- Audience: [manager / board / staff]
- Format: [PDF / Word / Excel]
- Columns/sections: [COLUMN_1], [COLUMN_2], [COLUMN_3] [... or section list for memo/summary]
- Organization: [by district / by resident / by departure reason / chronological]

[CONSTRAINTS]:
- Page/length limit: [N pages / one page]
- Output format: [PDF / Word / Excel]
- [ADDITIONAL_FORMAT_CONSTRAINTS: bold headers, line spacing, etc.]
```

## 4. Reference File Requirements

### File Types Needed
- **Tabular operational log (xlsx):** Move-out report, constituent feedback tracking log, or resident renewal history. Typical fields: unit/district identifier, person name, dates (move-out, lease end), and status/category fields. 10-200 rows is typical.
- **Supplemental notes or communications file (pdf or docx):** Resident-specific notes indicating exceptions to the default rule (alternate inspection dates, specific requests). Can also be a renewal letter providing tone/format reference.
- **Survey feedback data (xlsx):** For tenant retention variants — raw exit survey data with free-text or partially coded departure reasons. Fields: resident ID, departure reason text, and optionally a category field to be populated by the worker.

### Data Characteristics
The tabular operational log should contain: a primary key identifier (unit number, district ID, resident ID), person name, one or more date fields (move-out date, lease end date), and optionally a status or category column. The notes or feedback file should contain at least one exception case and one case conforming to the default rule, to test exception-detection logic. Exit survey data should contain enough entries to clearly identify the leading departure reasons when categorized (a small set of predefined categories helps structure this). All data should be realistic for the industry (residential property management, government services, financial services).

### File Complexity Spectrum
- **Minimal:** Single-file task — a constituent feedback log (xlsx) with 10-15 entries across several districts; produce a one-page district-organized summary and staff talking points (no exception handling, no date logic)
- **Moderate:** Two-file cross-reference — move-out report (xlsx) + tenant notes (pdf); apply default inspection date with exception handling for 2-3 residents; produce email communication and a multi-column tracking table
- **Complex:** Two-file analysis + strategic planning — exit survey data (xlsx) + current renewal letter (docx); categorize qualitative feedback into a small set of predefined categories; identify the leading departure reasons; produce a multi-component strategic retention memo (e.g., departure analysis, a tiered renewal offer structure, a phased communication plan, and community engagement ideas) within a 1-2 page limit

## 5. Output Specification

### Primary Deliverable
- **Format:** PDF (most common), Word document, or Excel tracking table
- **Structure:**
  - External communication: email or letter format with header/subject, greeting, body covering required content, professional sign-off
  - Internal tracking document: tabular format with fixed columns or structured memo format with defined sections
  - Dual deliverable: both the communication and the tracking document are required; often both in PDF
- **Key quality signals:** All relevant records from source data are included (no omissions); default rule applied correctly to all base cases; exceptions correctly identified from notes file and applied; tracking table columns correctly populated; communication tone matches the organizational register; section structure matches specified headers

### Secondary Deliverables (if any)
- Talking points document (for government constituent summary variant): bullet-pointed staff reference for board meeting, organized by district or topic, separate from the external-facing summary
- Tiered renewal offer structure table (for tenant retention memo variant): structured table showing early, standard, and month-to-month renewal tiers with incentives per tier

### Gold Output Characteristics
A gold output: (1) correctly identifies all relevant records from the source data (all move-outs in the target period, all districts in the feedback log); (2) applies the default rule to all base cases; (3) correctly detects and applies exceptions from the notes/feedback file without omission; (4) produces both deliverables with appropriate audience-specific register; (5) follows all structural constraints (column schema, page limits, section headers, formatting rules); and (6) for strategic variants, grounds the recommendations in the actual source data rather than producing generic content.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of source files | 1 file (simple log) | 2 files (log + notes/exceptions) | 2-3 files (log + feedback + reference letter) |
| Exception handling | No exceptions; default rule applies universally | 1-2 clearly stated exceptions in notes file | 3-5 exceptions with varying conditions; some ambiguous or implicit |
| Deliverable count | 1 deliverable (communication OR tracker) | 2 deliverables (external communication + internal tracker) | 2 deliverables where the second requires synthesis of a multi-part strategic plan |
| Data analysis required | No analysis; direct extraction | Simple grouping/filtering (by district, by date range) | Qualitative categorization of free-text feedback into a small set of predefined categories to identify the leading drivers |
| Communication scope | Single communication to all recipients | Same communication with per-recipient date customization | Multi-component communication plan (a phased cadence with different message types per milestone) |
| Domain complexity | Property management (straightforward operational rules) | Government benefits (retirement-fund details, military-civilian transition rules) | Tenant retention strategy (requires external benchmarking of community engagement ideas) |
| Page constraints | No page limit | 1-page internal summary | 1-2 page strategic memo covering multiple distinct analytical components |

## 7. Boundary Cases & Adjacent Patterns

**B3 — Compliance Report from Transaction Data:** Both B3 and F3 cross-reference multiple source documents and produce a dual-deliverable output. The distinction is purpose and audience: B3 produces a compliance findings report (flagging violations, regulatory exceptions, SAR narratives) for internal compliance or regulatory audiences; F3 produces a communication to the external party (tenants, clients, constituents) plus an operational tracking document. If the primary output is a compliance report or exception finding, it is B3. If the primary output is a communication to the affected party, it is F3.

**F1 — Luxury Travel Itineraries:** Both F1 and F3 produce client-facing communications from operational data and may include scheduling elements. F1 is distinguished by the itinerary/travel nature of the output and the luxury service context; F3 is distinguished by the tenant/customer relationship, the operational tracking component, and the dual-audience deliverable structure.

**C1 — Standard Operating Procedure / General Order:** A tenant retention strategy memo sits at the F3/C1 boundary because it produces a strategic planning document rather than a communication. It belongs to F3 when the primary deliverable is a client-communication-adjacent document (a retention strategy memo that informs future communications) grounded in analysis of tenant feedback data. If the prompt produces a general operational policy document without reference to specific client data, it would be C1.
