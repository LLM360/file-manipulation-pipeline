# Project Timeline & Milestone Planning

**Macro Category:** K — Scheduling, Space Planning & Logistics
**Pattern ID:** K4

## 1. Pattern Description

The worker creates a structured visual timeline or milestone-based plan for a bounded project or event, with a hard start date, a hard end date, sequenced phases, and a color-coding system that differentiates task types or ownership. The cognitive core is phase sequencing logic: some tasks must be completed before others can begin, some can overlap, revision rounds must be counted, and calendar exceptions (weekends, holidays) must be excluded from working-day calculations. The output is a standalone, visually readable planning artifact — a Gantt chart, countdown calendar, or color-coded schedule — designed to circulate to stakeholders for resource awareness and execution coordination. This pattern is distinct from K1 (Workforce Scheduling) in that it plans a one-time project, not a recurring personnel rotation; and distinct from K2 (Production Planning) in that the deliverable is a timeline document rather than a capacity-output projection.

## 2. O*NET Grounding

### Occupation Families
- 27-2012 Producers and Directors — create production schedules for video, audio, or live event projects with defined phases, review cycles, and delivery milestones
- 13-1082 Project Management Specialists — build Gantt charts and milestone plans for bounded projects across industries
- 41-1011 First-Line Supervisors of Retail Sales Workers — create countdown action plans for retail events (seasonal sales peaks, holiday season) with weekly milestones and team launch materials
- 11-2021 Marketing Managers — develop campaign timelines with phase dependencies and stakeholder review cycles
- 27-3043 Writers and Authors / 27-4032 Film and Video Editors — contribute to or manage production timeline design for creative projects

### Key Work Activities (O*NET vocabulary)
- Scheduling Work and Activities
- Planning and Prioritizing Work
- Coordinating Production Activities
- Communicating with Supervisors, Peers, or Subordinates
- Developing Objectives and Strategies
- Organizing, Planning, and Prioritizing Work

### Knowledge Domains (O*NET vocabulary)
- Administration and Management
- Communications and Media
- English Language
- Fine Arts (for creative production contexts)
- Sales and Marketing (for retail/event contexts)
- Production and Processing (for manufacturing/media contexts)

### Generalizable Work Context
Any organization managing a bounded project or event with a fixed delivery deadline: an advertising agency producing a client video, a retail store preparing for a promotional event, a software team planning a product release, or a nonprofit preparing for a fundraising campaign. The task is triggered when a project is kicked off (or is already underway) and stakeholders need a visual timeline to coordinate resources, set expectations, and track progress. The primary audience for the output is not the individual worker but a broader group: a client, a management team, or a department that needs to see the full picture at a glance.

## 3. Prompt Construction Template

### Persona Pattern
Assign a project lead, producer, manager, or coordinator role responsible for delivering a specific bounded output (a video, a retail event, a campaign launch). The persona has authority over the project timeline and is accountable to both internal stakeholders and external clients or leadership. Seniority: manager to senior manager level. The role should imply comfort with visual planning tools (Excel, Google Sheets, PDF export, project management software) and responsibility for stakeholder communication.

### Scenario Pattern
The scenario establishes: (1) the project type and its phases (pre-production, production, post-production; or preparation, event day, follow-up; or planning, execution, review), (2) the kickoff date and hard delivery deadline, (3) the specific task list with durations, (4) which tasks are internal vs. client-facing, (5) revision round requirements, and (6) any known calendar constraints (holidays, weekend exclusions). The trigger is either a project kickoff or a management request for a formal plan before the project begins.

### Instruction Pattern
Instructions specify: (1) the planning horizon (start date to end date), (2) the complete task list with durations in working days, (3) phase overlap rules (which tasks can run concurrently), (4) revision round counts and buffer days for client review, (5) the color-coding schema (by phase, by ownership, by status), and (6) the output format (PDF Gantt chart, Excel calendar, project management tool export). Instructions are most effective as a narrative intro establishing the project context, followed by assumptions/rules, then the complete task list, then color-coding and format requirements.

