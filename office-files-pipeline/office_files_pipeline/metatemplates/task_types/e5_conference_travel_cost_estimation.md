# Conference & Travel Cost Estimation

**Macro Category:** E — Research-to-Document Tasks
**Pattern ID:** E5

## 1. Pattern Description

The worker conducts live web research across multiple booking and vendor platforms to price out a real-world travel or procurement scenario — conference registration, flights, hotels, ground transportation, equipment — and compiles the findings into a structured cost estimation document with embedded evidence (screenshots or web links) and a budget summary. The defining characteristic of this pattern is the documentary evidence requirement: each cost item must be supported by a screenshot or hyperlink to the source, making this a verifiable rather than an estimated output. Secondary features include budget constraint logic (comparing estimated costs against funding caps with visual indicators) and proportional cost-splitting when multiple people or periods are involved. The cognitive core is multi-platform research choreography: visiting different types of sites in the right order, capturing evidence, and assembling results into a cost structure that enables a procurement or travel approval decision.

## 2. O*NET Grounding

### Occupation Families
- 43-6013 Medical Secretaries and Administrative Assistants — conference travel planning for physicians is a standard medical secretarial task
- 27-4014 Sound Engineering Technicians — equipment sourcing and budget planning for touring productions
- 43-6011 Executive Secretaries and Executive Administrative Assistants — travel arrangement and cost estimation for senior staff
- 43-5061 Production, Planning, and Expediting Clerks — procurement planning with budget constraints
- 13-1082 Project Management Specialists — conference and event logistics budgeting
- 11-1011 Chief Executives / 11-3011 Administrative Services Managers — approvers of travel cost documents (define the downstream audience)

### Key Work Activities (O*NET vocabulary)
- Getting Information
- Communicating with Persons Outside Organization
- Organizing, Planning, and Prioritizing Work
- Documenting Information
- Analyzing Data or Information
- Scheduling Work and Activities

### Knowledge Domains (O*NET vocabulary)
- Administration and Management
- Customer and Personal Service
- Geography
- Mathematics
- Computers and Electronics
- Economics and Accounting (budget management)

### Generalizable Work Context
An administrative or operations professional is asked to plan and cost out a trip, equipment purchase, or conference attendance for one or more people, within a defined budget. The trigger is an upcoming event (conference, tour, meeting) for which travel or equipment has not yet been booked. The worker must source real prices from live platforms rather than using estimates, because the output serves as the basis for a purchase authorization or department reimbursement decision. Multiple people, budget sources, or cost-sharing arrangements typically add a calculation layer on top of the raw price research.

## 3. Prompt Construction Template

### Persona Pattern
Assign an administrative or technical support role responsible for logistics planning: medical secretary, touring audio technician, executive assistant, office manager, project coordinator. The persona should have a named supervisor or organizational authority figure who must approve the spending. Include specific contextual details — the number of travelers, the event name, the budget source structure. Seniority level: individual contributor, administrative or technical level.

### Scenario Pattern
A specific event (named conference, touring production, equipment procurement) has a defined date range and location. The worker must plan the logistics from a defined departure point, within a defined budget, for a defined number of people. Multiple stakeholders may have different attendance durations or cost allocations. Budget structure should be explicit — total cap, per-person cap, departmental vs. discretionary split.

### Instruction Pattern
Organize the task as a sequence of research steps (one platform type per section), each with a defined deliverable (screenshot + cost summary). Then specify the final budget summary structure (table showing allocation, total cost, and remainder with conditional formatting). Name the output file. Specify the date constraints and any equipment or logistics exclusions. Make the screenshot requirement explicit — without it, the task collapses into a generic estimation task.

### Constraint Injection Points
- **Budget cap:** total or per-person spending ceiling, with dual-fund structure (departmental vs. discretionary) adding calculation complexity
- **Traveler count and duration:** one vs. multiple travelers, different attendance lengths creating proportional split logic
- **Geographic constraints:** departure city, proximity requirements for hotel (within N blocks of venue), star rating floor
- **Temporal constraints:** conference dates, specific departure constraints (e.g., must leave by X time on day Y)
- **Booking class constraints:** economy vs. business class, shared room vs. individual rooms
- **Screenshot/evidence requirement:** per-section vs. per-item evidence capture
- **Date stamping:** must document when information was captured
- **Equipment exclusions:** items already owned that must not be included in cost
- **Output format:** Word document vs. PDF, specific filename required
- **Color-coding requirement:** green if covered by primary fund, red if requires secondary fund

### Structural Template

```
[PERSONA]: You are a [ROLE] for [DEPARTMENT] at [ORG_NAME], [CITY].

[SCENARIO]: [N] [PROFESSIONALS / STAFF] will attend [EVENT_NAME] in [CITY] from [DATE_RANGE]. Your department has allocated $[AMOUNT] per person from the [FUND_NAME]; any additional costs will be covered by [SECONDARY_FUND].

[TRAVELER DETAILS]:
- [PERSON_1]: Attending [DATES], [SPECIFIC_DEPARTURE_CONSTRAINT if any]
- [PERSON_2]: Attending [DATES], [ROOM_SHARING_ARRANGEMENT]

[TASK]: Produce a Word document titled "[OUTPUT_FILENAME]" with the following sections. Each section must include an embedded screenshot from the relevant website and an itemized cost summary.

[SECTION 1 — REGISTRATION]:
Research the registration cost at [CONFERENCE_WEBSITE]. Screenshot required.

[SECTION 2 — TRAVEL & TRANSPORTATION]:
Research economy class flights from [DEPARTURE_CITY] to [DESTINATION_CITY] for each traveler. Research [GROUND_TRANSPORT_TYPE] from airport to hotel and return. Use [BOOKING_PLATFORM] or similar. Screenshot required per item.

[SECTION 3 — LODGING]:
Research hotels within [N] blocks of [VENUE_NAME], [STAR_RATING] or higher. Use [PROXY_DATES] if actual dates are not available. Split room cost proportionally: [PERSON_1] stays [N] nights, [PERSON_2] stays [N] nights. Screenshot required.

[SECTION 4 — TOTAL COSTS]:
Create a table with two columns (one per person) showing:
- Department funding: $[AMOUNT]
- Total estimated cost
- Remainder (green if department covers cost; red if discretionary fund required)

[OUTPUT]: Save as "[FILENAME]". Date-stamp each section with when the information was captured.
```

