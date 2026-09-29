# Screenwriting & Script Development

**Macro Category:** H — Creative & Media Production
**Pattern ID:** H5

## 1. Pattern Description

The worker writes a production-ready script or screenplay following industry-standard formatting conventions and producing original creative writing constrained by a provided story framework. Two sub-types are present: a documentary basic script aligned to a provided voiceover script and sequence overview, and a narrative short film screenplay following a provided story breakdown and character descriptions. The cognitive core is dual: creative craft (character voice, dramatic structure, "show don't tell" execution) combined with strict format compliance (screenplay font/margins, scene heading conventions, element types, page count targets). What makes this pattern distinct from general creative writing is that the output format is itself a technical deliverable — an industry-standard document that production crews, actors, and directors will use directly in production. The formatting rules are non-negotiable constraints, not stylistic preferences.

## 2. O*NET Grounding

### Occupation Families
- 27-3043 Writers and Authors — primary occupation for screenwriting and script development
- 27-4032 Film and Video Editors — relevant when the script writer also functions as the editor (e.g., a video editor who is assigned script-writing duties before cutting the piece)
- 27-2012 Producers and Directors — adjacent when the writer is developing material for their own production
- 27-2011 Actors — tangentially relevant for understanding dialogue naturalism and character voice requirements

### Key Work Activities (O*NET vocabulary)
- Writing Creative Content (original dialogue, action lines, dramatic scenes)
- Applying Industry-Standard Format Conventions to Written Documents
- Developing Characters and Narrative Structure from Provided Outlines
- Communicating Complex Ideas Through Written Language for Diverse Audiences
- Coordinating Writing Activities with Visual and Audio Production Requirements
- Adapting Tone and Style for Specified Audience Demographics
- Researching Content to Inform Accurate Creative Writing
- Using Technology (word processing, screenplay formatting software) to Produce Deliverables

### Knowledge Domains (O*NET vocabulary)
- English Language (grammar, style, dialogue craft)
- Fine Arts (narrative structure, dramatic tension, character development)
- Communications and Media (documentary conventions, broadcast standards, script types)
- Education and Training (audience calibration for educational/documentary content)

### Generalizable Work Context
A writer or editor working in a production company, documentary house, or independent film context receives a creative brief containing a story framework (outline, breakdown, or voiceover script) and must develop it into a production-ready formatted document. The trigger is a production milestone: the project has been greenlit and needs a shooting-ready script. Stakeholders include the director (will shoot from the script), the producer (approves format and tone), the editor (will assemble footage based on script structure), and — for documentary or educational content — the subject-matter expert who approved the content approach. Page count and scene count constraints reflect production time and budget limits.

## 3. Prompt Construction Template

### Persona Pattern
Assign the writer a specific role in the production context: video editor assigned script writing duties (documentary), auteur/screenwriter (narrative film), or TV writer on staff. The persona should reflect the client relationship (writing for a client brand, writing for a director, writing as auteur) since this affects the degree of creative latitude vs. adherence to provided framework. Include the genre and tone as part of the persona context.

### Scenario Pattern
Two primary scenario patterns:
- **Documentary/non-fiction:** A client has finalized a voiceover script and sequence overview; the editor/writer must translate these into a structured basic script with timestamps, generalized scene descriptions, and tone calibration for a defined audience demographic.
- **Narrative fiction:** A director or producer has created a story breakdown and character profiles; the screenwriter must execute the story into a full screenplay with proper format, "show don't tell" execution, and production-ready scene structure.

In both cases, the scenario should specify: who the deliverable is for, what format it will be used in (broadcast, streaming, festival), and the specific format requirements.

### Instruction Pattern
For documentary scripts: describe the VO/sequence alignment requirement, the timestamp convention, the page limit, and the tone requirements. For narrative screenplays: extensively describe the formatting rules (font, margins, scene heading format, element types) before getting to the content instructions, since format compliance is the dominant constraint. Reference attached documents (story breakdown, formatting guide) as the content authority. Conclude with scene/page count constraints and output format.

