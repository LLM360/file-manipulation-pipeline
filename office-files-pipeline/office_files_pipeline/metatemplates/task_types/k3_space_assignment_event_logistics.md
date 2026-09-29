# Space Assignment & Event Logistics

**Macro Category:** K — Scheduling, Space Planning & Logistics
**Pattern ID:** K3

## 1. Pattern Description

The worker assigns entities (vendors, contractors, tenants, booths) to physical spaces (tables, rooms, units, floors) while satisfying a layered set of spatial constraints: location preferences, utility access requirements (electricity, water), adjacency rules (no same-type neighbors, required proximity to specific others), and timeline sequencing where the assignment must be completed before work begins. The cognitive core is constraint-driven spatial matching — a combinatorial problem where each entity has one or more attributes that restrict which spaces it can occupy, and placing any single entity can create or resolve conflicts for others. What distinguishes K3 from K1 (Workforce Scheduling) is that the scarce resource is physical space, not staff time; and from K4 (Project Timeline Planning) in that the primary output is a spatial map or assignment table, not a temporal Gantt chart. The output is always a dual artifact: a visual floor plan or unit layout showing who occupies which space, plus a structured data file (Excel or table) recording the assignment formally.

## 2. O*NET Grounding

### Occupation Families
- 11-9141 Property, Real Estate, and Community Association Managers — coordinate unit turn scheduling, vendor assignments, and space allocation in residential and commercial properties
- 13-1121 Meeting, Convention, and Event Planners — assign vendor spaces, booth assignments, and room layouts for events and conventions
- 39-9032 Recreation Workers — plan space allocation for recreation programs, bazaars, and community events in multi-room facilities
- 11-3011 Administrative Services Managers — oversee facility space planning and resource allocation across departments or operational units
- 43-9021 Data Entry Keyers / 11-9199 Managers, All Other — perform the data reconciliation between spatial plans and record-keeping systems

### Key Work Activities (O*NET vocabulary)
- Scheduling Work and Activities
- Coordinating Special Events
- Analyzing Data or Information
- Communicating with the Public or Vendors
- Documenting Information
- Resolving Conflicts and Negotiating with Others
- Organizing, Planning, and Prioritizing Work

### Knowledge Domains (O*NET vocabulary)
- Administration and Management
- Customer and Personal Service
- Building and Construction
- Mathematics
- English Language

