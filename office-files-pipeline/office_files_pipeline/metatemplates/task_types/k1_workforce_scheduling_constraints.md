# Workforce Scheduling with Constraint Satisfaction

**Macro Category:** K — Scheduling, Space Planning & Logistics
**Pattern ID:** K1

## 1. Pattern Description

The worker builds a multi-period personnel schedule — spanning days, weeks, or months — that satisfies simultaneous, often competing constraints: rotation patterns (e.g., 5-on/2-consecutive-off), minimum daily coverage requirements, named time-off requests, and visual differentiation rules. The cognitive core is constraint satisfaction: every cell in the output schedule must respect all applicable rules at once, and conflicts must be explicitly flagged rather than silently violated. What makes this pattern distinct from K2 (Production Planning) is that the scarce resource is people, not machines or output volume — the task is about who works when, not what gets made when. The output is always a structured, color-coded visual artifact (typically an Excel calendar) that a manager can read at a glance to verify coverage.

## 2. O*NET Grounding

### Occupation Families
- 11-3011 Administrative Services Managers — oversee workforce scheduling, coverage planning, and operational calendars in a wide variety of organizations
- 51-1011 First-Line Supervisors of Production and Operating Workers — create and manage shift schedules for factory/processing floor personnel, often with complex rotation patterns
- 39-9032 Recreation Workers — coordinate part-time or seasonal staff schedules for programs with variable hours and minimum coverage requirements
- 11-9199 Managers, All Other — program coordinators and department leads who must schedule small teams (interns, specialists) across multi-week cycles

### Key Work Activities (O*NET vocabulary)
- Scheduling Work and Activities
- Coordinating Work and Activities of Others
- Documenting Information
- Monitoring and Controlling Resources
- Making Decisions and Solving Problems
- Communicating with Supervisors, Peers, or Subordinates

### Knowledge Domains (O*NET vocabulary)
- Administration and Management
- Personnel and Human Resources
- Mathematics
- Production and Processing (where applicable)
- Computers and Electronics (for Excel-based delivery)

### Generalizable Work Context
Any organization running a small team (3–30 people) on a rotating or recurring schedule across a defined planning horizon (one week to six months). The trigger is either a new planning period beginning, a staff change requiring schedule reconstruction, or a coverage audit revealing gaps. Stakeholders include the scheduler's direct manager, the scheduled employees (who have submitted time-off requests), and any downstream operational teams who depend on minimum coverage. The organization may be a production facility, a recreation department, a clinical unit, or any service operation with predictable demand cycles.

## 3. Prompt Construction Template

### Persona Pattern
Assign a supervisory or coordinating role with direct authority over a small, named team. The role should imply responsibility for both daily operations and personnel management. Seniority: first-line supervisor, program coordinator, department manager, or equivalent. The persona should be plausibly the person who both receives time-off requests and creates the official schedule.

### Scenario Pattern
The scenario trigger is the opening of a new scheduling period (e.g., a season, a quarter, a month) or a coverage problem surfaced by management. Named employees with distinct time-off requests have been identified. A recurring constraint (rotation pattern, minimum daily coverage, shift length) is in effect. The task is to produce the official schedule before the period begins.

### Instruction Pattern
Instructions specify: (1) the scheduling horizon and output format (Excel with tabs by month or week), (2) the rotation rule (e.g., 5-on/2-consecutive-off), (3) minimum coverage per day, (4) per-employee time-off dates, (5) the color-coding schema, and (6) a coverage-gap flagging requirement. Instructions are most effective as a numbered constraint list after a narrative intro. Deliverable is a single workbook with one tab per time unit plus one summary tab.

### Constraint Injection Points
- **Rotation pattern:** varies from simple (Mon–Fri only) to complex (5-on/2-off rolling, staggered starts per employee, different shift lengths)
- **Team size:** 2–5 employees makes constraint conflicts tractable; 6–15 adds combinatorial difficulty
- **Time-off requests:** zero to four days per employee; consecutive vs. non-consecutive; overlapping vs. non-overlapping across employees
- **Coverage minimum:** one person (trivial), two people (moderate tension), N-1 of team (near-impossible some days)
- **Planning horizon:** one month (easy), three months (moderate), five or six months (hard — pattern drift and holiday accumulation)
- **Color-coding complexity:** two states (working/off) vs. three states (working/scheduled off/requested off) vs. four+ states (working/off/holiday/training)
- **Flagging behavior:** flag any coverage-deficient day with a note vs. automatically escalate vs. no flag required

### Structural Template

```
[PERSONA]: You are a [ROLE] at [ORG_TYPE], supervising a team of [N] [STAFF_TYPE].

[SCENARIO]: The [SEASON/PERIOD] is beginning and you need to produce the official [HORIZON]-month schedule for your team: [NAME_1], [NAME_2], and [NAME_3]. Each team member works a [ROTATION_PATTERN] rotation (e.g., 5 days on, 2 consecutive days off).

[DELIVERABLE]: Create an Excel workbook (.xlsx) with [N+1] tabs:
- One tab per [month/week] covering [START_DATE] through [END_DATE]
- One tab listing all time-off requests

[SCHEDULING RULES]:
1. All team members follow a [ROTATION_PATTERN] pattern
2. At least [COVERAGE_MIN] team members must be present each working day
3. Days with fewer than [COVERAGE_MIN] team members must be flagged in the schedule

[TIME-OFF REQUESTS]:
- [NAME_1]: [DATE_1], [DATE_2], ...
- [NAME_2]: [DATE_3], [DATE_4], ...
- [NAME_3]: [DATE_5], [DATE_6], ...

[COLOR-CODING]:
- [COLOR_1] / "[LABEL_1]": [STATE_1 description]
- [COLOR_2] / "[LABEL_2]": [STATE_2 description]
- [COLOR_3] / "[LABEL_3]": [STATE_3 description]
Include a legend on the first tab.

[OUTPUT SPECIFICATION]: Excel workbook (.xlsx), [N+1] tabs, color-coded cells, legend on first tab, coverage-gap flags visible inline.
```

