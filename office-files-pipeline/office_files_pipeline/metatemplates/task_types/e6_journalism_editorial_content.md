# Journalism & Editorial Content

**Macro Category:** E — Research-to-Document Tasks
**Pattern ID:** E6

## 1. Pattern Description

The worker produces journalism-grade written content — news articles, opinion editorials, feature articles, editorial pitches, or policy guidance documents — grounded in web-sourced facts and subject to publication-specific style rules. The defining characteristics are: (1) a named style guide governs writing conventions (The Guardian, SPJ code of ethics, AP style), (2) source-level credibility requirements constrain which outlets can be cited, and (3) specific journalistic structural elements must be present (headline, standfirst, subheadings, word count within a defined range). When reference files are present, they are typically the raw material of journalism — interview notes, reporter drafts, press releases — not data files requiring computation. The cognitive core is source-grounded writing under professional constraints: selecting an appropriate topic or angle, synthesizing multi-source information into a coherent narrative, and producing text that meets the word count, structural, and style requirements simultaneously.

## 2. O*NET Grounding

### Occupation Families
- 27-3023 News Analysts, Reporters, and Journalists — core occupation; news articles, investigative reporting, election coverage
- 27-3041 Editors — editorial review, fact-checking, tracked-changes feedback, editorial pitches
- 27-3043 Writers and Authors — feature articles, science writing, opinion editorials
- 21-1099 Community and Social Service Specialists (adjacent) — editorial policy guides for organizational communication standards
- 11-2031 Public Relations Specialists (adjacent) — press release drafting that mirrors journalistic structure

### Key Work Activities (O*NET vocabulary)
- Communicating Through Written Language
- Thinking Creatively
- Getting Information
- Interpreting the Meaning of Information for Others
- Evaluating Information to Determine Compliance with Standards
- Editing Written Information

### Knowledge Domains (O*NET vocabulary)
- English Language
- Communications and Media
- Science (for science journalism variants)
- Economics and Accounting (for financial/economic news)
- Law, Government and Jurisprudence (for elections, regulatory reporting)
- Astronomy (for space/science variants)
- Computers and Electronics (for technology journalism)

### Generalizable Work Context
A journalist, editor, or senior reporter at a digital or print publication is assigned a writing task with a named audience (general public, policy-makers, scientifically curious non-experts), a defined publication context (science magazine, local newspaper, online news outlet), and explicit style and structural requirements. The task may be self-initiated topic selection within constraints, or tightly specified (a named report, a named research paper, a named event). The output is a deliverable ready for editorial review, publication, or pitch submission — not a draft requiring substantial further work.

## 3. Prompt Construction Template

### Persona Pattern
Assign a journalism role at a named or described publication: editor at an international science magazine, journalist at a local newspaper, senior reporter at a digital outlet, senior science editor at a specialty publication, technology journalist at a UK-based outlet. Include the publication's audience profile and editorial standards as part of the persona context. Specify the reporter's beat (science, elections, economics, technology, astronomy) to constrain topic scope. Seniority level: staff journalist to senior editor.

### Scenario Pattern
Provide a specific writing assignment: a named topic or event to cover, a specific research paper or report to summarize, a reporter draft to review, or an open topic selection within a defined beat. Include the publication context and downstream use (publication, editorial review, pitch submission). Specify the target audience explicitly — this drives the language register and explanatory depth required.

### Instruction Pattern
State the article type first (news, opinion, feature, pitch, editorial policy). List structural requirements explicitly: headline required, standfirst required, subheadings required, word count range. Name the style guide and provide its URL. List any named sources that must or may be used. Specify the output format (Word, PDF). For editorial review tasks, describe what types of feedback are expected and the evidence standard for corrections.

### Constraint Injection Points
- **Word count range:** tight range (300–500 words) vs. broad range (1,000–1,500 words); minimum and/or maximum
- **Style guide:** named guide with URL (The Guardian, SPJ, AP); language variant (UK English vs. US English)
- **Source requirements:** named tier-1 outlets required (Nature, Science, Reuters, AP); minimum number of sources; source date constraints
- **Structural elements:** headline (SEO-optimized vs. standard), standfirst, subheadings, call to action, verification links
- **Neutrality constraint:** politically neutral, impartial, factual vs. opinion-based editorial with perspective
- **Reference file types (for editing/writing from notes):** reporter drafts, press releases, interview notes, background explainer articles
- **Output format:** Word with tracked changes (editorial review) vs. PDF (final publication copy)
- **Topic freedom:** fully open (worker chooses topic from broad beat) vs. partially specified (named report, named event) vs. fully specified (named article, specific data points required)

