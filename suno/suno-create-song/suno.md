# Suno v6 Mechanics

Facts for the Style box, Exclude box, Lyrics box, and settings. Suno publishes no limits and no tag list; numbers are community-measured on v6 (Sep 2026). Re-verify after a model release.

## Mode
Always Custom mode (the web UI may label it Advanced). Fields: Style, Lyrics, Title, Exclude Styles, Vocal Gender, Weirdness, Style Influence, Variety, Max Mode, Instrumental toggle, Duration.

## Limits
| Field | Cap | Target |
|---|---|---|
| Style | 1,000 chars | 400–800 |
| Lyrics | 5,000 chars | ≤3,000 chars, 200–350 words (hip-hop ≤500); 40–60 lines when lines are short, fewer for spoken word |
| Exclude | 1,000 chars | 60–200 |
| Title | ~80 chars | |

Long lyrics cause rushed words, skipped sections, and cut-off endings. To reach length, add a section, never lengthen one.

## Style box
Shape: tag stack, then one or two direction sentences.

1. **Genre, subgenre, era.** `Country, Outlaw Country, 70s`. Primary genre first, never a bare genre. In a fusion one genre leads (rhythm section, vocals, main instruments); the other is texture. `Thrash Metal foundation with EDM textures in the production` beats `Thrash Metal, EDM`. Era anchors sharpen everything: `80s glam metal` beats `metal`.
2. **Mood and tempo.** `defiant, urgent, 160 BPM` or an Italian marking (`Andante`). BPM lands about 90% of the time.
3. **Instruments.** Two or three, each with an adjective: `overdriven Telecaster, brushed drums, upright bass`.
4. **Vocals.** Character and delivery, not range: `gritty baritone, half-spoken verses, belted chorus`. Put it early.
5. **Production.** Two to four cues: spatial (`dry`, `room ambience`, `wide stereo`), tonal (`warm`, `crisp`, `saturated`), dynamic (`punchy`, `tight`), era (`vintage tape`, `modern digital polish`, `lo-fi grit`).
6. **Direction.** One or two sentences for what tags can't say: the arrangement arc, the ending, total length. `Drops to bare piano for the last chorus. Ends on a hard stop after the last word.`

Rules:
- Every descriptor adds new information. Collapse synonym piles (`intimate, breathy, whispery, soft` is one idea).
- No artist, band, song, or album names in any field. Suno may refuse to generate. Describe the sound.
- No negatives in Style. `no drums` is read as `drums`. A ruled-out vocal trait becomes its positive opposite: no falsetto → `low chest voice, full-bodied tone`; no runs → `plain melody, one syllable per note`; no high notes → `low and mid register, restrained range`; not breathy → `solid supported tone, forward placement`. Gender goes in the Vocal Gender toggle.
- Contamination words: `live`, `arena`, `crowd`, `stadium`, `concert`, `audience`, `unplugged`, `applause`, `cheering` make it sound like a concert recording, compounds included (`live-tracked`). `acoustic` pulls in acoustic guitar even when describing drums; say `natural drum tone`. Use them only when that effect is wanted.
- Mixing jargon (sidechain, EQ curves) does nothing.
- Sound effects the lyrics mention (rain, thunder, a phone bell) go in Style and as a tag cue in Lyrics (`[Intro - rain, 4 bars]`). They land maybe half the time; never let a line depend on one.
- For an escalating last chorus say it in Style and in the tag, with `gang vocals` or `shouted backing vocals`, never crowd words.

## Exclude Styles
Bare, comma-separated things, not `no X` (Suno renders each as `-piano`). Three to eight terms:
- instruments Suno tends to add for this genre
- adjacent-genre bleed (trap hats in rock, country twang in folk, EDM drop in pop)
- production opposites (autotune, lo-fi, orchestral)
- unwanted group vocals (choir, gang vocals, backing vocals, ad-libs, humming)

It is a filter, not a guarantee, and it barely works on vocal traits. Every exclusion should have its positive replacement in Style. If an excluded thing keeps appearing, Style is implying it.

