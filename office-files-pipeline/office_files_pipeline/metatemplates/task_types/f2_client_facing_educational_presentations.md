# Client-Facing Educational Presentations

**Macro Category:** F — Client Communication & Outreach Materials
**Pattern ID:** F2

## 1. Pattern Description

The worker produces a presentation (PowerPoint or PDF) designed to educate a client, board, or stakeholder audience on a technical or specialized subject — financial products, trust structures, tax strategies, government partnerships, or luxury retail collections. The cognitive core is translating domain expertise into an accessible, structured narrative that a non-specialist audience can act on: a client choosing between investment vehicles, a board deciding whether to approve a partnership, or a retail buyer browsing a curated collection. This pattern is distinct from internal analytical presentations (B1) because the audience is always external or semi-external (clients, advisory boards, retail customers), and the goal is persuasion or comprehension, not executive reporting. It is distinct from training materials (C4) because the audience is a client or decision-maker, not staff.

## 2. O*NET Grounding

### Occupation Families
- 13-2052 Personal Financial Advisors — producing client education decks on financial instruments, tax vehicles, and estate planning strategies
- 11-9141 Property, Real Estate, and Community Association Managers / 11-9151 Community Service Managers — presenting partnership proposals and strategic rationale to advisory boards in government contexts
- 41-2031 Retail Salespersons — curating brand collection presentations for client outreach
- 13-2061 Financial Examiners — advisory comparison reports for high-net-worth clients evaluating complex trust structures

### Key Work Activities (O*NET vocabulary)
- Communicating with Persons Outside the Organization
- Advising and Consulting Others
- Selling or Influencing Others
- Thinking Creatively (slide architecture, narrative arc)
- Providing Consultation and Advice to Others
- Analyzing Data or Information (financial products, trust mechanics, market data)
- Training and Teaching Others (educational framing)
- Establishing and Maintaining Interpersonal Relationships (client relationship context)

### Knowledge Domains (O*NET vocabulary)
- Economics and Accounting (stock options, trust structures, tax treatment)
- Law, Government, and Jurisprudence (estate planning law, regulatory frameworks, municipal government)
- Customer and Personal Service
- Sales and Marketing
- English Language
- Administration and Management (for government/board-facing presentations)

### Generalizable Work Context
A client-facing professional (financial advisor, wealth planner, government director, retail advisor) needs to prepare an in-person or board-delivered presentation. The trigger is an upcoming client meeting, board session, or staff briefing. The audience is a non-specialist who must be guided to a decision or comprehension outcome. The worker has domain expertise and must translate it into accessible, visually structured slides. Reference files are rare; the task is primarily knowledge-driven. Web research is occasionally required when regulatory data or collection imagery must be sourced.

## 3. Prompt Construction Template

### Persona Pattern
Assign a senior, client-facing advisory role: Financial Advisor, Wealth Planner (CFP), Director of a government department, or Senior Client Advisor (luxury retail). Include the organization type (regional bank, RIA firm, county parks department, luxury boutique). Optionally describe the client relationship briefly (long-term client, new prospect, skeptical board).

### Scenario Pattern
The trigger is an upcoming in-person meeting or board session. Introduce: (1) the client or audience profile (age, net worth, specific financial situation, or institutional stakeholder role), (2) the educational topic the client has requested or needs to understand, (3) the decision the client must make after the presentation. For advisory comparison reports, the client situation includes specific parameters (sale proceeds, estate exposure, age, filing status) that must be reflected in scenario illustrations.

### Instruction Pattern
Instructions specify the required content areas as a bulleted or numbered list, the slide or page count constraint, and the output format. For financial planning presentations, content areas map to defined analytical sections (definitions, calculations, tax treatment, recommendation). For persuasive government presentations, content areas map to a narrative arc (rationale, partner profile, benefits). Numerical examples with hypothetical data are commonly required.

