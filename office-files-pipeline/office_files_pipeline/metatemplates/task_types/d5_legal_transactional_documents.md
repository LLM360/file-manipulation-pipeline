# Legal & Transactional Documents

**Macro Category:** D — Strategic & Advisory Document Authoring
**Pattern ID:** D5

## 1. Pattern Description

The worker drafts a formal legal or quasi-legal document — a will, letter of intent, compensation framework, or inter-organizational contract — that must follow specific legal conventions, reference jurisdiction-specific requirements, and use precise legal terminology. The cognitive core is applied legal drafting: translating a set of specified parties, terms, and requirements into a legally coherent document with the correct structure, provisions, and execution formalities. What distinguishes this pattern from SOPs or program plans is the legal formality of the output — documents in this pattern would be signed by parties, potentially reviewed by attorneys, and may be legally binding or near-binding. What distinguishes it from narrative advisory documents (D2, D3) is that the deliverable IS the legal instrument, not a recommendation or analysis about it. Reference files, when present, are structural outlines, boilerplate legal language, or source documents containing terms to be incorporated.

## 2. O*NET Grounding

### Occupation Families
- 23-1011 Lawyers — drafts wills, LOIs, legal memos, and contracts from scratch; applies jurisdiction-specific law
- 23-2011 Paralegals and Legal Assistants — drafts routine legal documents under attorney supervision
- 41-9021 Real Estate Brokers — drafts letters of intent and transaction documents for commercial real estate acquisitions
- 11-3111 Compensation and Benefits Managers — drafts compensation framework documents for multi-state brokerage operations
- 11-9151 Community Service Managers — drafts inter-organizational agreements for government or nonprofit program partnerships

### Key Work Activities (O*NET vocabulary)
- Drafting Legal Documents
- Analyzing Data or Information (for financial terms, cap rate calculations)
- Interpreting Legal Requirements and Applying to Specific Situations
- Communicating with Persons Outside the Organization (parties, brokers, signatories)
- Documenting Information
- Making Decisions and Solving Problems

### Knowledge Domains (O*NET vocabulary)
- Law and Government
- Economics and Accounting (for financial calculations embedded in legal documents)
- English Language
- Customer and Personal Service
- Administration and Management
- Sales and Marketing (for brokerage compensation structures)

### Generalizable Work Context
An attorney, paralegal, real estate broker, or senior manager at an organization that manages legally formalized relationships is tasked with producing a legal document from scratch or from a provided structural outline. The trigger is a client request (estate planning engagement), a transaction requiring documentation (commercial real estate acquisition), a new organizational structure needing a framework document (multi-state brokerage launch), or a partnership requiring formal contractual definition (inter-organizational program agreement). The document will be reviewed by counterparties, executed by named signatories, or submitted to a city attorney before signature. In some cases (wills, LOIs) no reference files exist and all terms come inline; in others (inter-organizational agreements) multiple reference files provide the structural outline, boilerplate language, and factual content to be incorporated.

## 3. Prompt Construction Template

### Persona Pattern
Assign a specific legal or quasi-legal practitioner role: Attorney or Paralegal at an estate planning firm, Real Estate Broker at a commercial brokerage, Qualifying Broker managing multi-state brokerage compliance, Director of Parks and Recreation drafting an inter-governmental program agreement. Include the organizational context that explains the relationship (attorney-client, broker-counterparty, government-university) and the jurisdiction where the document will be executed (e.g., a single state for an estate matter, a specific metro market for a real estate transaction, a multi-state licensing footprint, a state for a government partnership). The persona should be credible for drafting this type of document in this jurisdiction.

### Scenario Pattern
Establish the concrete transaction or legal need: a client needs a comprehensive will drafted for a specific estate plan; a buyer needs an LOI for a commercial real estate acquisition; a new brokerage firm needs a compensation framework for qualifying brokers; two organizations need a formal agreement to operate a joint program. Name all parties explicitly with full legal names or entity names. Specify all terms that must appear: financial figures (purchase price, cap rate, deposits, percentage splits, FTE targets), timelines (feasibility periods, closing windows, program durations, vesting ages), conditions (1031 exchange, renewal options, spendthrift provisions), and execution details (date, jurisdiction, signatories, witnesses, notary requirements). Provide enough terms inline that the document can be drafted without requiring the worker to invent terms.

### Instruction Pattern
Specify the output format (PDF, Word document), approximate length (page range or page limit), and the complete list of required provisions or sections. For wills: all major provision categories (executor, beneficiaries, testamentary trust, spendthrift, fiduciary powers, survivorship, residuary, execution block). For LOIs: all standard business terms (price, deposits, feasibility period, closing timeline, escrow, PSA drafting rights, cost allocation). For compensation frameworks: named sections (Purpose, Commission Split Structure, Summary) with multi-tier stakeholder coverage. For inter-organizational agreements: articles and subsections per the attached outline, incorporated boilerplate language, and exhibits.

