# Commercial Quotations & Proposals

**Macro Category:** F — Client Communication & Outreach Materials
**Pattern ID:** F4

## 1. Pattern Description

The worker prepares a formal commercial quotation or structured intake proposal for a client or business partner by consolidating pricing, logistics, and commercial terms from multiple internal and external reference sources. The cognitive core is translating internal pricing data, freight forwarder quotes, and client procurement requests into a correctly structured, compliant commercial document that can be sent directly to the client. This pattern is distinct from financial modeling (A3/A4) because the output is not an internal analytical model but an externally deliverable commercial document; and distinct from strategic proposals (D2) because it is operational rather than strategic — it quotes specific products/quantities/prices rather than proposing business strategies. Key domain knowledge includes Incoterms (EXW, CIF, DAP), payment terms conventions, and multi-transport-mode cost comparison.

## 2. O*NET Grounding

### Occupation Families
- 41-4011 Sales Representatives, Wholesale and Manufacturing (Technical and Scientific Products) — account managers preparing product quotations for NGO and commercial clients
- 13-1081 Logisticians — incorporating freight mode comparisons and transport cost calculations into commercial quotations
- 13-1023 Purchasing Agents and Buyers, Farm Products / 11-3061 Purchasing Managers — brand onboarding intake form preparation and vendor assessment
- 11-2022 Sales Managers — preparing distribution partner intake forms and brand onboarding materials

### Key Work Activities (O*NET vocabulary)
- Selling Products and Services to Organizational Customers
- Documenting or Recording Information
- Communicating with Persons Outside the Organization
- Coordinating Logistics
- Analyzing Costs and Benefits
- Getting Information (from internal pricing tables and freight forwarder quotes)
- Organizing, Planning, and Prioritizing Work
- Developing Policies and Procedures (for intake/onboarding forms)

### Knowledge Domains (O*NET vocabulary)
- Sales and Marketing
- Transportation (Incoterms, freight mode selection, transit time)
- Economics and Accounting (unit pricing, volume-based tiers, total cost calculation)
- Administration and Management
- Customer and Personal Service
- Medicine and Dentistry (for humanitarian/medical supply contexts)

### Generalizable Work Context
An account manager or sales professional at a wholesale, distribution, or supply company receives a formal procurement request or purchase order from a client (NGO, distributor, or brand partner). The worker must look up internal pricing for the requested products, add applicable freight or logistics costs, apply commercial policy constraints (payment terms, offer validity, Incoterms), and produce a structured quotation or proposal document. The trigger is a client RFP or purchase inquiry. The output is sent externally to the client and must follow precise format and naming conventions. For intake form variants, the trigger is onboarding a new brand partner and the output is a structured question-based form rather than a priced quotation.

## 3. Prompt Construction Template

### Persona Pattern
Assign an account manager or sales manager role at a wholesale distribution company. Include the organization name and type (international medical wholesaler, consumer goods distributor). Specify the client relationship context (new NGO client requiring prepayment per company policy, or existing client needing a quotation revision). The persona should carry domain knowledge of trade terms and the relevant product category.

### Scenario Pattern
The trigger is a client procurement request (RFP or purchase inquiry) for a specific product line at specific quantities. Introduce: (1) the client name and organization type, (2) the product being quoted (kit, SKU list, or category), (3) the quantity ordered (may trigger volume pricing tiers), (4) applicable trade terms (Incoterms) and payment conditions, and (5) any additional elements to include (freight options, regulatory or standards-body reference URLs, offer validity period). For revised quotations, specify what has changed from the original (updated price, updated lead time, addition of freight options).

### Instruction Pattern
Instructions enumerate the required fields/columns in the quotation as a bulleted or numbered list. For Excel quotation tasks, the instruction specifies: column schema, calculation logic (EXW total + freight per mode = grand total), conditional formatting rules (red font for specific remarks), and file naming conventions. For intake form tasks, instructions specify the content areas (operational capacity, product logistics, sales data) and format rules (text-based, question-based, no form fields, a short page limit).

### Constraint Injection Points
- **Incoterms basis:** EXW (ex-warehouse, no freight) vs. CIF/DAP (including freight) — determines whether transport costs are added to the quotation
- **Transport mode options:** single mode (EXW only) vs. multi-modal (air, sea, road) — multi-modal requires parallel rows with per-mode grand totals and suitability notes
- **Quantity and volume pricing:** fixed quantity (straightforward lookup) vs. quantity-triggered pricing tier (a threshold quantity may unlock a discounted rate vs. the standard rate)
- **Payment terms and offer validity:** standard policy constraints (full prepayment required for new clients, a fixed offer-validity window) that are non-negotiable; can vary by client relationship tier
- **Risk flagging:** some transport routes require a disruption warning (e.g., road freight through active conflict zones); specified in red font or remarks column
- **File naming convention:** exact prescribed filenames required; format includes client/project identifiers and quotation reference numbers
- **Module/SKU structure:** uniform quantities (1 unit per module) vs. mixed quantities (a higher quantity for one module, a uniform lower quantity for the rest)
- **Intake form vs. priced quotation:** for onboarding/brand intake variants, the output is a structured question document rather than a priced Excel quotation

