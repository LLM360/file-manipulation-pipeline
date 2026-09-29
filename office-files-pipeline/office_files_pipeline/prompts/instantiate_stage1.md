Quick frame before you open the inputs. We're producing roughly 990,000 of
these, and each one seeds a task that runs, gets scored, and becomes a trace
in a training corpus for agents doing real office work. The runners we train
on this corpus will literally act from these traces — pull numbers out of
spreadsheets, write memos, build decks, reconcile references. So the question
hanging over this call isn't "can I produce a plausible design space for this
file." It's "will the task an author instantiates from what I write put the
runner in a spot where doing the work well means doing *professional work* —
or in a spot where doing it well means performing a cosmetic repaint of a job
that already exists a hundred times elsewhere in the corpus."

The adversary here is averaging. With 990K generations, the distribution
collapses toward the metatemplate's centre of gravity — generic persona,
generic trigger, generic deliverable — because any given file is, on average,
generic in the absence of a reader who noticed what is specific about it.
Your reading is what prevents that collapse for this pair. Not a thorough
reading in the completionist sense; a noticing reading — the kind that sees
the particulars of this file and holds them against the shape of a
professional who would plausibly do something with them.

In `inputs/` you have a metatemplate describing a pattern cluster, the
classified source file, a field report the classifier left on it, and
`THE_REAL_WORK_MANIFOLD.md`. Read the manifold first. It isn't a set of
rules — it's a description of where real work varies from itself and how to
tell diversity that changes what a worker *does* apart from diversity that
just repaints the surface. The calibration check it gives — picture two
neighbouring values on an axis and ask whether the runner opens different
files, consults different parts of the source, makes different judgments, or
produces a structurally different deliverable — is the thing from the
manifold you should actually apply, per axis, before you commit to it.

You're in a protected sandbox with write access to the working directory and
to package caches. Install anything that helps you actually look at this
file — `uv` for Python libraries, `node`/`npm` for the JS ecosystem, whatever
the file type calls for. Don't constrain yourself to a minimal toolset; the
stakes of this call warrant any means that improve your reading. If the file
is a workbook, reach for openpyxl or polars. If it's a PDF, pymupdf or
pdfplumber. If it's an image, OCR. The only constraint is what the sandbox
physically permits, and that's generous.

Now the frame that makes this interesting. What you write here — the
`design_space.json` plus the prose you append to `design_brief.md` — is the
only input the task author will see that knows anything about *this specific
pair*. They'll read the same metatemplate you read and the same source file,
and they have their own anchor on what real tasks feel like. Those are
static. Your brief is live. If your brief is transposable — if it could
plausibly have been written for a different file classified under the same
metatemplate — the task author has no fulcrum and defaults to the
metatemplate's average. If your brief is rooted in the particulars of this
file — named entities visible on the sheet, structural oddities, an internal
system the header implies, the specific professional context the contents
commit to — the task author has somewhere to push against and writes
something the runner can't fake.

So the design space is not a menu of knobs. It's the skeleton of a small
family of jobs that could plausibly land this file on a worker's desk. Each
axis is a hypothesis about what could legitimately differ across that family,
in ways that would make a real worker do structurally different things. Some
axes come from the manifold's lens (source-to-deliverable relationship,
where the ambiguity lives, how inputs relate when there are several, where
latitude lives and where it's pinned). Some come from the metatemplate's §6
Complexity Knobs. Some are ones only you can see because you actually read
this file — axes you could not have drafted from the metatemplate's name
alone. Each axis carries `values`, a `behavioral: true|false` flag, and a
one-line `rationale` that would survive a colleague asking "why does this
axis earn its place."

Then hand the cell selection to `cast.py`. It exists because authors trust
samplers — our own preferences collapse faster than a uniform draw, and this
is the work that prevents that. Run:

    uv run inputs/cast.py --seed {task_hash} outputs/design_space.json

On pass, cast writes `outputs/design_brief.md` with the sampled cell as YAML
frontmatter. On fail, cast prints per-axis diagnostics — revise the space
and rerun. You can iterate freely; cast is cheap.

The prose section of the brief is where your reading actually lives. The
frontmatter is a row of values; the prose is what those values *mean* when
projected onto this specific pair. Write it in the voice a practitioner uses
briefing a colleague — what kind of worker is this for, at what kind of
organisation, what plausibly triggered the work now, which parts of the file
will be load-bearing in whatever the author builds, which parts carry the
imperfect operational mess a real worker would notice and react to, what
specific professional judgment the work is going to demand of the runner.
Write so that an informed reader could almost guess the source file back
from your prose alone. If a paragraph describes a generic professional in a
generic context doing generic work with a file of this class, that paragraph
is doing no work the metatemplate isn't already doing — cut it.

`touch outputs/.done` when you're finished. By then the brief should read
like something you'd hand to a colleague and let them run with.

** Operational **

Check your directory after your work, it should look like this:
```
$ tree .
.
└── outputs/
    ├── design_space.json   # must exist; you write this, make sure you used cast.py to validate it
    ├── design_brief.md     # created by cast.py, make sure to fill the free-form section
    └── .done               # must exist; is your last marker, only write it after you're done with all your work.
```
