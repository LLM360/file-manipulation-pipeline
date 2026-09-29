# Investment & Financial Advisory Reports

**Macro Category:** D — Strategic & Advisory Document Authoring
**Pattern ID:** D3

## 1. Pattern Description

The worker produces a client-facing or board-level document that analyzes investment opportunities, asset allocation views, market conditions, or financial planning strategies and presents findings to an external client or institutional audience. The cognitive core is applied financial expertise: selecting frameworks (GRAT vs. CRAT, ISO vs. NQSO, UW/N/OW positioning), modeling client-specific scenarios, and translating technical financial analysis into language appropriate for the target audience (retail investors, high-net-worth clients, institutional allocators, or C-suite). What distinguishes this pattern from internal financial modeling (Macro A) is that the output is advisory and audience-calibrated — it explains and recommends, not just calculates. What distinguishes it from general strategy proposals (D2) is the financial services domain and the client-facing framing.

## 2. O*NET Grounding

### Occupation Families
- 13-2052 Personal Financial Advisors — produces client education presentations on stock options, estate planning trusts, insurance products
- 13-2051 Financial Analysts — produces trading strategy memos, market commentary, M&A pitch materials, asset allocation tables
- 41-3031 Securities, Commodities, and Financial Services Sales Agents — produces investor-facing product summaries, fund one-pagers
- 11-3031 Portfolio Managers — produces quarterly asset class views, portfolio strategy reports
- 13-1111 Management Analysts — produces advisory presentations for institutional clients on market landscape and deal sourcing

### Key Work Activities (O*NET vocabulary)
- Advising Clients on Financial Matters
- Analyzing Financial Data or Market Conditions
- Preparing Presentation Materials and Reports
- Explaining Complex Financial Concepts to Non-Expert Audiences
- Evaluating Investment Opportunities and Risks
- Communicating with Persons Outside the Organization

### Knowledge Domains (O*NET vocabulary)
- Economics and Accounting
- Law and Government (for estate planning, regulatory compliance)
- English Language
- Mathematics
- Sales and Marketing (for client-facing positioning)
- Geography (for regional investment analysis)

### Generalizable Work Context
A financial professional (advisor, analyst, portfolio strategist, or sales director) at a wealth management firm, investment bank, asset manager, or fintech platform must produce a document for an external audience — a client meeting, a quarterly board review, a deal pitch, or a platform listing. The trigger is a scheduled client touchpoint, a market event requiring commentary, a client question about product alternatives, or a platform requirement for investor-facing documentation. The document must balance analytical rigor with audience accessibility — institutional clients and C-suite recipients expect data-grounded analysis; retail clients and HNW individuals expect plain-language explanation with worked examples.

## 3. Prompt Construction Template

### Persona Pattern
Assign a specific financial services role with clear institutional context: Managing Director at an investment bank (sector specialist), Financial Advisor at a regional bank serving HNW executives, Wealth Advisor (CFP®) at an RIA firm, Portfolio Strategist at a large asset manager, or Sales Director at a fintech fund platform. Include the organizational context that defines the client relationship — what kind of clients does this person serve, what is their mandate. Seniority should reflect who would plausibly produce this type of client-facing document.

### Scenario Pattern
Establish a concrete client need or business trigger: a client's stock options are vesting and they need to understand net-proceed differences; an institutional client is considering reducing EM exposure; a quarterly portfolio review is due; a new fund needs investor-facing marketing materials; an M&A advisory conversation needs to be initiated. Include the client profile when relevant — age, net worth, estate size, investment goals, risk tolerance. Specify whether the document is for an in-person meeting, a quarterly board package, a platform listing, or a one-time advisory request.

### Instruction Pattern
Specify the deliverable format (PDF, PowerPoint, Word), length constraint (pages or slides), and required content areas with explicit enumeration. For client education presentations: list the content topics that must be covered with hypothetical calculation examples. For strategy reports: specify named sections (executive summary, market overview, bond analysis, recommendations). For asset allocation tables: specify the column structure and required line items. For fund one-pagers: list the required sections by name. Make the required content areas explicit enough that a new analyst could produce a correctly structured document.

