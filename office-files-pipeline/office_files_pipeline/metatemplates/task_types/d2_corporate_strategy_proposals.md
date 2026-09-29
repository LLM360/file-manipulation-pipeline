# Corporate Strategy & Business Proposals

**Macro Category:** D — Strategic & Advisory Document Authoring
**Pattern ID:** D2

## 1. Pattern Description

The worker produces a persuasive strategic document — a proposal, memo, strategy presentation, or one-pager — that advocates for a specific course of action in a business context. The cognitive core is combining situational analysis (market reality, operational pain points, or competitive dynamics) with structured recommendation frameworks (BATNA/ZOPA, phased roadmaps, differentiated investment strategies) to produce a document that moves decision-makers to act. What distinguishes this pattern from pure financial analysis is that the deliverable argues for a position and is framed for a named stakeholder audience (CPO, CEO, Board, leadership team); the analytical content supports the argument rather than being the end in itself. Reference files, when present, are operational process documents or quotation/issue logs that ground the proposal; often no files are provided and the worker draws on domain knowledge and inline parameters.

## 2. O*NET Grounding

### Occupation Families
- 11-3061 Purchasing Managers — produces sourcing workflow proposals, supplier negotiation strategies, partnership proposals
- 11-2021 Marketing Managers — produces channel strategy presentations and executive one-pagers for brand leadership
- 13-1111 Management Analysts — produces business improvement proposals and process change recommendations
- 11-2022 Sales Managers — produces ERP process change proposals and key account strategy documents
- 19-3099.01 Transportation Planners — produces competitive strategy presentations for ride-hailing and mobility sectors
- 11-9141 Property, Real Estate, and Community Association Managers — produces strategic investment recommendations for distribution channels

### Key Work Activities (O*NET vocabulary)
- Developing Objectives and Strategies
- Analyzing Operations and Identifying Improvement Opportunities
- Communicating with Supervisors, Peers, and Subordinates
- Documenting Information
- Negotiating with Suppliers or Partners
- Preparing Presentation Materials for Leadership

### Knowledge Domains (O*NET vocabulary)
- Administration and Management
- Sales and Marketing
- Production and Processing
- Economics and Accounting
- English Language
- Transportation (for mobility/logistics subtypes)

### Generalizable Work Context
A senior functional manager or strategy lead at a mid-to-large organization faces a business decision that requires executive buy-in — a supplier partnership, a market entry strategy, a negotiation approach, a channel investment plan, or a system/process redesign. The trigger is typically a crisis (supplier halt, competitive threat), a leadership mandate (CPO direction, CEO brief), or an optimization opportunity (reporting gap, ROI improvement). The document is the vehicle for influencing the decision; it must be persuasive, clearly structured, and calibrated to a named senior audience.

## 3. Prompt Construction Template

### Persona Pattern
Assign a senior functional role (Senior Manager, Director, Head of Strategy, Sales Manager) within a specific organization type (e.g., a manufacturer, a platform business, or a consumer brand). Include the organizational context that explains why this person's recommendation matters and who has decision authority above them (CPO, CEO, incoming leadership). The persona should be domain-credible — someone who would plausibly produce this type of document in this industry.

### Scenario Pattern
Establish a concrete business trigger: a supplier crisis requiring immediate resolution, a new CEO needing a market briefing, a leadership mandate to propose process improvements, or a recurring business challenge (low ROI channels, reporting gaps) demanding a strategic fix. Name the stakeholder audience explicitly. Include relevant background data inline — cost parameters, timeline constraints, market data, or pain points from an attached reference document. The scenario should create genuine analytical work: the situation is not simple and the proposed approach requires judgment, not just template-filling.

### Instruction Pattern
Specify the deliverable type (Word document, PowerPoint presentation, single slide), length constraint (pages, slides), and required structural elements. For proposals: include rationale, framework sections (BATNA, roadmap, partnership structure), and named analytical components. For presentations: specify slide count and strategic areas to cover. For one-pagers: specify exactly what must appear in the limited space. Explicitly name the audience and purpose (executive approval, CEO briefing, leadership meeting pitch).

### Constraint Injection Points
- **Document length:** 2–3 pages (detailed proposals), 5–6 slides (strategy decks), 1 slide/page (executive one-pagers)
- **Framework requirements:** BATNA/ZOPA analysis, phased roadmap with regulatory milestones, differentiated channel strategy, modular cost/pricing structure
- **Financial parameters:** cost savings calculations with specified rates/volumes/currencies, cap rate conversions, specific partnership ownership splits
- **Audience specificity:** named individuals (CPO, incoming regional CEO, regional strategy lead, brand leadership team)
- **Data sourcing constraints:** publicly available data only, specific named industry or regulatory sources, specified date cutoffs
- **Reference file content:** must incorporate terms from attached document; must address pain points enumerated in reference
- **Regulatory/compliance alignment:** named regulatory frameworks (e.g., government localization or industrial-policy programs) must be addressed

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_NAME], a [ORG_TYPE]. [DOMAIN_CONTEXT — product/market/functional area you own].

[SCENARIO]: [TRIGGER_EVENT — crisis / leadership mandate / strategic opportunity]. [STAKEHOLDER_CONTEXT — who has decision authority, who is the audience]. [BACKGROUND_PARAMETERS — cost data, timeline, competitive context, pain points — may be inline or from attached reference].

[DELIVERABLE]:
Produce a [FORMAT] ([LENGTH_CONSTRAINT]) for [NAMED_AUDIENCE] covering:
1. [SECTION_1 — situation analysis or partnership structure]
2. [SECTION_2 — framework application or roadmap]
3. [SECTION_3 — financial analysis or cost model]
4. [SECTION_4 — risks and mitigation or negotiation levers]
5. [SECTION_5 — next steps or recommendation]