### Structural Template

```
[PERSONA]: You are a [ROLE] at [PUBLICATION_NAME/TYPE], a [DESCRIPTION_OF_PUBLICATION] covering [BEAT/TOPICS]. Your publication serves [AUDIENCE_DESCRIPTION].

[SCENARIO]: [ASSIGNMENT_CONTEXT — e.g., "Your editor has assigned you to cover..." / "A reporter has submitted a draft for your editorial review..." / "You are preparing a pitch for a story about..."].

[TASK]: Write a [ARTICLE_TYPE] of [WORD_COUNT_RANGE] words on the following topic: [TOPIC_SPECIFICATION].

[SOURCE REQUIREMENTS]:
- Must include information from: [NAMED_SOURCE_1], [NAMED_SOURCE_2]
- Minimum number of sources: [N]
- Source date constraint: [published after / as of DATE]
- Include hyperlinks to all referenced sources
- [ADDITIONAL: verification links for sub-editor review, if applicable]

[STRUCTURAL REQUIREMENTS]:
Your article must include:
1. Headline: [SEO-optimized / standard / proposed working headline]
2. Standfirst: [brief summary sentence below headline]
3. Body: [NARRATIVE_STRUCTURE_DESCRIPTION — e.g., "led by news hook, background, expert reaction, implications"]
4. Subheadings: [required / optional]
5. [CALL TO ACTION / CONCLUSION requirement, if applicable]
6. [URL at end / Verification links embedded, if applicable]

[STYLE REQUIREMENTS]:
- Follow [STYLE_GUIDE_NAME] style guide: [URL if provided]
- Language variant: [UK English / US English]
- Tone: [neutral and factual / opinion-led / accessible to non-experts / professional and clinical]
- [NEUTRALITY REQUIREMENT: e.g., "Do not express opinions about candidates or platforms"]

[OUTPUT FORMAT]: [Word document / PDF]
[NO IMAGES requirement, if applicable]
```

## 4. Reference File Requirements

### File Types Needed
- **None (web-research-only):** For news articles, editorials, and pitches, all source material is gathered via web research from named URLs or named publications. No pre-attached files needed.
- **Reporter draft (DOCX):** For editorial review tasks, the reporter's first draft is attached. This is a narrative text document (~500–1,000 words) requiring expert review for scientific accuracy, clarity, and audience appropriateness. Contains claims requiring fact-checking against primary sources.
- **Interview notes/transcripts (DOCX):** For feature articles, raw interview notes (contemporaneous or transcribed) from multiple subjects are attached. May be grammatically imperfect, use non-native English, or mix reporting formats.
- **Press releases (DOCX):** For feature articles, company-provided press releases about a product, event, or research finding serve as the primary factual foundation. Marketing-language tone must be converted to journalistic register.
- **Background explainer (DOCX):** A technical or contextual background document on a topic (e.g., what a specialized technology or process is) that provides domain grounding for the journalist.

### Data Characteristics
**Web research inputs:** News articles from named publications with specific date constraints, research papers on arXiv or similar preprint servers, government websites (e.g., a state elections authority, an international financial institution, or a federal agency), official press releases, and authoritative institutional sources. All must be publicly accessible without paywall.

**Reference file inputs (when present):** Narrative text documents varying from polished press releases to rough interview transcripts. Key properties: 500–1,500 words per file, contain factual claims with varying degrees of sourcing, may be in non-standard English (interview notes from non-native speakers), may require transformation in register (marketing → journalism, rough notes → polished quotes).

### File Complexity Spectrum
- **Minimal:** No reference files; single named source or report to summarize; 300–500 words; standard headline + body structure; one style guide referenced.
- **Moderate:** No reference files; multiple named sources (3–5 URLs provided); 500–1,000 words; full journalistic structure (headline, standfirst, subheadings, links, call to action); named style guide URL.
- **Complex:** Multiple reference files (press releases + interview notes + background explainer); 1,000–1,500 words; SEO headline, standfirst, subheadings; UK English; Guardian style guide; quote-driven narrative structure with non-native speaker notes requiring cleanup; OR: one reporter draft requiring tracked-changes editorial review with multi-source fact-checking.

