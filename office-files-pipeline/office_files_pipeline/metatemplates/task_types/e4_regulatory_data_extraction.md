# Regulatory Data Extraction & Comparison

**Macro Category:** E — Research-to-Document Tasks
**Pattern ID:** E4

## 1. Pattern Description

The worker navigates government or institutional websites, portals, or regulatory documents to extract specific compliance-relevant data across multiple jurisdictions, entities, or time periods, and then organizes the findings into a structured comparison table with an accompanying strategic or operational recommendation. The inputs are named regulatory sources (e.g., state licensing boards, CMS, EPA, or a state agency's regulatory data portal) rather than commercial platforms or academic databases. The defining cognitive core is regulatory interpretation: translating legal/regulatory language from different jurisdictions into a consistent schema that enables direct comparison, then synthesizing the variation into an actionable recommendation for a business or clinical decision. This distinguishes E4 from general web research — the source authority and the comparative structure across named jurisdictions or entities are non-negotiable.

## 2. O*NET Grounding

### Occupation Families
- 11-9111 Medical and Health Services Managers — state-level scope-of-practice research for hiring strategy
- 29-1141 Registered Nurses — regulatory compliance research (CMS quality measures, discharge planning standards)
- 29-1051 Pharmacists — state pharmacy board compliance checklists, formulary regulatory research
- 13-1041 Compliance Officers — multi-jurisdiction regulatory screening and checklist development
- 19-2041 Environmental Scientists and Specialists — EPA regulatory portal data extraction for site selection
- 13-1082 Project Management Specialists — regulatory data aggregation for infrastructure project planning
- 13-2051 Financial Analysts — regulatory comparison informing operational risk assessments

### Key Work Activities (O*NET vocabulary)
- Analyzing Data or Information
- Getting Information
- Documenting Information
- Evaluating Compliance with Regulations
- Making Decisions and Solving Problems
- Interpreting the Meaning of Information for Others

### Knowledge Domains (O*NET vocabulary)
- Law, Government and Jurisprudence
- Medicine and Dentistry (for healthcare regulatory contexts)
- Administration and Management
- Engineering and Technology (for environmental/infrastructure contexts)
- Mathematics (for well depth, aquifer type, or dosage criteria)
- English Language

### Generalizable Work Context
A professional with regulatory compliance or operational expansion responsibility needs to understand how rules, requirements, or allowances differ across a defined set of jurisdictions, entities, or facilities — and to translate that comparison into an operational recommendation. The trigger is typically a business expansion decision (entering a new state market, building a new facility, opening a new pharmacy) where the regulatory environment determines strategic choices. The worker is expected to research current regulations directly from authoritative sources rather than relying on secondhand summaries, because the stakes (licensing, compliance, penalties) require source-level accuracy.

## 3. Prompt Construction Template

### Persona Pattern
Assign a role with regulatory awareness in an expansion or compliance context: director of a multi-state healthcare service, environmental project manager, pharmacy owner, care-coordination case manager. The persona should have a clear business decision that depends on regulatory accuracy (hiring strategy, site selection, compliance program design). Seniority level: director-to-senior manager — responsible for the recommendation, not just the data collection.

### Scenario Pattern
The organization is planning to expand into new markets, sites, or service lines where regulatory requirements vary. The worker must research named jurisdictions or entities to understand regulatory variation, then translate findings into a recommendation that answers a specific business question (which states favor our model? which wells meet our technical threshold? which compliance tasks must be completed daily vs. quarterly?).

### Instruction Pattern
Specify the named jurisdictions or entities explicitly (state names, water system names, facility types). Provide the regulatory dimensions to compare as a structured list of columns or data fields. Name the authoritative source(s) — typically government URLs or named documents. State the recommendation requirement explicitly. Provide any simplifying assumptions (e.g., "assume equal cost/hourly rate — base recommendation solely on regulatory advantage").

### Constraint Injection Points
- **Named jurisdictions/entities:** specific states, named water systems, named facilities — cannot be substituted
- **Regulatory dimensions:** specific legal/compliance parameters to compare (e.g., independent practice authority, chart co-signature, supervision ratio; or well depth, aquifer type, active status)
- **Source authority:** exact government URLs or named regulatory documents required — not general web research
- **Output format:** comparison table (Excel or Word) with specific column schema
- **Recommendation requirement:** collective recommendation across all jurisdictions vs. per-jurisdiction rating
- **Cost/competitive neutrality assumption:** simplifying constraints that isolate regulatory advantage
- **Checklist frequency structure:** daily / weekly / monthly / quarterly / annual temporal categorization
- **Output count:** single comparison document vs. multiple separate documents by frequency or jurisdiction

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE] planning to [EXPANSION_CONTEXT].

