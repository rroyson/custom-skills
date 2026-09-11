# Influence research brief (subagent prompt)

Fill the two placeholders and pass the whole thing as the subagent's prompt.

---

You are researching a songwriting influence for a lyric-writing profile. Today is <DATE>. Work in the project directory <PROJECT_DIR>.

INFLUENCE: <the artist, song, or pasted lyrics the user gave>

CURRENT VOICE FILE:
<contents of lyrics/voice.md, or the exact text "(no voice.md yet)">

Goal: a concise trait card, at most twelve bullets of at most 25 words each, describing how this influence writes lyrics, so a co-writer can borrow the craft without copying the words.

How to research:
- Pasted lyrics: analyze them directly. No web needed.
- An artist or song: use WebSearch and WebFetch (or firecrawl skills if available). Read three to six sources: interviews about their writing process, lyric analyses, annotation sites, respected reviews. Stop after six sources or twenty-five tool calls, whichever comes first. Prefer the artist's own words about craft over fan commentary.

What the card must contain, one line each, plain and specific:
- POV: who speaks, to whom, which tense, how often it shifts
- Detail: what kinds of concrete things appear (brand names, place names, objects, work, weather), and how many per verse
- Rhyme: schemes they favor, perfect vs slant ratio, internal rhyme, how loose
- Lines: typical syllable range, sentence or fragment, how conversational
- Structure: forms they use, where the title lands, what the bridge or last verse does
- Diction: register, contractions, humor, profanity, recurring verbs
- Borrow: two or three moves worth stealing (a technique, never a phrase)
- Leave alone: what would read as pastiche
- Sound, name-free: one Style-box description of their musical sound with no proper names of any kind (no artist, band, producer, studio, or label), e.g. "Southern rock leaning Americana, warm baritone, story-first delivery, Telecaster and pedal steel"
- Sources: one or two URLs

Hard rules: never quote more than four consecutive words of any lyric. No proper names in the "Sound, name-free" line; Suno blocks generation on artist names. Plain bullets (`- POV:`), no bold. If a number is your own read rather than sourced, say "my read" in that bullet. If the influence is obscure and nothing solid turns up, say so in the card instead of guessing.

Output: write the card as a markdown section headed `### <Name> (added <DATE>)` to `<PROJECT_DIR>/lyrics/voice-proposed.md` (create `lyrics/` if missing; overwrite the file), and return the same card verbatim as your reply, with nothing before or after it.
