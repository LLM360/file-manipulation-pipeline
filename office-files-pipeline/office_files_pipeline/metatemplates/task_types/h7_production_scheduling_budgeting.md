# Production Scheduling & Budgeting

**Macro Category:** H — Creative & Media Production
**Pattern ID:** H7

## 1. Pattern Description

The worker creates a production planning artifact — either a visual production schedule (Gantt/calendar) or a detailed cost breakdown (Excel budget) — for a media production project. The visual schedule sub-pattern is a color-coded production schedule spanning a defined date range with 30+ tasks organized by phase, client vs. internal responsibility, and federal holiday exclusions. The cost breakdown sub-pattern is an Excel cost breakdown applying a rate sheet to a defined crew configuration and video series list. The cognitive core in both cases is structured decomposition and constraint satisfaction: breaking a complex production into phases and line items, then satisfying multiple simultaneous constraints (date exclusions, rate card accuracy, overlap logic, color-coding systems, revision round counts). What distinguishes this pattern from general project management tasks (Macro Category E) is the domain specificity: the tasks require knowledge of video production workflows (phase sequencing, crew roles, post-production stages) to produce plausible and complete plans.

## 2. O*NET Grounding

### Occupation Families
- 27-2012 Producers and Directors — primary occupation; production scheduling and budgeting are core producer functions
- 13-1082 Project Management Specialists — adjacent; the scheduling work is project management applied to media production
- 13-2031 Budget Analysts — relevant for cost estimation and rate card application tasks
- 27-4032 Film and Video Editors — adjacent when post-production scheduling requires editorial expertise
- 11-9021 Construction Managers — analogous; manages multi-phase projects with resource allocation (different domain, same cognitive pattern)

### Key Work Activities (O*NET vocabulary)
- Scheduling Production Activities and Resources Across Multiple Phases
- Estimating Costs and Developing Budgets for Production Projects
- Planning Work Sequences and Identifying Phase Dependencies
- Coordinating Internal and Client-Facing Task Timelines
- Applying Rate Cards and Fee Schedules to Variable Crew Configurations
- Identifying and Excluding Non-Work Days (holidays, weekends) from Schedules
- Developing Color-Coded Visual Planning Artifacts for Team Communication
- Managing Multiple Concurrent Workstreams with Overlapping Timelines

### Knowledge Domains (O*NET vocabulary)
- Communications and Media (production phase vocabulary, crew roles)
- Mathematics (date calculation, cost arithmetic, duration aggregation)
- Fine Arts (production workflow knowledge)
- English Language (task naming, document structure)
- Administration and Management (resource planning, scheduling tools)

### Generalizable Work Context
A producer or production coordinator at an advertising agency, media company, or production house is assigned to create a planning document for a new project. The trigger is project kickoff or client scope approval. For scheduling tasks, the trigger is a confirmed start date and delivery deadline with a defined scope; the producer must sequence all production tasks within this window. For budgeting tasks, the trigger is receipt of a client video list and a rate sheet; the producer must calculate costs for the defined scope. Stakeholders include the client (reviews schedule/budget for approval), internal production team (executes against the schedule), and finance/accounting (uses budget for billing).

## 3. Prompt Construction Template

### Persona Pattern
Assign the worker as a video producer or production coordinator at an advertising agency or production company. The persona should reflect a client-services context — the producer is creating the plan for a specific project that has been scoped with a client. Specify the type of project (live-action B2B video, educational series, music video) as this determines which production phases apply.

### Scenario Pattern
For scheduling tasks: a project has been kicked off with a confirmed start date and delivery date; the producer must build the complete production schedule showing all phases, tasks, and durations within that window. For budgeting tasks: a client has provided a list of videos to produce; the producer must calculate the cost of delivering this scope based on the organization's standard rate sheet.

Two scenario sub-patterns:
- **Visual schedule:** Hard start/end dates, defined task list with durations, phase overlap logic, client review/revision rounds, holiday exclusions, color-coding schema.
- **Cost breakdown:** Defined crew configuration, rate sheet provided, scope list provided, pre-production only vs. full production scope, line-item Excel output.

### Instruction Pattern
For schedules: enumerate the complete task list with durations, specify the date range and exclusion rules, describe the color-coding system, and specify any overlap logic (phases that run concurrently). For cost breakdowns: describe the crew configuration, scope boundary, and reference file roles (rate sheet, video list); the output structure (Excel with line items and totals) should be specified.

