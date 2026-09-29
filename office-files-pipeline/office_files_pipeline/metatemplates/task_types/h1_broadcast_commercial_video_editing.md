# Broadcast Commercial & Video Editing

**Macro Category:** H — Creative & Media Production
**Pattern ID:** H1

## 1. Pattern Description

The worker assembles a broadcast-ready video deliverable — a short-form commercial, public-interest spot, or showreel — by sourcing stock footage and music, constructing an editorial timeline from a script or brief, applying graphic treatments (title cards, supers, overlays), and exporting to precise technical specifications. The cognitive core is editorial judgment: selecting clips that match the intended tone, pacing cuts to music, and executing technically constrained timelines (exact durations, codec/resolution requirements). What distinguishes this pattern from general video production is the hard brevity constraint (15–90 seconds) combined with simultaneous creative, licensing, and delivery obligations. The worker is both editor and media researcher in a single workflow.

## 2. O*NET Grounding

### Occupation Families
- 27-4032 Film and Video Editors — core occupation; the worker is explicitly an editor assembling a timeline from reference materials
- 27-1014 Special Effects Artists and Animators — relevant when showreels or graphic treatment tasks involve CGI or compositing elements
- 27-2012 Producers and Directors — adjacent when the editor also makes creative/licensing decisions autonomously

### Key Work Activities (O*NET vocabulary)
- Editing Film or Video Footage to Produce a Finished Product
- Selecting and Combining the Most Appealing Shots from Filmed Material
- Integrating Audio Materials (music, SFX, voiceover) with Visual Footage
- Researching and Evaluating Available Media Assets for Licensing Suitability
- Coordinating Activities with External Suppliers (stock footage platforms)
- Applying Color Grading and Image Correction Techniques
- Creating or Modifying Visual Graphic Elements (titles, supers, cards)
- Verifying Technical Delivery Specifications (codec, resolution, duration)

### Knowledge Domains (O*NET vocabulary)
- Communications and Media
- Fine Arts
- Computers and Electronics
- English Language (script alignment, VO scratch recording)
- Law and Government (licensing, royalty-free compliance)

### Generalizable Work Context
A freelance or agency-employed video editor receives a project brief from an advertising, political campaign, or corporate client. The brief includes a script (PDF or Word) with cue descriptions, and sometimes pre-built graphic assets (PSD files). The editor is responsible for both sourcing the visual and audio raw materials and assembling the final deliverable without production crew support. The task is triggered by a client deadline and a finalized script/brief. Stakeholders include the client (reviews final cut), the creative director (provides brief), and the technical deliverer (broadcast station or digital platform with delivery specs).

## 3. Prompt Construction Template

### Persona Pattern
Assign the worker as a video editor at a freelance, agency, or studio context. Include the client relationship (e.g., political campaign agency, CGI studio) and the nature of the engagement (single deliverable, time-sensitive). Seniority should be mid-level — experienced enough to make autonomous creative decisions but operating within a defined brief.

### Scenario Pattern
The client has provided a finalized script or project brief. A deadline exists. The editor must source missing materials (stock footage, music) from approved platforms, assemble the edit, apply specified graphic treatments, and export to exact delivery specs. The triggering event is receipt of the brief/script, and the deliverable is a single video file plus (optionally) a sourcing log.

### Instruction Pattern
Use a numbered multi-step workflow that mirrors the editorial pipeline: (1) source materials, (2) assemble timeline per script, (3) apply graphics/supers, (4) mix audio, (5) apply color/speed treatments, (6) export. Each step should embed the relevant constraints (e.g., exact timestamp for graphic card, music edit requirements, speed manipulation limits). This pattern naturally generates specificity without requiring the prompt to be overly prescriptive.

### Constraint Injection Points
- **Duration constraint:** hard exact duration (e.g., exactly 15, 30, 60, or 90 seconds); varies by broadcast slot
- **Codec/resolution:** H.264 .mp4 at 1920×1080 is standard; can vary to ProRes, 4K, vertical 9:16 for social
- **Graphic treatment:** title cards (white on black) vs. lower-thirds vs. PSD super overlays; number and placement tied to script cues
- **Stock sourcing rules:** can vary between "watermarked previews only" (no purchase) to "must be licensed" to "client-provided clips only"
- **Music constraints:** genre, energy, and edit-to-duration requirement; can vary between provided track and free-sourcing
- **Color treatment:** neutral (no treatment) vs. desaturate/darken (somber) vs. warm grade (optimistic); toggled by emotional tone
- **Sourcing log:** optional deliverable; can be omitted for simpler variants or required with full URL documentation

### Structural Template

