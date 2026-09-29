# VFX Compositing & Post-Production

**Macro Category:** H — Creative & Media Production
**Pattern ID:** H2

## 1. Pattern Description

The worker creates a polished visual effects shot by executing a technically precise multi-step compositing pipeline: stabilizing source footage, isolating elements via masking and alpha channel creation, stitching non-contiguous clip segments, locking the composite via motion tracking, matching color between layers, and adding practical or stock VFX elements (flashes, smoke, particles). The cognitive core is technical craft at the frame level — knowing which tool achieves which visual result and in what order operations must be performed. This pattern is distinct from H1 (broadcast editing) in that the unit of work is a single shot or sequence, not a program-length timeline, and the key skills are compositing and effects work rather than editorial assembly. Success depends on seamless visual integration: the viewer should not be able to detect the composite.

## 2. O*NET Grounding

### Occupation Families
- 27-1014 Special Effects Artists and Animators — primary occupation; involves creating visual effects and composited imagery
- 27-4032 Film and Video Editors — relevant when the compositor also handles editorial context around the VFX shot
- 17-2061 Computer Hardware Engineers — tangentially relevant for render pipeline and hardware knowledge
- 27-4011 Audio and Video Technicians — adjacent for technical format compliance aspects

### Key Work Activities (O*NET vocabulary)
- Creating and Modifying Visual Effects Using Specialized Software
- Editing Film or Video Footage Using Digital or Computerized Tools
- Stabilizing and Correcting Source Footage
- Applying Motion Tracking and Perspective Locking Techniques
- Creating Masks, Mattes, and Alpha Channels for Element Isolation
- Matching Color and Exposure Between Composite Layers
- Sourcing and Integrating Stock VFX Elements (smoke, fire, particles)
- Verifying Output Format Fidelity (dimensions, framerate, codec match)

### Knowledge Domains (O*NET vocabulary)
- Fine Arts
- Computers and Electronics
- Communications and Media
- Engineering and Technology (render pipelines, codec specifications)
- Mathematics (motion tracking algorithms, color science)

### Generalizable Work Context
A compositor or VFX artist working in post-production receives raw production footage (multiple camera angles or takes) and a creative brief describing a required visual effect. The task is triggered by the creative director or VFX supervisor identifying a shot that requires digital enhancement or replacement that was not fully captured on set. Stakeholders include the director (defines the visual intent), the VFX supervisor (sets quality bar), and the colorist (for final grade alignment). The compositor works autonomously to deliver a single polished shot file that will be cut into the timeline by the editor.

## 3. Prompt Construction Template

### Persona Pattern
Assign the worker as a compositor or VFX artist in a film/TV/commercial post-production context. The role should have technical expertise (knowledge of NLE/compositing software, motion tracking, color grading) but operate under a creative director or VFX supervisor's direction. The organizational context should be a post-production house, VFX studio, or in-house post team at a production company.

### Scenario Pattern
A specific shot was not captured cleanly in production, or a visual effect needs to be created digitally to achieve the director's intended result. The compositor receives the raw footage clips (base plate, overlay/action clip) and a description of what the final shot should look like. A stock VFX element (smoke, fire, particles) may need to be sourced from royalty-free libraries. The task is bounded: deliver one finished shot file at the same specifications as the base clip.

### Instruction Pattern
Use a numbered sequential workflow — each step must be completed before the next can begin, since operations are dependent (must stabilize before masking, must track before compositing, etc.). Embed creative and technical requirements within each step. The numbered structure mirrors professional compositing pipeline order and naturally produces a well-structured, testable task.

### Constraint Injection Points
- **Output format parity:** Output must match base clip's resolution, framerate, and codec exactly; can vary the base format (1080p/24fps, 4K/25fps, etc.)
- **Timecode guidance:** Specific start/end times for clip segments to stitch; can be precise (e.g., an exact timecode) or approximate (e.g., "starting partway into the clip")
- **Masking complexity:** Simple rectangular isolation vs. rotoscoped organic shape vs. alpha-channel window/object mask; drives difficulty
- **Motion tracking type:** Static camera (no tracking needed) vs. simple 2D translation vs. perspective/planar tracking for moving camera
- **VFX elements required:** None vs. single overlay (smoke) vs. multiple layers (flash + smoke + color pulse)
- **Color grading precision:** No note (judge by eye) vs. match specific exposure/saturation to base plate
- **Stabilization requirement:** Not needed (locked-off camera) vs. digital stabilization of handheld footage before any other work

### Structural Template