### Constraint Injection Points
- **Date exclusions:** Weekends only vs. weekends + specified public holidays; requires knowledge of actual calendar for a given date range
- **Phase overlap:** Fully sequential (no overlaps) vs. specified phases run concurrently (e.g., casting and location scouting concurrent with scripting)
- **Client vs. internal task differentiation:** No distinction vs. separate color for client tasks vs. separate column/row for client tasks
- **Revision round count:** Single revision vs. multiple rounds per deliverable type (e.g., fewer rounds for an earlier-stage deliverable and more rounds for the deliverable that typically draws the most client feedback)
- **Color-coding schema:** Monochrome (phase names only) vs. color-per-phase vs. color-per-phase + separate client task color
- **Visibility constraints:** All tasks visible without truncation vs. scrollable view acceptable
- **Scope boundary (budgeting):** Pre-production only vs. pre-production + production vs. full production + post
- **Crew configuration (budgeting):** Fixed and specified vs. variable per video type vs. scaled by day count
- **Rate card type:** Simple flat day rates vs. variable rates by role + equipment + setup time

### Structural Template

```
[PERSONA]: You are a [ROLE: video producer / production coordinator] at [ORG: advertising agency / production company / media organization].

[PROJECT_CONTEXT]: You are [building a production schedule / creating a cost estimate] for a [PROJECT_TYPE: live-action B2B video / educational video series / music video] for client [CLIENT_TYPE: brand, music artist, organization].

[REFERENCE_FILES (if applicable)]:
- [FILE_1]: [e.g., "Video series list (PDF) — list of all educational videos in the series with titles and descriptions"]
- [FILE_2]: [e.g., "Service fee rate sheet (PDF) — standard crew and equipment day rates for the organization"]

[SCHEDULE_TASK_LIST (for scheduling variant)]:
Phase [PHASE_NAME] ([DURATION]):
- Task: [TASK_NAME] ([N] days) [CLIENT/INTERNAL designation]
- Task: [TASK_NAME] ([N] days) [CLIENT/INTERNAL]
- ...
Phase [PHASE_NAME]:
- ...

[ASSUMPTIONS AND CONSTRAINTS]:
- Project start date: [DATE] (kickoff call)
- Project delivery date: [DATE] (final delivery)
- No work on: weekends; [HOLIDAY_LIST: US federal holidays in the date range, or specified regional holidays]
- [PHASE_OVERLAP: phases X and Y may run concurrently]
- [REVISION_ROUNDS: [N]x [deliverable] revisions, [M]x [deliverable] revisions]
- [COLOR_SCHEMA: phase-specific colors per attached legend; client review tasks in [COLOR]]
- [VISIBILITY: all tasks must be visible without user interaction — no "+X more" truncation]

[CREW_CONFIGURATION (for budgeting variant)]:
- [ROLE_1]: [billing rate and conditions per rate sheet]
- [ROLE_2]: [billing rate]
- [EQUIPMENT_1]: [day rate]
- Setup time: [N–M hours per shoot day, billable at [RATE]]
- [SCOPE_BOUNDARY: e.g., pre-production only; specific phases or crew roles explicitly excluded]

[OUTPUT_SPECIFICATION]:
For scheduling: [PDF (visual calendar or Gantt chart)] with full color-coding system visible, all tasks present without truncation, covering [START_DATE] through [END_DATE]
For budgeting: [Excel spreadsheet] with line-item cost breakdown per video / per shoot day, rate-card-accurate totals, and summary of full series cost
```

## 4. Reference File Requirements

### File Types Needed
- **Video series / scope list (PDF):** A document listing all videos in the production scope with titles and brief descriptions. Used in budgeting tasks to determine the number of shoot days and items to cost. Should contain 5–20 distinct video items with enough description to understand scope (e.g., duration, subject, special requirements).
- **Service fee rate sheet / rate card (PDF):** The organization's standard pricing document listing crew roles (producer, camera operator, audio tech) and equipment (cameras, audio kit) with their day rates, hourly rates, and any applicable conditions (minimum call times, overtime). Should cover all roles referenced in the crew configuration. Rates should be realistic for the industry segment (e.g., $400–$1,200/day for crew roles, $200–$600/day for equipment).
- **No reference files needed (schedule variant):** Production schedule tasks of this type derive all inputs from the prompt description alone — no attached files are needed. The task list, durations, and date range are all specified inline.

### Data Characteristics
Rate sheets should list 5–12 distinct roles or equipment items with clearly defined billing units (per day, per hour, flat fee). Rates should be internally consistent (senior roles priced higher than junior, equipment bundles cheaper than à la carte). Video series lists should contain enough variety that different videos might have different resource implications, but the crew configuration specified in the prompt should apply uniformly to normalize the calculation. Production schedules should have 25–40 tasks with durations of 1–10 days each, organized into 4–7 named phases covering the full production lifecycle from kickoff through delivery.