[SCENARIO]: Your [ORGANIZATION] is evaluating [N] target [JURISDICTIONS / SITES / ENTITIES]: [ENTITY_LIST]. You need to understand how [REGULATORY_DOMAIN] varies across these [JURISDICTIONS / ENTITIES] to support a decision on [BUSINESS_QUESTION].

[RESEARCH TASK]:
Research the current [REGULATORY_DOMAIN] for each of the following [JURISDICTIONS / ENTITIES]:
1. [ENTITY_1]
2. [ENTITY_2]
...
N. [ENTITY_N]

[DATA SOURCES]: Use only the following authoritative sources:
- [SOURCE_1_URL_OR_NAME]
- [SOURCE_2_URL_OR_NAME]
[Note any fallback or supplementary sources if primary is unavailable]

[OUTPUT — COMPARISON TABLE]:
Produce an [Excel / Word] document with a comparison table. For each [JURISDICTION / ENTITY], include the following columns:
- [DIMENSION_1 — e.g., Independent Practice Authority (Yes/No)]
- [DIMENSION_2 — e.g., Chart Co-Signature Required]
- [DIMENSION_3 — e.g., Physician Supervision Ratio]
- [ADDITIONAL COLUMNS as needed]

[RECOMMENDATION REQUIREMENT]:
Based on the comparison, provide a [COLLECTIVE / PER-ENTITY] strategic recommendation addressing [BUSINESS_QUESTION]. [SIMPLIFYING ASSUMPTION if applicable — e.g., "Assume equal hourly rates — recommend based solely on regulatory advantage."]