### Constraint Injection Points
- **Format standard:** Industry-standard screenplay format (Courier 12pt, specific margins) vs. simplified documentary script format vs. broadcast TV format
- **Length:** Page count (e.g., a short-format page-count range) and scene count (e.g., a modest scene-count range); these are independent knobs
- **Documentary length:** If applicable, the target runtime range in minutes (e.g., a short runtime measured in single-digit minutes)
- **Audience demographic:** Single specified audience vs. dual-audience calibration (e.g., a children's age band AND an adult age band with a wide gap between them)
- **Alignment constraint:** How tightly the script must follow the provided reference (exact VO alignment vs. interpretive framework)
- **Script type:** Basic/pre-papercut documentary script (generalized scenes, no shot specifics) vs. full shooting script (specific shots, camera directions) vs. feature screenplay
- **Output format:** DOCX vs. PDF; formatted via dedicated software vs. standard word processor
- **Tone specification:** Client brand personality attributes (e.g., warm, professional, reassuring) vs. genre conventions (tense, dramatic, comedic)

### Structural Template

```
[PERSONA]: You are a [ROLE: screenwriter / video editor assigned script writing / staff writer] working [CONTEXT: for a video production company serving [CLIENT_TYPE] / as an independent auteur / on a [GENRE] [FORMAT: short film / documentary / TV episode]].

[PROJECT_CONTEXT]: The [PROJECT_NAME] is a [FORMAT] [DURATION or RUNTIME] for [DISTRIBUTION: broadcast television / streaming / festival / client digital channel]. Target audience: [DEMOGRAPHIC_1] and [optional DEMOGRAPHIC_2]. Tone: [TONE_DESCRIPTION: warm and reassuring / tense and dramatic / educational and accessible].

[REFERENCE_FILES]:
- [FILE_1]: [e.g., "Story breakdown PDF — scene-by-scene narrative outline and character descriptions for [PROJECT_NAME]"]
- [FILE_2]: [e.g., "Voiceover script and sequence overview — narrative text for the documentary paired with a per-segment content overview"]
- [FILE_3]: [e.g., "Formatting guide (JPG) — visual reference showing industry-standard screenplay margins, font, and element placement"]

[FORMAT_REQUIREMENTS]:
- Font: [Courier 12pt / non-negotiable] (for narrative scripts) OR [standard Word formatting] (for documentary scripts)
- [Scene headings: ALL CAPS, INT./EXT. + LOCATION + TIME OF DAY]
- [First character introduction: character name in ALL CAPS]
- [Script type: basic pre-papercut script / shooting script / full feature screenplay]
- [Scene count: [N]–[M] scenes]
- [Page count: [N]–[M] pages]
- [Output format: .docx draft acceptable, PDF final]

[CONTENT_REQUIREMENTS]:
- [For documentary]: Include general timestamps throughout. Scenes should be generalized (not shot-specific). Align to provided VO script sequence exactly. Align to sequence overview for per-segment content.
- [For narrative]: Follow the provided story breakdown scene by scene. Apply "show, don't tell" throughout — dramatize information rather than stating it. Maintain consistent character voice per provided character descriptions.

[CONSTRAINTS]:
- [PAGE_LIMIT: Hard limit — under [N] pages]
- [ALIGNMENT: Must align with provided [VO / story breakdown] — no new plot elements]
- [AUDIENCE: Dual-audience calibration — appropriate for [DEMO_1] and [DEMO_2] simultaneously]
- [TONE: Brand personality — [BRAND_ATTRIBUTES]]
- [SOFTWARE: Recommended tool: [e.g., a dedicated screenplay-formatting add-on or tool]]

[OUTPUT_SPECIFICATION]: [PDF or DOCX]; [N]–[M] pages; [script type]; aligned to reference documents; industry-standard format throughout
```

## 4. Reference File Requirements

### File Types Needed
- **Story breakdown / narrative outline (PDF):** Scene-by-scene description of the story, character names and descriptions, dramatic arc, key beats. This is the content authority for narrative scripts — the screenwriter executes it, not invents it. Should include 10–20 scene descriptions, character profiles, and a brief thematic statement.
- **Voiceover script (DOCX or PDF page):** The finalized narration text for a documentary, organized by sequence. The screenplay must align to this — the VO is the content spine, and the visuals described in the script must support it. Should be 1–3 pages of narrative text organized by topic sequence.
- **Sequence overview (DOCX page or section):** A per-segment description of what each documentary section should cover, paired with the VO script. Together these form the creative brief for documentary script writing.
- **Formatting guide (JPG or PDF):** A visual reference showing correct screenplay formatting — margins, indentations, font, element types (scene heading, action line, character name, dialogue, parenthetical). This is typically an image of a correctly formatted screenplay page. Online formatting tools or add-ons may be referenced as alternatives.

### Data Characteristics
Story breakdowns should describe a complete short narrative arc: a clear inciting incident, at least one complication, and a resolution. Characters should have a small number of named principal roles with distinct personality notes. Voiceover scripts for documentary tasks should be organized into a handful of named sequences corresponding to distinct content areas. All reference files should be consistent — the VO and sequence overview should not contradict each other. For narrative scripts, the breakdown should not over-specify dialogue (to leave creative latitude for the writer) but should specify dramatic beats and character dynamics.

### File Complexity Spectrum
- **Minimal:** Single reference document (voiceover script only); documentary basic script; no strict format requirement; short in length.
- **Moderate:** Story breakdown PDF; full screenplay format required; a moderate page-count range; "show don't tell" required; standard single audience.
- **Complex:** Story breakdown + formatting guide (JPG) + dual-audience requirement; strict industry-standard format (Courier, ALL CAPS conventions); scene count and page count simultaneously constrained; software tool needed for formatting compliance.

## 5. Output Specification

### Primary Deliverable
- **Format:** DOCX (draft acceptable) or PDF (final delivery); for narrative screenplays, PDF is the industry standard final format
- **Structure:** For documentary: sequential sections with timestamps, generalized scene descriptions, tone-calibrated narration. For narrative: proper screenplay format throughout (scene headings, action lines, dialogue blocks, transitions)
- **Key quality signals:** Page count within specified range; scene count within specified range; format compliance (correct font, margins, element types); content alignment with reference documents (no deviation from provided breakdown/VO); "show don't tell" principle applied (no expository action lines that state emotion directly); audience-appropriate tone maintained throughout

### Secondary Deliverables (if any)
- None required by this pattern. Some commissioning contexts request a one-page synopsis or beat sheet alongside the script, but that is outside the core pattern.

### Gold Output Characteristics
A gold documentary script has timestamps at each sequence transition, scene descriptions that align exactly to the provided VO sequence order, and a tone that matches the brand personality specification throughout — not shifting to a dry or overly technical register. A gold narrative screenplay uses correct Courier 12pt throughout (no font mixing), applies ALL CAPS to every scene heading and first character introduction, contains exactly the number of scenes specified, and executes each scene from the breakdown with dramatic showing rather than telling. Dialogue sounds like real character voice, not narration. No new plot elements are introduced beyond what the breakdown specifies. The output is production-ready: a director could begin prepping based on it immediately.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Script type | Documentary basic script (generalized scenes) | Full narrative screenplay, standard format | Narrative screenplay, strict Courier + margin spec + software required |
| Reference alignment | Single reference document to follow | VO + sequence overview (two aligned documents) | Story breakdown + formatting guide + VO (three documents, all must be honored) |
| Audience | Single specified demographic | Dual demographic (e.g., general adult) | Dual demographic with wide age gap (e.g., a children's age band and an adult age band) |
| Length constraint | Open-ended (writer's judgment) | Page limit only | Page count + scene count independently constrained |
| "Show don't tell" | Not specified | Mentioned as preference | Required throughout with explicit prohibition on expository statements |
| Tone specificity | Genre convention (thriller, comedy) | Named brand attributes (2–3 adjectives) | Multi-attribute brand personality with defined emotional register |

## 7. Boundary Cases & Adjacent Patterns

- **C4 (Training Materials & Educational Presentations):** C4 produces documents designed to teach (slide decks, training guides, case studies). H5 produces production scripts designed to be filmed or broadcast. If the deliverable will be used to train people, it's C4; if it will be shot or recorded, it's H5. An educational video script is H5.
- **C1 (SOP / General Order):** Both produce structured documents with defined sections, but SOPs are operational procedures, not creative scripts. No realistic overlap.
- **H1 (Broadcast Commercial & Video Editing):** H1 tasks consume scripts as input; H5 tasks produce scripts as output. If a video editor is also asked to write a script before editing, that's an H5 sub-task followed by an H1 task. A task is classified as H5, not H1, whenever the script writing itself is the primary deliverable — even when the same worker will go on to edit the footage.
- **H6 (Moodboard & Visual Direction):** H6 produces a visual moodboard synthesizing aesthetic direction; H5 produces written text in script format. H6 informs the visual feel; H5 defines the narrative structure. Adjacent in production workflow but different outputs and different cognitive work.
- **G1 (Research-to-Document authoring):** G1 tasks require web research to synthesize a knowledge document. H5 tasks may have a URL reference (formatting software, example scripts) but the primary work is creative writing from a provided framework, not synthesis of researched information. If the majority of the task is finding and synthesizing information, it's G1; if it's writing original creative content from a provided outline, it's H5.
