# Moodboard & Visual Direction

**Macro Category:** H — Creative & Media Production
**Pattern ID:** H6

## 1. Pattern Description

The worker synthesizes aesthetic direction from multi-stakeholder creative brainstorming notes into a single visual moodboard document that communicates the intended look, feel, color palette, and reference imagery for a media production. The deliverable is a visual artifact (PNG or PDF) — not a text document — that will guide the cinematographer, art director, production designer, and costume designer during pre-production. The cognitive core is creative synthesis and visual curation: reading qualitative notes about emotional tone and aesthetic preferences, translating those abstractions into a coherent visual language, and selecting reference images that collectively embody the intended direction without any single image being the literal target. This pattern is distinct from all other H-pattern tasks because the output is a curated image composition, not edited media, code, or text.

## 2. O*NET Grounding

### Occupation Families
- 27-1011 Art Directors — primary occupation; moodboard creation is a core art direction tool
- 27-2012 Producers and Directors — common in music video and commercial production contexts
- 27-1025 Interior Designers — adjacent; moodboarding is also a core design tool in interior and spatial contexts
- 27-1021 Commercial and Industrial Designers — relevant in product and advertising design contexts
- 27-4032 Film and Video Editors — adjacent when the editor also handles pre-production creative direction

### Key Work Activities (O*NET vocabulary)
- Developing Creative Concepts and Visual Direction for Media Productions
- Synthesizing Stakeholder Input into Coherent Creative Frameworks
- Curating Reference Images and Color Palettes for Visual Communication
- Communicating Visual Aesthetic Direction to Production Teams
- Researching and Sourcing Reference Materials from Online and Archival Sources
- Evaluating Creative Materials for Alignment with Project Tone and Brand
- Creating Visual Layouts and Compositions (moodboard design)
- Coordinating Creative Vision Across Multiple Stakeholders (artist, director, art director)

### Knowledge Domains (O*NET vocabulary)
- Fine Arts (color theory, visual composition, aesthetic traditions)
- Communications and Media (production workflows, creative direction tools)
- Design (typography, layout, image selection principles)
- English Language (interpreting meeting notes, understanding creative language)
- Psychology (understanding emotional associations with visual stimuli)

### Generalizable Work Context
A music video or commercial producer, art director, or production designer receives compiled brainstorming notes from a multi-stakeholder creative meeting (artist, director, art director, or brand team) and must consolidate the various aesthetic inputs into a single visual document that the entire production team can reference. The task is triggered at the pre-production milestone where creative direction has been discussed but not yet formalized visually. The moodboard replaces a long verbal description and serves as the shared reference for all visual decision-making from that point forward. It is typically created before any budgets are locked to cinematography, costuming, set design, or locations.

## 3. Prompt Construction Template

### Persona Pattern
Assign the worker as a music video producer, art director, or production coordinator in a music, advertising, or film pre-production context. The persona should reflect that they were present at the creative meetings and are now responsible for translating those discussions into a visual document. Include the collaborative context: the worker must balance multiple stakeholders' expressed preferences, not just their own aesthetic judgment.

### Scenario Pattern
A creative project (music video, commercial, short film, fashion editorial) has completed its initial brainstorming phase. Notes from the meeting have been compiled into a reference document. The worker must now produce a moodboard that captures the agreed-upon aesthetic direction. A tonal reference (e.g., a YouTube link to a similar song, a film reference, or a brand reference) may be provided to help calibrate the emotional register. The moodboard will be shared with the full production team.

### Instruction Pattern
Specify the input document type (meeting notes PDF), the output format (PNG, with a defined composition structure including color palette section and reference image grid), and the tonal calibration reference (if any). List the aesthetic dimensions to address: color palette, visual texture, lighting mood, compositional style, and emotional register. For music video contexts, include the song description as context for tonal alignment.

