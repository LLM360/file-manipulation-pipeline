# Compliance Report from Transaction Data

**Macro Category:** B — Data-Driven Document Authoring
**Pattern ID:** B3

## 1. Pattern Description

The worker cross-references one or more transaction or operational data files against a policy, regulatory standard, contract schedule, or clinical protocol to identify non-compliant items, calculate the scope of exceptions, and produce a formal written report documenting findings. The cognitive core is a two-layer task: first, applying defined criteria to flag individual records or line items as compliant or non-compliant; second, synthesizing those findings into a formal compliance narrative or report document that can be used for regulatory submission, management review, or remediation planning. What makes B3 distinct is the mandatory dual-output structure (a narrative document plus a supporting data file) and the regulatory or policy grounding that shapes both the analytical logic and the report language. The analyst does not invent the criteria — they are derived from attached regulatory guidance, contracts, clinical protocols, or internal policies.

## 2. O*NET Grounding

### Occupation Families
- 13-2061 Financial Examiners — AML investigators writing SAR narratives based on transaction data and FinCEN guidance
- 13-1041 Compliance Officers — order analysts identifying billing errors and producing exception reports with remediation recommendations
- 11-9141 Property, Real Estate, and Community Association Managers — leasing agents cross-referencing inspection data against vendor schedules to produce scheduling compliance reports
- 43-5061 Production, Planning, and Expediting Clerks — analysts validating order data against business rules and documenting violations
- 29-1141 Registered Nurses — dialysis nurses applying clinical protocols to patient lab data to document required medication changes

### Key Work Activities (O*NET vocabulary)
- Evaluating Compliance with Standards
- Analyzing Data or Information
- Documenting Information
- Identifying Objects, Actions, and Events
- Communicating with Supervisors, Peers, or Subordinates
- Resolving Conflicts and Negotiating with Others

### Knowledge Domains (O*NET vocabulary)
- Law, Government and Jurisprudence
- Economics and Accounting
- Public Safety and Security (for AML/financial crime variants)
- Medicine and Dentistry (for clinical protocol variants)
- Transportation (for logistics/scheduling variants)
- English Language

### Generalizable Work Context
A compliance analyst, investigator, or operations professional receives a dataset of transactions, orders, claims, lab results, or work events and is tasked with determining which records fall outside defined policy parameters. The policy is either provided as an attached document or referenced via regulation. The trigger is usually a periodic audit cycle, a management directive following an anomaly, or a regulatory filing deadline. The analyst must both identify the violations in the data and write the formal document that makes those findings actionable — for a regulator, a manager, or a clinical team.

## 3. Prompt Construction Template

### Persona Pattern
Assign a role whose job function inherently involves policy or regulatory compliance: an AML investigator, a leasing agent, an order analyst, a dialysis nurse applying standing orders, a compliance officer reviewing billing records. The role should have organizational authority to file, submit, or recommend action based on compliance findings. Specify the institution type (bank, property management company, wholesale distributor, dialysis facility) to ground the regulatory vocabulary.

### Scenario Pattern
Describe the compliance situation that triggered the task: a law enforcement tip, a manager request to audit a billing cycle, a quarterly vendor scheduling review, or a monthly lab tracking workflow. Name the policy or regulation being applied (FinCEN SAR guidelines, bank secrecy act, contract service schedule, clinical standing orders). Specify the population being analyzed (a set of accounts, a batch of purchase orders, a group of patients, a set of units). Include any background context (suspect behavior narrative, prior exception history, clinical patient assignments) that the worker must incorporate into the report.

### Instruction Pattern
Provide explicit compliance criteria as numbered or bulleted rules. Specify both the analytical task (flag records meeting criterion X or Y) and the document task (write a narrative covering who/what/when/where/why; or organize findings by exception category; or produce a section-by-section compliance report). Enumerate the required document sections. Specify the supporting data file structure. Include any hard limits (page limit on narrative, required regulatory citation format, named entities that must appear).