### File Complexity Spectrum
- **Minimal (scheduling):** 10–15 tasks, 2–3 phases, no phase overlap, weekends only excluded, single color per phase, output as simple Gantt.
- **Moderate (scheduling):** 20–30 tasks, 4–5 phases, some specified overlaps, weekends + public holidays excluded, client vs. internal color distinction, client review buffers specified.
- **Complex (scheduling):** 30+ tasks, 6+ phases, multiple specified phase overlaps, weekends + named holidays excluded, multi-dimension color system (phase color + client color), multiple revision round counts per deliverable type, visibility requirement, hard start/end dates.
- **Minimal (budgeting):** 3–5 videos, flat day rate only, one crew role, no setup time.
- **Moderate (budgeting):** 8–12 videos, 3–4 crew roles with different rates, setup time included, total and per-video subtotals.
- **Complex (budgeting):** 15+ videos, 5+ roles, equipment costs, setup time variable per day, scope boundary conditions (pre-production only), summary sheet + detail sheet in Excel.

## 5. Output Specification

### Primary Deliverable
- **Format (scheduling):** PDF (visual production schedule — calendar or Gantt format)
- **Format (budgeting):** Excel spreadsheet (.xlsx)
- **Structure (scheduling):** Complete visual timeline with color-coded phase blocks, task labels, durations, and date boundaries; a legend showing color meanings; all tasks visible without overflow; client tasks differentiated from internal tasks
- **Structure (budgeting):** Line-item rows for each crew role and equipment item; columns for rate, quantity (days/hours), and extended cost; video-level or phase-level subtotals; overall project total
- **Key quality signals (scheduling):** All specified tasks present; correct durations applied; no weekend or holiday work days included; phase overlaps correctly implemented; color-coding matches specified schema; all tasks visible (no overflow truncation); hard start/end dates respected
- **Key quality signals (budgeting):** Rate card values applied accurately (no invented rates); all specified crew roles included; setup time calculated correctly; scope boundary honored (no post-production costs if pre-production only); totals correctly sum line items

### Secondary Deliverables (if any)
- None for this pattern. Some production contexts include a companion Word document (cover page, assumptions summary), but the primary deliverable is the schedule or budget artifact itself.

### Gold Output Characteristics
A gold production schedule is visually legible to a non-technical viewer: phase blocks are clearly color-coded, task names are readable at normal viewing size, client review tasks are visually distinct, and the timeline runs without gaps or date errors from start to finish. Every holiday in the specified date range has been correctly excluded. The specified revision rounds and client review buffers appear at the correct points in the sequence. Phase overlaps are accurately represented (concurrent tasks appear at the same time, not sequentially). A gold cost breakdown applies every rate from the rate sheet exactly as specified, with no rounding errors or missing line items. The scope boundary is cleanly enforced (no post-production line items if pre-production only was specified). Setup time is included in every shoot day's calculation at the specified rate.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Task count | 10–15 tasks, 2–3 phases | 20–30 tasks, 4–5 phases | 30+ tasks, 6+ phases |
| Date exclusions | Weekends only | Weekends + 2–3 named holidays | Weekends + full federal holiday calendar for specified period |
| Phase overlap | No overlaps (fully sequential) | 1–2 specified concurrent phases | Multiple overlapping phases with specified start points |
| Color-coding | Single color scheme | Phase colors + client task color | Multi-layer color system (phase + task type + client indicator) |
| Rate card complexity | Flat day rate for 1 role | 3–4 roles with different rates | 6+ roles + equipment + variable setup time |
| Scope boundary | Entire production lifecycle | Pre-production only | Pre-production only with an explicit exclusion list (e.g., specific crew roles or line items marked out of scope) |
| Deliverable format | Simple list or table | Calendar or basic Gantt | Styled PDF with legend, color blocks, and fully visible task labels |

## 7. Boundary Cases & Adjacent Patterns

- **E-category (Project & Workflow Management):** Macro Category E covers project management artifacts (project plans, workback schedules, resource allocation tables) across all industries. H7 is specifically video/media production scheduling and budgeting — the domain knowledge of production phases (pre-production, production, post), crew roles, and rate cards is required. If the scheduling task could apply equally to any industry (construction, software development, consulting), it belongs in E. If it requires production phase knowledge (script → production → VFX → color → delivery), it belongs in H7.
- **B4 (Cost Analysis & Budget Reconciliation Reports):** B4 involves analyzing existing cost data against a budget, often producing variance analysis or recommendations. H7 is prospective — building a budget or schedule before the work happens, not analyzing after. If the task is "here's what was spent, analyze it," it's B4. If the task is "here's what we plan to produce, estimate the cost," it's H7.
- **H1 (Broadcast Commercial & Video Editing):** H1 produces the video deliverable; H7 produces the plan for delivering it. In the production lifecycle, H7 comes first. No overlap in output type.
- **A5 (Operational Metrics Dashboard / KPI Reporting):** Both can produce Excel outputs with structured data. A5 transforms historical operational data into dashboards; H7 builds prospective cost estimates from rate cards. The inputs and cognitive work are different: A5 analyzes existing data; H7 applies pricing formulas to defined scope.
- **H6 (Moodboard & Visual Direction):** H6 and H7 are both pre-production tasks, but H6 is about creative direction and H7 is about planning and budgeting. Both belong to the same workflow phase but require entirely different skills. No realistic overlap in outputs.