### Structural Template

```
[PERSONA]: You are an Account Manager at [ORG_NAME], a [ORG_TYPE] specializing in [PRODUCT_CATEGORY] for [CLIENT_SEGMENT].

[SCENARIO]: [CLIENT_NAME] ([CLIENT_TYPE: NGO / distributor / brand partner]) has submitted a request for [PRODUCT/KIT_NAME] — [QUANTITY_DETAILS]. [CLIENT_RELATIONSHIP: new client requiring prepayment per company policy / existing client needing quotation update]. [TIMING_CONTEXT_IF_APPLICABLE: grant cycle deadline, project reference number].

[REFERENCE_FILES]:
- [FILE_1]: [internal pricing document — e.g., xlsx with EXW unit prices, lead times, shelf life per SKU/module]
- [FILE_2]: [client RFP or request document — specifying required items, quantities, and project reference]
- [FILE_3 (if applicable)]: [freight forwarder quote(s) — air, sea, road — with per-mode costs, transit times, validity periods]

[TASK]: Prepare a formal quotation [or intake form] saved as "[EXACT_FILENAME]".

[REQUIRED_FIELDS/COLUMNS]:
- [FIELD_1]: [description and source]
- [FIELD_2]: [description and source]
- [FIELD_3]: [e.g., EXW unit price — from internal pricing document]
- [FIELD_4]: [e.g., quantity — from client RFP]
- [FIELD_5]: [e.g., total EXW — calculated: unit price × quantity]
- [FIELD_6]: [e.g., shelf life — from internal pricing document]
- [FIELD_7]: [e.g., lead time — from internal pricing document]
- [FIELD_8]: [e.g., payment condition — company policy: prepayment required for new clients]
- [FIELD_9]: [e.g., offer validity — company policy: a fixed validity window from quotation date]
[... for multi-modal transport quotation: add freight section below EXW total]

[TRANSPORT_OPTIONS] (if applicable):
Below the EXW total line, add three rows for:
- Air freight: cost from [FREIGHT_PDF_1], transit time [N days], remarks: [suitability note]
- Sea freight: cost from [FREIGHT_PDF_2], transit time [N days], remarks: [suitability note]
- Road freight: cost from [FREIGHT_PDF_3], transit time [N days], remarks: [FLAG: potential border disruptions]

Each transport option row: Grand Total = EXW Total + freight cost

[FORMATTING_RULES]:
- General freight remark ("[REMARK_TEXT]") must appear in red font
- [ANY_OTHER_CONDITIONAL_FORMATTING]

[OUTPUT_SPECIFICATION]: Excel file named "[EXACT_FILENAME.xlsx]"
```

## 4. Reference File Requirements

### File Types Needed
- **Internal pricing table (xlsx):** The core reference file. Contains per-SKU or per-module rows with: item description, article/product number, EXW unit price, availability status, shelf life, and lead time. May include volume-tiered pricing (different unit price at different quantity breaks). 5-30 rows is typical.
- **Client RFP or request document (pdf):** Formal procurement request specifying: required items/modules, quantities, project reference number, and optionally delivery destination and timeline. Provides the quotation scope and project reference fields.
- **Freight forwarder quotes (pdf, 1-3 files):** Per-transport-mode shipping quotes from a freight forwarder. Each PDF contains: mode (air/sea/road), total freight cost for the specified shipment (weight + volume given), transit time, validity period, and any route notes. Required only for multi-modal quotation variants.
- **Original quotation template (xlsx):** For revision tasks — the existing quotation file serves as the base; the worker updates specific fields and adds new sections without changing unchanged elements.

### Data Characteristics
Internal pricing tables should have realistic wholesale price ranges, standard lead times (2-8 weeks for medical supply), and shelf-life data (18-36 months for medical kits). Quantities in client RFPs should be specific enough to test volume-tier lookup (e.g., a larger order quantity may trigger a different unit price than a smaller one). Freight quotes should show realistic mode-specific cost differentials (air freight is 3-5x more expensive than sea, transit time inverse), with transit times ranging from 3 days (air) to 30-45 days (sea). File naming conventions should follow a realistic quotation numbering format (client code + sequential reference number).

