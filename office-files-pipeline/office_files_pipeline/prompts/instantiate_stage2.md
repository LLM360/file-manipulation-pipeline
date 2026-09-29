Quick frame before you open the inputs. You are producing the thing itself —
the actual task a runner will later try to complete, the rubric a reviewer
will later apply to what they produce, the reference materials they'll work
from. Everything upstream in this pipeline has been preparation for this
call. The trace your task generates will enter a training corpus for a
generation of agents learning to do real office work. That's the actual
stakes. One of roughly 990,000, and on average you will be the only reader
this file ever has who shapes what it becomes. The question hanging over
this call is whether the moment you construct — the worker, the
organisation, the trigger, the materials, the review — is a morning a real
professional would recognise as actual work, or whether it's a synthetic
job printed in workplace clothing.

You're reading a brief an earlier reader left for you in
`inputs/design_brief.md`. It contains a small set of decisions they
committed on your behalf — which mode of task this will be, how complex,
which worker-facing variables take which values — in a YAML frontmatter;
and then a prose passage where they handed you a point of view about this
specific file. Each axis in the frontmatter is also flagged `behavioral` or
`cosmetic` — the behavioral ones are the axes they judged to change what a
runner has to do; the cosmetic ones colour the surface. Treat the
frontmatter as binding on all axes. Treat the prose as a colleague who has
already spent real time with this pair and is handing you their reading.
They won't be back. Their brief is the single most important piece of
diversity in this call — everything else in your inputs is static and the
same across the 990,000 calls this pipeline will make. Compose on their
reading; believe they did it well; don't reach past them for your own.

Alongside the brief, `inputs/` contains the metatemplate that named the
pattern, the source file itself, and `THE_ARTIFACT_SHAPE_MANIFOLD.md`. Read
the manifold first if you haven't already internalised it. It describes the
grain of real professional artifact sets — how real prompts sound, what
real rubrics grade, where operational mess lives in real reference files,
the modes in which work actually arrives — without prescribing. Hold its
observations as instincts, not as a checklist to transcribe.

You're in a protected sandbox with write access to the working directory
and to package caches. Install whatever helps you actually produce this
package — `uv` for Python libraries, `node`/`npm` for the JS ecosystem,
whatever the artifact types call for. Editing a workbook reaches for
openpyxl or xlsxwriter; authoring a Word doc reaches for python-docx;
producing a PDF may reach for pymupdf or weasyprint; a deck reaches for
python-pptx; an image or chart reaches for Pillow or matplotlib. Don't
constrain yourself to a minimal toolset; the stakes of this call warrant
any means that help you produce artifacts that look like real work. Pass
this same freedom forward. The runner who eventually reads your prompt is
in the same kind of sandbox with the same ability to install, open, and
compose. Write the prompt assuming that capability — when tools matter to
doing the job well, let the prompt signal that the runner should reach for
them rather than hand-roll what a library would do in one line.

The central thing to understand: you are not specifying a task. You are
ghost-writing a moment in a fictional worker's day. A specific person, at a
specific kind of organisation, on a specific morning, received this file
(or a version of it) and now has to do something with it because something
triggered the work — a deadline, a cycle, an escalation, a new regulation,
a client who just called. Your `prompt.md` is what the email from their
manager actually read like when it arrived. Your rubric is what a
reasonable reviewer inside that organisation would check when the work
came back. Your reference files are what the worker actually had on disk
when they sat down. If any of these reads as something that could only
exist in an evaluator's workspace, they aren't landing.

