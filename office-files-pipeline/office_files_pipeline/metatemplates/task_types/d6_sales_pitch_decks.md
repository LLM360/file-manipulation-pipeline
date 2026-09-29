# Sales Pitch Decks & Capabilities Presentations

**Macro Category:** D — Strategic & Advisory Document Authoring
**Pattern ID:** D6

## 1. Pattern Description

The worker creates a polished, client-facing sales or capabilities presentation designed for use in external sales meetings or on marketing platforms, structured slide-by-slide or section-by-section from provided source documentation. The cognitive core is information architecture and persuasive framing: taking detailed service, product, or operational documentation and reorganizing it into a compelling, audience-calibrated narrative for C-suite or decision-maker audiences. What distinguishes this pattern from advisory presentations (D3) is that the document sells the capabilities of the producing organization to prospective clients — the subject is "what we can do for you," not "what you should do with your capital." What distinguishes it from training materials (C4) is the external sales orientation: D6 decks are for prospect or client-facing contexts, not internal education. Reference files providing service documentation or CEO briefs are required; the worker must transform source material (not merely transcribe it) into a coherent, persuasive sales narrative.

## 2. O*NET Grounding

### Occupation Families
- 11-2022 Sales Managers — produces capabilities presentations for agency sales engagements with brand clients
- 11-2011 Advertising and Promotions Managers — structures marketing agency service offerings into client-facing pitch materials
- 11-2021 Marketing Managers — develops sales operations process documents and investor-facing pitch frameworks for growth functions
- 13-1111 Management Analysts — produces comprehensive business process framework documents used in a sales or growth context

### Key Work Activities (O*NET vocabulary)
- Preparing Sales Presentations
- Communicating with Prospective Clients
- Developing Marketing Materials
- Developing Objectives and Strategies
- Documenting Information
- Analyzing Business Operations (to translate operational detail into persuasive messaging)

### Knowledge Domains (O*NET vocabulary)
- Sales and Marketing
- Communications and Media
- Computers and Electronics (for digital marketing or fintech platform context)
- Administration and Management
- Economics and Accounting (for fintech or alternative investment context)
- English Language

### Generalizable Work Context
A sales manager, VP of Sales, or business development lead at a service firm, agency, or fintech startup is tasked with producing a client-facing presentation or comprehensive sales process document ahead of a new business push. The trigger is a new client segment being targeted, a platform listing requirement, or the formalization of a previously informal sales process. The audience is C-suite buyers (CEOs, founders, brand leads) or institutional issuers who need to assess the firm's capabilities quickly. Source documentation exists internally (service descriptions, CEO brief, capability lists) and must be transformed into a professionally structured, audience-calibrated deliverable. Visual design quality, consistent formatting, and concise language are key constraints alongside content completeness.

## 3. Prompt Construction Template

### Persona Pattern
Assign a senior sales or growth role at a service-oriented company or startup: Sales Manager at a marketing agency, VP of Sales & Growth at a fintech marketplace, or equivalent business development lead. Include the company context — what the company does, who it serves, and what the sales motion looks like (client pitches for agency services; platform listings for fund products; structured sales operations for a new growth function). The persona should be credible as someone who would produce this type of document in this organizational context.

### Scenario Pattern
Establish the business trigger for the document: the agency needs a deck to pitch brand clients at meetings; the fintech startup needs to formalize its sales operation as the company scales; a new client segment is being targeted that requires a new presentation. Name the target audience explicitly (CEOs, founders, brand leads; asset issuers and retail investors; institutional clients). Specify how the document will be used (sales meetings, platform listing, internal rollout). Reference the attached source documentation that grounds the content (services documentation, CEO brief, publicly available industry best practices).

### Instruction Pattern
Specify the deliverable format (PDF, Word), page/slide count range, and the complete required structural framework — section by section. For slide decks: specify per-slide structure (title, summary sentence(s), bulleted capabilities, visual type). For comprehensive process documents: specify the numbered sections and sub-components, including two visual flowcharts. Name the required content areas explicitly enough that a new analyst can fill in the structure without content decisions beyond editorial judgment. Specify visual and tone constraints (premium yet approachable; consistent formatting; open-source images; C-suite language).