## 5. Output Specification

### Primary Deliverable
- **Format:** Word document (.docx) or PDF
- **Structure:** Headline → Standfirst → Body paragraphs with subheadings → Conclusion/Call to action → Source links; OR: tracked-changes edited document with explanatory comments (editorial review variant)
- **Key quality signals:** Word count within specified range; all required structural elements present (headline, standfirst — not just body text); named style guide conventions followed (capitalization, hyphenation, date format, UK vs. US English); named sources cited with hyperlinks; factual claims supported by linked evidence; neutrality maintained where required; quote attribution clear and accurate

### Secondary Deliverables (if any)
- JPG chart or graph accompanying an economics/data news article
- Separate verification links list embedded in document for sub-editor use

### Gold Output Characteristics
A gold output falls within the specified word count range (not marginally over or under), includes all required structural elements in the correct journalistic order, follows the named style guide consistently throughout (not just in headline format), cites sources with embedded hyperlinks rather than bibliography entries, preserves factual accuracy against named source material, applies the correct language variant (UK English: "organisation", "colour", "focuses" not "focusses"), and — for editorial review tasks — provides explanatory comments with specific source-linked justification for factual corrections alongside actionable rewrites or prompts. Opinion pieces state a clear position backed by named evidence; news pieces maintain neutrality and cite named parties rather than editorializing.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Word count | 300–500 words | 500–1,000 words | 1,000–1,500 words (hard floor and ceiling) |
| Topic freedom | Fully specified topic with named data source | Partially specified (named area, worker chooses angle) | Fully open topic selection within a broad beat |
| Source requirements | 1–2 named sources | 3–5 sources from named tier-1 outlets | 6–8 provided URLs that must all be synthesized and hyperlinked |
| Structural elements | Headline + body | Headline + standfirst + body + links | Headline (SEO-optimized) + standfirst + subheadings + call to action + verification links + source URL list |
| Reference file complexity | None | None (web research only) | Several files: press releases + interview notes (non-native English) + background explainer |
| Style constraint | General professional tone | Named style guide referenced | Named style guide URL required, specific language variant (UK English) enforced |
| Output variant | Standard article (Word) | Article + chart (JPG) | Tracked-changes editorial review with explanatory comments and per-correction sourcing |

## 7. Boundary Cases & Adjacent Patterns

**C4 (Training Materials & Educational Presentations):** C4 produces instructional content (slide decks, guides, case studies) designed to teach a skill or knowledge domain to an organizational audience. E6 produces journalism-grade content for publication audiences subject to professional journalism standards. When the output must follow a journalism style guide, include a standfirst, and be grounded in cited current sources, use E6.

**D2 (Corporate Strategy & Business Proposals):** D2 produces strategic or advisory documents for internal or client-facing business use. E6 produces publication-ready journalism content for public audiences. The audience (internal stakeholders vs. general public) and the accountability standard (journalism ethics vs. business strategy) distinguish the two.

**C3 (Clinical Guidelines & Reference Guides):** C3 produces authoritative clinical guidance documents authored from evidence and professional standards. E6 may produce science journalism grounded in clinical research, but E6 requires journalistic structure (headline, standfirst, style guide) and public audience framing, while C3 requires clinical prescription format for healthcare professional audiences.

**E1 (Literature Review & Evidence Synthesis):** Both patterns involve multi-source web research and document production. E1 produces academic-style synthesis organized by research subthemes with formal citation methodology. E6 produces journalism-style narrative content with embedded hyperlinks and story structure. The output format and accountability standard (academic evidence synthesis vs. journalistic publication) are the key distinguishers.

**F5 (Peer Feedback & Coaching Documents):** F5 involves reviewing colleagues' work (chat transcripts, field reports) and providing constructive coaching feedback. An editorial-review task with tracked changes superficially resembles F5, but E6 applies journalism-domain expertise and source-verification standards rather than general professional quality standards. When the review requires cross-referencing a scientific paper and a press release to evaluate factual accuracy, use E6 rather than F5.