### Constraint Injection Points
- **Slide/page count:** hard upper limit ranging from 4 slides (simple retail lookbook) to 12 pages (complex advisory report); drives information density decisions
- **Required content areas:** 4-8 specific topics that must be covered, specified as a bulleted list in the prompt; the pipeline can vary which topics and in what order
- **Client scenario specificity:** ranges from generic (no specific client parameters) to highly specific (e.g., a stated age and marital status, a specific transaction or liquidity-event amount, and estate tax exposure tied to a particular tax year's law)
- **Technical domain:** stock options (ISO/NQSO), trust structures (ILIT, GRAT/CRAT), RMD strategy, CD vs. annuity, municipal partnerships, luxury retail curation — each requires different knowledge grounding
- **Tone and persuasion level:** neutral educational (explain mechanics) vs. persuasive advocacy (recommend a specific action, e.g., argue against rolling CDs into annuities)
- **Visual design requirements:** basic slide layout vs. curated imagery from brand lookbook vs. side-by-side comparison table vs. time-cycle diagram

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE]. [BRIEF_CLIENT_RELATIONSHIP_CONTEXT].

[SCENARIO]: [CLIENT/AUDIENCE_DESCRIPTION]. [UPCOMING_EVENT: client meeting / board session / staff briefing]. [CLIENT_DECISION_OR_NEED].

[TASK]: Prepare a [SLIDE_COUNT]-slide PowerPoint [or PDF, page count] presentation [titled "[TITLE]" if specified] to [EDUCATIONAL_GOAL: help your client understand / persuade the board to support / equip new staff to...].

[REQUIRED_CONTENT_AREAS]:
- [TOPIC_1]: [brief description of what must be covered]
- [TOPIC_2]: [brief description]
- [TOPIC_3]: [brief description]
- [TOPIC_4]: [brief description]
[... up to 8 topics]

[SCENARIO_ILLUSTRATION] (if applicable): Use hypothetical data to illustrate [CALCULATION_OR_SCENARIO]. Client-specific parameters: [AGE], [FILING_STATUS], [ASSET_VALUE], [TAX_YEAR_IF_APPLICABLE].

[ADDITIONAL_REQUIREMENTS]:
- Include [VISUAL_ELEMENT: side-by-side comparison table / time-cycle diagram / curated imagery / hypothetical calculation walkthrough]
- Tone: [educational and accessible / persuasive and balanced / practical and non-corporate]
- Audience: [non-specialist client / skeptical advisory board / field advisors / retail staff]