### Constraint Injection Points
- **Planning horizon:** 4–6 weeks (easy), 8–10 weeks (moderate), 12+ weeks with multiple phases (hard)
- **Task list size:** 5–10 tasks (easy), 15–25 tasks (moderate), 30+ tasks with sub-tasks (hard)
- **Phase overlap logic:** no overlap (strictly sequential), some concurrent tasks specified, complex overlap rules where certain phases must be N% complete before another begins
- **Calendar exclusions:** weekdays only (simple), weekdays + named federal/stat holidays (moderate), weekdays + holidays + client blackout periods (hard)
- **Revision rounds:** none (single pass), 1–2 rounds per deliverable, 3+ rounds with mandatory client review buffers after each
- **Color-coding system:** monochromatic (one color, shading for phases), two-category (internal/client), multi-category (one color per phase type + separate client color)
- **Visibility requirements:** no constraint, all tasks must be visible without scrolling/interaction, legend required
- **Dual deliverable:** single timeline only vs. timeline + companion planning document (e.g., team launch deck, strategic objectives brief)

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE]. You are responsible for delivering [PROJECT_TYPE] by [DEADLINE_DATE].

[SCENARIO]: The project kicked off on [START_DATE]. You need to create a [TIMELINE_TYPE: color-coded production schedule / multi-week countdown plan / Gantt chart] covering [START_DATE] through [END_DATE] for circulation to [AUDIENCE: client / department / management team].

[PROJECT ASSUMPTIONS]:
- Working days only: exclude weekends and [HOLIDAY_LIST]
- Hard start: [START_DATE]
- Hard deadline: [END_DATE]
- [PHASE OVERLAP RULES, e.g.: A later-phase task may begin before an earlier phase is fully complete]
- [REVISION RULE, e.g.: Allow [N] business days for client review after each deliverable]
- [COLOR-CODING RULE, e.g.: Use distinct colors per production phase; client tasks in a separate color]

[TASK LIST]:
Phase 1 — [PHASE_NAME]:
- [TASK_1]: [N] business days
- [TASK_2]: [N] business days
...

Phase 2 — [PHASE_NAME]:
- [TASK_3]: [N] business days
...

[Revision rounds]:
- [DELIVERABLE_1]: [N] rounds, [N]-day client review buffer per round
- [DELIVERABLE_2]: [N] rounds, [N]-day client review buffer per round

[COLOR-CODING SCHEMA]:
- [COLOR_1]: [PHASE/CATEGORY_1]
- [COLOR_2]: [PHASE/CATEGORY_2]
- [CLIENT_COLOR]: All client review or approval tasks
Include a legend.

[OUTPUT FORMAT]: [PDF / Excel / PowerPoint] — all tasks must be fully visible without user interaction.

