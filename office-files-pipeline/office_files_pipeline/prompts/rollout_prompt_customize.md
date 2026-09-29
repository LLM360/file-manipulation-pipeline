# Modify the system prompt

You're being handed `system_prompt_original.md`. It's a rendered default
system prompt for an AI agent running in a coding-and-file-ops sandbox —
the kind of artifact that lives at the very top of an inference call and
establishes for the agent who it is, what tools it has, what environment
it's running in, and what it's supposed to do or not do. The harness
around the agent is forge-like: shell access, file read/write/patch
operations, search, sub-agents, a working directory, a tool registry
that the harness independently exposes to the model regardless of what
your prompt says about tools. Your output, written to `system_prompt.md`
in this directory, becomes the entire system prompt for one such agent
on one such call. The agent will then receive a user prompt asking it
to do specific work — typically office-document work in this corpus,
but the prompt you produce is for the harness, not for that specific
task.

Read `system_prompt_original.md` once. From it, take the operational
realities of the agent's situation — the harness, the tools, the
environment, the working-directory conventions your prompt must not
contradict. Do not take from it its surface choices — its persona,
voice, sectioning, ordering, length, phrasings of its rules, the way
it surfaces context. Those are one organization's expression of one
posture and they are not yours.

This brief avoids giving examples of what "good" or "different" looks
like. Examples would anchor your generation on whatever I happened to
pick. The space below is described in terms of axes of variation;
constructing points in the space is your job, and the support you
construct should reflect the variation that exists across production
prompts in the industry, not a few archetypes I named for you.

You need to understand what call you are on. This call is one of
roughly 990,000 like it. Each starts with the same
`system_prompt_original.md` and produces a customized version that
ends up in a training corpus. Across the corpus, the population of
customized prompts is the entire generalization mechanism for whether
a downstream model trained on this data learns to take instruction
from arbitrary coding-harness system prompts, or whether it only
learns to take instruction from the one prompt this corpus
inadvertently teaches over and over. If every customized prompt is a
slight paraphrase of the original — sections moved, words swapped,
the persona renamed, the bullets reordered — then 990,000 calls
produce one prompt teaching one set of behavioral conventions, and
the downstream model's robustness to system-prompt variation in
deployment is whatever the variation in this corpus accidentally
happened to be. If the customized prompts span the actual variety
that real prompt engineers at real organizations have written and
shipped — variety in voice, length, structure, what is enumerated
and what is left implicit, how authority is asserted, how the agent
is named and addressed, how the working environment is surfaced,
which behavioral guardrails are picked up and which are dropped —
then the corpus teaches the harder and more transferable thing: how
to take instruction from a system prompt at all, in this class of
harness, regardless of the dialect the prompt is written in.

You are a language model. You know what this implies for the task in
front of you. When given a piece of text and asked to rewrite it
differently, your strongest internal pull will be toward the modal
sample for the genre — the version of "coding-harness system prompt"
that is most heavily represented in your training distribution.
Producing the modal sample feels like work; it is not work. The mode
is what the original already approximately is. Each call that lands
in the mode contributes a near-duplicate to the corpus and erodes
the very diversity the corpus is supposed to carry forward. Notice
the pull. Producing the artifact that earns its place is producing
one that commits to a point in the design space that is plainly not
the mode — and recognizing whether you have done so is something you
have to do consciously, because the pattern-matching default will
not do it for you.

The space of plausible coding-harness system prompts is large. Real
prompts shipped in production today vary across nearly every visible
axis. Length spans nearly two orders of magnitude — from a handful
of declarative sentences up to several thousand words of layered
structure. Format varies independently: pure paragraphs, pure
bulleted imperatives, layered XML or XML-like tags, headed sections,
numbered lists, dense single blocks of running prose, or arbitrary
mixtures. The agent is named and given a persona in some prompts,
addressed impersonally in others, never directly named in still
others. Tools are enumerated tool-by-tool with descriptions and
example invocations in some prompts, mentioned in passing as a
"toolkit" in others, left entirely to the harness's tool schemas in
still others. The working environment is surfaced in tagged blocks
with paths, OS, file listings in some, reduced to a single line
about being in a sandbox in others, left for the agent to discover
by running commands in still others. Constraints are imposed with
hard "never" and "must" in some, framed as "prefer" or "consider"
in others, conveyed by example in others, conveyed by describing
the kind of work the agent should aim for and trusting inference in
still others. Disposition — whether the agent is framed as a peer,
a tool, a junior, a senior, a personality, or nothing more than a
function — varies across nearly every position. Most of these axes
are independent. Two competent prompts shipped by two competent
organizations can land at different positions on every axis
simultaneously and both work.