[OUTPUT_SPECIFICATION]: [PowerPoint / PDF], [SLIDE/PAGE_COUNT], [FILENAME_IF_SPECIFIED]
```

## 4. Reference File Requirements

### File Types Needed
- **None (knowledge-driven, no reference files):** The majority of samples in this pattern require no reference files. The domain expertise is entirely the worker's. The pipeline should model these as zero-reference-file tasks.
- **Brand lookbook or web imagery (web research):** For luxury retail collection presentation variants, the agent must select a real brand's current-season resort/cruise collection from its official website and source imagery. No downloadable reference file — this is a live web research task.
- **Regulatory source documents (web URLs provided):** For financial advisory variants that cite specific regulations, named URLs may be provided (e.g., FINRA investor guides, NAIC suitability briefs). These are web-fetched at task execution time, not static reference files.
- **Client assumptions document (docx):** Optional variant — a one-page brief listing the client's financial profile (account balance, income, tax bracket, age, goals) serves as input for scenario illustrations. Fields: client age, filing status, account type and value, income, marginal tax bracket, investment return assumption.

### Data Characteristics
For financial advisory presentations: domain knowledge of financial instruments (stock option mechanics, trust structures, insurance products, tax law) is the primary content. Hypothetical numerical examples must be self-consistent (e.g., exercise price × quantity - taxes = net proceeds). For government/institutional presentations: knowledge of public-private partnership frameworks, Chamber of Commerce functions, or recreation administration. For retail presentations: current brand collection content from official websites, with consistent thematic curation across 4-6 selected looks.

### File Complexity Spectrum
- **Minimal:** 4-6 slide retail collection presentation; agent selects a brand, curates looks from web, drafts client outreach email — no calculations, no regulatory content
- **Moderate:** 8-10 slide financial planning presentation (e.g., stock options, ILIT, Roth conversion) using hypothetical data; covers 4-8 content areas; no reference files; knowledge-driven
- **Complex:** Up to 12-page comparative advisory report (e.g., GRAT vs. CRAT) with client-specific scenario modeling, year-specific regulatory values, professional recommendation, and page limit constraint requiring dense but precise writing

## 5. Output Specification

### Primary Deliverable
- **Format:** PowerPoint (.pptx) or PDF
- **Structure:**
  - PowerPoint: slide-by-slide with topic headers; optional title slide and summary/recommendation slide
  - PDF: section-based with defined headers, sometimes structured as a formal professional report
- **Key quality signals:** All required content areas covered; hypothetical numerical examples are self-consistent; client-specific parameters (age, proceeds, tax year) correctly reflected in scenario illustrations; appropriate language complexity for lay audience; comparison tables/diagrams present where specified; recommendation clearly stated and reasoned where required

### Secondary Deliverables (if any)
- Client outreach template (for retail collection variant): a template email or text message staff can use to invite clients to book appointments after reviewing the presentation
- Supporting Excel model (for a complex tax-planning variant, adjacent to this pattern): year-by-year tax comparison model; only triggered when the task explicitly adds a modeling component alongside the presentation

### Gold Output Characteristics
A gold output: (1) covers all required content areas in order, (2) uses accurate domain knowledge (correct tax treatment, correct trust mechanics, correct regulatory citations), (3) applies client-specific scenario parameters precisely (age, filing status, dollar amounts, applicable tax year), (4) maintains client-appropriate (non-specialist) language throughout, (5) includes specified visual elements (side-by-side table, time-cycle diagram, curated imagery), (6) stays within the slide/page count constraint, and (7) where a recommendation is required, provides a clearly justified professional recommendation aligned to the client's stated goals.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Technical domain depth | Retail collection curation (no technical knowledge required) | Financial product comparison (ISOs vs. NQSOs, CDs vs. annuities) | Complex trust structures (ILIT, GRAT vs. CRAT) with year-specific tax law |
| Client scenario specificity | Generic educational content, no client parameters | Named client type with general profile | Fully specified client (age, marital status, asset value, filing status, specific tax year) |
| Slide/page count | 4-6 slides | 8-10 slides | 10-12 pages (PDF report format) |
| Required content areas | 2-3 broad topics | 4-6 specified topics | 8+ specific sub-topics with prescribed analytical dimensions |
| Persuasion requirement | Neutral/informational | Educational with recommendation | Explicit advocacy position (argue for/against a product or strategy) |
| Visual elements required | None beyond basic slides | Side-by-side comparison table | Multiple visual elements: comparison table + time-cycle diagram + hypothetical calculation walkthrough |
| Regulatory/source grounding | No external sources | Named URLs provided for reference | Mandatory citations from two specific regulatory sources with content integration |

## 7. Boundary Cases & Adjacent Patterns

**C4 — Training Materials & Educational Presentations:** Both C4 and F2 produce educational presentations. The critical distinction is audience: C4 targets internal staff (new hires, field advisors, nurses learning a protocol), while F2 targets external clients, advisory boards, or stakeholders. If the prompt says "for your team" or "for new hires," it is C4. If the prompt says "for your client" or "for the board," it is F2.

**D3 — Investment & Financial Advisory Reports:** D3 and F2 both produce client-facing financial documents. D3 tends to be research-grounded (market data, EM index performance, deal memos) and produces written reports rather than presentations. F2 is presentation-format and education-focused. If the primary output is a Word document or PDF report synthesizing market data, it is D3. If the primary output is a slide deck or structured presentation translating domain knowledge into client education, it is F2.

**D6 — Sales Pitch Decks & Capabilities Presentations:** D6 is also a client-facing presentation but is explicitly a sales or capabilities pitch (here is what our firm offers, here is why you should hire us). F2 is an educational presentation (here is how this financial instrument works, here is what you need to understand before deciding). The distinction is whether the presentation is selling a service/product relationship or educating the client on a topic relevant to their decision.