[OUTPUT FORMAT]: [Excel workbook / PDF / Word document]. [Multi-document output if applicable: e.g., "separate PDFs grouped by frequency tier"]
```

## 4. Reference File Requirements

### File Types Needed
- **None (web-research-driven, most cases):** All regulatory data is sourced from named government URLs. The prompt provides the URLs inline.
- **Optional: Formulary template (XLSX):** A pre-structured Excel template defining the column schema for the comparison table. Provides the organizing scaffold without pre-populating regulatory data.

### Data Characteristics
No pre-provided data files in most cases. The "data" is extracted from government regulatory documents, state board portals, and institutional databases during task execution. The key abstract properties: content is jurisdiction-specific, authoritative, and often embedded in longer legal or policy documents (statutory codes, technical reports, factsheets). The worker must locate the relevant passage, extract the specific parameter, and normalize it to a consistent comparison schema. Data types include: binary (Yes/No for authority or requirement), categorical (aquifer type, supervision tier), numerical (supervision ratios, well depths, follow-up timeframes in days), and temporal (daily/weekly/monthly/annual).

### File Complexity Spectrum
- **Minimal:** No reference files; 2–3 named jurisdictions; 2–3 comparison dimensions; single-tab Excel table; simple recommendation paragraph.
- **Moderate:** No reference files; 4–6 named jurisdictions; 4–6 comparison dimensions; two-tab Excel (all data + filtered/qualifying subset); 1–2 paragraph recommendation.
- **Complex:** URL-driven extraction from 2+ regulatory documents; 8+ named entities; 8–10 columns; multiple output documents (separate PDFs by frequency tier); comprehensive enough to serve as an operational quality assurance tool.

## 5. Output Specification

### Primary Deliverable
- **Format:** Excel workbook (.xlsx) with comparison table and filter/flag columns; or multiple PDF documents (for checklist outputs)
- **Structure:** Rows = jurisdictions/entities/facilities; Columns = regulatory dimensions; plus one or more derived columns (filter flag, qualifying status, recommendation rating); or sequential checklist structure organized by frequency (daily, weekly, monthly, etc.)
- **Key quality signals:** Data extracted from named authoritative sources (not paraphrased from secondary sites); each jurisdiction/entity represented in every comparison column; consistent data type within each column (all Yes/No, all numerical, etc.); recommendation explicitly tied to specific regulatory findings; no jurisdictions omitted from the specified list

### Secondary Deliverables (if any)
- Written recommendation email or memo (when research output is sent to a manager or stakeholder)
- Second Excel tab with only the qualifying entities (filtered subset meeting all criteria)

### Gold Output Characteristics
A gold output sources all data directly from named government or institutional URLs rather than general reference sites; populates every intersection of jurisdiction × regulatory dimension; applies any required filtering or flagging logic correctly (active status, depth range, aquifer type); normalizes varied regulatory language into a consistent schema; and delivers a recommendation that is specific (naming preferred jurisdictions/options), reasoned (citing specific regulatory advantages), and calibrated to the stated business constraints (e.g., "assuming equal cost, favor NPs in states X and Y because they operate without supervision requirements"). For checklist outputs: tasks are correctly categorized by temporal frequency, actionable for non-regulatory-expert staff, and comprehensive without redundancy.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Jurisdiction/entity count | 2–3 named | 4–6 named | 8–10+ named with possible sub-entities |
| Regulatory dimension count | 2–3 comparison columns | 4–5 columns | 6–10 columns including derived/calculated columns |
| Source complexity | 1 named URL | 2 named URLs with distinct document structures | 2+ complex government documents requiring navigation (e.g., a single lengthy regulations document vs. a portal presenting per-entity factsheets) |
| Output format complexity | Single-tab comparison table | Two-tab Excel (all data + qualifying subset) | Multiple separate PDF documents, split by frequency tier |
| Recommendation depth | Brief paragraph | 1–2 paragraphs with per-state rationale | Full strategic recommendation memo with business case reasoning |
| Domain expertise requirement | General compliance concepts | Specialized domain (pharmacy law, NP scope) | Highly technical domain (aquifer geology, CMS quality measure methodology) |
| Filtering logic | No filtering required | Single threshold filter (yes/no per criterion) | Multi-criteria filter with exclusion keywords and combined-flag logic |

## 7. Boundary Cases & Adjacent Patterns

**E3 (Market Research & Deal Sourcing):** Both patterns involve structured web data extraction, but E3 sources from commercial market platforms (financial data sites, real estate deal platforms, retail pricing sites) for investment or pricing decisions. E4 sources exclusively from government and institutional regulatory portals for compliance and operational decisions. The source authority (regulatory vs. commercial) is the primary distinguishing factor.

**C2 (Compliance Checklist / Assessment Tool Design):** C2 produces assessment tools and checklists designed from domain expertise or provided regulatory text URLs — the checklists may reference regulation by name but the primary cognitive task is form design. E4 requires active extraction from regulatory documents accessed via specific government URLs, with the extracted content forming the checklist substance. When a regulatory URL is the source rather than just a reference, prefer E4.

**E1 (Literature Review & Evidence Synthesis):** E1 sources from academic and research literature (PubMed, CINAHL, CDC research publications) and produces evidence synthesis organized by thematic findings. E4 sources from government regulatory portals and legal documents and produces compliance-oriented comparison tables. The output type (evidence synthesis vs. regulatory comparison) is the clearest distinction.

**B3 (Compliance Report from Transaction Data):** B3 cross-references transaction or claims data against attached policy documents to identify compliance exceptions. E4 researches regulatory rules from government sources to understand what the rules are — not to evaluate whether specific transactions comply. B3 is about exception identification; E4 is about regulatory knowledge gathering.