### Constraint Injection Points
- **Exception criteria definition:** the rules that determine what constitutes a violation (price mismatch, structuring behavior, weight threshold exceeded, lab value outside protocol range)
- **Regulatory framework:** named regulation or policy that must be cited or applied (FinCEN, Bank Secrecy Act, AML typologies, clinical standing orders by physician group)
- **Named entities:** suspects, accounts, patients, stores, vendors whose data must be analyzed and named in the report
- **Report format and length:** SAR narrative under a page limit; scheduling report with a fixed section count; exception summary with specific required headings
- **Dual deliverable structure:** narrative document format + supporting data file format
- **Escalation or approval path:** output is for senior management review, regulatory submission, or physician approval

### Structural Template

```
[PERSONA]: You are a [ROLE] at [INSTITUTION_TYPE]. [BRIEF_ROLE_CONTEXT].

[SCENARIO]: [TRIGGER_EVENT — e.g., "Following a [law enforcement tip / quarterly audit / management request], you have been asked to review [DATA_DESCRIPTION] and produce a [COMPLIANCE_REPORT_TYPE]"].

[REGULATORY_CONTEXT]: [POLICY_OR_REGULATION] governs this situation. [BRIEF_POLICY_SUMMARY or reference to attached policy document].

[DATA_SOURCE]:
- Attached file 1: [FILE_TYPE] containing [DESCRIPTION — e.g., "transaction records for accounts belonging to [ENTITIES] from [DATE_RANGE]"]
- Attached file 2: [FILE_TYPE] containing [DESCRIPTION — e.g., "policy document defining reimbursement parameters" or "clinical standing orders"]

[ANALYTICAL_TASK]:
Apply the following compliance criteria to the data:
1. [CRITERION_1 — e.g., "Flag any record where [FIELD] exceeds [THRESHOLD] and [CONDITION]"]
2. [CRITERION_2]
3. [ADDITIONAL_CRITERIA]

[DOCUMENT_TASK]:
Produce a [DOCUMENT_TYPE] (max [PAGE_LIMIT]) covering:
- [SECTION_1 — e.g., "Who: entity descriptions and account relationships"]
- [SECTION_2 — e.g., "What: specific suspicious behaviors identified"]
- [SECTION_3 — e.g., "When/Where: chronology and geography of activity"]
- [SECTION_4 — e.g., "Why: red flag typologies and regulatory basis"]
- [SECTION_5 — e.g., "Recommendations for remediation"]

[SUPPORTING_FILE_TASK]:
Compile a [EXCEL_FILE_DESCRIPTION — e.g., "supporting transaction record extract with columns X, Y, Z organized for management review"].

[CONSTRAINTS]:
- [NAMED_ENTITIES_THAT_MUST_APPEAR]
- [CITATION_REQUIREMENT]
- [APPROVAL_PATH — e.g., "for senior management review and approval"]
- [FORMAT_CONSTRAINT]
```

## 4. Reference File Requirements

### File Types Needed
- **Transaction or operational data file (xlsx):** The primary analytical input containing individual records to be screened against compliance criteria. Could be: transaction ledger with amounts, dates, and entity identifiers; purchase order lines with price and unit fields; patient monthly lab results; work order log with timestamps; rental damage records with revenue amounts.
- **Policy or regulatory reference document (docx or pdf):** The document containing the criteria, thresholds, or rules the analyst applies. Could be: a FinCEN guidance document, an insurance policy defining reimbursement eligibility, clinical standing orders by physician, a vendor contract schedule, a business rule set.
- **Supporting context document (docx, optional):** Background narrative, prior investigation notes, or management communication that provides context for interpreting the data (e.g., suspect background in AML investigation, prior billing period for comparison).

### Data Characteristics
The transaction data file should contain 20-200 rows with each row representing a discrete event (transaction, purchase order line, patient lab draw, work order). Key fields: an entity or account identifier linking records to a named subject; a date or timestamp; a numerical measure (amount, unit count, lab value); and one or more categorical fields (transaction type, account type, damage type, UOM code). The data should contain a mix of compliant and non-compliant records — approximately 10-40% exception rate — to make the screening task meaningful but not trivially obvious.

