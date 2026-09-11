---
name: suno-voice
description: Build and update lyrics/voice.md, the artist's lyrical profile: record taste notes, research influences in the background, apply reviewed changes.
disable-model-invocation: true
---

# Suno Voice

Maintains `lyrics/voice.md`, the per-project profile that `suno-create-song` and `suno-lyric-cowrite` read. Everything in it is a guideline; the request wins when they conflict. Observed lines describe what the user has written, never what they must write; a request that breaks the pattern is not a mistake. No change reaches voice.md until the user has seen it and said yes.

## Branch by what follows the command
- `add influence <artist, song, or pasted lyrics>` → step 1
- `review` → step 3 with `lyrics/voice-proposed.md`
- `sample` plus pasted lyrics, or lyrics the user wrote arriving through the other skills → a Samples entry (at most two sections, one-line tag) plus one dated Observed line under 20 words naming what the lyrics actually do: POV, line length, rhyme habit, where the detail comes from. Step 3.
- anything else is a taste note → step 2

## 1. Influence, in the background
Launch one general-purpose subagent with the Agent tool. Its prompt is [influence-brief.md](influence-brief.md) with the influence and the current voice.md pasted in. Tell the user in one line that it's running and return to whatever they were doing. Never wait on it, never pretend to know its result. When the result arrives: if the user's last message was this command, go to step 3 now; if they've moved on, hold it and open your next reply with one line, "Influence card for X is ready. Review now or later?"

The card is craft traits only: POV habits, detail style, rhyme density and types, line length, structure moves, diction, what to borrow, what to leave alone. No quoted lines. No artist name for a Suno field; the card carries a name-free sound description instead.

## 2. Taste note
Distill the feedback to one dated line per distinct point, under 20 words each, under Preferences or Never: `- 2026-09-11: slant rhyme in choruses; every-line perfect rhyme reads sing-song to him`. Then step 3.

## 3. Review and apply
Vet first: strip any proper name (artist, band, producer, studio) from the Sound line, cut any quoted lyric over four words, trim any bullet over 25 words, and say in one line what you changed. Then show the proposed addition in full. Ask: apply, edit, or drop.
- Apply: create `lyrics/voice.md` from the template below if it doesn't exist (drop placeholder lines you didn't fill; keep the empty Defaults), insert under the right heading, keep the file under about 120 lines by merging repeats and trimming the oldest lines (Samples keeps the three newest, Observed the eight newest), delete `lyrics/voice-proposed.md` if present. Show the changed sections.
- Edit: take their wording verbatim, then apply.
- Drop: delete the proposal, say so in three words.

## Template
~~~markdown
# Voice
Guidelines, not rules. The request wins when they conflict.

## Defaults
- Genre:
- Vocal gender:
- Usual length:

## Preferences
- YYYY-MM-DD: <one guideline the user stated>

## Observed
- YYYY-MM-DD: <what a lyric they wrote actually does; a lean, not a lock>

## Influences
### <Name> (added YYYY-MM-DD)
- POV:
- Detail:
- Rhyme:
- Lines:
- Structure:
- Diction:
- Borrow:
- Leave alone:
- Sound, name-free (for Style):
- Sources:

## Samples
### <title or tag>
<two sections at most>

## Never
- YYYY-MM-DD: <word or move the artist hates>
~~~

## Never
Write voice.md without a yes · turn an Observed line into a rule · paste quoted lyric lines from an influence · put an artist name anywhere a Suno prompt will read it · let the file grow past what one read can absorb.
