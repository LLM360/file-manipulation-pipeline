# Audio Composition, Editing & Mixing

**Macro Category:** H — Creative & Media Production
**Pattern ID:** H3

## 1. Pattern Description

The worker composes, edits, or mixes audio material — original music, stems, or isolated instrument tracks — using a DAW and professional audio engineering judgment. Tasks span the full audio production spectrum: composing original instrumentation to a reference track, resyncing and processing a displaced instrument within a full mix, and performing timecode-based edits to a specific instrument stem before reassembling all stems into a final mix. The cognitive core combines musical judgment (key, timing, note correctness) with technical craft (loudness normalization, true peak limiting, export format compliance). This pattern is distinguished from H1 (video editing) in that the output is an audio file or audio archive — video is never the deliverable. It is also distinguished by its precision requirements: specific BPM, key, LUFS targets, sample rates, and bit depths are all explicitly constrained.

## 2. O*NET Grounding

### Occupation Families
- 27-2041 Music Directors and Composers — primary occupation for composition tasks
- 27-4014 Sound Engineering Technicians — primary occupation for editing and mixing tasks
- 27-4011 Audio and Video Technicians — relevant for technical format compliance and equipment operation
- 27-2042 Musicians and Singers — adjacent when the task requires live performance judgment about correct notes or phrasing

### Key Work Activities (O*NET vocabulary)
- Composing Original Music to Client Specifications (key, tempo, structure)
- Synchronizing Instrumentation to a Reference Track
- Editing Audio Content at Timecode-Specified Locations
- Correcting Pitch and Timing Errors in Recorded Performances
- Applying Signal Processing (reverb, delay, compression, limiting) to Audio Tracks
- Normalizing Audio Loudness to Broadcast Standards (LUFS)
- Exporting Audio Files to Specified Technical Formats (WAV, stems, master)
- Using Technology to Produce, Edit, and Mix Music (DAW operation)

### Knowledge Domains (O*NET vocabulary)
- Fine Arts (music theory, composition, arrangement)
- Telecommunications (audio signal chain, broadcast standards)
- Engineering and Technology (DAW systems, audio formats, metering)
- Computers and Electronics (audio software, plugin operation)
- English Language (interpreting client briefs, edit spot documents)

### Generalizable Work Context
An audio professional working as a freelance contractor or in-house studio engineer receives a client brief (or an ongoing project brief from a band/artist) requiring specific audio deliverables. The triggering event is receipt of reference audio files (drum tracks, rough mixes, out-of-sync stems, multitrack sessions) combined with a technical brief specifying the required output. Stakeholders include the artist or client (defines creative intent), the mixing/mastering engineer (receives final files), and the distribution platform (imposes loudness/format standards). The audio professional works autonomously in a DAW to produce the deliverable.

## 3. Prompt Construction Template

### Persona Pattern
Assign the worker as a music producer, sound engineer, or mix engineer in a freelance, studio, or in-house capacity. The persona should specify the relevant expertise: composition (for original music tasks), audio editing (for timecode-based correction tasks), or mix engineering (for stem assembly and loudness normalization tasks). Include the client relationship — who is the project for, what is the artistic context.

### Scenario Pattern
Three scenario archetypes exist for this pattern:
- **Composition:** Client provides a drum reference track and a creative brief (genre, key, BPM, structure); worker composes all remaining instrumentation and delivers master + stems.
- **Resync/Edit:** A recording session produced a misaligned or technically flawed audio element; worker must identify the correct placement by reference comparison, perform edits, apply processing, and deliver a fixed mix.
- **Stem Mix Assembly:** A client provides multitrack stems and an edit guide (timecode document listing specific correction points); worker performs edits on the target stem, then assembles all stems into a final deliverable.

### Instruction Pattern
For composition tasks: describe the creative brief (genre, mood, key, BPM, structure/timestamps) then enumerate stem deliverables and format requirements. For editing tasks: describe the problem state (out-of-sync, wrong notes, noise), provide reference files and their roles, then give step-by-step technical instructions (resync, edit, process, mix, export). This pattern naturally segments into: problem diagnosis → correction operations → export spec.

