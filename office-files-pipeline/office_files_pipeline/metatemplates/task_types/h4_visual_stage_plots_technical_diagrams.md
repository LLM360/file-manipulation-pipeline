# Visual Stage Plots & Technical Diagrams

**Macro Category:** H — Creative & Media Production
**Pattern ID:** H4

## 1. Pattern Description

The worker creates a precise technical diagram — a stage plot, process map, or electrical schematic — that communicates spatial, procedural, or signal-flow information using domain-specific visual conventions and symbology. The deliverable is always a structured visual document (typically PDF) that will be used by practitioners in the field for operational alignment, safety compliance, or venue/team coordination. What makes this pattern distinct is the combination of domain-specific symbology rules (IEC electrical standards, process mapping conventions, stage plot conventions) with spatial layout precision — elements must be positioned correctly relative to each other, labeled according to strict naming conventions, and formatted to a specified paper size and orientation. The cognitive core is translating domain knowledge into a visual language that is unambiguous to its intended audience.

## 2. O*NET Grounding

### Occupation Families
- 27-4014 Sound Engineering Technicians — for stage plot tasks in live audio/music contexts
- 17-2112 Industrial Engineers — for process map tasks in logistics or manufacturing contexts
- 17-2071 Electrical Engineers — for schematic design tasks in automation/control contexts
- 17-3012 Electrical and Electronics Drafters — for detailed electrical drawing tasks
- 13-1081 Logistics Analysts — adjacent for process mapping in supply chain contexts

### Key Work Activities (O*NET vocabulary)
- Designing Layouts and Specifications for Operational Systems
- Documenting Information in Diagrams, Charts, and Schematics
- Applying Industry-Standard Symbology (IEC, process mapping symbols, stage conventions)
- Coordinating Work Activities Across Teams via Visual Documentation
- Analyzing System Configurations and Representing Them Visually
- Verifying Technical Accuracy of Design Documents Against Specifications
- Organizing Spatial Information for Clarity and Operational Use
- Applying Naming Conventions and Labeling Standards to Technical Drawings

### Knowledge Domains (O*NET vocabulary)
- Engineering and Technology
- Fine Arts (spatial composition, visual hierarchy)
- Telecommunications (for audio signal routing in stage plots)
- Production and Processing (for manufacturing process maps)
- Physics (for electrical schematic design)
- English Language (labeling, annotation, title blocks)

### Generalizable Work Context
A technical professional working in live event production, industrial engineering, or automation design receives a need to document a system or process that will be used by multiple practitioners who were not involved in its design. The trigger is either a venue advance (stage plot), a cross-functional alignment need (process map), or a new equipment installation requiring engineered documentation (electrical schematic). Stakeholders include venue sound engineers and stage managers (stage plots), operational leadership and cross-functional teams (process maps), and electricians, safety inspectors, or equipment installers (schematics). The document must be self-explanatory to its intended audience with no additional verbal guidance.

## 3. Prompt Construction Template

### Persona Pattern
Assign the worker to a specific technical role within the relevant domain: IEM tech / monitor engineer for stage plots, industrial engineer for process maps, electrical/controls engineer for schematics. The persona should establish operational context (touring band, logistics hub, automation manufacturer) and the intended audience for the diagram. Include enough domain familiarity to make the symbology expectations natural.

### Scenario Pattern
The triggering event should be a practical need: an upcoming venue advance requires a stage plot (live music), operational leadership has requested a standardized process map (industrial), or a new safety circuit needs documented design (electrical). The scenario should name the specific system or band/production being documented and describe the current state (no standardized document exists, or an existing system needs formal documentation).

### Instruction Pattern
For stage plots: enumerate each band member's equipment and monitoring requirements, describe their stage position (left/right/center), and specify the Input/Output list format. For process maps: describe the process steps, decision points, and swimlane structure. For schematics: enumerate the components, connections, and naming conventions. In all cases, provide explicit format requirements (paper size, orientation, symbol standards, labeling conventions) separately from the content requirements.