### Constraint Injection Points
- **Output format:** PNG vs. PDF vs. PPTX; affects tool choice and layout flexibility
- **Color palette specification:** Required vs. optional; number of colors in palette; whether exact hex codes are needed or general color families
- **Reference image count:** How many images to include (4, 8, 12, 16+); affects visual density and diversity
- **Stakeholder count and alignment complexity:** Two stakeholders (director + artist) vs. three+ (artist + director + art director + brand team); more stakeholders = more potentially conflicting aesthetic inputs to reconcile
- **Tonal reference type:** YouTube music reference vs. film references vs. brand/campaign references vs. no reference provided
- **Aesthetic dimensions specified:** Generic ("dark and moody") vs. specific (named visual traditions, named directors, named color grading styles)
- **Input document structure:** Organized meeting notes with clear preferences vs. raw brainstorming notes with contradictions to resolve

### Structural Template

```
[PERSONA]: You are a [ROLE: music video producer / art director / production coordinator] working on the music video for [ARTIST_NAME]'s [SONG_TITLE], a [GENRE/MOOD_DESCRIPTION: downtempo ballad / upbeat pop track / experimental electronic piece].

[CREATIVE_CONTEXT]: The [DIRECTOR], [ARTIST], and [ART_DIRECTOR] have completed their initial brainstorming sessions. The attached [meeting notes / creative brief PDF] captures the aesthetic direction discussed, including [key aesthetic themes from notes: e.g., warm nostalgia, architectural environments, muted palette with one bold accent color].

[TONAL_REFERENCE]: For additional tonal context, refer to this [YouTube / Vimeo link] as a reference for the song's emotional register: [URL].

[TASK_REQUIREMENTS]:
1. Read the attached [REFERENCE_FILE: meeting notes PDF] and identify the key aesthetic preferences, agreed-upon visual themes, and any specific references mentioned by each stakeholder.
2. Curate [N] reference images that collectively embody the agreed aesthetic — representing [VISUAL_DIMENSIONS: lighting style, color palette, setting type, costume direction, compositional framing].
3. Define a color palette of [N] colors (with [hex codes / general color description]) that captures the emotional register of the visual direction.
4. Compose all elements (color palette + reference images + [optional: title/project text]) into a single [FORMAT: PNG / PDF] moodboard.

[AESTHETIC_PARAMETERS]:
- Emotional tone: [e.g., playful and upbeat, somber and restrained, glamorous, gritty and raw]
- Visual references to embody: [e.g., dramatic stage lighting, rich architectural interiors, high contrast black and white with single color accent]
- Visual references to avoid: [e.g., overly commercial, bright and cheerful, literal music-video clichés]
- Music alignment: align visual mood with [SONG_DESCRIPTION: orchestral swell / up-tempo energy / melancholic introspection]

[CONSTRAINTS]:
- Must reflect all stakeholder inputs from the meeting notes (not just the director's or artist's)
- Color palette must be included
- Reference images must be curated, not generated (sourced from public domain, stock, or cited references)
- Output must be a single [PNG / PDF] file

[OUTPUT_SPECIFICATION]: Single [PNG / PDF] moodboard — [approximate dimensions or aspect ratio if specified] — containing color palette + reference images + [optional: production title text]
```

## 4. Reference File Requirements

### File Types Needed
- **Compiled meeting notes (PDF or DOCX):** A synthesis of brainstorming discussions from multiple stakeholders, organized by attendee or by topic. Should capture aesthetic preferences in qualitative language: emotional descriptions, references to films or art movements, color descriptors, likes/dislikes, and any specific visual requests. Should also capture areas of disagreement or tension that the moodboard must reconcile. Typically 2–5 pages of structured notes.
- **Tonal reference link (URL, embedded in prompt):** A YouTube or Vimeo link to a musical or visual reference that calibrates the emotional register. Not a file, but a reference point embedded in the prompt. Used to help the worker understand the mood the visuals must support.

### Data Characteristics
Meeting notes should reflect genuine multi-voice creative discussions — not a single unified aesthetic vision but a constellation of related inputs that need synthesis. Notes should reference at least three distinct aesthetic dimensions (e.g., color/lighting, spatial setting, emotional register). They should include at least one concrete reference (a named film, director, photographer, or art movement) alongside more abstract descriptions. At least one tension or unresolved preference should exist to challenge the worker to exercise aesthetic judgment. The tone reference URL should be accessible public content (YouTube, Vimeo) and should be genuinely tonally relevant to the described aesthetic.