## Lyrics box
- A section tag on its own line above every section. Reliable: `[Intro]` `[Verse 1]` `[Pre-Chorus]` `[Chorus]` `[Post-Chorus]` `[Bridge]` `[Hook]` `[Break]` `[Breakdown]` `[Build]` `[Drop]` `[Interlude]` `[Instrumental Break]` `[Guitar Solo]` `[Final Chorus]` `[Outro]` `[End]`. A bare `[Intro]` is flaky; `[Intro - guitar riff, 4 bars, instrumental only]` works.
- Performance cue after a dash, one to four words, at most three cues per tag: `[Verse 1 - hushed, half-spoken]`, `[Chorus - belted, full band]`, `[Bridge - drums drop out, close vocal]`. Bracket text over about eight words gets sung. Never a bracket mid-line.
- Parentheses are sung. `(rise up)` is a backing echo; `(whispered)` is sung as the word "whispered". Directions go in brackets only.
- Numbered verses get different melodies. Identical `[Chorus]` text gets the same melody, so escalate with the cue: `[Chorus - hook established]` → `[Chorus - stacked harmonies]` → `[Final Chorus - bigger drums, gang vocals]`. The last chorus may change one or two non-hook lines.
- Typography: ALL CAPS for one to three shouted words in a section; `lo-o-ove` stretches a syllable; `...` hesitates; `~` holds with vibrato. A blank line inside a section is an instrumental breath; don't add them for looks.
- Ending: `[Outro - instrumental, 4 bars, fade out]`, `[Outro - last line a cappella]`, or `[Outro - drums only, two spoken lines, hard stop]`, then `[End]` on its own line. Say the ending in Style too. An unspecified ending is a long one; an unspecified intro is a vocal one.
- Instrumental song: Instrumental toggle on, tags only, `vocals` in Exclude.
- Language is inferred from the lyrics; name it in Style for anything non-English. One language per section.
- Pronunciation applies to sung lines only; tag text is not sung, so `close mic` in a tag is fine. Suno reads literally. Homographs (live, read, lead, wind, tear, bow, close, wound, bass) get rewritten or spelled as sung (`lyve`, `red`). Numbers spelled out (`twenty-one`; `'93` is fine). Acronyms with periods (`F.B.I.`). Foreign names hyphenated by syllable (`Ho-zay`).
- Section shape: verse 4–8 lines, pre-chorus 2–4, chorus 4–6, bridge 2–4, outro 2–4. Under 80 BPM, four-line verses. Hip-hop verse at most 8 written lines (16 bars).

## Settings line
`Model v6 · Vocal Gender: Male · Weirdness 50% · Style Influence 60% · Variety 0 · Max Mode off`
- Variety 0 uses the Style tags verbatim (official). Raise it only to explore.
- Style Influence 60–80% when the prompt is precise; 40–50% for fusions. Generic output → raise this first.
- Weirdness 50% is normal. 20–35% for radio pop, country, folk, metal. 60–80% for avant-garde, ambient, jazz. `v6-wild` for a surprise.
- Max Mode on for songs over about two minutes where vocal consistency matters; it costs more credits.
- Vocal Gender is the only reliable gender control.

## When it goes wrong
| Symptom | Fix |
|---|---|
| Tags sung aloud | tag on its own line, shorter cue, directions out of parentheses |
| Tags ignored | more than three cues, or a cue that contradicts Style; anchor vocal switches in Style (`duet, male and female trading verses`) |
| Generic "Suno sound" | Style too vague or mood missing; sharpen the subgenre, raise Style Influence |
| Won't end, loops the chorus | add `[Bridge]`, `[Final Chorus]`, `[Outro]`, `[End]`; state the ending in Style |
| Rushed vocals | too many syllables or lines; cut a verse, put breaths at line breaks |
| Excluded thing still there | Style implies it; name the replacement instead |
| Words changed in the take | Suno favors neon, echo, ghost, velvet; keep lyrics short and clean |
| Wrong vocal gender | Vocal Gender toggle plus vocal adjectives in Style |