### Constraint Injection Points
- **Named parties with full legal identifiers:** full legal names (individuals), entity names, addresses, state of jurisdiction, relationship designations (executor, trustee, beneficiary, qualifying broker, signatory)
- **Specific financial terms:** purchase price from cap rate calculation (a stated cap rate applied to stated NOI), deposit amounts, percentage splits, FTE reduction percentages, cost parameters
- **Timeline parameters:** feasibility period, closing window, extension options, trust duration (maximum 21 years), minimum distribution age (a specified milestone age), program term (a stated duration with renewal options)
- **Jurisdiction-specific compliance:** state probate/estates code requirements (e.g., will execution formalities such as witnesses and notarization); local market conventions for closing cost allocation; state real estate licensing requirements across a multi-state brokerage footprint; state public entity laws for government agreements
- **Document length:** 8–11 pages (comprehensive will), maximum 5 pages (LOI), 1 page (compensation framework), multi-article agreement of unspecified length
- **Execution formalities:** execution date, two named witnesses, notary block, signature lines for all signatories
- **Style/format conventions:** professional section headings; non-binding LOI conventions (vs. PSA depth); Word document vs. PDF final output

### Structural Template

```
[PERSONA]: You are a [ROLE] at [FIRM_TYPE] in [JURISDICTION]. [ORGANIZATIONAL_CONTEXT — new firm, no templates; established brokerage; city department].

[SCENARIO]: [LEGAL_TRIGGER — client estate planning request / acquisition transaction / new brokerage launch / inter-organizational program]. [PARTIES — full legal names/entity names for all required parties]. [RELATIONSHIP — executor/testator, buyer/seller, qualifying broker/agent, city/university].

[DELIVERABLE]:
Draft a [DOCUMENT_TYPE] in [FORMAT] ([PAGE_RANGE_OR_LIMIT]) covering all of the following:
1. [REQUIRED_PROVISION_1 — executor designation / purchase price and cap rate / purpose section]
2. [REQUIRED_PROVISION_2 — beneficiary structure / deposit schedule / commission split structure]
3. [REQUIRED_PROVISION_3 — testamentary trust terms / feasibility and closing timeline / summary section]
4. [REQUIRED_PROVISION_4 — fiduciary powers / escrow and title / exhibit incorporation]
...

[FINANCIAL_TERMS]:
- [CALCULATION_REQUIRED — cap rate → price conversion; FTE percentage; split percentages]
- [SPECIFIC_DOLLAR_AMOUNTS — deposit amounts, purchase price range, cost per unit]

[TIMELINE_TERMS]:
- [TIMELINE_1 — feasibility period duration]
- [TIMELINE_2 — closing window, extension option]
- [TIMELINE_3 — program term, renewal options]

[JURISDICTION_AND_EXECUTION]:
- Jurisdiction: [STATE/CITY]
- Execution date: [DATE]
- Witnesses: [NAMED_WITNESSES or "two witnesses required"]
- Notary: [REQUIRED/NOT_REQUIRED]
- Output format: [FORMAT]

[REFERENCE_FILES if applicable]:
- [FILE_1 — contract outline with articles and subsections]
- [FILE_2 — official boilerplate legal language for Miscellaneous section]
- [FILE_3 — compensation model ideas to incorporate]
```

## 4. Reference File Requirements

### File Types Needed
- **Contract structural outline (DOCX):** Articles and subsections, contact information for named parties at both organizations, exhibit identifiers, and equipment liability language — provides the scaffolding the agreement must follow
- **Boilerplate legal language document (DOCX):** Standard city or institutional contract language for a specific section (Miscellaneous) — must be incorporated into the agreement
- **Compensation model ideas document (DOCX):** Narrative or structured document containing compensation terms, split structures, and stakeholder tier definitions — source material for drafting a formal compensation framework
- **No reference file (pure knowledge):** Wills and LOIs in this pattern are commonly drafted from inline-specified terms alone, requiring deep jurisdiction-specific legal knowledge

### Data Characteristics
For wills: party names (testator, spouse, children, alternate beneficiaries, trustees, guardians, witnesses), city and state, trust parameters (minimum distribution age, maximum duration), execution date, spendthrift provision, survivorship period, residuary distribution structure. For LOIs: NOI value (to calculate purchase price from cap rate), cap rate, deposit schedule (amounts and timing), feasibility period, closing window, extension terms, escrow and title company, PSA drafting rights, 1031 exchange designation, cost allocation conventions. For compensation frameworks: tier structure (Qualifying Broker, Agent, Associate Broker), split percentages, purpose language. For inter-organizational agreements: space descriptions, scheduling minimums, staff responsibilities, funding structure, mutual indemnification language, signatory names and titles for both organizations.