### Constraint Injection Points
- **Tempo (BPM):** Fixed value (e.g., a specific BPM appropriate to the genre); drives all timing decisions; can vary widely
- **Key:** Fixed tonal center (e.g., a specific major or minor key); can include modulation at a specific timestamp (e.g., a shift to a different key for a bridge section)
- **Duration:** Approximate target (e.g., a target length expressed in minutes) or exact with reference track as anchor
- **Timing precision:** Grid quantization to a specific note value at a stated BPM, with a defined tolerance window; can be relaxed or tightened
- **Loudness target:** LUFS average (broadcast standard -16 dB, streaming -14 dB, etc.); always comes with true peak ceiling (-0.1 or -1 dBTP)
- **Audio format:** Sample rate (44.1 / 48 kHz) + bit depth (16-bit / 24-bit / 32-bit float); both must be specified
- **Stem structure:** What stems are required (e.g., Guitars, Bass, Keys, Drums) and whether a master mix is also required
- **Edit precision:** Whether corrections are "replace with silence" (noise) vs. "replace with in-key note from elsewhere in the song" (wrong note)

### Structural Template

```
[PERSONA]: You are a [ROLE: music producer / sound engineer / mix engineer] working [CONTEXT: at a recording studio / as a freelancer / with a band on their album].

[CLIENT_BRIEF]: [CLIENT/ARTIST] needs [DELIVERABLE_TYPE: a composed instrumental track / a corrected and mixed final track / a resynchronized and processed mix] for [PROJECT: album, sync licensing, video project].

[REFERENCE_FILES]:
- [FILE_1]: [role in task — e.g., "drum reference track WAV: rhythmic foundation to sync to"]
- [FILE_2]: [role — e.g., "rough mix MP3: reference for correct positioning of displaced element"]
- [FILE_3]: [role — e.g., "edit spots DOCX: timecode locations of specific corrections needed"]
- [FILE_N]: [role]

[TASK_REQUIREMENTS]:
1. [STEP_1]: [e.g., Sync the [ELEMENT] to the provided reference by [METHOD: visual waveform alignment / listening comparison]. Correct position is [DESCRIPTION].
2. [STEP_2]: [e.g., Edit [ELEMENT] for [PRECISION: quantized to a specific note value at [BPM] BPM, within a defined tolerance window]. Replace [NOISE_TYPE: string noise / clicks / pops] with silence.
3. [STEP_3]: [e.g., Apply [PROCESSING: tasteful reverb and delay] to [ELEMENT] so it blends with the existing mix without [PROBLEM: muddying clarity / excessive wash].
4. [STEP_4]: [e.g., Mix [ELEMENT] into all other stems at a level matching the provided [REFERENCE: rough mix] without altering other instrument levels.
5. [STEP_5]: Normalize final output to [LUFS_TARGET: -16 dB LUFS] average (±[TOLERANCE: 1 dB]) with true peak never exceeding [PEAK_CEILING: -0.1 dB].
6. Export [DELIVERABLE_LIST: master WAV + stem WAVs / single stereo WAV] at [SAMPLE_RATE: 48kHz], [BIT_DEPTH: 24-bit] [SUBTYPE: float / integer].

[CONSTRAINTS]:
- Track lengths must remain identical after editing (all stems must remain in sync)
- Wrong notes must be replaced with in-key alternatives from [SOURCE: elsewhere in the song], not silence
- Noise/clicks replaced with silence (not removed — no length change)
- [NAMING: Output file named exactly "[FILENAME]"]
- [QUALITY: Preserve [AESTHETIC: the source recording's natural character / modern clarity] — minimal artificial processing]

[OUTPUT_SPECIFICATION]: [FORMAT: WAV files / ZIP archive with master + stems] at [SAMPLE_RATE]Hz / [BIT_DEPTH]-bit [SUBTYPE]; [LOUDNESS_TARGET]; [PEAK_CEILING]; [NAMING_CONVENTION]
```

## 4. Reference File Requirements

### File Types Needed
- **Drum reference track (WAV/AIFF):** Rhythmic foundation for composition tasks; establishes BPM and groove; all composed instruments must sync to this. Should be a full-length drumbeat at the specified BPM, with enough dynamic variation to reflect natural song structure (verse, chorus, bridge transitions).
- **Full mix reference (MP3/WAV):** Serves as positional or level reference in editing/mixing tasks. In resync tasks, this is the "correct state" reference showing where a displaced element should be. In mixing tasks, this is the target level reference. Can be lower quality (MP3) since it is for reference only.
- **Isolated stem (WAV):** The raw, unedited instrument track requiring correction. Should contain realistic flaws: timing drift, wrong notes at specific timecodes, or noise artifacts. Used in editing tasks.
- **Multiple instrument stems (WAV, set of 4–8):** All individual instrument tracks of a multitrack recording. Used in stem mix assembly tasks. Each file represents one instrument or group (bass, drums, guitars, organ, vocals, etc.).
- **Edit spot document (DOCX):** A structured document listing timecoded edit locations with brief descriptions of what is wrong at each location (wrong note, string noise, click). Uses mm:ss:ms format. Lists both the error description and the edit type needed (note replacement vs. silence insertion).

