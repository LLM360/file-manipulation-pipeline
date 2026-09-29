Your task is to classify the file `{task_filename}` in your working directory by
assigning it zero or more metatemplates from a fixed taxonomy, and to write a
freeform annotation describing what the file contains.

## Inputs in your working directory

- `task.json` — read this first if you want provenance context. Its `raw_url`
  and `file_path` fields reveal the corpus (github repo, intranet, forum, etc.)
  and are strong evidence about whether this is a real workplace document or
  a software test fixture. Other useful fields (file_ext, repo_full_name,
  etc.) are also present.
- `{task_filename}` — the actual file to classify. You MUST read this file and actually inspect its contents.

The working directory contains exactly these two items at the start. Anything
else you create (extracted text, scratch notes) should go under `/tmp` —
`mktemp -d` is your friend.

## Taxonomy

Metatemplates live in `{templates_dir}`. Start by reading
`{templates_dir}/../taxonomy_overview.md` to understand the structure and build
a shortlist of candidate templates. Only THEN read the individual template files
for your shortlist — do not read all templates up front.

A `template_id` is the relative path from the `metatemplates/` package
directory, e.g. `task_types/a1_audit_sampling.md`. **The `.md` suffix is
mandatory** — the schema validator rejects `task_types/a1_audit_sampling` without
it and will force a retry loop. Always include `.md`.

## Tools

You're inside a sandbox. Use it in full, use uv, node, apt-get, snap, whatever you need, your changes are ephemeral. Do whatever it takes to properly inspect the file and assign the appropriate templates.
`uv` is preferred for faster python management/installations.
Do your scratch work in `/tmp` (mktemp -d), not in the working directory.

## Guidelines

- **The taxonomy covers workplace *tasks*, not workplace-origin *files*.** The 57 templates
  describe professional knowledge-work tasks (see `{templates_dir}/../taxonomy_overview.md` §1).
  A file qualifies when it could serve as a **reference input** to one of those tasks,
  regardless of where the file itself was produced — a conference slide deck, an academic
  paper, a vendor whitepaper, or a public-repo document can all match if a worker would
  plausibly attach them when performing the template's task. What disqualifies a file is
  its **content** being outside professional knowledge work (lorem-ipsum scaffolding,
  game/entertainment data, localization/i18n string tables, personal notes), not its
  venue of origin. Each template's "Reference File Requirements > File Types Needed" list
  describes **content profiles**, not a closed enumeration of file forms: a conference
  deck whose body walks through a system's architecture matches D1's "existing architecture
  summary" profile; a polished slide deck that decomposes a topic pedagogically with named
  sections and worked examples matches C4's "program curriculum or manual" profile. Match
  on what the body teaches or specifies, not on whether the literal form-name appears in
  the bullet list.
- **Substantive body content is required for every assignment.** Before assigning any
  template, you must have inspected the file's body and found enough professional content
  to justify the rationale you write — a coherent narrative arc, named sections, prose,
  tables, captioned figures, or equivalent. Filename, path, file format, and dimensions
  are never enough on their own. A one-page banner image with no extractable text, a
  thumbnail, an icon, or any file you cannot actually read does NOT match D1's
  "architecture diagram" profile (or any other) just because the form-name fits — D1's
  diagram entry assumes a topology diagram dense enough to mirror, not a single
  decorative image. When the body is empty, image-only, or unreadable, write zero
  assignments and describe what you saw in the annotation. Test-fixture and academic
  coursework paths (`test/`, `tests/`, `spec/`, `fixtures/`, `sample-files/`,
  `example_data/`, `LayoutTests/`, `testdata/`, `integration_tests/`, `cypress_test/`,
  `test_data/`, plus academic gradebook folders such as `*Assignment*/Fall*/`,
  `*Case*Study*Repo*`, `Group *-* cluster*`, `*Activity *.docx`) are a hint that the
  body is more likely to be synthetic (lorem ipsum, smoke-test strings, hello-world
  scaffolding, generated dummy rows, student assignment prompts) — apply the same
  body-content gate, and if the body is real third-party professional content vendored
  as a test asset, assign normally.