### File Complexity Spectrum
- **Minimal:** No reference files; all terms specified inline; requires jurisdiction-specific legal knowledge to structure correctly (will, LOI drafted from client parameters alone)
- **Moderate:** One reference file containing source terms to incorporate (compensation model ideas); primarily a drafting and synthesis task with light structural decisions
- **Complex:** Three reference files of different types (contract outline + boilerplate language + facility description), each contributing a distinct structural or content layer; must integrate all three into a single coherent formal agreement ready for attorney review

## 5. Output Specification

### Primary Deliverable
- **Format:** PDF (wills, one-page compensation frameworks) or Word document (.docx) (LOIs, inter-organizational agreements)
- **Structure:** Formal section headings or numbered articles; legal recitals or preambles where appropriate; specific provision language for each required term; execution block with signature lines, witness lines, and notary block where required
- **Key quality signals:** All named parties appear correctly in the right sections; financial terms are accurate (cap rate calculation verifiable); jurisdiction-specific requirements are met (state-specific will execution formalities such as witnesses and notarization; LOI includes non-binding disclaimer; inter-organizational agreement includes mutual indemnification and self-insurance language); document length is within the specified range; no required provision is omitted

### Secondary Deliverables (if any)
- None typical; all content is in the single primary legal document

### Gold Output Characteristics
A gold output is structurally complete — every required provision or article is present, named parties appear in the correct provisions, and no required section is missing. Financial calculations are correct and transparent: if a cap rate and NOI are specified, the purchase price is computed correctly and rounded as specified. Jurisdiction-specific requirements are met: the will follows its state's witness and notary requirements; the inter-organizational agreement references the applicable state law. Execution details are accurate: date, named witnesses, signatory blocks for all parties. Legal formalities are observed: LOIs include appropriate non-binding language; wills include survivorship clauses; compensation frameworks distinguish between stakeholder tiers. The document reads as professionally drafted — not template-like, not conversational, using appropriate legal register and terminology for the document type.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Document length | 1 page (compensation framework or one-pager) | 5 pages (LOI with standard business terms) | 8–11 pages (comprehensive will with full trust structure; multi-article inter-organizational agreement) |
| Party complexity | Two parties, one relationship | Multiple beneficiary tiers (primary, contingent, residuary) or multiple stakeholder types | Full fiduciary appointment structure (executor, alternate executor, trustee, alternate trustee, guardian, alternate guardian, temporary local guardian) |
| Financial calculation | No calculation required | One calculation (cap rate to purchase price, or split percentage) | Multiple layered calculations (FTE reduction percentage + proportional reduction logic + position-level analysis) |
| Jurisdiction-specific content | Generic professional document | One jurisdiction's legal requirements | Specific state code compliance (e.g., a state's probate/estates code); multi-state brokerage licensing requirements across several states; city or public-agency attorney standards |
| Reference file synthesis | No reference files; all terms inline | One reference file to incorporate (compensation model ideas) | Three reference files of different types (structural outline + boilerplate language + facility content) |
| Execution formality | No execution block required | Signature lines for named parties | Full execution block with date, two named witnesses, notary acknowledgment, self-insurance declarations |

## 7. Boundary Cases & Adjacent Patterns

- **vs. D4 (Program & Evaluation Plans):** D4 and D5 can overlap at the boundary of inter-organizational program agreements. The distinction is the primary purpose: D4 agreements are primarily organizational program documents (defining how a collaborative program runs) that happen to have some legal language; D5 documents are primarily legal instruments that happen to define program parameters. If the document is explicitly intended for attorney review before signature and requires jurisdiction-specific compliance language, it is D5. If it is primarily a program planning document with standard institutional agreement language, it is D4.
- **vs. C1 (Standard Operating Procedure):** C1 documents define how processes are executed operationally; D5 documents create formal legal relationships or obligations. If the document is a step-by-step procedure for staff to follow, it is C1. If the document is signed by named parties and creates enforceable obligations or transfers of rights, it is D5.
- **vs. D2 (Corporate Strategy Proposals):** D2 proposals advocate for a course of action using analytical frameworks; D5 documents constitute or formalize the action itself in legal terms. A negotiation strategy document (D2) recommends how to negotiate; a letter of intent (D5) executes the result of that negotiation. If the document argues for an action, it is D2; if the document IS the action, it is D5.
- **Choose D5 when:** The deliverable is a legal instrument (will, contract, LOI, compensation agreement) intended to be signed and/or enforceable; specific named parties with legal names or entity names are identified; jurisdiction-specific legal requirements govern the document's structure; the document would be reviewed by an attorney before execution; financial terms are specified as binding parameters rather than as recommendations.