### File Complexity Spectrum
- **Minimal:** Single data file with 20-30 rows, one compliance criterion, one violation type, simple threshold comparison. Output: short Word document (1-2 pages) plus annotated Excel.
- **Moderate:** Single data file with 50-100 rows, 2-3 compliance criteria (different violation types), dual-output structure, one policy reference document. Report requires findings organized by exception category with financial impact summary.
- **Complex:** Multi-entity transaction ledger (multiple accounts, locations, date ranges), 3-5 FinCEN-style red flag typologies to identify, multi-document regulatory reference set, dual deliverable (page-limited SAR narrative + organized transaction file), named entities requiring character-level investigation.

## 5. Output Specification

### Primary Deliverable
- **Format:** Word document (narrative report, SAR, PIP-style compliance document) or PDF
- **Structure:** Formal sections covering who is involved, what violations were found, when and where they occurred, why they are reportable/non-compliant, and what remediation or action is recommended
- **Key quality signals:** All flagged items are grounded in specific data points from the attached file; regulatory citations are correct and applicable; named entities match the data; the narrative does not invent findings not supported by the data; the report is actionable (a regulator, manager, or clinical team could use it directly)

### Secondary Deliverables (if any)
- Excel workbook: Annotated transaction data with flag columns, exception labels, and aggregate summary tabs (total revenue by category, exception rate by type, organized transaction extract)
- Scheduling or tracking document: A structured report organizing findings by entity or category (e.g., by vendor vs. by unit; by exception type vs. by account)

### Gold Output Characteristics
A gold output applies compliance criteria without error — all and only records meeting the defined conditions are flagged. The narrative report accurately characterizes the scope, nature, and significance of violations. Regulatory language is used correctly; typological red flags are identified precisely. The dual-output structure is complete — both the narrative document and the supporting data file are present and consistent. Named entities appear correctly in both documents. The report is formatted appropriately for its intended audience (senior management review, regulatory filing, physician communication) and conforms to any page limits.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of compliance criteria | 1 | 2-3 | 4-5 with different data fields each |
| Number of entities / accounts | 1-3 | 4-8 | 10+ with cross-entity relationship analysis |
| Regulatory framework depth | Single internal policy | Named external regulation (FinCEN, contract) | Multiple overlapping frameworks (e.g., AML plus an adjacent financial-crime typology) |
| Report length and formality | 1-2 page summary | 2-3 page structured report | Longer, page-limited regulatory submission (e.g., SAR narrative) |
| Data volume | 20-40 rows | 50-100 rows | 100-300 rows across multiple entities |
| Dual-output complexity | Single deliverable | Annotated data + short Word document | Formal narrative + structured transaction extract with prescribed columns |
| Background context | Minimal | One-paragraph scenario | Extended investigative narrative with OSINT elements |

## 7. Boundary Cases & Adjacent Patterns

**A1 (Audit Sampling & Compliance Testing):** A1 produces a filtered/flagged Excel output — the deliverable IS the annotated data file. B3 uses the same analytical process but requires a formal written narrative document as the primary deliverable. If the task is to produce a compliance screening dataset without a narrative report, use A1. If a written compliance document is the primary output, use B3.

**B2 (HR & Workforce Decision Reports):** B2 applies thresholds to employee performance data and produces HR documents (PIPs, selection rationale). B3 applies regulatory or policy criteria to transactional data and produces compliance reports. The population being analyzed (employees vs. transactions) and the regulatory grounding (HR policy vs. financial/clinical regulation) are the key differentiators.

**B5 (Data Entry with Protocol-Driven Decision Making):** B5 focuses on populating a template or tracker by applying embedded rules — the output is a completed spreadsheet, not a written narrative. B3 requires a formal document explaining findings. If there is no narrative report and the deliverable is purely a populated data file, use B5.

**B1 (Performance Analysis Presentation):** B1 translates data analysis into a slide presentation for leadership. B3 produces a formal compliance document (Word report, SAR) for regulatory or management action. If the format is slides rather than a regulatory or compliance document, use B1.