## 4. Reference File Requirements

### File Types Needed
- **Employee roster (xlsx or inline):** Names, roles, any skill or seniority attributes relevant to coverage; used to populate the schedule; may include existing time-off request history
- **Time-off request log (xlsx or inline):** Per-employee list of requested dates with any approval status; can be embedded in the prompt as a bulleted list or provided as a standalone file
- **Existing schedule template (xlsx, optional):** Pre-formatted calendar shell that the worker fills in; adds constraint that only designated cells may be modified
- **Coverage policy document (docx or inline):** Describes rotation rules, minimum staffing levels, and escalation procedures for coverage gaps

### Data Characteristics
The core data is a small personnel roster (3–20 names) and a set of date-specific availability flags. The planning horizon determines the number of cells: the total scales with team size multiplied by the number of days in the horizon, so a longer horizon or a larger team quickly multiplies the number of cells the worker must populate and check. Time-off requests are sparse (typically 4–12 days per employee per multi-month horizon). Coverage minimums are simple integer thresholds (1, 2, or N-1). Rotation patterns are rule-based and deterministic once the start day is fixed.

### File Complexity Spectrum
- **Minimal:** 2–3 employees, one-month horizon, simple Mon–Fri availability, one or two time-off requests per employee, no color coding, single tab
- **Moderate:** 3–5 employees, 2–3 month horizon, 5-on/2-off rotation, 3–4 time-off requests per employee, three-state color coding, per-month tabs plus summary
- **Complex:** 5–10 employees, 5–6 month horizon, staggered rotation starts per employee, overlapping time-off including multi-day consecutive blocks, minimum coverage near team size creating infeasibility windows, multi-state color coding, coverage gap flags, separate time-off request tab

## 5. Output Specification

### Primary Deliverable
- **Format:** Excel workbook (.xlsx)
- **Structure:** One tab per planning period (month or week) plus one summary/time-off tab; each tab is a calendar grid with employees as rows and dates as columns (or vice versa); cells contain status labels and background colors
- **Key quality signals:** All constraints satisfied simultaneously (rotation pattern, coverage minimum, time-off requests); coverage-deficient days explicitly flagged; color-coding consistent with stated schema; legend present and accurate

### Secondary Deliverables (if any)
- Brief written summary or email body explaining the schedule logic, any coverage risks, and recommended manager actions for flagged days

### Gold Output Characteristics
A gold output verifiably satisfies every stated constraint for every day in the planning horizon. Coverage counts per day are correct. Time-off requests appear on exactly the requested dates with the correct color/label. Rotation patterns are maintained consistently (no employee works more than the stated consecutive days without a break). Any infeasible dates (where no valid assignment exists given all constraints) are flagged with a clear note rather than silently violated. The legend matches the actual color schema used in the calendar cells.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Team size | 2–3 employees | 4–6 employees | 7–15 employees |
| Planning horizon | 1 month | 2–3 months | 5–6 months |
| Rotation pattern | Simple Mon–Fri | 5-on/2-off rolling | Staggered starts, variable shift lengths |
| Time-off requests | 0–1 per employee, non-overlapping | 2–3 per employee, one overlap | 4+ per employee, consecutive blocks, multiple overlaps |
| Coverage minimum | 1 of N | 2 of N | N-1 of N (creates infeasibility risk) |
| Color-coding | Binary (working/off) | Three-state (working/off/requested) | Four+ states with category distinctions |
| Flagging requirement | None | Flag days with gaps | Flag + note recommended action per gap |

## 7. Boundary Cases & Adjacent Patterns

**K2 (Production Planning & Recovery Scheduling):** The most similar adjacent pattern. K1 schedules people; K2 schedules production output (units, hours, batches). If the task specifies throughput targets, catch-up timelines, or capacity utilization rates, it belongs in K2. If it specifies coverage counts and rotation patterns for named employees, it belongs in K1.

**K3 (Space Assignment & Event Logistics):** K3 assigns physical resources (tables, units, rooms) to entities; K1 assigns time slots to people. Both involve constraint satisfaction, but K3 is spatial and K1 is temporal. If the task involves floor plans or room assignments, use K3.

**K4 (Project Timeline & Milestone Planning):** K4 produces visual Gantt-style timelines for project phases; K1 produces operational calendars for recurring personnel schedules. If the output is a one-time project timeline rather than a recurring staffing calendar, use K4.

**B5 (Data Entry with Protocol-Driven Decision Making):** If the schedule is pre-structured as a template with rules embedded in the file and the task is to fill in cells, it may border B5. The distinction is that K1 requires the worker to design the schedule logic (which employee works which day), not merely populate pre-determined values.
