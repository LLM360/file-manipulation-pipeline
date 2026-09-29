# Curated Local Resource Guides

**Macro Category:** E — Research-to-Document Tasks
**Pattern ID:** E2

## 1. Pattern Description

The worker researches a geographically scoped set of real-world resources — restaurants, wineries, community service organizations, schools paired with nearby properties — and compiles the findings into a structured reference document with consistent per-entry multi-field data. The defining characteristic is the geographic constraint: all entries must fall within a defined location boundary (a city neighborhood, a drive-time radius, a zip code), often with a fixed origin point from which distances are measured. Entries require data collected from multiple web sources (business directories, mapping tools, MLS platforms, review aggregators), and the deliverable is formatted for repeated use as an operational reference rather than a one-time analytical output. The cognitive core is systematic data aggregation under geographic and category constraints, combined with formatting discipline across dozens of entries.

## 2. O*NET Grounding

### Occupation Families
- 39-6012 Concierges — restaurant and local attraction guides are a core concierge deliverable
- 21-1021 Child, Family, and School Social Workers — community resource guides for client referral are standard social work tools
- 41-9022 Real Estate Sales Agents — school profile reports and neighborhood guides are standard buyer representation materials
- 41-3041 Travel Agents — curated destination and accommodation guides mirror concierge resource compilation
- 11-9179 Lodging Managers — local vendor and amenity guides for guests

### Key Work Activities (O*NET vocabulary)
- Providing Information to Others
- Organizing, Planning, and Prioritizing Work
- Performing for or Working Directly with the Public
- Getting Information
- Documenting Information
- Searching for Information

### Knowledge Domains (O*NET vocabulary)
- Customer and Personal Service
- Geography
- English Language
- Sales and Marketing (for real estate and hospitality contexts)
- Education and Training (for school-focused guides)
- Sociology and Anthropology (for social services resource guides)

### Generalizable Work Context
A client-facing professional is asked to prepare a reference document for an audience (residents, guests, clients, buyers) who need to navigate local resources in an unfamiliar or specific geographic area. The trigger is typically an upcoming client interaction — a new resident moving in, a concierge guest arriving, a family shopping for a home — where the professional is expected to deliver curated, locally verified information rather than pointing the client to a search engine. The deliverable must be polished enough to be handed directly to the client or posted as a reference document.

## 3. Prompt Construction Template

### Persona Pattern
Assign a role whose professional value is local knowledge and curated recommendations: luxury concierge, social worker, real estate agent, community liaison. The persona should have an established client relationship that creates a clear motivation for producing the guide. Seniority level: individual contributor with direct client-facing responsibility.

### Scenario Pattern
A specific client, resident, buyer, or colleague needs locally scoped resource information that the professional is expected to compile. The origin point (hotel, agency address, service area) should be named explicitly. The audience and purpose should drive category selection — a new resident needs social services; a hotel guest needs dining; a homebuying family needs schools and nearby listings.

### Instruction Pattern
Describe the deliverable as a formatted document organized by category, then provide explicit per-entry data field requirements. List the exact column names for tables or the exact fields per entry. Specify the geographic scope precisely (city name, zip code, radius in miles, drive-time cap). Name the primary and supplemental web data sources. Note any exclusion rules (closed businesses, non-matching criteria). Specify typography or formatting requirements if applicable.

### Constraint Injection Points
- **Geographic scope:** single neighborhood vs. drive-time radius (e.g., a fixed number of minutes by car) vs. zip code boundary
- **Origin point:** fixed address from which all distances/times are measured
- **Category taxonomy:** named category labels with fixed vocabulary (dining tier names, service categories) vs. worker-determined categories
- **Per-entry field count:** 3 fields (minimal) to 9+ fields (full detail)
- **Entry count:** open-ended (all qualifying) vs. capped (top N)
- **Exclusion rules:** closed/inactive entries, non-compliant businesses
- **Formatting specificity:** exact font, size, color codes vs. general "professional formatting"
- **Hyperlink requirement:** name linked vs. no hyperlinks
- **Language requirement:** bilingual (English + Spanish) vs. English only
- **Photo/image requirement:** royalty-free header image vs. no images

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG/PROPERTY] serving [CLIENT TYPE] in [GEOGRAPHIC_AREA].

[SCENARIO]: [CLIENT CONTEXT — e.g., "A new resident is moving into our building" / "A family with school-age children is considering homes in the area"].

[TASK]: Create a [FORMAT] document titled "[DOCUMENT_TITLE]" that lists [RESOURCE_TYPE] in [GEOGRAPHIC_SCOPE].

[GEOGRAPHIC CONSTRAINT]: All entries must be within [RADIUS/DRIVE_TIME] of [ORIGIN_ADDRESS]. Use [MAPPING_TOOL] to calculate distances from this origin.

[DATA REQUIREMENTS]: For each entry, include the following fields:
- [FIELD_1] (e.g., Name, hyperlinked to website)
- [FIELD_2] (e.g., Address)
- [FIELD_3] (e.g., Phone Number)
- [FIELD_4] (e.g., Hours of Operation)
- [FIELD_5] (e.g., Description — 1-2 sentences)
- [FIELD_6] (e.g., Distance and Drive Time from [ORIGIN])
- [FIELD_7] (e.g., Category)