### Generalizable Work Context
Any organization that manages a shared physical facility and must allocate space among multiple external parties simultaneously — a property management company coordinating unit repairs during a turn cycle, a recreation department assigning vendor tables for a community event, or a convention center allocating booth space for a trade show. The task is triggered by an upcoming event date or occupancy deadline. Stakeholders include the facility manager or owner (needs the plan before the event), external vendors or contractors (have preferences or constraints they've communicated in advance), and operational staff who will execute the plan on the day.

## 3. Prompt Construction Template

### Persona Pattern
Assign a coordination or management role responsible for a specific physical facility. The persona has received information from multiple parties (vendors, contractors, residents) about their requirements and preferences. Seniority: manager, coordinator, or senior agent level — someone with decision-making authority over space allocation. The role should imply responsibility for both the logistics plan and the record-keeping that follows.

### Scenario Pattern
The scenario trigger is an upcoming event, turn cycle, or planning deadline. A set of entities (vendors, contractors, units) need to be placed in a set of physical spaces within a defined timeframe. One or more parties have communicated preferences or constraints (location preference, utility need, adjacency request). The worker must resolve all constraints and produce an official assignment before work begins.

### Instruction Pattern
Instructions specify: (1) the entities to be assigned (with attributes: preference, utility need, adjacency request, count of spaces needed), (2) the available spaces (with attributes: location, utility access, capacity), (3) constraint rules (no same-type adjacent, electricity limits, no two contractors same day per unit), (4) the dual-output requirement (visual layout updated + data file updated), and (5) any timeline constraints (sequencing rules for work phases). Instructions are most effective as a narrative scenario followed by an enumerated constraint list, then a deliverable specification.

### Constraint Injection Points
- **Location preference:** binary (one room vs. another; unit vs. common area) vs. ranked preference vs. hard requirement
- **Utility access:** no electricity constraint (trivial), limited outlets (moderate), outlet locations mapped on floor plan (hard — placement-specific)
- **Adjacency rule:** no same-type adjacent (diversity constraint) vs. must be adjacent to specific vendor (proximity request) vs. both simultaneously
- **Entity count per space:** each entity needs exactly 1 space (simple) vs. some entities need 2+ contiguous spaces (adds spatial reasoning)
- **Number of spaces/rooms:** single room (easy), two rooms with distinct characteristics (moderate), three or more zones with different utility and capacity profiles (hard)
- **Timeline sequencing:** no sequencing constraint (purely spatial) vs. contractor sequencing rules (no two vendors same day per unit, appliance delivery before installation) vs. multi-phase dependency chain
- **Output format:** text list (easy), updated spreadsheet only (moderate), annotated PDF floor plan + updated spreadsheet (hard)

### Structural Template

```
[PERSONA]: You are a [ROLE] at [FACILITY/ORG_TYPE]. You are responsible for planning [EVENT/CYCLE_TYPE] at [FACILITY_NAME].

[SCENARIO]: [EVENT/CYCLE] is scheduled for [DATE/PERIOD]. You have [N] [ENTITIES: vendors/contractors/units] to place in [M] available [SPACES: tables/units/rooms]. Each [ENTITY] has communicated their requirements, which you must honor.

[AVAILABLE SPACES]:
- [SPACE_TYPE_1]: [N1] spaces, [UTILITY_ATTRIBUTE], [LOCATION_ATTRIBUTE]
- [SPACE_TYPE_2]: [N2] spaces, [UTILITY_ATTRIBUTE], [LOCATION_ATTRIBUTE]
[See attached [FLOOR_PLAN] for numbered positions.]

[ENTITY REQUIREMENTS]:
[See attached [VENDOR_LIST / UNIT_SCHEDULE] for each entity's: location preference, utility needs, number of spaces, and special requests.]

[ASSIGNMENT RULES]:
1. [DIVERSITY RULE: e.g., No two vendors selling the same product type may be assigned adjacent spaces]
2. [UTILITY RULE: e.g., Only tables near electrical outlets may be assigned to vendors requiring electricity]
3. [ADJACENCY RULE: e.g., Vendors who requested proximity to a specific other vendor should be placed adjacent where possible]
4. [CAPACITY RULE: e.g., Vendors with multiple tables must receive contiguous table numbers]
5. [TIMELINE RULE if applicable: e.g., No two contractors may work in the same unit on the same day]

[DELIVERABLES]:
1. Updated [FLOOR PLAN PDF / VISUAL LAYOUT]: Annotate each [space] with the assigned [entity name]
2. Updated [SPREADSHEET / TABLE]: Add a "[Table Assignment / Assigned Unit]" column to the [ENTITY_LIST], listing the assigned [space number(s)] for each [entity]

[OUTPUT SPECIFICATION]: [PDF with annotations] + [xlsx with added column], ready for [distribution to vendors / review by manager].
```

## 4. Reference File Requirements

### File Types Needed
- **Floor plan PDF(s):** Visual layout of the physical space with pre-numbered positions (tables, units, rooms); may show utility outlet locations; used to perform the spatial assignment and annotate the output; one file per distinct space (e.g., a separate floor plan for each room or zone)
- **Entity attribute spreadsheet (xlsx):** One row per entity (vendor, contractor, resident) with columns for: name/ID, product type or service category, number of spaces needed, location preference, utility requirement (boolean), and special requests (free text); this is the primary data source for constraint reading
- **Inspection or status report (pdf or xlsx, optional):** Per-unit work requirements, appliance orders, or repair items; used in property management turn-scheduling variants to determine what each unit needs and from which contractors
- **Vendor/contractor availability schedule (pdf or xlsx, optional):** Days/windows when each contractor is available; used in scheduling variants to enforce no-conflict rules

### Data Characteristics
The entity count is typically 10–50 (vendors at a bazaar, contractors for a unit turn cycle). The space count is typically slightly larger than the entity count, leaving some unassigned spaces. Entity attributes are mostly categorical (location preference: primary room/secondary room; electricity: yes/no; product type: crafts/apparel/food/etc.) with occasional free-text requests. Floor plan PDFs are spatial documents: the pipeline needs pre-numbered table position files, not generic room images. For property management variants, inspection reports have 3–15 line items per unit across 4–10 units.

### File Complexity Spectrum
- **Minimal:** Single room, 10–15 vendors, no electricity constraint, no same-type rule, output is an updated spreadsheet only (no annotated floor plan)
- **Moderate:** Two distinct rooms with different profiles, 20–35 vendors with mixed electricity needs, same-type adjacency rule, some proximity requests, dual output (annotated floor plans + updated spreadsheet)
- **Complex:** Multiple spaces with distinct utility profiles, 40+ entities including some requiring contiguous multi-space assignments, electricity outlet positions mapped to specific table numbers, multiple constraint types active simultaneously (diversity + utility + proximity + capacity), contractor scheduling with no-conflict rules, multi-phase timeline with dependency chain

## 5. Output Specification

### Primary Deliverable
- **Format:** Annotated PDF (floor plan) + updated Excel spreadsheet (.xlsx)
- **Structure:** PDF shows the physical space with each assigned position labeled by entity name; spreadsheet adds one or more assignment columns to the original entity list
- **Key quality signals:** Every constraint is satisfied for every entity (location preference honored, electricity-requiring entities placed near outlets, no same-type adjacency, proximity requests honored where feasible); every entity has an assigned space; no space is double-assigned; multi-space entities have contiguous assignments

### Secondary Deliverables (if any)
- Written conflict log or notes column in the spreadsheet flagging any constraints that could not be fully satisfied and the reason why
- Scheduling timeline (for property management variants) showing which contractor works in which unit on which day

### Gold Output Characteristics
A gold output assigns every entity to a valid space with no constraint violations, or explicitly documents which constraints were relaxed and why. The floor plan annotation is complete and matches the spreadsheet assignment column exactly. In property management variants, the timeline is sequenced correctly (appliance deliveries before installation, no two contractors in same unit same day, on-site staff on Mon–Fri only) and the make-ready date impact is flagged if the constraint chain pushes the timeline past the original date.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Number of spaces/rooms | 1 room | 2 rooms with distinct profiles | 3+ zones with different utility and capacity attributes |
| Entity count | 5–10 | 15–30 | 40+ |
| Constraint types active | 1 (location preference only) | 2–3 (location + utility + diversity) | 4+ (location + utility + diversity + proximity + capacity + timeline) |
| Utility access detail | Boolean (yes/no, anywhere) | Outlet-near-specific-tables only | Outlet positions mapped on floor plan, limited count |
| Multi-space entities | None (all entities = 1 space) | A few entities need 2 adjacent spaces | Multiple entities need 2–4 contiguous spaces |
| Output format | Updated spreadsheet only | Spreadsheet + text assignment list | Annotated PDF floor plan + updated spreadsheet |
| Timeline sequencing | No sequencing | Simple ordering (A before B) | Full dependency chain with daily conflict rules and milestone flags |

## 7. Boundary Cases & Adjacent Patterns

**K1 (Workforce Scheduling with Constraint Satisfaction):** Both involve constraint satisfaction, but K1 is temporal (who works which day) and K3 is spatial (who occupies which space). If the primary output is a calendar grid, use K1. If the primary output is a floor plan annotation or space assignment table, use K3.

**K4 (Project Timeline & Milestone Planning):** Variants with a timeline dependency chain (e.g., contractor sequencing by day) superficially resemble K4. The distinction is that K4 produces a Gantt-style project timeline as the primary deliverable, while K3 uses a timeline to constrain a spatial assignment. The primary output in K3 is always the space assignment (who goes where), not the timeline itself.

**B3 (Compliance Report from Transaction Data):** Some K3 variants also generate a structured report from multiple source documents. The distinction from B3 is that K3's report output is a logistics plan (who works where/when) rather than a compliance finding or exception narrative. If the deliverable is primarily a compliance finding with regulatory citations, use B3. If it is a logistics assignment plan, use K3.

**F1 (Luxury Travel Itineraries):** Both K3 and F1 involve scheduling multiple activities or vendors across a timeline. The distinction is that F1 is client-facing, experience-oriented, and research-driven; K3 is operationally-oriented, constraint-driven, and based on pre-gathered data files rather than web research.
