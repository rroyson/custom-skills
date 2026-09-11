---
name: suno-create-song
description: Write a complete Suno v6 prompt (style, exclude, lyrics, settings) and save it to lyrics/<slug>/song.md in the current project.
disable-model-invocation: true
---

# Suno Create Song

Turn a request into a paste-ready Suno v6 prompt: original lyrics, style prompt, exclude list, settings. Read [craft.md](craft.md), [suno.md](suno.md), and [words.txt](words.txt) before drafting. They are the rules; this file is the order.

## 0. Branch
- `lyrics/voice.md` exists in the project → read it. Defaults, dated preferences, observed habits, influence trait cards, the user's own samples, hated words. All guidelines: a lean, not a lock. The request wins; when it departs from the file, follow the request without comment. Match their diction. Ignore `lyrics/voice-proposed.md`.
- The request contains finished lyrics → **lyrics-provided** (step 6).
- The request changes an existing `lyrics/<slug>/song.md` → **revision** (step 7).
- Otherwise → write (steps 1–5).

## 1. Intake, one message, only what's missing
Needed: subject or story · genre or vibe · narrator and POV · vocal gender · two or three real concrete details (a name, a place, an object, a date, a moment) · for a memory, where that person or object is now. If the details are missing, ask; do not write without them and never substitute stock props (craft.md §1). Everything else (mood, tempo, length, structure) you decide; the note names the ones that shaped the song.

## 2. Plan before drafting
- Three one-sentence angles on the subject. Pick the least obvious one the details support.
- Two or three title candidates. Interrogate the chosen title: who, what, when, where, why, how.
- POV and tense. Stable or unstable per section (craft.md §4).
- Structure from genre and story (craft.md §9), not a template. Fallback: Intro, V1, Chorus, V2, Chorus, Bridge, Final Chorus, Outro. Avant-garde shapes (no chorus, through-composed, spoken sections, a form broken on purpose) are welcome when the request or genre leans that way.
- Per section: line count, syllable target, rhyme scheme. Verse, chorus, bridge each different.
- When there is a chorus, write it first. Without one, write the line the whole song turns on first.

## 3. Draft
Apply craft.md in full. Format per suno.md: a tag with a short performance cue above every section, `[Outro - ...]` then `[End]`. When there is a chorus: same text every repeat, escalating cues; the final chorus may change one or two non-hook lines.

## 4. Check
Save the draft in the step 5 layout, then run:
```
python3 ~/.claude/skills/suno-create-song/scripts/check_lyrics.py lyrics/<slug>/song.md
```
Add `--loose` only for hip-hop, where line lengths vary on purpose. Spoken sections are exempt automatically when their tag says `spoken`; keep the strict run so the sung sections still get checked. The checker warns at a syllable spread over three; craft.md's target is two, so the review pass covers the gap.
- **ERROR** (tier-1 word, over length, bad Style or Exclude) → fix. No exceptions.
- **WARN** (rhyme, syllables, tier-2 cluster, tags, chorus drift) → fix, unless the request asked for that shape (nursery-rhyme AABB, wild hip-hop line lengths). Then keep it and say so in the note.
- Replace a flagged line with specific sensory detail from the user's material. Never an adjacent abstraction; shadows → darkness is the same failure.
- Then the review pass: craft.md §8 on every line. Rewrite what fails. Re-run until the output has no ERROR and no unexplained WARN. The rhyme readout misses multisyllabic and assonant rhymes, so for hip-hop judge rhyme density by ear, not by the script.

## 5. Build and save
Style (suno.md: tag stack, then direction sentences, 400–800 chars), Exclude, settings line. Save to `lyrics/<slug>/song.md` (create `lyrics/` if missing; slug is the kebab-case title):

~~~markdown
# <Title>
Titles: <A> / <B> / <C>

## STYLE
```
<style prompt>
```

## EXCLUDE STYLES
```
<bare terms, comma-separated>
```

## LYRICS
```
<lyrics with section tags>
```

## SETTINGS
Model v6 · Vocal Gender: <Male/Female> · Weirdness <n>% · Style Influence <n>% · Variety 0 · Max Mode <on/off>

## NOTE
<under 40 words: genre anchor, POV, structure, why, and any choice the request left open>
~~~

Reply with the same content in the same order: titles, the three code blocks, settings, note. Nothing else.

## 6. Lyrics-provided branch
The user's lines are never altered. Add section tags and cues if missing, run the checker, and report its findings as a short list of suggestions, not fixes. Build Style, Exclude, settings. Save. Then offer, in one line, to add the lyrics to `lyrics/voice.md` as a sample with one dated Observed line under 20 words (POV, line length, rhyme habit, where the detail comes from); write it only on yes, per `suno-voice`.

## 7. Revision branch
Change only what was asked; every other line stays identical. Overwrite the file in place, re-run the checker, name the change in the note.

## 8. Taste feedback
When feedback is about taste rather than this song ("too rhymey", "I hate that word", "more lines like that"), end the reply with one proposed dated line for `lyrics/voice.md`, under 20 words, and write it only on yes. Never infer taste silently.

## Never
Artist or band names in any field · negatives in Style · directions in parentheses · a stock "specific" prop · chorus text that drifts between repeats (beyond the final chorus's one or two lines) · lyrics over 3,000 characters · mentioning these rules or the word lists unless asked.