## 4. Reference File Requirements

### File Types Needed
- **None (web-research-driven):** All pricing data is sourced from live booking and vendor platforms. No pre-attached reference files are required for this pattern.
- **Optional: Conference agenda / program brochure:** Provided only when the worker must identify which specific sessions or registration tiers are applicable. Not typically required for cost estimation tasks.

### Data Characteristics
No reference files. The pipeline must ensure that prompts name specific, real-world events or plausible event types so that research tasks are grounded in realistic booking scenarios. Key data characteristics of the output: itemized cost entries with per-unit price and quantity; screenshot evidence embedded as images; a budget summary table with arithmetic (funding cap minus total cost equals remainder); conditional formatting on the remainder value (positive = green, negative = red). Equipment procurement variants add a parts list with per-item prices and totals.

### File Complexity Spectrum
- **Minimal:** No reference files; single traveler; one conference; 3 cost categories (registration, flight, hotel); simple itemized list with total; no color-coding; no screenshots (or screenshots optional).
- **Moderate:** No reference files; two travelers with different attendance durations; 4 cost categories including ground transport; proportional room cost split; one screenshot per section; color-coded budget remainder table; specific output filename.
- **Complex:** No reference files; multi-person technical production setup; equipment across multiple categories (e.g., core technical equipment, supporting hardware, cables/accessories); signal flow diagram required; cost breakdown as embedded PNG of Excel; budget under specific dollar cap; exclusion rules for equipment already owned.

## 5. Output Specification

### Primary Deliverable
- **Format:** Word document (.docx) or PDF
- **Structure:** Sequential sections by cost category, each with an embedded screenshot and itemized cost table; final section with budget summary table; total cost vs. funding cap comparison with visual indicators
- **Key quality signals:** Screenshots embedded per specified section; costs are itemized (not aggregated); proportional splits correctly calculated; budget remainder correctly computed; color-coding applied correctly (green/red based on comparison to funding cap); output filename matches specification; date of research documented

### Secondary Deliverables (if any)
- Embedded PNG of Excel cost breakdown spreadsheet (for production equipment variant)
- Signal flow chart in PNG format (for audio equipment procurement variant)

### Gold Output Characteristics
A gold output sources all prices from named or appropriate booking platforms, embeds a screenshot per cost category section (with date stamped), applies proportional cost-sharing correctly when multiple travelers share expenses for different durations, calculates the total cost accurately across all line items, and presents the budget comparison table with correct conditional formatting (green = department budget covers, red = requires supplemental funding). All specified constraints (hotel star rating, hotel proximity, flight class, equipment exclusions) are honored. The output file is named exactly as specified.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Traveler count | 1 person | 2 people, same duration | 2+ people, different attendance durations requiring proportional splits |
| Cost category count | 2 categories (registration + hotel) | 3–4 categories (registration, flight, hotel, transport) | 5+ categories (registration, multi-leg flights, ground transport, hotel, per diem, equipment) |
| Budget structure | Single fund, single cap | Two-fund structure (departmental + discretionary) | Multiple budget sources with per-category allocation rules |
| Evidence requirement | No screenshots | One screenshot per section | Per-item screenshot with date stamp on each |
| Calculation complexity | Simple sum | Proportional split by nights/days | Multi-variable split with cost-per-use allocation across participants |
| Output format | Bulleted list in Word | Sectioned Word document with tables | Embedded PNG charts/images within PDF |
| Constraint density | No exclusions | 1–2 constraints (hotel proximity, flight class) | 4+ constraints (hotel stars, block radius, proxy dates, exclusion of owned items, budget cap per person, color-coding logic) |

## 7. Boundary Cases & Adjacent Patterns

**F1 (Luxury Travel Itineraries):** F1 creates styled, experience-focused itineraries for client-facing delivery — the product is a planned experience with venue descriptions, photos, and scheduling detail. E5 creates cost estimation documents for budget approval — the product is a financial justification with evidence screenshots and arithmetic. F1 emphasizes experience curation; E5 emphasizes cost documentation. When the output includes a budget table, screenshots, and funding-vs-cost comparison, use E5.

**E2 (Curated Local Resource Guides):** E2 compiles reference directories of local services for ongoing use. E5 produces point-in-time cost estimates for a specific event or procurement decision. The difference is transactionality: E5 has an explicit budget, a specific purchase decision, and a deadline.

**B4 (Cost Analysis & Budget Reconciliation Reports):** B4 analyzes cost data from pre-provided reference files (rate cards, pricing spreadsheets) to compute variances or cost-effectiveness. E5 requires live web research to collect the cost data before any analysis can begin. If the prices are given in attached files, use B4; if the worker must find prices through web research with screenshots, use E5.

**D4 (Program & Evaluation Plans):** D4 may include budget sections within a program proposal but is primarily about program design and evaluation methodology. E5 is exclusively about cost research and budget documentation. If cost estimation is the entire deliverable rather than one section of a larger proposal, use E5.
