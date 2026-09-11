# custom-skills

Personal Claude Code skills, grouped one folder per suite. Each skill folder is symlinked into `~/.claude/skills/` so the slash command is the folder name, wherever the folder lives.

## Layout

```
custom-skills/
└── <suite>/
    ├── <skill-name>/SKILL.md   one folder per skill, symlinked into ~/.claude/skills/
    ├── examples/               sample output worth keeping
    └── research/               sourced reports the suite was built from
```

Install a skill:

```
ln -sfn ~/code/custom-skills/<suite>/<skill-name> ~/.claude/skills/<skill-name>
```

All skills here are user-invoked (`disable-model-invocation: true`): they run only when you type the slash command, and cost no context otherwise.

## Suite: suno

Writes Suno v6 prompts with original, non-generic lyrics, and Studio 2.0 chat prompts for added parts. Four commands, one rule set.

| Command | Does | Writes |
|---|---|---|
| `/suno-create-song <idea>` | Full prompt: style, exclude list, lyrics with section tags, slider settings | `lyrics/<slug>/song.md` in the current project |
| `/suno-lyric-cowrite` | Co-writer on your own draft: names the stall, offers three directions, then candidate lines in your diction | only the section you accept |
| `/suno-voice ...` | Your lyrical profile: taste notes, influences researched in the background, samples of your own lyrics | `lyrics/voice.md`, only after you approve each change |
| `/suno-session-musician <instrument or ask>` | Session player for one part on a song you already have in Suno Studio 2.0: charts the track, picks the role and the hole, writes the Studio Chat message per region | `lyrics/<slug>/parts.md` when the song folder exists |

How they fit:
- `suno-create-song/craft.md` is the songwriting rulebook (specificity, POV, prosody, rhyme, structure, AI tells). `suno.md` is the Suno v6 mechanics (limits, style box, tags, exclude box, sliders). `words.txt` is the two-tier cliché list. All three skills read them.
- `scripts/check_lyrics.py` runs on every song: blocks tier-1 words, scores tier-2 density, reads rhyme schemes and syllable spread, flags lazy rhyme pairs, chorus drift, tag mistakes, digits, and bad Style or Exclude text. `--self-test` verifies it.
- `suno-session-musician/session.md` is the session-playing rulebook (listening pass, roles, arrangement rules, instrument idioms, prompt vocabulary, judging takes). Studio 2.0 mechanics are sourced in `research/suno-studio.md`.
- `lyrics/voice.md` is per project and optional. Everything in it is a guideline, never a lock: defaults, dated preferences, observed habits from lyrics you wrote, influence trait cards, samples, hated words. The request always wins.

Typical flow:

```
/suno-voice add influence <artist>          # background research, card shown for approval
/suno-create-song <idea + 2-3 real details> # song.md saved, paste the three blocks into Suno
/suno-lyric-cowrite I'm stuck on verse 2 of lyrics/<slug>/song.md
/suno-session-musician lap steel on lyrics/<slug>/song.md   # Studio 2.0: select the region, paste the chat message
```

Give real details. The skill asks for two or three concrete ones (a name, a place, an object, a moment) and refuses stock props. That is the whole anti-slop strategy; the word lists only catch what slips through.

Maintenance:
- Suno v6 shipped 2026-09-09 and retired older models. Numbers in `suno.md` are community-measured; re-verify after each Suno release.
- Studio 2.0 shipped 2026-08-13 (Premier only). Its chat is documented as tempo-aware, not key-aware; the Style field beside the chat and the per-generation credit cost are unverified. See `research/suno-studio.md`.
- Cliché lists drift. Re-check r/SunoAI every few months; today's fix becomes next year's tell.
- `research/` holds the sourced reports (Suno mechanics, lyric craft, the packs this was built from). `examples/` holds test songs that passed the checker.