### Constraint Injection Points
- **Slide/page count:** a specified slide-count target for an agency capabilities deck; a specified page limit for a comprehensive sales operations document
- **Per-unit structure:** each slide contains title + 1–2 sentence summary + bulleted capabilities + visuals; each document section follows a fixed set of mandatory sub-components
- **Content source alignment:** content must align exactly with the attached reference document; no invented capabilities; coverage of all service categories in the source
- **Visual requirements:** open-source images only; dashboards, product images, and icons appropriate to service category; two embedded flowcharts (one per customer type) in process documents
- **Tone and design consistency:** premium yet approachable; C-suite accessible language; consistent formatting across all slides/sections
- **Dual audience segmentation:** separate process tracks for asset issuers vs. retail investors; separate service framing across two distinct platform or channel contexts
- **Regulatory compliance inclusion:** fintech/securities regulatory requirements must be addressed within the sales process framework

### Structural Template

```
[PERSONA]: You are a [ROLE] at [COMPANY_NAME], a [COMPANY_TYPE] serving [TARGET_CLIENT_SEGMENT]. [COMPANY_CONTEXT — what products/services offered, business model, recent growth stage].

[SCENARIO]: [BUSINESS_TRIGGER — new client segment / platform listing / scaling sales function]. [AUDIENCE — who will receive and evaluate this document: CEOs/founders/brand leads / institutional issuers / retail investors]. [USE_CONTEXT — sales meetings / online platform / internal rollout].

[DELIVERABLE]:
Produce a [FORMAT] ([SLIDE/PAGE_COUNT_RANGE]) organized as follows:

[SECTION_STRUCTURE]:
- [INTRO_SECTION]: [Overview / company positioning]
- [SERVICE/PROCESS_SECTION_1]: [Service category or process section name] — [content spec]
- [SERVICE/PROCESS_SECTION_2]: [Second service category or section] — [content spec]
- ...
- [CLOSING_SECTION]: [CTA / next steps / contact information]

[PER-UNIT REQUIREMENTS]:
Each [slide/section] must include:
- [ELEMENT_1 — title]
- [ELEMENT_2 — 1–2 sentence summary / overview paragraph]
- [ELEMENT_3 — bulleted capabilities or sub-components]
- [ELEMENT_4 — visual or flowchart requirement]

[CONTENT_CONSTRAINTS]:
- All content must align with attached [REFERENCE_FILE_DESCRIPTION]
- [ADDITIONAL_COVERAGE_REQUIREMENTS — all service categories / both customer types / regulatory compliance]
- [VISUAL_CONSTRAINT — open-source images / brand colors / icons]

[TONE_AND_FORMAT]:
- [TONE — premium yet approachable / professional / institutional]
- [FORMAT_CONSISTENCY — consistent slide formatting / naming conventions]
- [AUDIENCE_LANGUAGE — C-suite accessible / retail-investor friendly / institutional]

[OUTPUT]:
- Format: [PDF / Word]
- File output: [named or generic]
```

## 4. Reference File Requirements

### File Types Needed
- **Services documentation (DOCX):** Detailed descriptions of the organization's service offerings — each service category with description, deliverables, and capability list; serves as the content source for all slide or section copy in the capabilities deck
- **CEO or executive brief (PDF):** Strategic context document from leadership describing the company's business model, target customers, sales and growth mandate, and high-level priorities; grounds the sales operations process document and determines scope
- **Industry best practices (web research):** Publicly available information about sales operations methodology, fintech regulatory requirements, or process frameworks that supplements the CEO brief

### Data Characteristics
Services documentation: service category names, one-paragraph descriptions per service, bulleted capability or deliverable lists per category, platform or technology context (e.g., e-commerce marketplace account management, social-commerce storefront setup, paid advertising strategy, analytics). CEO briefs: company business model description (two-sided marketplace, agency model), target customer segments with named examples, department mandate, strategic growth priorities, existing or aspirational revenue metrics (AUM, ARR, retention). For process documents: sales funnel stages (lead generation, qualification, conversion, onboarding, retention), stakeholder roles (SDR, AE, CS, compliance), KPIs, risk factors, regulatory compliance requirements (KYC/AML, accredited investor rules).

### File Complexity Spectrum
- **Minimal:** Single services documentation file (DOCX) with well-organized service descriptions; capabilities deck produced primarily from straightforward extraction and reformatting of existing content
- **Moderate:** CEO brief (PDF) requiring interpretation and editorial expansion to produce a comprehensive process document; web research to supplement with industry best practices
- **Complex:** CEO brief + web research for regulatory/compliance context + industry process standards; a comprehensive, page-limited document with numerous numbered sections, a fixed set of mandatory sub-components per section, and two embedded visual flowcharts for distinct customer segments

