# Literature Review & Evidence Synthesis

**Macro Category:** E — Research-to-Document Tasks
**Pattern ID:** E1

## 1. Pattern Description

The worker conducts a structured multi-database academic or institutional literature search, applies explicit inclusion/exclusion criteria, and synthesizes the findings into a formal document organized by prescribed thematic sections. The output is not a simple list of sources but a synthesized analysis that extracts study-level data (design, setting, findings) and draws cross-cutting conclusions or implications. This pattern is distinct from general web research tasks because it requires engagement with peer-reviewed or government-grade sources and documentation of search methodology. The cognitive core is applying evidence evaluation standards — filtering by source quality, date, and topical relevance — and then synthesizing findings into coherent subtheme narratives rather than summaries of individual sources.

## 2. O*NET Grounding

### Occupation Families
- 29-1171 Nurse Practitioners — clinical literature reviews are a core evidence-based practice competency for advanced practice nurses
- 11-3011 Administrative Services Managers — government program planning often requires literature-grounded rationales for policy decisions
- 11-9151 Social and Community Service Managers — nonprofit program evaluation and grant applications require evidence synthesis
- 19-3099 Social Scientists and Related Workers — research synthesis is a core work activity across social science disciplines
- 13-1111 Management Analysts — policy and process change recommendations are often evidence-grounded

### Key Work Activities (O*NET vocabulary)
- Analyzing Data or Information
- Getting Information
- Documenting Information
- Updating and Using Relevant Knowledge
- Interpreting the Meaning of Information for Others
- Making Decisions and Solving Problems

### Knowledge Domains (O*NET vocabulary)
- English Language
- Medicine and Dentistry (for clinical reviews)
- Psychology / Sociology and Anthropology (for social program reviews)
- Administration and Management (for policy/government reviews)
- Education and Training (for program evaluation contexts)
- Computers and Electronics (for identifying and accessing databases)

### Generalizable Work Context
A knowledge worker in a professional or healthcare organization needs to justify a policy, program, or clinical practice change with an evidence base. The trigger is typically an upcoming strategic decision, grant application, or quality improvement initiative. The worker is expected to locate, evaluate, and summarize primary literature rather than rely on secondary summaries. Stakeholders are typically senior leadership or peer reviewers who expect structured, citation-supported synthesis rather than anecdotal reasoning.

## 3. Prompt Construction Template

### Persona Pattern
Assign a role with professional responsibility for evidence-based decision-making: advanced practice clinician, government policy analyst, nonprofit program director, public health advisor. The role should have a plausible reason to conduct literature work without a research librarian (mid-level independent professional, not a PhD researcher with full database access). Seniority level: mid-to-senior individual contributor.

### Scenario Pattern
A decision-maker (department head, clinical director, executive sponsor) has asked for an evidence-grounded document to support a program launch, policy revision, or strategic planning process. The timeline is short enough to require focused searching rather than exhaustive review. The topic should be actionable within the worker's professional domain, connecting public-health or organizational evidence to a concrete workplace decision.

### Instruction Pattern
Lead with the purpose statement (what decision the review will inform), then specify the document structure as numbered sections with named headings. Provide the literature search scope as explicit inclusion criteria: named databases, publication date floor, source type (peer-reviewed, government), and keyword terms. Specify the number of sources required. State whether a table or narrative format is expected per section.

### Constraint Injection Points
- **Source count:** how many articles/studies required — ranges from 3 (tight overview) to 30+ (full review)
- **Publication date filter:** recency requirement — last 3 years vs. last 10 years
- **Source type constraints:** peer-reviewed only vs. peer-reviewed + government + gray literature
- **Named databases:** a mix of major indexes (e.g., PubMed, CINAHL), specialized databases (e.g., Cochrane, ERIC), broad academic search engines (e.g., Google Scholar), and relevant government or professional-association sites — narrows search scope
- **Page/word limit:** drives depth — 1-page table vs. 10-15 page narrative review
- **Subtheme structure:** number of required thematic subheadings (2–6 range)
- **Citation format:** APA, AMA, Vancouver — affects reference section complexity
- **Output format:** tabular (one row per study) vs. narrative essay vs. hybrid

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE] in [GEOGRAPHIC/SECTOR CONTEXT].

[SCENARIO]: Your [SUPERVISOR/DIRECTOR] has asked you to develop an evidence-based [DOCUMENT TYPE] to support [STRATEGIC DECISION/PROGRAM GOAL]. This document will be used to [DOWNSTREAM USE CASE].

[TASK]: Conduct a structured literature search and produce a [PAGE_COUNT]-page [DOCUMENT TYPE] on the topic of [TOPIC STATEMENT].

[SEARCH REQUIREMENTS]:
- Databases: Search [DATABASE_1], [DATABASE_2], [DATABASE_3], and [DATABASE_4]
- Publication date: Include only sources published after [YEAR]
- Source type: [PEER-REVIEWED ARTICLES / GOVERNMENT SOURCES / GRAY LITERATURE]
- Key terms: [KEYWORD_SET]
- Include/exclude: [INCLUSION_CRITERIA]