[SECONDARY DELIVERABLE if applicable]: [DESCRIPTION — e.g., a multi-week preparation plan with a strategic-objectives section; a team launch deck for event day]
```

## 4. Reference File Requirements

### File Types Needed
- **Performance targets or KPI comparison document (pdf or xlsx):** Year-over-year targets and actuals; used in retail event planning to populate the strategic objectives and performance goals sections of the countdown plan and launch deck
- **Marketing or promotional materials document (pdf):** Campaign offers, discounts, or messaging; used to populate action items and promotional execution tasks in the timeline
- **Project brief or scope document (docx, optional):** Specifies deliverables, client requirements, and project parameters; may define the task list or phase definitions from which the timeline is built
- **Previous schedule or reference timeline (pdf or xlsx, optional):** Prior year's production schedule used as a structural template; relevant when the task asks the worker to adapt an existing format

### Data Characteristics
Many K4 tasks require no reference files at all — the task list and durations are provided inline in the prompt. When reference files are present, they are brief (1–5 pages or 10–30 rows) and contain qualitative information (promotional offers, performance goals) rather than large datasets. The primary data burden is the task list itself: typically 15–35 tasks with specific durations. Calendar knowledge (which dates are recognized federal or public holidays, when specific weekdays fall) must be applied accurately. Color-coding systems are specified by the prompt, not derived from data.

### File Complexity Spectrum
- **Minimal:** No reference files; 10–15 inline tasks; one color per phase; single-room planning horizon of 4–6 weeks; no client review buffers; weekdays only
- **Moderate:** 1–2 reference files (a performance-targets document + a promotional-materials document); 20–25 tasks; two-category color coding (internal/client); 8–10 week horizon; 1–2 revision rounds; named federal holidays excluded; single deliverable
- **Complex:** No reference files but 30+ inline tasks with complex overlap rules; multi-category color coding (5+ phase colors + separate client color); 12–16 week horizon; multiple revision rounds per deliverable (with the highest count on the most iteration-heavy task); multiple concurrent phase streams; all tasks must be visible without truncation; dual deliverable (timeline + companion document)

## 5. Output Specification

### Primary Deliverable
- **Format:** PDF (preferred) or Excel / PowerPoint exported to PDF; may be a Gantt-style bar chart or a calendar grid
- **Structure:** Rows = tasks or phases; columns = working days or weeks; colored bars or cells indicating duration; legend; hard start/end dates marked; revision rounds and client review buffers visible inline
- **Key quality signals:** All tasks sequenced correctly (dependent tasks respect predecessor completion); working-day math is accurate (correct task end dates given start date and duration, excluding weekends and holidays); color-coding matches stated schema; legend present; all tasks visible without interaction; revision round counts match specification

### Secondary Deliverables (if any)
- Companion planning document (PDF): a countdown action plan, strategic objectives brief, or team launch deck that draws on the same reference data as the timeline but is formatted for a different audience or use case (e.g., a team briefing on event day vs. a manager's multi-week preparation tracker)

### Gold Output Characteristics
A gold output has zero working-day arithmetic errors: every task starts the business day after its predecessor ends, every duration is correctly counted in business days, and all specified holidays are correctly excluded. Phase overlaps are applied exactly where specified and not elsewhere. Revision rounds are accounted for with the correct buffer days between the delivery of a draft and the start of the next task. The color-coding schema is applied consistently across all tasks, the legend matches the colors used, and all tasks are fully visible. In dual-deliverable tasks, both documents are consistent (the same performance goals appear in both the timeline and the companion deck).

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Planning horizon | 4–6 weeks | 8–10 weeks | 12–16 weeks |
| Task list size | 5–10 tasks | 15–25 tasks | 30+ tasks with sub-tasks |
| Phase overlap logic | Strictly sequential | A few concurrent pairs specified | Complex overlaps with partial-completion dependencies |
| Calendar exclusions | Weekdays only | Weekdays + named federal holidays | Weekdays + holidays + client blackout periods |
| Revision rounds | None | 1–2 rounds per deliverable | 3+ rounds with mandatory client review buffers after each |
| Color-coding system | Monochromatic / binary | 3–4 phase colors + client color | 5+ phase colors + client color + status overlay |
| Deliverable count | Single timeline | Timeline + brief narrative summary | Timeline + fully developed companion document (launch deck, strategic brief) |

## 7. Boundary Cases & Adjacent Patterns

**K2 (Production Planning & Recovery Scheduling):** Both produce timeline-based plans in Excel or PDF. The distinction is the nature of the work being planned. K2 plans manufacturing output (units produced per day, open orders fulfilled, capacity ramping) with quantitative throughput metrics as the central output. K4 plans project phases (scripting, shooting, editing, client review) with durations and dependencies as the central output. If the timeline tracks units produced or capacity utilization, use K2. If it tracks project phase completion, use K4.

**K3 (Space Assignment & Event Logistics):** K3 includes a timeline constraint in some variants (e.g., contractor sequencing by day). The key distinction is primary deliverable: K3's primary output is a spatial assignment (who goes where), and the timeline is a secondary constraint. K4's primary output is the timeline itself. If the main question the output answers is "when does each task happen," use K4. If it is "who occupies which space," use K3.

**D4 (Program & Evaluation Plans):** D4 produces multi-section program proposals with timelines as one section among many (objectives, methodology, budget, evaluation framework). K4 produces the timeline as the entire deliverable. If the timeline is embedded in a broader advisory or proposal document, use D4.

**C4 (Training Materials & Educational Presentations):** A dual-deliverable K4 variant pairs a team launch deck with the preparation timeline; the launch deck alone would be classified as C4 (training/instructional material). The pattern is K4 when the timeline is the primary deliverable and the companion document is secondary. If the companion document (team briefing, coaching guide) is the primary ask and the timeline is supplementary, reconsider C4 or D4.