[ORGANIZATION]: Organize entries by [CATEGORY_TYPE]. Use the following category labels: [CATEGORY_1], [CATEGORY_2], [CATEGORY_3].

[DATA SOURCES]: Primary source: [PRIMARY_URL]. Supplemental sources: [SECONDARY_SOURCE_1], [MAPPING_TOOL].

[EXCLUSIONS]: Exclude any [RESOURCE_TYPE] that [EXCLUSION_RULE — e.g., "are permanently closed" / "do not offer tasting experiences"].

[FORMAT REQUIREMENTS]:
- Output format: [WORD / PDF]
- Maximum length: [N] pages
- Typography: [FONT_SPEC if applicable]
- [HYPERLINK / PHOTO / BILINGUAL] requirements as applicable
```

## 4. Reference File Requirements

### File Types Needed
- **None (web-research-driven):** All entry data is sourced from live web research. Prompts typically name specific websites as data sources.
- **Optional: Logo/branding image:** In real estate contexts, a company logo (webp or docx-embedded) may be provided as an attachment for inclusion in the report header.

### Data Characteristics
No structured data files are provided as input. The pipeline must simulate or describe the web research process. Each entry in the output will have: a name, address, phone number, business hours or contact info, a short description (1–3 sentences), and a distance/travel-time calculation from a fixed origin. Categories are predefined labels (dining tier, service type, school level). Geographic filtering is the primary selection criterion.

### File Complexity Spectrum
- **Minimal:** No reference files; 5–10 entries in one category; 3 fields per entry; single-page Word document; no formatting requirements beyond basic table.
- **Moderate:** No reference files; 15–30 entries organized into 4–6 categories; 5–7 fields per entry including hyperlinks and distance calculations; 3–4 page Word document with category headers and introductory text.
- **Complex:** No reference files (or logo image only); multiple resource types combined in one document (e.g., school data + nearby property listings); 5+ schools each with 8+ data fields plus 5–10 property listings per school; a per-school page cap × N sub-reports; branding incorporated.

## 5. Output Specification

### Primary Deliverable
- **Format:** Word document (.docx) or PDF
- **Structure:** Title/header section followed by category-organized tables or structured entries; consistent per-entry layout across all categories; often includes an introductory passage
- **Key quality signals:** All entries fall within the specified geographic boundary; distances/drive times are referenced from the correct origin address; exclusion rules applied (no permanently closed locations); all required fields populated; category labels match specified vocabulary; hyperlinks functional; formatting consistent across entries

### Secondary Deliverables (if any)
- Bilingual versions (English + Spanish) as separate files — social services context
- Map companion document (pins on a geographic map) — real estate context

### Gold Output Characteristics
A gold output contains only entries meeting all stated criteria (open businesses, correct geography, correct category), with all specified fields populated per entry, distances calculated from the stated origin, entries organized under correct category headings with the specified label vocabulary, hyperlinks on names where required, and consistent typography throughout. The document includes a title, introductory passage if specified, and any required footer text. Closed or out-of-scope entries are excluded without mention.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Entry count | 5–10 total | 15–30 total | 50+ across multiple reports or bilingual |
| Field depth per entry | 3 fields | 5–6 fields | 8–9 fields including distance calculation and hyperlink |
| Geographic scope | Single named area, no distance calculation | Radius constraint with calculated drive times | Exact drive-time cap requiring Google Maps per entry |
| Category structure | 1–2 categories | 4–6 categories with named labels | Multiple resource types per category (e.g., schools + homes combined) |
| Output count | Single document | Single document with bilingual variant | Multiple separate reports (e.g., one per school, one per category) |
| Source complexity | Single named website | Two distinct platforms | Three platforms (specialty directory + mapping + MLS) |
| Formatting requirements | Basic table | Consistent typography, font specs | Font/color/footer specs + royalty-free photo + branding logo |

## 7. Boundary Cases & Adjacent Patterns

**E3 (Market Research & Deal Sourcing):** E3 involves collecting quantitative market data (property financial metrics, pricing benchmarks) from commercial deal platforms and producing reports supporting investment or pricing decisions. E2 compiles operational service-directory information (contact details, hours, descriptions) for client reference use. When the output is a navigational/reference guide for a client rather than an analytical report for a transaction decision, choose E2.

**F1 (Luxury Travel Itineraries):** F1 produces styled, personalized multi-day itineraries with scheduling logic, photos, and curated vendor selections for a specific client trip. E2 produces comprehensive, category-organized reference directories intended for repeated use by multiple clients. F1 is a bespoke one-off; E2 is a reusable reference resource.

**G4 / C5 (Form & Template Design):** Social services contexts can overlap — a social worker may produce both a needs assessment form (C5) and a resource guide (E2) in the same task. The resource guide component is E2 when it requires web research to compile local contact information; if it merely designs a form structure with no data collection, it belongs in C5.

**E4 (Regulatory Data Extraction):** E4 extracts from government regulatory portals (state boards, CMS, EPA) and produces compliance-oriented comparison tables. E2 aggregates service-directory information from consumer-facing platforms (Google Maps, Niche, Yelp) and produces operational reference documents. The source type and downstream use distinguish the two.