[DOCUMENT STRUCTURE]:
Your document must include the following sections:
1. [SECTION_1_NAME]: [BRIEF DESCRIPTION]
2. [SECTION_2_NAME]: [BRIEF DESCRIPTION including required subthemes: SUBTHEME_A, SUBTHEME_B, SUBTHEME_C]
3. [SECTION_3_NAME]: [BRIEF DESCRIPTION]
4. References: Maximum [N] citations

[OUTPUT CONSTRAINTS]:
- Format: [TABLE / NARRATIVE ESSAY / HYBRID]
- Length: [PAGE_COUNT] pages
- Style: [CITATION_FORMAT], [WRITING_STYLE]
- Column headers (if table): [COLUMN_1], [COLUMN_2], [COLUMN_3]
```

## 4. Reference File Requirements

### File Types Needed
- **None (web-research-driven):** The literature search itself IS the reference activity; no pre-attached files are needed. URLs to specific databases or authoritative sources may be provided inline in the prompt.
- **Optional: Search strategy log:** A short bulleted document listing prior search terms and databases consulted can be provided to simulate a handoff scenario where the worker builds on prior research.

### Data Characteristics
No structured data files. The "reference material" is web-accessible academic literature. The key abstract properties are: articles are peer-reviewed or government-published, they have identifiable authors, publication dates, journals/institutions, study designs (RCT, observational, systematic review), and findable conclusions. The pipeline should generate prompts that name specific plausible databases and keyword combinations rather than generic "search the web" instructions.

### File Complexity Spectrum
- **Minimal:** No reference files; prompt specifies 3–5 articles in a simple 3-column table (study info | key findings | implications); 1-page output.
- **Moderate:** No reference files; prompt specifies 8–15 sources across 3 databases with 3–4 thematic subthemes; 5–8 page narrative review with references section.
- **Complex:** Inline URLs to named resources; 15–30 sources across 5+ databases; 10–15 page formal literature review with methodology section, subtheme analysis, strengths/limitations, and max-citation constraint.

## 5. Output Specification

### Primary Deliverable
- **Format:** Word document (.docx)
- **Structure:** Sequential sections with named headers (Introduction/Background, Search Strategy, Results [organized by subtheme], Strengths and Limitations, Conclusion, References); sometimes a summary table per section
- **Key quality signals:** Search strategy explicitly documented; inclusion criteria applied consistently; findings attributed to specific sources; subthemes structurally organized not just listed; conclusions grounded in evidence rather than opinion; reference count within specified maximum

### Secondary Deliverables (if any)
- Occasionally a separate summary table (if main output is narrative and a tabular abstract is also requested)

### Gold Output Characteristics
A gold output explicitly states the search strategy (databases, date range, terms, N results), presents findings organized by prescribed subthemes with cross-source synthesis rather than source-by-source summaries, attributes all factual claims to specific citations, keeps the reference count within the specified ceiling, and concludes with implications tied directly to the stated organizational decision. The writing is concise and professional — not padded to reach page limits.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Source count | 3–5 sources | 8–15 sources | 20–30 sources |
| Page/length requirement | 1-page table | 5–8 pages narrative | 10–15 pages formal review |
| Database scope | 1–2 named databases | 3–4 named databases | 5+ databases (including specialized, e.g., CINAHL + Cochrane + ERIC) |
| Subtheme structure | Free-form narrative | 2–3 prescribed subthemes | 4–6 prescribed subthemes with distinct content requirements |
| Output format | Simple table (one row per source) | Hybrid (table + narrative synthesis) | Full research paper format (methodology section, APA citations, appendix) |
| Topic complexity | Single clear domain | Two intersecting domains | Emerging/contested area requiring critical appraisal |
| Citation format | Informal (links acceptable) | APA or AMA | Strict academic citation format with DOIs |

## 7. Boundary Cases & Adjacent Patterns

**E4 (Regulatory Data Extraction & Comparison):** Both involve systematic web research and structured synthesis, but E4 extracts from regulatory/legal sources (state boards, CMS, EPA portals) and organizes findings into comparison tables with strategic recommendations — not academic evidence synthesis. Choose E1 when the source type is peer-reviewed or government research literature and the task produces a research-style document; choose E4 when extracting rule-based data from compliance portals for operational decision-making.

**E3 (Market Research & Deal Sourcing):** E3 involves collecting quantitative market data (pricing, property metrics) from commercial platforms rather than synthesizing qualitative/evidential conclusions from academic literature. E1 requires critical appraisal and synthesis; E3 requires enumeration and calculation.

**D4 (Program & Evaluation Plans):** D4 may involve referencing external URLs to select validated instruments (e.g., PHQ-9), but the primary deliverable is a program plan document rather than a literature review. D4 uses web resources instrumentally; E1 treats the literature search as the central work product.

**C3 (Clinical Guidelines & Reference Guides):** C3 produces prescriptive clinical guidance documents authored from domain expertise and professional standards, sometimes citing named guidelines. E1 requires documented search methodology and explicit source synthesis, not just knowledge-grounded authorship.