### Constraint Injection Points
- **Client-specific parameters:** age, marital status, asset values, tax filing status, estate size, years to vesting, financial goals
- **Year/regulatory context:** specific tax year values (a stated year's estate tax exemption or gift tax exclusion amount), IRS rate environment (an applicable trust-valuation rate), AMT implications
- **Page/slide limits:** 4-12 page reports, 5-slide pitch decks, 1-page fund summaries, 20+ slide advisory presentations
- **Data currency requirements:** data through a specific cutoff date (a stated quarter-end; an "as of" month and year; a named season and year)
- **Source constraints:** a named index-data provider's website for performance figures; major financial news publications for macro context; free/publicly available sources only; no paid data terminal
- **Column/table structure:** UW/N/OW positioning table with change indicators and conviction levels; required public comp metrics (EV/Revenue, EV/EBITDA, P/E)
- **Audience-appropriate language:** retail-investor accessible (not institutional); client comprehension as primary criterion; non-prescriptive framing for independent assessment

### Structural Template

```
[PERSONA]: You are a [ROLE] at [FIRM_TYPE] serving [CLIENT_SEGMENT]. [MANDATE_CONTEXT — sector coverage, AUM range, client relationship type].

[SCENARIO]: [TRIGGER_EVENT — client meeting, quarterly review, platform listing, deal initiation]. [CLIENT_PROFILE — age, net worth, goals, situation, relevant holding/portfolio details]. [BUSINESS_CONTEXT — why this document is needed now].

[DELIVERABLE]:
Produce a [FORMAT] ([PAGE/SLIDE_LIMIT]) for [AUDIENCE_TYPE] covering:
1. [SECTION_1 — overview or executive summary]
2. [SECTION_2 — product/strategy mechanics or market analysis]
3. [SECTION_3 — financial illustration or comparative analysis]
4. [SECTION_4 — risks, scenarios, or positioning rationale]
5. [SECTION_5 — recommendation or next steps]

[ANALYTICAL_REQUIREMENTS]:
- [FRAMEWORK — e.g., GRAT vs. CRAT comparison / UW-N-OW table / ISO vs. NQSO tax treatment]
- [CALCULATION_REQUIREMENT — step-by-step with hypothetical data / scenario modeling for client situation]
- [DATA_SOURCE — index-provider data from [URL] / free public sources / domain knowledge only]

[CONSTRAINTS]:
- [PAGE_LIMIT]
- [DATA_CUTOFF — information through [DATE] only]
- [YEAR_CONTEXT — use [YEAR] tax law values]
- [AUDIENCE_LANGUAGE — retail-investor accessible / institutional framing / client-comprehension primary]
- [FORMAT — PDF / PowerPoint / Word]

[REFERENCE_FILE if applicable]: [FILE_DESCRIPTION — IM to compress / prior quarter views document to update / research material to draw on].
```

## 4. Reference File Requirements

### File Types Needed
- **Investment Memorandum (PDF):** Full-length private placement or fund disclosure document containing fund structure, financial projections, token/unit economics, team profiles, and legal disclosures — source material for compression into one-pager
- **Prior quarter views document (PDF):** Existing asset allocation framework document containing categorized asset classes and prior positioning views — source material for updating to current quarter
- **Research material document (DOCX):** Compiled energy market data or sector research containing price data, supply/demand metrics, and issuer-level bond information — grounds the strategy memo
- **No reference file (pure knowledge):** The majority of client education presentations (ISO/NQSO, ILIT, GRAT/CRAT) require no reference files; all content derives from financial domain knowledge with inline client parameters

### Data Characteristics
Investment memoranda: fund name, target raise, IRR projections, token supply and pricing, distribution frequency, investment strategy narrative, team member bios. Asset allocation documents: hierarchical categorized asset classes with prior UW/N/OW positioning and supporting commentary. Research materials: tabular market data (price levels, supply/demand metrics) with dates; issuer-level bond characteristics (duration, credit quality, sector). Client parameters (inline): age, marital status, estate value, proceeds from liquidity event, tax filing status, years to option vesting, exercise price, FMV.

### File Complexity Spectrum
- **Minimal:** No reference files; all client parameters and regulatory context provided inline; pure financial domain knowledge required (ISO/NQSO tax mechanics, GRAT/CRAT mechanics, ILIT structure)
- **Moderate:** One reference file (prior quarter views PDF or research material DOCX) to update or draw on; document requires interpretation and selective incorporation rather than wholesale use
- **Complex:** Multiple sources required — reference file for content plus web research for current market data (index performance figures, financial-press macro commentary) within a specified date cutoff; document must synthesize across sources with clear attribution

## 5. Output Specification

### Primary Deliverable
- **Format:** PDF (most common for client-facing materials), PowerPoint (for in-person client presentations), Word (for strategy memos and reports)
- **Structure:** Named sections with clear headers; for presentations, slide-per-topic with bullet points, comparison tables, and worked numerical examples; for reports, narrative sections with embedded financial tables; for one-pagers, dense layout fitting all required content on a single page
- **Key quality signals:** Analytical framework is applied to the specific client situation, not described generically; calculations use actual client parameters; regulatory/tax values are accurate for the specified year; the document is calibrated to the intended audience (accessible to retail investor vs. sophisticated enough for institutional client); recommendation is clear and actionable

### Secondary Deliverables (if any)
- Excel data workbook accompanying a strategy memo (e.g., index return data and a correlation matrix)
- M&A pitch deck slides alongside a deal sourcing report

### Gold Output Characteristics
A gold output demonstrates the analytical framework with the actual client parameters — a side-by-side GRAT vs. CRAT comparison uses the client's actual age, sale or liquidity-event proceeds, estate tax context, and philanthropic goals, not generic examples. Tax values are year-specific and accurate. Client education presentations include step-by-step worked calculations with clearly labeled hypothetical numbers. Asset allocation views tables show genuine position changes (not all "N/no change") with one-sentence rationales that reference the specific macro context stated in the prompt. One-pagers achieve all required sections within the page constraint without truncating any required content area. The recommendation is explicitly stated and connected to the client's stated goals.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Analytical depth | Single-product explanation (ISO mechanics) | Side-by-side comparison of two structures | Multi-dimensional comparison (mechanics + tax + scenarios + recommendation) across complex trust or investment structures |
| Client-specificity | Generic educational presentation with hypothetical client | Named client profile with specific parameters (age, assets, goals) | Named client with multi-goal profile (estate reduction + charitable intent + income stream) requiring scenario modeling |
| Data sourcing | Pure domain knowledge; no external data | One reference file (IM or prior views) to draw on | Multiple sources: reference file + web research (an index data provider, financial press) with date cutoff |
| Regulatory/tax complexity | Product mechanics only | One regulatory framework (gift tax exclusion, capital gains treatment) | Multiple regulatory layers (estate tax + gift tax + AMT + an IRS trust-valuation rate + state law) |
| Document length | 1 page (fund one-pager or single slide) | 5–12 pages/slides | Long-form comprehensive advisory presentation (20+ slides) |
| Audience calibration | Single audience (retail investor or HNW client) | Dual register (institutional + accessible) | Multi-stakeholder (institutional clients + internal MDs + deal counterparties) |

## 7. Boundary Cases & Adjacent Patterns

- **vs. D2 (Corporate Strategy Proposals):** D2 documents advise an organization's own leadership on what the organization should do (internal strategic decisions); D3 documents advise clients on what to do with their capital or financial planning (external advisory relationship). If the audience is a client and the subject is investments, estate planning, or market positioning, it is D3.
- **vs. A3 (NPV/IRR & Investment Evaluation):** A3 produces quantitative financial models in Excel (the model IS the deliverable); D3 produces advisory documents where the analysis supports a written recommendation (the narrative IS the deliverable). If the output is an Excel workbook with calculation tabs, it is A3. If the output is a PDF or Word report with embedded numbers, it is D3.
- **vs. C4 (Training Materials):** D3 client education presentations (ISO/NQSO, ILIT) could superficially resemble training materials, but the distinction is audience: D3 presentations are for an external client in an advisory relationship; C4 training materials are for internal staff, advisors, or trainees in an educational context. If the audience is a client making financial decisions, it is D3.
- **vs. D6 (Sales Pitch Decks):** D6 pitch decks sell the capabilities of a service provider; D3 documents advise on investment or financial planning. If the document is about what the firm can do for the client (agency capabilities), it is D6. If it is about what the client should do with their money, it is D3.
- **Choose D3 when:** The document is addressed to an external client or institutional investor; the content is financial analysis, market commentary, or financial planning; the goal is to advise or inform a capital allocation or planning decision; audience calibration (accessible language, scenario illustrations) is a primary design requirement.