```
[PERSONA]: You are a [ROLE: video editor / post-production specialist] working for [ORG_TYPE: advertising agency / political campaign firm / VFX studio]. You are completing a [PROJECT_TYPE: 30-second commercial / 15-second spot / showreel] for client [CLIENT_NAME/TYPE].

[TASK_DESCRIPTION]: You have received the attached [REFERENCE_FILES: broadcast script PDF / project brief / footage archive]. Your task is to produce a broadcast-ready video deliverable following the specifications below.

[REQUIREMENTS]:
1. Source [N] royalty-free [footage clips / music tracks] from [PLATFORMS: e.g., AdobeStock, Shutterstock, Pond5, YouTube Audio Library]. [Watermarked previews acceptable / licensed files required]. Log all URLs.
2. Assemble a timeline matching the attached script, placing [footage type: B-roll, talking head] to corresponding script cues.
3. Insert [N] graphic [title cards / text supers / overlay assets] at the following cue points: [CUE_DESCRIPTIONS].
4. Edit the music track to exactly [DURATION] with [strong opening and closing / music bed under VO / SFX at designated moments].
5. Apply [COLOR_TREATMENT: none / desaturate and darken / warm color grade] to all footage.
6. [Optional: Record a scratch VO track aligned to script timing.]
7. Export as [CODEC: H.264] .mp4 at [RESOLUTION: 1920×1080], exactly [DURATION] in length.

[CONSTRAINTS]:
- Hard duration: exactly [N] seconds (no tolerance)
- [GRAPHIC_RULE: Each super must appear on a unique shot / First shot must be super-free]
- [SPEED_RULE: Speed changes up to a specified maximum permitted / No speed manipulation]
- Music must not include copyrighted material; [attribution / watermark] rules apply
- [ASSET_RULE: Use provided PSD assets for supers / recreate from script copy]

[OUTPUT_SPECIFICATION]: Single .mp4 file (H.264, 1920×1080, [N] seconds) + [optional: URL sourcing log in .txt or .docx]
```

## 4. Reference File Requirements

### File Types Needed
- **Broadcast script (PDF or DOCX):** Short-form script (15–120 seconds) with voiceover copy, scene/shot descriptions, duration notes per segment, and marked graphic card moments. Should indicate tone and emotional register.
- **Graphic asset file (PSD or PNG, optional):** Pre-built text supers or title card assets ready for NLE import. Used when graphic treatment is pre-designed rather than created by editor.
- **Footage archive (ZIP, optional):** Collection of source video clips (MP4, MOV) with or without embedded audio. Used in showreel/demo reel variants where all footage is provided.
- **Music track (MP3 or WAV, optional):** Provided royalty-free music file, used when client specifies a particular track rather than leaving sourcing to the editor.

### Data Characteristics
The script should be 1–2 pages for a short-form commercial, with segment-level timing annotations (e.g., ":00–:08 — establishing shot, city skyline"). Graphic card moments should be explicitly identified in the script. PSD files should be layered with named text elements. Video clip archives should contain 5–20 discrete clips of varying lengths (10–60 seconds each), possibly with naming conventions that indicate intended content or sequence.

### File Complexity Spectrum
- **Minimal:** Single PDF script with cue descriptions; no pre-built assets; editor sources everything. One output file.
- **Moderate:** PDF script + PSD super file; editor sources footage and music; specific placement rules for supers.
- **Complex:** PDF script + PSD supers + footage archive (10+ clips) + provided music track; complex audio assignment rules (SFX-to-clip pairings, embedded audio retention for specific clips); URL sourcing log required.

## 5. Output Specification

### Primary Deliverable
- **Format:** H.264 .mp4 (standard broadcast delivery)
- **Structure:** Single video file; exact duration (no handles); audio mix (music bed + VO scratch or SFX)
- **Key quality signals:** Duration exactly matches requirement; graphic elements appear at correct cue points; music edits have strong in/out points; color treatment is consistent across all footage; codec and resolution verified

### Secondary Deliverables (if any)
- **Sourcing log (DOCX or TXT):** List of URLs for all stock footage clips and music used, with platform and licensing notes
- **Alternate cuts:** Some briefs specify a :15 cut in addition to a :30 — can be added as a complexity variant

### Gold Output Characteristics
A gold output respects the hard duration to the frame. Graphics appear on the correct shots per script cues, with no duplicate shots sharing a super. Music has a deliberate in-point and out-point (not a raw cut from the middle of a track). Color treatment is uniform. The sourcing log contains direct, working URLs. If a scratch VO was required, it is intelligibly recorded and synchronized. The editorial choices (shot selection, pacing, music genre) align with the specified tone (e.g., somber, optimistic, or high-energy).

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Duration | 60+ seconds (more editorial flexibility) | 30 seconds | 15 seconds (maximum constraint) |
| Graphic treatment | No graphics / simple title card | 1–2 graphic cards at marked cues | Multiple supers, one per shot, PSD assets, sequencing rules |
| Stock sourcing | All footage provided in archive | 3–5 clips to source, genre specified | Full sourcing from scratch, 10+ clips, URL log required |
| Audio complexity | Single provided music track, no edit needed | Music must be edited to exact duration | Music edit + SFX assignments to specific clips + scratch VO |
| Color/speed treatment | No treatment required | One treatment applied uniformly | Clip-specific speed manipulation + color grade for tone |
| Deliverable count | Single video file | Video + sourcing log | Video + sourcing log + alternate cut |

## 7. Boundary Cases & Adjacent Patterns

- **H2 (VFX Compositing & Post-Production):** H1 involves timeline assembly and stock sourcing; H2 involves frame-level compositing work (motion tracking, alpha channels, green screen). The distinction is whether the task is editorial (cutting, assembling, sourcing) vs. compositional (layering visual elements with technical precision). A showreel edit that happens to include some VFX clips is H1; a task that requires stabilizing footage and perspective-tracking an overlay is H2.
- **H4 (Visual Stage Plots & Technical Diagrams):** Both can involve visual output in PDF, but H4 is diagrammatic/technical (IEC symbols, swimlanes) while H1 is cinematic/editorial. No ambiguity in practice.
- **H3 (Audio Composition, Editing & Mixing):** H1 tasks include music as a supporting element in a video context; H3 tasks treat audio as the primary deliverable. If the output is a video file, it's H1 even if audio work is required.
- **H7 (Production Scheduling & Budgeting):** H7 produces planning artifacts for a video project; H1 produces the actual video deliverable. Choose H7 when the task is about planning/budgeting a shoot, H1 when the task is about editing the media itself.