### File Complexity Spectrum
- **Minimal:** Structured meeting notes from two stakeholders, two aesthetic dimensions specified, no specific references mentioned; produce a simple moodboard with 4 images and a 4-color palette.
- **Moderate:** Meeting notes from three stakeholders with some aesthetic tension; specific film/director references mentioned; produce a moodboard with 8–10 images, a 6-color palette, and labeled image sources.
- **Complex:** Meeting notes from four stakeholders with conflicting preferences (e.g., one stakeholder wants minimalist and restrained, another wants ornate and maximalist); specific aesthetic tradition references; produce a moodboard with 12+ images organized by visual dimension (lighting, costume, setting, texture) plus a color gradient palette; tonal reference URL provided; PNG format with designed layout.

## 5. Output Specification

### Primary Deliverable
- **Format:** PNG (most common for this pattern; PDF is also acceptable)
- **Structure:** Composed visual layout containing: (a) a color palette section (color swatches, optionally with hex codes), (b) a grid or arrangement of reference images, (c) optionally a project title or brief descriptive text overlay
- **Key quality signals:** Color palette is coherent and tonally appropriate to the described aesthetic; reference images collectively embody the aesthetic direction (no image contradicts the direction); the composition itself reads as professionally designed (not a random collage); all stakeholder inputs from the notes are representable in the final direction (no major preference ignored)

### Secondary Deliverables (if any)
- None required for this pattern. In some production contexts, a written one-paragraph "visual direction statement" accompanies the moodboard, but it is not a required deliverable.

### Gold Output Characteristics
A gold moodboard has an immediately legible visual tone: a viewer unfamiliar with the notes could describe the aesthetic in terms consistent with the stakeholder intent. The color palette feels intentional — the colors relate to each other harmonically and to the emotional register specified. Reference images span multiple visual dimensions (not all landscape shots, not all costume shots) but feel unified by shared tonal quality. No single image is jarring or off-register. The composition has visual hierarchy — there is a dominant image or focal zone, not pure grid uniformity. The overall file is high enough resolution to be printed and displayed in a production meeting.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Stakeholder count | 1 creative director (unified vision) | 2 stakeholders (director + artist) | 3–4 stakeholders with partially conflicting preferences |
| Aesthetic specificity | Abstract descriptors only ("dark and moody") | Mix of abstract and named references | Named directors, specific art movements, or precise color grading styles |
| Image count | 4–6 reference images | 8–10 images | 12+ images organized into visual categories |
| Color palette depth | 3–4 general colors | 5–6 colors with descriptors | Full palette with hex codes and rationale for each color |
| Tonal reference | No external reference provided | 1 URL (music or visual reference) | Multiple cross-medium references (film, photography, music video) |
| Output format | Any image format | PNG with basic layout | Designed PNG at specified dimensions with labeled sections |

## 7. Boundary Cases & Adjacent Patterns

- **H5 (Screenwriting & Script Development):** H5 produces written text in script format; H6 produces a visual image composition. Both are pre-production creative documents, but the cognitive work and output format are entirely different. A project might need both — H5 for the script, H6 for the visual direction — but they are distinct tasks.
- **H7 (Production Scheduling & Budgeting):** H7 produces planning documents (schedules, budgets); H6 produces creative direction documents (moodboards). Adjacent in the production workflow but different in cognitive work (logistical vs. creative) and deliverable format (structured table/calendar vs. visual composition).
- **C4 (Training Materials & Educational Presentations):** C4 produces instructional content; H6 produces creative direction content. No realistic overlap.
- **B1 (Performance Analysis Presentation):** B1 may include visual elements (charts, graphs) but is data-driven; H6 is aesthetics-driven. If a PowerPoint contains charts and data interpretation, it's B1; if it contains curated imagery and color palettes, it might be H6.
- **H1 (Broadcast Commercial & Video Editing):** H1 produces a finished video; H6 produces a pre-production reference document that would inform what H1 produces. In the production timeline, H6 comes before H1.