### Constraint Injection Points
- **Paper format and orientation:** landscape vs. portrait; standard page vs. large format (11×17)
- **Symbology standard:** IEC (electrical) vs. ANSI vs. process mapping standard (tasks as rectangles, decisions as diamonds) vs. stage plot conventions (icon-based)
- **Naming conventions:** Wire labels, node labels, member titles, input/output numbering — each has specific rules that can be varied
- **Layout direction:** Stage plots have "front of stage at bottom" convention; electrical diagrams read left-to-right; process maps can flow top-to-bottom or left-to-right
- **Swimlane / lane structure:** Number of lanes (1, 2, or more), what each lane represents
- **Icon sourcing:** Stage plots often require sourced icons for equipment; can be simplified to text-only representation
- **Dual output lists:** Stage plots require Input and Output lists as annexes; can be varied in format (side-by-side, separate page, embedded)
- **Component count / complexity:** Number of devices, circuit branches, process steps, or band members drives difficulty

### Structural Template

```
[PERSONA]: You are a [ROLE: IEM tech / industrial engineer / electrical/controls engineer] working with [ORG: national touring band / logistics hub / automation equipment firm].

[TASK_DESCRIPTION]: Create a [DIAGRAM_TYPE: stage plot / process map / safety circuit schematic] for [SYSTEM: band name and configuration / facility name / machine name] that will be used by [AUDIENCE: front-of-house engineers / operational leadership / electricians and safety inspectors].

[CONTENT_REQUIREMENTS]:
- [ELEMENT_1]: [describe component, position, and connection: e.g., "Performer A: stage-right position, primary instrument DI box, secondary instrument DI box, in-ear monitor split, monitor wedge at a specified stage angle"]
- [ELEMENT_2]: [describe]
- [ELEMENT_N]: [...]
- [DECISION_POINT if applicable]: [describe routing logic or branching]
- [FAILURE_HANDLING if applicable]: [describe rerouting logic]

[SPECIFIC_LABELING_RULES]:
- [INPUT_LIST: numbered, named by member/instrument role, side-by-side with Output list at top of page]
- [OUTPUT_NUMBERING: e.g., a fixed rotational order starting from a specified reference position]
- [WIRE_LABELS: e.g., a power/polarity-coded wire ID, naming convention specified]
- [LANE_LABELS: swimlane names describing each lane's handling method, e.g., an automated-path / manual-path pair]

[FORMAT_REQUIREMENTS]:
- Output format: PDF
- Orientation: [landscape / portrait]
- Paper size: [standard / 11×17]
- Symbol standard: [IEC / process mapping standard / stage plot conventions]
- [ADDITIONAL_FORMAT_RULES: connector width, component spacing, title block requirements]

[OUTPUT_SPECIFICATION]: Single PDF page — [ORIENTATION], [PAPER_SIZE], fully labeled, following [SYMBOL_STANDARD] conventions, with [TITLE_BLOCK / INPUT-OUTPUT LISTS / SWIMLANE LABELS] as specified
```

## 4. Reference File Requirements

### File Types Needed
- **Machine/facility layout image (PNG/JPG, optional):** A physical layout reference showing where components are spatially located in the real environment. Used in schematic tasks to establish the physical context for the circuit design. For stage plots, no reference image is needed — the layout derives from the prompt description.
- **Component specification (PDF via URL, optional):** Technical specification document for a key component (e.g., safety relay pinout). Required when wiring must follow manufacturer-specified pin designations. The pipeline should retrieve these from URLs provided in the prompt.
- **Existing process documentation (DOCX, optional):** Notes, prior process descriptions, or ad-hoc documentation of the current (unstandardized) process. Used in process mapping tasks to give the engineer raw material to formalize.

### Data Characteristics
For stage plots: no reference files are needed; all content derives from the prompt description of equipment per band member and stage positions. For process maps: the process description embedded in the prompt serves as the reference, with no attached files. For electrical schematics: a physical layout image (PNG, typically simple black-and-white diagram) showing equipment positions, plus a URL pointing to a manufacturer specification document. The image should be clearly labeled with component names/IDs matching those referenced in the prompt.