## 5. Output Specification

### Primary Deliverable
- **Format:** PDF (for agency capabilities decks and investor-facing materials) or Word (.docx) (for comprehensive sales process documents)
- **Structure:** For decks: title/intro slide(s), one slide per service category or topic, closing/CTA slide — each slide with consistent layout (title, summary, capabilities bullets, visual); for process documents: a numbered multi-section structure with consistent sub-components, embedded flowcharts with textual breakdowns
- **Key quality signals:** All service categories from the reference document are represented with no gaps; per-slide or per-section structure is consistently applied; content reads as polished and persuasive to the named audience type (C-suite language, institutional framing, or retail-accessible); visual elements are appropriate to the service category; the document could be handed to a salesperson for immediate use in a client meeting

### Secondary Deliverables (if any)
- None typical; all content is in the single primary document

### Gold Output Characteristics
A gold output achieves complete coverage of all service categories or process sections from the reference document, with no categories missing or compressed into a single generic slide. Each unit (slide/section) has a genuinely useful title, a crisp summary sentence or paragraph that captures the value proposition, and a bulleted list that is specific to that service/process rather than generic agency language. For decks: visual descriptions are specific enough that a designer could implement them (not just "image here"). For process documents: the dual-audience structure (asset issuers vs. retail investors) is maintained consistently, flowcharts have logical step sequences with named decision points, and sub-components per section are all substantively populated. Tone is consistent throughout — no slides in formal register followed by slides in casual register. Page/slide limits are respected.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Slide/page count | 5–8 slides (short capabilities overview) | 12–20 slides (full agency capabilities deck) | 20–25 pages (comprehensive sales operations process document) |
| Service/section complexity | 3–4 service categories to cover | 6–8 service categories with distinct framing | Many numbered sections, each with a fixed set of mandatory sub-components |
| Reference file complexity | Well-organized single DOCX services document | CEO brief requiring interpretation and editorial expansion | CEO brief + web research for regulatory requirements + industry best practices |
| Audience segmentation | Single audience type | Two target customer types (e.g., buyers and sellers, or two distinct platform/channel contexts) | Two fully distinct process tracks with separate flowcharts, risk factors, and compliance requirements |
| Visual requirement | No specific visual requirement | Open-source images appropriate to service category per slide | Two embedded process flowcharts (one per customer type) with textual breakdowns within a page-limited document |
| Regulatory/compliance layer | No regulatory content required | One platform or sector compliance note | Full regulatory compliance section covering fintech securities law (accredited investor rules, KYC/AML) within the sales process |

## 7. Boundary Cases & Adjacent Patterns

- **vs. D3 (Investment & Financial Advisory Reports):** D3 documents advise clients on what to do with their capital; D6 documents sell what the firm can do for clients. If a document from a fund firm describes the firm's investment process and past performance to attract new investors, it is at the boundary. Rule: if the document is fundamentally about the client's financial decisions, it is D3; if it is fundamentally about the firm's capabilities and service offering, it is D6.
- **vs. B1 (Performance Analysis Presentation):** B1 presentations analyze data from reference files and report performance findings; D6 decks transform service documentation into a sales narrative. If the primary analytical work is analyzing data and producing charts and tables, it is B1. If the primary work is information architecture and persuasive reframing of existing documentation, it is D6.
- **vs. C4 (Training Materials):** C4 materials educate internal staff or client-facing staff on products, processes, or knowledge domains; D6 decks sell the firm's capabilities to external prospective clients. If the audience is internal advisors or employees being trained, it is C4. If the audience is prospective clients being pitched, it is D6.
- **vs. D2 (Corporate Strategy Proposals):** D2 documents advocate for an internal organizational decision; D6 documents sell the organization's capabilities to external buyers. If the document is addressed to the organization's own leadership, it is D2. If it is addressed to external clients or platform audiences, it is D6.
- **Choose D6 when:** The deliverable is used in external sales or business development contexts; the subject is the producing organization's capabilities, services, or operational process; reference files are internal service/product documentation or executive briefs rather than market data or client financial information; the output will be handed to a salesperson for use with prospective clients.