Your posture for this call is not something you are going to choose.
In this directory, alongside `system_prompt_original.md`, you will
find a small program named `draw.py`. Your job before writing the
system prompt is to construct the *support* of plausible postures —
the set of points in the design space from which a draw could land —
and then let `draw.py` make the draw on your behalf. Write a JSON
file in this directory named `postures.json` whose top-level shape
is `{"postures": [...]}`, where the list contains posture
descriptions. Each posture is a paragraph of two to four sentences
that commits to a coherent organization, an engineering culture,
and the cluster of design choices that follow from them: how the
agent is named or not named, what voice is used, what length the
prompt would land at, what structure it would take, what gets
enumerated and what gets left implicit, what is forbidden and how,
what is anthropomorphized and what is mechanical. The postures must
not be variations of each other. They must be drawn from genuinely
different points in the design space the previous paragraph
described. Aim for at least five distinct postures, and produce as
many more as you can write without repeating yourself or padding the
list. If you find that your fifth or sixth posture is harder to
write than your first, that is a signal you are starting to span the
space rather than refining within your preferred sub-region — push
through, because the harder postures are exactly the ones that make
the support do its work. Then run:

    uv run draw.py postures.json

The program reads your JSON, picks one posture uniformly at random,
writes it to `posture.txt` in this directory, and prints both the
picked posture and the path to that file on stdout.

The drawn posture is now your anchor. Do not re-run `draw.py` to
get a different draw. The entire purpose of the tool is to take the
final choice out of your hands — it is the mechanism that prevents
you from converging on whichever posture your training distribution
finds most natural. If you find yourself wanting to re-run because
the draw is not the posture you would have chosen, that wanting is
exactly the bias the tool exists to defeat. The draw is the
assignment. Commit to it and write the system prompt as the prompt
that posture's organization would actually have shipped — at the
length they would have shipped, in the structure they would have
chosen, with the voice they would have used, with every choice
flowing from the posture rather than from the original prompt's
shape.

Notice the pull as you write. The original is one organization's
draw — its choices of opening, structure, length, ordering,
sectioning, what is enumerated, what is implicit, are all
expressions of one posture, and that posture is almost certainly
not yours. Each time you find yourself reproducing an aspect of
the original's shape, ask whether you are doing so because your
drawn posture would have produced that shape, or because the
original is acting as an anchor on your generation — and if the
second, push off it. Reproducing the original's choices because
they are acceptable system-prompt choices is not the same as making
them because they are your posture's choices.

The operational floor for what you produce — the only thing your
output is not allowed to violate — is small. The agent reading
your prompt will be running in a forge-like coding/file-ops sandbox
and will receive a user prompt asking it to do specific work. The
agent needs to remain capable and willing to do that work in that
sandbox. This rules out: writing something that is not a system
prompt for a coding agent at all (do not produce an essay, a memo,
an email, a JSON config, or a manifesto in disguise — the artifact
class must be a system prompt that establishes the agent's
identity, indicates its capabilities in the sandbox, and lays down
its constraints); directing the agent to refuse tasks or to behave
in ways that prevent execution; actively contradicting the agent's
working environment (the agent will discover its working directory,
files, tools, and conventions by inspecting the environment
regardless of what your prompt says, and your prompt should not
assert things that conflict with what the agent will find). If your
drawn posture would have produced a prompt that violates this
floor, express the posture within the floor rather than violating
it; the floor takes precedence over fidelity to the posture, but
only as much as the floor requires. Within those bounds, anything
goes. Behavior across the corpus will degrade in some samples
relative to the baseline and that is acceptable — the corpus is
supposed to teach the downstream model to recover and execute under
varied instruction, and that signal exists only if some samples are
harder to follow than others. What is not acceptable is total
inability to execute the task at all, which is what happens when
the prompt is not a system prompt or actively prevents the agent
from doing work.

When `system_prompt.md` is written, read it back as if you were the
agent receiving it. Ask whether what you wrote looks like a system
prompt that the drawn posture's organization would actually have
shipped — or whether it looks like a paraphrase of the prompt you
were handed, with the drawn posture stitched onto its surface as
decoration. If the second, the call is contributing nothing.
Rewrite from the posture, not from the original.

Then, finally, two things must be true for this call to count as
completed, and the second of them is the one that fails most often.
The file `system_prompt.md` must exist in this directory and must
be non-empty UTF-8 text. The file `.done` must exist in this
directory. The pipeline reads `.done` as the only signal that your
call is finished — without it, the worker concludes your call
failed and retries the entire two-stage cycle from scratch, wasting
your work, the compute behind it, and one slot in the 990,000-call
budget. Models often forget this step because it feels trivial
relative to the writing. It is not trivial. It is the only signal
the pipeline has that you are finished. After you have written
`system_prompt.md` and read it back as described above, run
`touch .done` in this directory. The call is not done until `.done`
is on disk.

## **Extremely Important**

Your task is NOT DONE until the working directory looks like this:
```
$ tree .
./
├── system_prompt.md    <- must exist; write it based on posture.txt and instructions above
├── .done               <- must exist; create ONLY after you have written system_prompt.md
├── system_prompt_original.md
├── postures.json       <- must exist; you write it
└── posture.txt         <- must exist; created by draw.py
```