```
[PERSONA]: You are a [ROLE: compositor / VFX artist / post-production specialist] working at [ORG_TYPE: film post-production house / VFX studio / in-house production team]. You are working on [PROJECT: film scene / commercial / broadcast insert].

[TASK_DESCRIPTION]: You need to create a polished [EFFECT_TYPE: teleportation / disappearance / environment replacement / title integration] VFX shot by compositing [CLIP_A: base plate clip name] with elements from [CLIP_B: overlay clip name]. The final output should match [CLIP_A]'s dimensions, framerate, and codec.

[REQUIREMENTS]:
1. [STABILIZE]: Stabilize [CLIP_B / designated footage] to remove [camera shake / drift / jitter].
2. [ISOLATE]: Create a [window mask / organic roto / alpha channel] around [ELEMENT] in [CLIP_B] to isolate it from the background.
3. [STITCH]: Select and stitch [DURATION_A] of [performance / action] from [START_TIMECODE] plus [DURATION_B] of [empty plate / background-only] to create [EFFECT_DESCRIPTION].
4. [COMPOSITE]: Use [planar / 2D / corner-pin] motion tracking on [CLIP_A] to lock [stitched element] into the scene across all frames.
5. [GRADE]: Apply a color grading pass to match [CLIP_B element] to [CLIP_A base plate] in [exposure / saturation / white balance].
6. [VFX]: Source royalty-free [smoke / fire / particle] VFX footage from [stock platforms]. Add [VFX element] synchronized to [EVENT: frame of disappearance / moment of impact]. Also add [PRACTICAL_EFFECT: light flash / color pulse] at [TIMING].
7. Export a single video file matching [CLIP_A]'s [resolution, framerate, codec] exactly.

[CONSTRAINTS]:
- Output must match base clip specifications exactly (no resolution or framerate changes)
- [TIMECODE_CONSTRAINT: Stitched segment begins at approximately [N] seconds into [CLIP_B]]
- [FLASH_CONSTRAINT: VFX flash must occur at the precise frame of [EVENT]]
- [STOCK_CONSTRAINT: All added VFX elements must be royalty-free / attribution-free]
- [STABILIZATION_NOTE: Stabilize before any other operations]

[OUTPUT_SPECIFICATION]: Single video file (format matching [CLIP_A]) — [filename convention if specified]
```

## 4. Reference File Requirements

### File Types Needed
- **Base plate clip (MP4/MOV):** The background or establishing shot that the composite will be built on. Typically a moving-camera or locked-off shot of the environment without the primary VFX subject. This is the "world" that everything else will be placed into.
- **Overlay/action clip (MP4/MOV):** The foreground or actor performance clip containing the element to be composited. May have camera drift/shake requiring stabilization. May be shot against a non-chroma-key background (requiring rotoscoping rather than keying).
- **Empty plate (optional):** A clean version of the scene with no subjects, used as the background state for before/after VFX moments.

### Data Characteristics
Clips should be realistic production footage — not stock clips of clearly different quality. The base plate should be shot on a moving or handheld camera to require tracking work. The overlay clip should have a visible stability issue (jitter, drift) requiring correction. Clip durations should be 15–60 seconds each. Both clips should share the same general scene/environment for plausibility. The overlay element should be clearly identifiable as requiring isolation (e.g., a subject framed within a structural element like a window, door, or defined zone).

### File Complexity Spectrum
- **Minimal:** Two clips (base + overlay), static camera (no tracking needed), simple rectangular mask, no stock VFX sourcing required. Single output file.
- **Moderate:** Two clips, moving camera requiring 2D tracking, organic mask shape, one stock VFX element to source and composite.
- **Complex:** Two clips with handheld instability, perspective/planar tracking on moving camera, alpha-channel isolation of complex shape, multiple VFX layers (flash + stock smoke), color grade required, output must match base clip's exact codec and framerate.

## 5. Output Specification

### Primary Deliverable
- **Format:** Video file (codec and resolution matching base clip exactly — typically H.264 MP4 or ProRes MOV)
- **Structure:** Single composited shot file at the same duration as the base clip
- **Key quality signals:** The composite is seamless (no visible edge artifacts on the mask); the motion tracked element does not drift or slip; color match is convincing; VFX overlay blends naturally; output file specs match the base clip

### Secondary Deliverables (if any)
- None for this pattern — output is a single shot file. In complex pipeline contexts a "comp breakdown" frame or project file might be requested, but this remains atypical for the pattern.

### Gold Output Characteristics
A gold output cannot be distinguished from a clean on-set capture by a non-technical viewer. The masked element has clean edges with no fringing. The motion tracking holds across all frames without sliding. The color grade matches the base plate's exposure and saturation within a normal tolerance. The VFX elements (smoke, flash) are time-synchronized to the correct frame and blend into the scene without obvious blending artifacts. The output file matches the base clip's resolution, framerate, and codec exactly.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Camera motion | Static camera (no tracking needed) | Simple 2D pan/tilt tracking | Perspective/planar tracking, moving camera with parallax |
| Mask complexity | Simple rectangular crop | Semi-organic shape (window, doorframe) | Rotoscoped organic subject requiring frame-by-frame refinement |
| VFX element count | No additional VFX | One stock overlay sourced online | Two+ VFX layers (practical + stock) at precise timing |
| Stabilization | Not needed | Single clip stabilized before masking | Both clips require stabilization with different parameters |
| Color grade | No note (judge by eye) | Match general exposure/saturation | Match specific technical target (exposure stops, LUT application) |
| Clip stitching | Single contiguous segment used | Two segments stitched at one point | Multiple segments from different timecodes stitched seamlessly |

## 7. Boundary Cases & Adjacent Patterns

- **H1 (Broadcast Commercial & Video Editing):** H1 tasks assemble a multi-clip timeline; H2 tasks work on a single shot. If the task asks the worker to "edit a commercial that includes some VFX work," it is H1 with VFX as a sub-task. If the entire task is delivering one composited shot with a specific technical compositing pipeline, it is H2.
- **H4 (Visual Stage Plots & Technical Diagrams):** Both require technical precision, but H2 is video-based while H4 is diagrammatic. No realistic overlap.
- **J1/J2 (Software Development):** If the "VFX" task is actually writing scripting tools or render automation (Python scripts for Nuke/After Effects), it belongs in Macro Category J. H2 tasks produce visual media files, not code.