[CONSTRAINTS]:
- [FINANCIAL_PARAMETER_1 — e.g., a currency conversion rate, volume, cost per unit]
- [FINANCIAL_PARAMETER_2]
- [AUDIENCE_CALIBRATION — executive clarity + technical blueprint / CEO-level pitch / brief elevator-pitch format]
- [REGULATORY_CONSTRAINT if applicable]

[REFERENCE_FILES if applicable]: [ATTACHED_DOC_DESCRIPTION — operational pain points / existing order types / compensation model ideas / market data].
```

## 4. Reference File Requirements

### File Types Needed
- **Operational process document (DOCX):** Enumerates existing system configurations (e.g., ERP order types), use cases, and documented pain points — serves as the problem statement grounding the proposal
- **Quotation or cost document (DOCX/XLSX):** Contains supplier quotes, cost structures, or pricing data to be incorporated into financial calculations in the proposal
- **Issue or challenge log (DOCX):** Lists specific operational failure modes or challenges that the proposal must address
- **Compensation or terms document (DOCX):** Contains existing or draft terms to be synthesized into a formal compensation or partnership framework

### Data Characteristics
Documents should contain a mix of qualitative problem descriptions and quantitative parameters. Operational documents: named categories (e.g., order or transaction types), their descriptions, and pain points stated in natural language. Financial documents: unit costs, volumes, conversion rates, split percentages, phased timelines. Issue logs: numbered or bulleted failure modes with observable business impact (chargebacks, delays, reporting errors). Reference file data should be specific enough to require selective synthesis rather than wholesale copying.

### File Complexity Spectrum
- **Minimal:** No reference files — all parameters provided inline in the prompt (cost data, timeline, volume, regulatory framework details)
- **Moderate:** One reference file containing qualitative problem description or draft terms to incorporate; one additional inline data set (e.g., cost parameters)
- **Complex:** Two reference files (problem description + cost/quotation data) requiring cross-referencing; plus inline regulatory or market context; web research for market data with named sources and date cutoff

## 5. Output Specification

### Primary Deliverable
- **Format:** Word document (.docx), PDF, or PowerPoint (.pptx) depending on variant
- **Structure:** Named sections with clear headers; for proposals: narrative paragraphs with embedded data tables or bullet lists; for presentations: slide-per-topic structure with bullet points and supporting data callouts; for one-pagers: dense layout with maximum information per unit of space
- **Key quality signals:** A specific recommendation is made and defended, not just options presented; financial calculations are explicit and traceable; framework sections (BATNA, roadmap, channel strategy) are applied to the specific situation, not described generically; the document reads as persuasive to the named audience

### Secondary Deliverables (if any)
- None typical for this pattern; occasionally a supporting data appendix or separate exhibit for financial calculations

### Gold Output Characteristics
A gold output stakes a clear position in the first section (or executive summary) and structures the rest of the document to support that position. Financial calculations are shown with explicit assumptions (conversion rate, volume, unit cost) so the reader can verify them. Framework sections (BATNA, ZOPA, phased roadmap) are applied to the specific situation, using the actual named parties, timelines, and constraints from the scenario — not described in general terms. Risks are named, not listed generically. The recommendation section gives actionable next steps with owners or timeframes where possible. Page limits and audience calibration are respected throughout.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Financial calculation burden | No calculations required (qualitative strategy) | One financial calculation (cost savings, cap rate conversion) | Multiple financial calculations with unit conversions, volumes, phased timelines, and currency conversions |
| Framework requirement | Simple recommendation memo | One named framework (BATNA or phased roadmap) | Multiple frameworks in combination (BATNA + ZOPA + transition timeline + tooling leverage) |
| Reference file synthesis | No reference files; all parameters inline | One reference file to synthesize into proposal | Two reference files of different types plus inline parameters |
| Audience specificity | Generic executive audience | Named executive (CPO, CEO) with defined needs | Multiple named stakeholders (incoming CEO + regional head; or CPO + IT platform team) with different reading purposes |
| Research requirement | No research; domain knowledge only | Inline market parameters provided | Web research required from named public sources with data recency constraints |
| Document length and format | Single slide or 1-page one-pager | 2–3 page Word document | 5–6 slide presentation or 2–3 page proposal with supporting financial exhibits |

## 7. Boundary Cases & Adjacent Patterns

- **vs. D3 (Investment & Financial Advisory Reports):** D2 proposals are internally focused (advising the organization's own leadership on what the organization should do); D3 reports are externally focused (advising clients on what they should do with their capital). If the document is addressed to a client and involves portfolio or estate recommendations, it is D3. If it is addressed to internal leadership and advocates for a business strategy, it is D2.
- **vs. D1 (Technical Design Documents):** D2 covers business/commercial strategy; D1 covers technical system design. If the document is making choices about system architecture, APIs, or code standards, it is D1. If it is making choices about supplier partnerships, market strategy, or channel investment, it is D2.
- **vs. C1 (Standard Operating Procedure):** If the document defines how a process should be executed operationally with steps, responsibilities, and timelines, it is C1. If it argues for why a new process should be adopted (proposal with rationale), it is D2. The distinction is prescriptive (C1) vs. persuasive (D2).
- **Choose D2 when:** The document is intended to persuade a decision-maker; a specific recommendation or course of action is advocated; the audience is named leadership or executive; the analytical work supports an argument rather than being the deliverable itself.