- **Assignments must be tight AND you must ask the right question.** A `template_id` belongs
  in `assignments.json` only if there is a clear, concrete task instantiation that would use
  this file as a **reference input**. Ask: *"if a worker were given this file as an attached
  reference, would any template's Reference File Requirements section plausibly match?"* Do
  NOT ask: *"is this file itself a task deliverable?"* — reference files are inputs, not
  outputs, and a file can match a template even if the file itself originated in an academic
  conference, a public repo, or any other non-workplace venue. Loose thematic matches are
  still rejected, and zero assignments is valid and expected for many files.
  Specifically for `a5_operational_metrics_dashboard`: a5's reference input is a
  **transactional/event-level operational extract** from a real operational system
  (POS, ERP, WMS, production log, rental agreement ledger, IT time-tracking, incident
  log) with enough rows to require aggregation (tens to hundreds of events per
  dimension) and at least one numeric metric computable at the event level. A short
  product-catalog / SKU master lookup (one row per product with static attributes like
  theme, piece count, MSRP) is NOT an a5 reference input even when the columns *look*
  like aggregation dimensions — it lacks the transactional grain a dashboard
  aggregates over. Academic statistics-textbook sample datasets (paths like
  `data-raw/`, `openintro`, `*_sample.xlsx`, repo-tree vignette datasets) are
  pedagogical artifacts, not operational-system exports, and do not become a5 inputs
  just because their columns are retail-shaped; an Assistant Buyer or merchandise
  planner would attach their own POS extract, not a 75-row textbook sample.
  **Pre-aggregated tabular outputs are NOT a5 reference inputs**, regardless of
  volume or columnar richness: a file whose grain is **one row per geography,
  period, or entity** with **already-computed ratios, averages, YoY deltas, slope
  or intercept coefficients, regression parameters, pivot subtotals, or rolling
  stats** (e.g. 290 rows of municipality × annual_CPEV_ratio + slope + intercept;
  national census counts per region; pre-joined annual summaries per facility) is
  a *downstream analytical deliverable*, not the raw operational extract a5
  consumes. The a5 dashboard author aggregates over events; if the file has
  already done the aggregation, a5 does not apply. Conversely, do not assign a5
  to pure research datasets, ML training feature tables, or scientific
  observation logs — those lack the business-operation framing a5 targets (POS,
  ERP, WMS, production, rental, IT service).
  Specifically for `c1_standard_operating_procedure`: a c1 task's reference inputs are
  "working session summary or issue log", "existing reference documentation" (prior
  version of the procedure, related policy framework, or **platform / tool / system
  documentation** the SOP must align with), and optional industry standards. A vendor or
  open-source **tool runbook / operational guide** that walks through prerequisites,
  execution modes, pass/fail checks, and remediation loops for a concrete operational
  task (e.g. an AD krbtgt reset script guide, a database failover runbook, a deployment
  tool execution guide) IS a prototypical c1 **reference input** — an ops manager
  adopting the tool would attach it when authoring the formal internal SOP. A
  **high-level governing policy framework** — a government directive, agency
  regulation, statute, or enterprise-wide policy — whose body enumerates purpose,
  applicability, policy principles, procedures, and responsibilities, and that
  explicitly delegates downstream implementation ("Heads of Components shall
  establish procedures", "Agencies shall issue local guidance", "Departments shall
  promulgate implementing rules") IS ALSO a prototypical c1 reference input: it is
  the "related policy framework" the c1 template explicitly names, and an installation
  SOP author would attach it when authoring the local procedural document that
  operationalizes the directive. Do not reject such files on the grounds that they
  themselves lack step-by-step operator instructions, named approving officials for
  the local unit, responsibility sections at the implementer level, or organizational
  governance specific to a single site — c1 reference inputs are raw procedural
  material *or* the upstream policy that raw procedures must align with, not finished
  local SOPs. When assigning c1 on that basis, name the SOP-authoring task you envision
  in your rationale.
  Specifically for `c3_clinical_guidelines_reference`: c3's reference profile is that the
  worker **authors** a formal clinical document — a prescribing guideline, formulary,
  care plan, SOAP note, SBAR template, or evidence-based clinical reference guide. The
  file must plausibly serve as raw clinical material that an **authoring clinician**
  (medical director, pharmacist, nurse practitioner) would mirror, cite, or adapt when
  producing that next clinical deliverable: a published clinical practice guideline, a
  named professional society standard, a prior prescribing guideline, a patient chart
  for a care-plan draft, or similar clinical source content. A **chart review form,
  reviewer scoring instrument, or annotation rubric** whose body is a list of
  diagnostic questions framed for a human reviewer to answer against a patient record
  — even when the questions explicitly operationalize published clinical criteria
  (Sampson anaphylaxis criteria, MELD score inputs, PHQ-9 items, Rockwood frailty
  assessment) — is NOT a c3 reference input. Its function is data collection by a
  reviewer, not clinical content authorship, and a clinician drafting a new
  prescribing guideline or care plan would not open it for clinical source material.
  Such files may still match c5 as form/template design (the form IS the instrument),
  but do not double-assign c3 on the grounds that the form references a clinical
  guideline or that a guideline author could conceivably consult it — that is a
  thematic match, not the "evidence-based clinical source material an author cites"
  profile c3 requires. When the file is a reviewer's data-collection instrument,
  write one assignment (c5 if the form carve-out applies) or none, not c5+c3.
  Specifically for `c4_training_materials_educational`: the file must exhibit pedagogical
  scaffolding. **ANY ONE** of the following is sufficient (they are alternatives, NOT a
  checklist — do not require multiple), BUT **criterion (a) is SUBJECT to the
  conference/meetup-talk exclusion below** — if the file is a solo
  engineer/architect/researcher presentation in a `presentation/` or `talks/` folder
  by a named author with no learner-cohort infrastructure (no objectives slide, no
  exercises slide, no assessment slide, no curriculum / module / lesson numbering,
  no course code), criterion (a) does NOT apply even when the body has progressive
  sequencing and worked examples. Such files route to empty `[]`, not c4:
  (a) progressive sequencing from foundational
  concepts to application with named sections AND at least one worked example, case
  study, or illustrative walkthrough; (b) exercises, practice problems, or discussion
  prompts for learners; (c) assessment mechanisms (quizzes, pre-tests, competency
  rubrics, homework trackers); (d) speaker notes that guide delivery pedagogy (not bare
  slide captions); (e) a named curriculum / module / lesson structure with learning
  objectives. A numbered course lecture deck from a university or course repo (e.g.
  `Slides/`, `Module N - Topic/`, `NN<Topic>.pptx`, `Lecture NN.pdf`) that walks through
  a topic with named sections and at least one worked example IS c4 — do not reject
  because it lacks exercises or quizzes. **This includes numbered AISystem /
  DeepLearningSystem / AI-hardware lecture decks** (e.g. `NN<Topic>.pptx` under
  `chenzomi12/AISystem/`, `DeepLearningSystem/`, `wangtongyouwen/DeepLearningSystem/`,
  or similar AI-curriculum repos) — files like `04Programing.pptx`, `05PipelineParallel.pptx`,
  `06NPUBase.pptx`, `06.npu.pptx`, `06CambriconArch.pptx`, `08TPU4.pptx`, `02Hardware.pptx`,
  `04NVSIMT.pptx`, `07.summary.pptx`, etc. are **c4, NOT d1**, even when their body
  enumerates dense hardware architecture vocabulary (NPU/TPU/GPU IPU/MPU/DMA/XFU-PIPE
  named components, chip topology, memory hierarchies, benchmark tables). The
  **lecture-series framing** — `NN<Topic>.pptx` filename, "Talk Overview" / 大纲 slide,
  numbered chapter TOC, Summary + References slide, optional "思考" / "Reflection"
  slide at the end, ZOMI or other lecturer branding — controls routing to c4. A
  lecture *about* a hardware system is pedagogical content, not a normative spec an
  engineer builds to; the d1 veto "research paper recap, methodology slide deck about
  an ML technique or algorithm, or any exposition whose subject is 'how this method
  works' rather than 'what this system is' is NOT d1" applies to these AI-hardware
  lectures — they explain how the systems work, they are not the systems' own spec. A **department-authored lecture or
  auditorium-exercise deck** (titled e.g. `Lecture N`, `Auditorne vježbe N`, `Vorlesung
  N`, `Clase N`, `Cours N`, with a department / chair / institute footer) whose body
  progresses through a technical topic with named sections, formulas, and one or more
  fully-worked numerical problems (given inputs → numerical solution) IS c4 even when
  the file is found inside a student-project tracker, a generic `uploads/` folder, an
  LMS assignment backend, or any other student-facing filesystem location — the
  **authorship and body profile** (teacher-authored lecture with worked problems)
  control, not the hosting directory. Do not conflate "file sits under
  `backend/uploads/`" with the test-fixture / academic-gradebook path hint above; that
  hint targets synthetic scaffolding or student-submitted coursework, not
  professor-authored course material that happens to be stored on a student-facing
  system. Substantive internal policy documents,
  procedure explainers, or regulatory documents can also qualify as c4 **reference
  inputs** (the c4 template's "Reference File Requirements" list "Internal policy
  document" explicitly) — when assigning c4 on that basis, name the training task you
  envision in your rationale. A **single-page statistical / regulatory indicator
  metadata tombstone** (a registry entry that merely documents an indicator's name,
  definition, unit, data source, update frequency, and a one-sentence calculation
  formula, published by a national statistics office, SDG portal, central bank
  dashboard, or analogous registry) is NOT a c4 reference input even when the body
  mentions a policy area or methodology — a 1-page definitional stub is a reference
  card for that single indicator, not the substantive policy/procedure/regulatory
  document the carve-out envisions. A training-development worker building a
  corporate upskilling module on SDG reporting, national accounts, or prudential
  supervision would attach the actual implementing methodology guide, sector manual,
  or compilation handbook — not a one-page indicator metadata sheet. Write zero
  assignments for such files (or match a different template if one applies). A
  **course syllabus / curriculum outline** (meeting
  schedule, enumerated topic list, problem-set outline, references, prerequisites) IS a
  valid c4 reference input even if the syllabus itself contains no worked examples or
  exercises — c4's "Reference File Requirements" explicitly lists "Program curriculum
  or manual" as the raw curriculum material a training specialist adapts into
  presentation format. A training-development worker would attach such a syllabus when
  building a corporate upskilling deck on the same subject. What is NOT c4: a flat API
  cheatsheet, language reference card, syntax quick-reference, or
  installation/quickstart guide that walks "what it is → how to install → advantages"
  without any worked example, case study, or assessment; a product capabilities /
  intro deck that walks "what is it → benefits → comparison table → configure"
  (a feature-comparison table is product positioning, not a pedagogical worked
  example — a worked example is a step-by-step solution to a specific problem
  applied to concrete inputs); a research / conference poster or publication
  deck in a `_publications/`, `papers/`, or `posters/` folder whose named sections
  are the IMRAD structure of scientific reporting (Background / Objective /
  Methods / Results / Conclusions / References) — research posters present
  experimental findings, they do not teach a learner progressively; an **IETF /
  W3C / IEEE / ISO standards-body working-group meeting slide deck** — typically
  4–12 slides hosted under `presentations/`, `slides/`, `wg/`, or
  `meetings/ietf-NNN/` in a standards-track draft repo (`lamps-wg/*`,
  `oauth-wg/*`, `httpbis/*`, `tls-wg/*`, `cose-wg/*` and siblings), whose body
  walks the meeting-template arc "Motivation → Updates → Open Issues / Key
  Discussion Points → Next Steps / Thank you" and discusses draft-spec design
  trade-offs (encoding choices, algorithm options, interop notes, hackathon
  status) — is NOT c4. The deck is a working-group status-and-discussion
  brief presented to WG participants, not a pedagogical lecture: its named
  sections are meeting-agenda slots, not curriculum modules; its "worked
  examples" are draft-design commentary rather than step-by-step problem
  walkthroughs; and it has no learning objectives, exercises, assessments, or
  progressive foundational-to-application sequencing a training specialist
  would mirror. Do not assign c4 to such decks on the grounds that they are
  "standards-body presentations a training developer could use to teach the
  technical foundations" — that is a thematic match, not the pedagogical
  scaffolding c4 requires. The normative draft itself may still match d1 when
  its body is a component-level spec; the WG meeting deck *about* the draft
  does not inherit that status. Write zero assignments for WG discussion decks
  (or match a different template only if one specifically applies). A **git /
  CLI / API command reference deck** that walks "setup → install client → learn the commands →
  list of commands with syntax → link to external cheatsheet" without a step-by-step
  worked problem (a concrete task broken into commands executed in sequence with
  narrative explaining why each command is chosen) — showing `git config --global
  user.name "foo"` in a syntax slot is a syntax example, not a worked example, and c4's
  worked-example requirement is a problem walkthrough, not a flag demonstration. Length
  and visual polish alone are not substitutes for pedagogical structure. **The
  "a training specialist would attach this as source content" rationale is NOT
  sufficient for c4** — any substantive document could be attached to any task; c4
  requires the file itself to exhibit pedagogical scaffolding per the disjunctive
  criteria above. What is NOT c4 regardless of how substantive the content is:
  (i) **government progress reports, inspection reports, audit findings, status-to-
  Congress reports** (Letter of Transmittal → Executive Summary → Part I/II/III →
  Recommendations → Appendices structure), (ii) **conference keynote / community
  meetup talks** that walk through a methodology or tool without structured learning
  objectives + exercises + assessment aimed at a learner cohort, (iii) **internal
  team charter / team norms / onboarding decks** that are operational process
  documents for a specific team (work preferences, PTO cadence, meeting rules,
  onboarding steps), even if a few slides mention a methodology, and (iv)
  **marketing/product overview "capabilities" decks** (already excluded above).
  These are outputs / operational artifacts / thought leadership; c4 reference
  inputs are curricula, lesson plans, syllabi, policy documents translated into
  training, or course lectures with worked examples. A
  **teacher-authored course-coded multiple-choice question bank with an answer key** —
  a document whose body is numbered MCQ items (each with alternatives i/ii/iii/iv or
  a/b/c/d) on a specific course topic followed by an "Answers" / "Answer Key" section,
  often headed with a course code and unit identifier (e.g. `18MAB302T — Unit-IV Group
  Theory`, `MATH 101 Chapter 5`, `EEE302 Quiz 3`, a named course module) — satisfies
  c4 criterion (c) "assessment mechanisms (quizzes, pre-tests, competency rubrics,
  homework trackers)" directly. Do NOT reject such a file on the grounds that "a test
  bank students use to evaluate their own knowledge is distinct from training
  materials a trainer uses as reference input", that "it lacks worked examples,
  instructional prose, or learning objectives", or that "quizzes are outputs, not
  inputs". C4's "Reference File Requirements" explicitly lists assessment mechanisms
  among the raw pedagogical material a training specialist adapts, and a corporate
  upskilling author drafting a Discrete Math (or any other subject) competency module
  would attach such a question bank as source content for assessment design. When
  assigning c4 on this basis, name the training task you envision in your rationale.
  The assessment-mechanism carve-out is **not limited to MCQ format**: it covers ANY
  **teacher-authored assessment artifact with a graded/gradable structure**, including
  (a) **coding quiz questions** with problem statement + expected output / sample
  I/O / points-allocated (e.g. "Q1 [5 marks]: What does this fork()/wait() program
  print?"), (b) **lab handouts / lab scripts** authored by an instructor with named
  Parts / Steps + a scoring rubric or points breakdown (e.g. "Part 1 [10 pts]: ...,
  Part 2 [15 pts]: ..., Total: 25 pts"), (c) **worked clinical / psychological / legal
  case studies** that present a vignette + question + a "Rubric" or "Model Answer"
  / "Rationale" block giving the expected reasoning (e.g. "28 y/o F with GAD
  symptoms — Which disorder best fits? Rubric: Generalized Anxiety Disorder;
  Rationale: ..."), and (d) **numbered preparation assignments with graded answer
  keys**. All of these are c4 reference inputs under criterion (c) — do not reject
  because they are student-facing or lack "learning objectives" wording; the
  presence of an instructor-authored answer key, scoring rubric, or points-marks
  allocation is the deterministic c4 assessment-mechanism tell.
  Specifically for `d1_technical_design_architecture`: the file must summarize or specify
  an **already-existing** system, standard, or engineering artifact — named components,
  interaction verbs (calls, writes to, serves), a topology, a normative spec, or
  quantitative engineering data — that an engineer would mirror, extend, or build from.
  A published normative specification from a standards body (e.g. an HL7 FHIR
  StructureDefinition / CapabilityStatement / resource schema, an IETF RFC schema, a
  W3C spec table) IS d1 when it enumerates named components with types, cardinality,
  bindings, or slicing — that is exactly the "existing architecture summary / normative
  spec" an implementer mirrors; do not reject such a file as "upstream standard source
  material" when its body is a component-level spec an engineer would build to.
  A **machine-readable EDIFACT / UN-CEFACT message implementation guide (MIG)**
  workbook — e.g. the BDEW `machine-readable_anwendungshandbuecher` family for the
  German energy market (UTILMD, ORDRSP, MSCONS, INVOIC, REMADV, ORDERS and siblings
  under paths like `FV<YYMM>/<MSGTYPE>/xlsx/<PID>.xlsx`), with sheets whose columns
  enumerate `Segmentname / Segmentgruppe / Segment / Datenelement / Code / Qualifier /
  Beschreibung / Bedingungsausdruck / Bedingung`, `Muss` / `Kann` / `X` flags, segment
  group nesting (`SG1..SGn`), UN/CEFACT message type / release / version headers
  (`ORDRSP / D / 10A / UN`, `UTILMD / D / 11A / UN`), and boolean condition expressions
  like `Muss [66] ⊻ [67]`, `X [529]`, `X ([60] ∧ [63]) ⊻ ...` — IS d1 and NOT b5.
  The reader is an EDI integration engineer building a parser / generator / validator
  that must mirror the segment tree, cardinality, qualifier enums, and conditional
  population rules of the standard; the workbook is the "component-level normative
  spec" the implementer builds to, exactly like an HL7 FHIR StructureDefinition.
  Assign d1 alone in this case; do not also double-assign b5 on the grounds that the
  same table could be consulted to populate a single message instance — the primary
  reference profile for this file family is normative-spec-an-engineer-builds-to.
  A research paper recap, a methodology slide deck about an ML technique or algorithm,
  or any exposition whose subject is "how this method works" rather than "what this
  system is" is NOT d1. A forward-looking build instruction (an assignment prompt, a
  "develop X" brief, a homework spec with a Submission section) is NOT d1 — d1's
  reference profile is an existing-system summary, not a to-be-built spec. Thematic
  technicality is not a substitute for a system or standard the reader could act on.
  A **figure / caption deck** whose body consists only of figure captions (one short
  paragraph per slide naming or describing an image that is NOT itself text-extractable)
  is NOT d1, even when the captions enumerate component names — a caption describing an
  architecture diagram is not the diagram, and an engineer cannot mirror topology they
  cannot see. If the entire extractable body is `Fig N. <one-sentence description>`
  across all slides, write zero assignments. This caption-deck exclusion extends to
  **single- or few-slide vendor-icon architecture diagrams** whose extractable text
  consists of component labels (service / node / subnet names like `AWS Fargate`, `VPC`,
  `ZooKeeper cluster`, `TOR Switch A`, `Spine Switch 1`) arranged around picture shapes,
  even when one or two short process phrases accompany the labels (`Scheduled rule that
  invokes workflow`, `Retries and timeout`, `Tiered storage`). The topology an engineer
  would mirror lives in the images — the relative position of icons, the connecting
  arrows, the containment of subnets — which is NOT text-extractable. A list of AWS /
  Azure / GCP service names plus a verb phrase is NOT the existing-architecture summary
  d1 requires: the reader cannot reconstruct who calls whom, what is in which subnet,
  or how the data flows from labels alone. When the file is a slide deck with few
  slides, many picture shapes, and an extractable body dominated by short component
  labels (with or without one or two verb-phrase captions), write zero assignments.
  D1 requires extractable prose or tabular spec content — named components tied
  together by sentences or a normative schema — not vendor-icon labels around
  unreadable images.
  Specifically for `b5_protocol_driven_data_entry`: the file must plausibly serve as a
  target template, protocol/rules document, or one of several source documents in a
  multi-file population task. An isolated source-data file (a single invoice, a single
  receipt, one pick-ticket) on a test-fixture path with synthetic dummy entities does
  not on its own justify b5 — b5 needs the population context, not just any structured
  file with rows. Conversely, a **normative field schema / data dictionary** that
  enumerates field names, required flags (SI/NO, Yes/No), field types, binding paths,
  visibility rules, enums, or conditional population rules for a real workflow IS a
  prototypical b5 **protocol/rules document** — the worker consults it to know which
  fields to populate in the target form and under what conditions. **Exception:**
  machine-readable EDIFACT / UN-CEFACT message implementation guides (the BDEW
  `machine-readable_anwendungshandbuecher` family: `FV<YYMM>/<MSGTYPE>/xlsx/<PID>.xlsx`
  for UTILMD / ORDRSP / MSCONS / INVOIC / REMADV / ORDERS and siblings, with
  `Segmentname / Segmentgruppe / Segment / Datenelement / Code / Qualifier /
  Beschreibung / Bedingungsausdruck / Bedingung` columns and `Muss` / `Kann` / `X`
  flags) route to **d1**, not b5 — see the d1 carve-out above. They are normative
  component-level specs an EDI integration engineer builds a parser / generator to,
  not protocol/rules documents a clerical worker consults to populate a single
  message instance. Directory evidence
  of a population workflow (a government use-case mapping folder, a methodology library
  with per-schema definitions, a regulatory submission system with many similar schema
  files) supplies the multi-file population context; the carve-out does not require
  that the target form, the source data, and the rules doc all be in the same working
  directory. A **standardized regulatory reporting workbook** — any file whose sheet
  structure is the authoritative, prescribed template that reporting entities
  must populate on a recurring submission cycle under a named framework —
  IS a prototypical b5 **target template AND its own protocol/rules document
  simultaneously**, and ALONE satisfies both b5 prerequisites. Concrete
  examples: UNFCCC Common Reporting Format (CRF) tables for national
  greenhouse gas inventories (filenames like `XXX_YYYY_*.xlsx` with 50+
  sheets named `Table1`, `Table1.A(a)s1`, `Table2(I)s1`, `Summary1.As1`,
  `Table10s1`, IPCC sector categories down column A, standardized GHG
  columns `CO2 / CH4 / N2O / NOx / CO / NMVOC / SO2 / HFCs / PFCs / SF6 /
  NF3`, and UNFCCC notation keys `NO / NE / IE / NA / C`); IPCC national
  inventory sheets; EPA CBI / TRI / GHGRP reporting forms; national
  statistical office return templates; central bank supervisory return
  workbooks; tax authority e-filing workbook templates; **national
  anti-corruption / public-official asset-and-income disclosure forms**
  (e.g. Russian Federal Law 273-FZ disclosures titled "Сведения о доходах,
  расходах, об имуществе и обязательствах имущественного характера"
  with standardized columns for Должность / вид объекта / вид собственности /
  площадь / страна расположения / Транспортные средства / Декларированный
  годовой доход, published annually by ministries and agencies for
  civil-servant staff and family members; analogous U.S. OGE 278e executive
  branch public financial disclosures; EU national declaration forms);
  **core-facility / shared research-infrastructure prescribed submission
  workbooks** — a sequencing / genomics / proteomics / imaging / HPC core's
  versioned sample- or pool-submission template (filenames like
  `fms_sample_submission_template_<ver>.xlsx`, `<platform>_sample_sheet.xlsx`,
  `nanopore_submission_v<N>.xlsx`, `cryo-em_intake_form.xlsx`) whose body
  combines one or more intake sheets (SampleSubmission, PoolSubmission,
  LibrarySubmission) enumerating mandatory fields marked `*` (Sample Kind,
  Container Kind, Container Barcode, Coord, Project, Taxon, Reference Genome,
  Volume, Concentration) with an **accompanying enumeration / index sheet**
  that lists the allowed values for each controlled field (Sample Kind enums,
  Container Kind enums, Taxon codes, Reference Genome builds). The second
  sheet is the embedded protocol/rules document — it tells the submitting lab
  which enum value to place in each column — and the workbook is the
  prescribed template every external submitter must populate per sequencing
  run / imaging session / compute allocation on a recurring cycle. Core-
  facility template status holds even when the workbook sits in a `config/`
  or `templates/` folder of a converter / validator repository — the
  versioned template filename and the intake-plus-index-sheet structure are
  the signal. The
  **file format does not matter** — b5 standardized-regulatory-workbook
  status applies equally to `.xlsx` with sheet tabs and to `.docx` whose body
  is a single wide standardized table (24+ rows of named officials / entities,
  20+ columns of prescribed fields, hierarchical section headers grouping
  rows by role or category). When you see such a
  file, b5 is the correct assignment even when (i) the workbook already
  carries a prior cycle's finalized values — it remains the authoritative
  template structure an analyst will mirror for the next cycle; (ii) no
  separate "rules document" is present in the working directory — the
  mandated CRF/IPCC/EPA/etc. framework IS the rules, and the workbook's
  column headers, notation keys, and sector taxonomy ARE the embedded
  population rules; (iii) the file sits alone without accompanying source
  documents — the recurring annual/quarterly submission cycle across
  jurisdictions IS the multi-file population workflow. Do NOT reject such a
  file on the grounds that it looks like "finalized regulatory submission
  output" rather than a blank template, that it lacks "embedded population
  rules", or that there is "no multi-file population workflow in the working
  directory" — these are exactly the rejection lines this carve-out
  preempts. The standardized regulatory workbook is the template, the rules,
  and the workflow context rolled into one. What still disqualifies b5 is
  synthetic-entity test fixtures, lorem-ipsum dummy rows, or isolated lone
  files that are NOT part of a recurring mandated reporting cycle.
  Specifically for `d6_sales_pitch_decks`: this template targets organization-level
  capabilities decks and sales operations process documents (agency service offerings,
  account management, SDR/AE funnel processes, vendor capability briefs). A personal
  academic job-interview deck, a researcher's job-talk, or a candidate's portfolio
  presentation is NOT d6 — d6 reference inputs are services documentation and executive
  briefs at a company level, not individual capabilities pitches. **Also NOT d6:**
  consumer product marketing collateral, real-estate project brochures (residential
  apartment developments, school admission brochures, car dealership flyers, restaurant
  menus, SaaS landing-page one-pagers), B2C advertising pamphlets, and event/program
  promotional brochures. d6's prototype is a **B2B service capabilities deck** —
  "our agency / consultancy / firm offers these services to your organization, here
  are our case studies with enterprise clients" — NOT "buy this apartment / car /
  product from us". If the audience is an individual consumer making a personal
  purchase, it is not d6 regardless of how glossy the brochure is.
  Specifically for `c5_form_template_design`: a file whose body consists of `<placeholder>`
  or `«token»` fields embedded in otherwise-coherent professional prose (form letters,
  intake questionnaires, fillable templates, consultation response letters) IS the
  prototypical C5 "existing form to revise" reference, regardless of subject-matter
  narrowness — domain specificity (archaeology, dialysis, HOA inspections, permit
  reviews) does not disqualify a form-template file from c5. What is NOT c5: a blank
  presentation / slide-layout scaffold whose body contains only generic layout markers
  (e.g. `TITLE`, `TEXT`, `PIC`, `Header`, `Body`, `Subtitle`) with no domain prose,
  no data-collection fields, and no workflow context — such a file is a visual wireframe
  for authoring presentations, not a fillable data-collection form. C5's "template" is
  an operational data-collection instrument (intake form, tracking spreadsheet, fax
  cover sheet, inspection checklist) with named fields that capture real data from a
  recurring process, not a blank slide shell. A file whose only substantive content is
  the words "TITLE" and "TEXT" repeated across slides fails the substantive-body-content
  gate regardless of the word "template" appearing in its filename or path. **A file
  whose entire body is a single naked mustache / templating token** (e.g. a docx
  containing only `{{processedText}}`, `{{CONTENT}}`, `${{VALUE}}`, `[[body]]`, or a
  similar runtime rendering-engine placeholder with no surrounding prose, no named
  field labels, no data-collection structure, and no workflow context) is NOT c5 —
  it is a downstream templating-pipeline artifact, not a fillable form. The c5
  placeholder rule requires tokens **embedded in coherent professional prose**; a
  bare token with no prose fails the substantive-body-content gate.
  Specifically for `d5_legal_transactional_documents`: a d5 task's reference inputs are
  "contract structural outline", "boilerplate legal language", and source documents
  containing terms to be incorporated. A **fully executed prior agreement** of a type
  an attorney or paralegal would reuse when drafting a new agreement of the same type
  (donor agreement of deposit, inter-institutional collection deposit contract, NDA,
  LOI, service agreement, license agreement, grant agreement, employment separation
  agreement) IS a prototypical d5 **structural outline + boilerplate language**
  reference — the worker opens the prior executed instrument to mirror its article
  structure, recitals, representation clauses, license-grant language, governing-law
  block, and execution formalities when drafting the next instance. Do not reject such
  a file on the grounds that "it is itself the deliverable, not a template" — in d5,
  an executed instrument of a reusable form IS the structural outline the next
  drafter mirrors. The file qualifies when its body contains identifiable provision
  articles (parties, asset/rights transfer, license grants, representations, term,
  termination, governing law, execution block) an attorney could reuse. When
  assigning d5 on this basis, name the drafting task you envision in your rationale
  (e.g. "paralegal drafting a new donor agreement of deposit for another institution
  pair"). What is NOT d5: a personal will or one-off legal deliverable whose terms
  are too bespoke to another party to serve as structural scaffolding; a court filing,
  judicial opinion, statute, or regulation (those are legal *sources*, not drafting
  templates); a legal bill, invoice, or engagement-letter receipt.
- **Template IDs must be real.** You may only cite filenames you have actually read under
  `{templates_dir}/`. No hallucinated paths.
- **Rationales explain the fit, not the template.** A rationale says why *this specific file*
  matches the template, not what the template is for.
- **Annotations are freeform.** No required headers or structure. Focus on: what the file
  contains, its current state (draft / final / template / partial), what tasks it could
  support, anything non-obvious that would help a downstream consumer.
- **Never re-download.** If the file is missing from the working directory, do NOT fetch
  from `raw_url`. The download step is a separate concern — write `.no_file` and stop.
- **Self-validate.** Check your proposed `assignments.json` against the schema below BEFORE
  writing it. This dramatically reduces retries.

## ** IMPORTANT **

Don't just lazily assign the file to zero templates, ask yourself if the file could plausibly be used as a reference input or output for any of the templates. Exhaust the available templates before giving up, but do follow the guidelines above, they serve as context for your decision.

** Procedure **: Follow these steps: You should start by reading the taxonomy first, then read the file, actually open it and inspect it, once you have good context, read some possible templates, read the file again, and then assign the templates.

## What to produce (success path)

Produce exactly these three files in the working directory:

1. `assignments.json` — MUST conform to this JSON schema:

   ```json
   {schema_json}
   ```

   An empty `assignments` array is valid for files where no template
   plausibly matches. Each non-empty entry is
   `{"template_id": ..., "rationale": ...}`.

2. `annotation.md` — freeform markdown about the file (what it contains,
   its state, what tasks it could support, anything non-obvious).

3. `.done_classify` — an empty marker file indicating success.

## Escape valve (rare — file is genuinely unprocessable)

If the source file is truly missing, corrupted, or impossible to read with
any available tool — and you have actually tried — write a single empty
marker `.no_file` and DO NOT write `assignments.json`, `annotation.md`, or
`.done_classify`. 

This path should be very rare.

## Final check

Before finishing, confirm the working directory contains exactly one of:

- (`assignments.json` + `annotation.md` + `.done_classify`) for the success
  path, OR
- `.no_file` alone (no `assignments.json`, no `annotation.md`, no
  `.done_classify`) for the escape-valve path.

Plus the inputs left untouched: `task.json` and the source file
(`{task_filename}`).

If you produced `assignments.json`, use the jsonschema library to validate it against the schema; that avoids wasted work.