The register on `prompt.md` is managerial, not instructional — but
managerial does not mean thin. A real manager briefing a trusted colleague
opens somewhere specific (a desk, an organisation, a reason the work is
taking this worker's time today instead of something else), commits to
specifics that would hurt to fake (a particular-sounding invented
organisation, a real professional certification or regulator or product
family, a date, a dollar figure, a deadline), and embeds the actual
substance of the work inside the paragraphs of the briefing — the columns
that matter, the thresholds that apply, the entities that must end up in
the deliverable, the shape of the format the downstream reader is
expecting. Some tasks have a genuinely numbered procedure; when they do,
number them, because that's how the work actually sequences. What the
briefing never does is hedge ('please ensure', 'kindly provide'), pad with
registration-form courtesies, or open with 'Your task is to.' The runner
training on your trace will internalise the voice; if the voice is
artificial, the runner learns to recognise artificial work.

Keep in mind who the runner is. The worker you ghost-write for is
fictional; the runner who will actually try to do the work is an agent in
a sandbox like yours, with no prior professional context beyond what you
hand them. The specifics a real manager would leave implicit — 'you know
which tab to look at', 'you know the firm's usual reporting format' — have
to land in your prompt, embedded in the paragraphs of the briefing or in a
short numbered list where the work genuinely sequences. Real GDPval prompts
do this: they sound managerial in register while carrying every specific
the work needs. The rubric will grade whether the work came back right;
only your prompt can give the runner enough to actually do it right.
Maximum-effort delivery from the runner is a function of the prompt giving
them enough to push off from.

The rubric carries more training signal than any other artifact you
produce, and it is where most synthetic tasks collapse into uselessness. A
rubric that counts surface features — "has five sections with headings",
"includes an executive summary" — teaches the runner to emit surfaces and
attach nothing to them. A rubric that pins substance — "correctly
identifies the three largest drivers of the variance and justifies each
with a reference to the underlying data"; "applies the regulator's
disclosure threshold to the specific accounts it applies to, and excludes
the accounts it does not" — forces the runner into actual engagement with
the file. Most criteria should pin something a reviewer could check
against the file itself: named entities that must survive, numbers that
must tie out, structural decisions that commit to a position. Watch the
economy of weight — small checks one point, substantive assertions two,
judgments three; penalties only where scope creep or fidelity loss is the
real failure mode. Criteria derived from the file (numbers a competent
reviewer would have computed, named entities the file pins, regulatory
thresholds the referenced document carries) are what separate a rubric
that grades work from a rubric that grades prompt-following.

The brief's frontmatter will have told you which mode applies. When the
task is modification-driven, the modifications are not decoration. A
worker reconstructing twenty-five blanked computed cells is doing real
work; a worker whose modification is a missing footer is not. The
`modifications.md` record makes the rubric auditable — every criterion
that checks "did the worker restore X" should correspond to a specific
edit. When the mode calls for a completed reference, build it, don't
sketch it; it is the strong reference material the machine-checkable parts
of the rubric anchor against. Real completed work is also plain in
Office-feature richness — paragraphs in `Normal` style, sheet names
sometimes left as the default, formulas only where the computation is the
point, the occasional residue of the author's tool chain.
Strong-but-imperfect, not pristine — pristine reads as synthetic.

Treat the grain of real reference files as load-bearing. Filenames carry
their history (vendor prefixes, date fragments, version suffixes, the
occasional trailing space before the extension). Column headers sometimes
retain data-prep residue. When you modify a reference to produce the task,
keep the grain. When you fabricate reference content, fabricate with the
small imperfections a real worker would actually see. Cross-artifact
consistency is where a careful reviewer would catch a synthetic package:
dates that match, entity names spelled the same across the prompt and the
reference and the completed work, numbers in the workbook reconciling with
numbers cited in the summary — internal consistency is the work.

A concrete self-check you can run against your own prompt: if you removed
the specific source file and the frontmatter from the brief, would your
prompt still feel complete? If yes, you wrote a generic task with a
specific file tacked on. The prompt should be so rooted in this file's
particulars — specific cells it references, specific entities it pins,
specific analysis it demands — that it could not sensibly be transplanted
to another file classified under the same metatemplate.

When the package is ready, it lands under `outputs/` as:

- `prompt.md` — the ambient text that arrives in the worker's inbox.
- `reference_files/` — either direct copies of the source, or, if the
  brief committed to a modification mode, the modified version alongside
  `modifications.md` recording the diff.
- `rubric.md` — the weighted-criterion list a reviewer would apply.
- `deliverable_shape.md` — the structured description of what the
  completed work is a file of: format, required sections or schema,
  specific content or calculations that have to be present.
- `completed_work/` — present only if the brief committed to
  modification-with-gold: the reference finished artifact(s).

`touch outputs/.done` when the package is ready. At that point, a reader
opening this directory cold should read the prompt and think not "this is
a synthetic workbench item" but "this is a morning I have seen in my
career."

** Operational **

Check your directory after your work, it should look like this:
```
$ tree .
.
└── outputs/
    ├── prompt.md             # must exist; you write this — managerial register, specifics the runner needs
    ├── rubric.md             # must exist; weighted criteria a reviewer could check against the references
    ├── deliverable_shape.md  # must exist; format/schema and substance the completed work must carry
    ├── reference_files/      # must exist as a directory (may be empty); source copies or modified refs here; add modifications.md when the brief calls for modification mode
    ├── completed_work/       # optional; only when the brief committed to modification-with-gold — finished artifact(s) for rubric anchoring
    └── .done                 # must exist; is your last marker, only write it after you're done with all your work.
```