### File Complexity Spectrum
- **Minimal:** No reference files; diagram generated entirely from prompt description of a simple 3–4 element stage plot or 5-step process map.
- **Moderate:** Single reference image (machine layout PNG) showing physical positions; 6–8 components to represent; standard symbols required.
- **Complex:** Physical layout PNG + manufacturer spec PDF (via URL); 12+ components with strict naming conventions for each connection; multi-channel wiring (several safety-interlock devices wired in series, multiple load outputs wired in parallel); IEC symbol standard; 11×17 landscape format with title block and minimum connector width/spacing specifications.

## 5. Output Specification

### Primary Deliverable
- **Format:** PDF (typically a single page for this pattern)
- **Structure:** Diagram with labeled elements + ancillary lists (Input/Output for stage plots; title block for schematics; swimlane labels for process maps)
- **Key quality signals:** All named components present and correctly positioned relative to each other; naming conventions applied correctly (no deviation from specified label formats); symbol standard adhered to throughout (no mixing of symbol styles); output is legible at intended use scale; no missing connections or unlabeled nodes

### Secondary Deliverables (if any)
- None — single PDF is the standard deliverable for this pattern

### Gold Output Characteristics
A gold stage plot has each band member's equipment correctly positioned (stage right/left/center), all equipment types represented with distinct icons, Input and Output lists with correct and consistently-applied numbering conventions, and front-of-stage orientation at the bottom of the page. A gold process map uses standard symbols without deviation (tasks as labeled rectangles, decisions as labeled diamonds), has correctly named swimlanes, and represents all specified decision branches including failure/rerouting paths. A gold electrical schematic uses only IEC-standard symbols, applies the specified wire label naming convention to every conductor, correctly represents the series/parallel wiring topology of safety circuits, and includes a compliant title block — all at the specified paper size and orientation with connector width and spacing within tolerance.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Component count | 3–5 elements | 6–10 elements | 12+ elements with distinct per-element rules |
| Symbology standard | Free-form / icon-based | One named standard (process mapping) | Strict IEC standard with specific connector/spacing specs |
| Naming convention | Descriptive labels only | Numbered lists with convention | Precise alphanumeric codes per conductor/node (e.g., a power/polarity-coded wire ID) |
| Layout complexity | Single lane / no spatial constraint | Dual swimlane with simple routing | Multi-lane with decision branches + failure rerouting |
| Reference file dependency | No files needed | Single layout image | Layout image + external spec PDF (URL-based retrieval) |
| Output format | Any digital format | Standard portrait PDF | Large-format landscape PDF (11×17) with title block and spacing constraints |

## 7. Boundary Cases & Adjacent Patterns

- **H1 (Broadcast Commercial & Video Editing):** H4 outputs are static diagrams in PDF; H1 outputs are video files. No realistic overlap.
- **H2 (VFX Compositing):** Both may involve spatial layout decisions, but H2 is video compositing work and H4 is static diagram creation. Different tools, different deliverables.
- **C5 (Form & Template Design):** Both H4 and C5 can produce PDF documents. H4 documents are technical diagrams with spatial/signal-flow content and domain symbology; C5 documents are fillable forms and intake questionnaires with field types and validation logic. If the output is a diagram showing how things connect, it's H4; if the output is a form for data collection, it's C5.
- **B1 (Performance Analysis Presentation):** B1 may include charts and diagrams as part of a presentation, but those diagrams are analytical visualizations (trend charts, histograms, control charts). H4 diagrams are operational technical drawings (how to connect, where things are positioned, what sequence to follow). Different cognitive work and different audiences.
- **J3 (API Specification & Technical Architecture Design):** Both can produce technical design documents. H4 produces visual diagram artifacts (PDFs) for operational practitioners; J3 produces machine-readable specifications (YAML, architecture text) for software engineers. If the output is a PDF diagram, it's H4.