### File Complexity Spectrum
- **Minimal:** Single-file task — internal pricing xlsx + client RFP; produce EXW-only quotation with 5-10 line items, fixed quantities, standard payment terms; no freight, no volume tiers
- **Moderate:** Two-file task — internal pricing xlsx + client RFP with mixed quantities (a higher quantity for one module, a lower uniform quantity for the rest); produce quotation with all required fields including a regulatory or standards-body reference URL; standard single-mode Incoterms
- **Complex:** Five-file task — original quotation xlsx + internal pricing xlsx + 3 freight forwarder PDFs (air, sea, road); produce revised quotation with updated unit price, 3 transport option rows with per-mode grand totals, conditional red-font remark, road freight risk flag, volume-adjusted pricing — all while preserving unchanged fields from original quotation

## 5. Output Specification

### Primary Deliverable
- **Format:** Excel workbook (.xlsx) for priced quotations; PDF for intake/onboarding forms
- **Structure:**
  - Excel quotation: header section (client, date, reference numbers, validity, payment terms) + line item table (item description, article number, quantity, unit price, total) + freight section (if applicable) + grand totals per transport option + remarks row
  - PDF intake form: section-organized, question-based prompts with answer space; no embedded form fields; a short page-count maximum
- **Key quality signals:** Exact prescribed filename; correct calculation of totals (unit price × quantity; EXW total + freight); correct volume-tier lookup when applicable; all required fields present; red-font formatting applied correctly; road freight risk flag present; original quotation unchanged fields preserved in revision tasks

### Secondary Deliverables (if any)
- A regulatory or standards-body reference URL included as a hyperlink in the quotation remarks or a dedicated cell (for humanitarian medical supply variants)
- None for intake form variants

### Gold Output Characteristics
A gold output: (1) uses the exact prescribed filename; (2) pulls all prices and product data from the internal pricing reference (not from memory or generic estimates); (3) applies volume-tiered pricing correctly if the quantity triggers a different tier; (4) calculates all totals accurately (no arithmetic errors); (5) positions the freight section correctly below the EXW total; (6) applies conditional formatting exactly (red font on specified remark); (7) includes all required fields without omission; (8) preserves unchanged elements in revision tasks; and (9) applies all commercial policy constraints (payment terms, offer validity) as non-negotiable rules.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of reference files | 1 (internal pricing only) | 2 (pricing + client RFP) | 5 (pricing + RFP + 3 freight PDFs + original quotation) |
| Transport modes | EXW only (no freight) | Single transport mode | Three parallel transport modes with per-mode grand totals |
| Quantity/pricing | Fixed quantity, single price | Multiple SKUs with different quantities | Volume-triggered pricing tier requiring lookup and comparison |
| Line item complexity | Uniform quantities, single product | Mixed quantities (one item at a higher quantity, the rest at a uniform lower quantity) | Multi-module kit with mixed quantities plus volume tier logic |
| Conditional formatting | None | Basic number formatting | Red font for specific remark text; risk flag in remarks column |
| Revision vs. new creation | New quotation from scratch | New quotation with structured template to follow | Revision of existing quotation preserving unchanged fields while updating specific cells and adding new sections |
| Output type | Priced Excel quotation | Priced quotation with embedded policy notes and URLs | Structured question-based intake form covering 4+ operational content areas |

## 7. Boundary Cases & Adjacent Patterns

**A3 — NPV/IRR & Investment Evaluation:** Both A3 and F4 involve multi-option cost comparison in a commercial context. The distinction is audience and purpose: A3 produces an internal financial model comparing investment scenarios (vendor selection, project ROI) for internal decision-making; F4 produces a client-facing commercial document (a quotation or proposal sent to the client). If the output is an Excel workbook with DCF or NPV calculations for internal review, it is A3. If the output is a formatted quotation sent to an external buyer or NGO, it is F4.

**D2 — Corporate Strategy & Business Proposals:** Both D2 and F4 involve proposals addressed to external parties. D2 produces strategic-level proposals (sourcing strategies, organizational recommendations, market entry plans) designed to persuade decision-makers on a course of action. F4 produces operational commercial documents (specific product quantities at specific prices with specific trade terms). If the document contains strategy, market analysis, or organizational recommendations, it is D2. If it contains line items, unit prices, Incoterms, and payment conditions, it is F4.

**C5 — Form & Template Design:** A brand or partner intake form sits at the boundary of F4 and C5. It belongs to F4 when the form is explicitly directed at an external business partner (e.g., a brand partner filling out the form) and serves as the first step in a commercial engagement — making it client communication rather than internal form design. C5 is for forms and templates designed for internal organizational use (patient intake forms, community association forms). If the form is sent to a business partner for them to complete, it is F4. If it is used internally by staff, it is C5.