### Data Characteristics
Audio files should be at professional specifications (48kHz or 44.1kHz, 24-bit). Stems should all be the same length (no truncation) and the same sample rate, so they sync correctly when combined. For composition tasks, the drum reference should be a realistic 2–3 minute groove with detectable structure. For editing tasks, the edit spot document should contain 5–15 edit points distributed across the track, with at least two categories of edits (note errors and noise). Stems in a multitrack set should represent a complete arrangement (bass, chordal instrument, drums, lead/melody, optional additional layers).

### File Complexity Spectrum
- **Minimal:** Single reference WAV + creative brief; one output WAV file required. No stems, no edit document.
- **Moderate:** Full mix reference (MP3) + isolated stem (WAV) to resync and process; single mix output WAV with loudness spec.
- **Complex:** Edit spot DOCX + rough mix reference WAV + 4–6 individual instrument stem WAVs; timecode-based editing of one stem; stem mix assembly; output named stereo WAV at specified LUFS and true peak targets.

## 5. Output Specification

### Primary Deliverable
- **Format:** WAV file (single stereo mix) or ZIP archive (master WAV + named stem WAVs)
- **Structure:** For composition tasks: ZIP with one master WAV + 4–6 named stem WAVs (e.g., Guitars.wav, Bass.wav, Keys.wav). For editing/mixing tasks: single stereo WAV file.
- **Key quality signals:** Sample rate and bit depth match specification; LUFS target met (verify with metering); true peak ceiling not exceeded; track length unchanged after edits; all stems in sync (no drift); edit corrections applied at correct timecodes; instrument names match required stem naming

### Secondary Deliverables (if any)
- None for this pattern. The audio deliverable stands alone.

### Gold Output Characteristics
A gold composition output has all stems synchronized to the drum reference, with audible key changes at the specified timestamps and instrumentation that matches the specified synthesizer or genre aesthetic. A gold editing output shows no audible glitch at edit boundaries, with corrected notes that are genuinely in-key and fit the harmonic context, and noise replaced cleanly by silence with no length change. A gold mix output meets the LUFS target within tolerance and never clips the true peak, with relative instrument levels matching the reference mix. In all cases, the output file name, sample rate, and bit depth match the specification exactly.

## 6. Complexity Knobs

| Knob | Easy | Medium | Hard |
|------|------|--------|------|
| Task type | Mixing only (no creative judgment) | Editing + mixing (correction + assembly) | Composition + stems (creative + technical) |
| Edit precision | Rough alignment, no grid spec | 1/4 note quantization at stated BPM | Finer-grained quantization with a tight tolerance window, at a specified BPM |
| Edit point count | 2–3 edit locations, same error type | 5–8 locations, two error types | 12+ locations, three error types, timecode in ms |
| Stem count | 1 stem (single instrument edit) | 4 stems to assemble | 6+ stems + master + naming conventions |
| Key modulation | Single key throughout | One modulation at a timestamp | Multiple key areas with defined ranges |
| Loudness spec | No loudness requirement | LUFS target stated | LUFS + true peak ceiling + tolerance window |
| Format precision | WAV, no further spec | Sample rate specified | Sample rate + bit depth + float/integer subtype all required |

## 7. Boundary Cases & Adjacent Patterns

- **H1 (Broadcast Commercial & Video Editing):** H1 tasks involve audio as a supporting layer in a video deliverable (background music, scratch VO). H3 tasks deliver audio files as the primary output. If the deliverable is a .mp4 video file, it's H1; if the deliverable is .wav/.mp3/.zip of audio files, it's H3.
- **H6 (Moodboard & Visual Direction):** No realistic overlap. H3 is technical audio craft; H6 is visual synthesis.
- **C4 (Training Materials):** If the task is to create an educational document about audio engineering (not to actually do the work), it belongs in C4. H3 tasks produce actual audio artifacts, not documentation about audio.
- **H2 (VFX Compositing):** Both involve multi-step technical workflows on media files. H2 is video-layer work; H3 is audio work. A task that involves both (e.g., syncing audio to picture in a composited shot) would typically be classified by the primary deliverable type.
