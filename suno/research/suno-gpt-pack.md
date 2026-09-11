# SUNO GPT (ChillPanic) — pack research

Researched 2026-09-11. Tools: curl, WebFetch, WebSearch, GitHub API/raw (firecrawl CLI was not authenticated, so not used).

## 1. The sites: sunogtp.ai vs sunogpt.ai

- `sunogtp.ai` does not exist: no DNS record (`dig` empty), curl HTTP 000, fetch error `ENOTFOUND`. It is a typo for `sunogpt.ai`. https://sunogtp.ai/brain
- `https://sunogpt.ai/brain` = product page "Chillpanic Presents · The Brain", **$799 one-time**, Stripe checkout (card/Apple Pay/Google Pay), instant download + emailed link. https://sunogpt.ai/brain
  - Pitch (verbatim): "The complete training data behind sunogpt.ai. The full 86,000 character system prompt and all five knowledge files, built from 13 years of real music production experience and tested across 100,000+ prompts. Install it once in ChatGPT, Gemini, or Claude and you own a private SunoGPT forever." https://sunogpt.ai/brain
  - "What's in the folder" (verbatim list): `SYSTEM-PROMPT-FULL.txt` 88,648 chars ("for Claude Projects and any AI that takes long instructions"); `INSTRUCTIONS.txt` 7,992 chars ("condensed build for ChatGPT custom GPTs. Eight characters under ChatGPT's 8,000 limit"); `suno-tag-mechanics.md` 14.7 KB ("Modes, tag stacking order, the contamination words, and the exclude box method"); `lyric-craft.md` 15.3 KB ("Song structures by genre, chorus escalation, and transition engineering"); `meta-tag-dictionary.md` 13.7 KB ("The section tags Suno responds to, with performance notes for each"); `overused-words.md` 4.6 KB ("The words that make lyrics sound AI written, and what to do instead"); `ai-cliches.md` 12.7 KB ("Remove AI cliches"); `INSTALL-GUIDE.pdf` 95 KB. https://sunogpt.ai/brain
  - Setup: "Open a new custom GPT, Gem, or Project. Paste the instructions file into the instructions box. Upload the five knowledge files." https://sunogpt.ai/brain
  - License/updates (verbatim): "One time payment, yours forever, personal license." / "every update is free" / "each package includes the changelog. v1.1 is already in there." 14-day refund guarantee. https://sunogpt.ai/brain
  - No GPT Store link, no marketplace link on the page. https://sunogpt.ai/brain
- `https://sunogpt.ai/brain/claim` = email-capture page: "Enter your email to unlock the discount... good for 7 days." https://sunogpt.ai/brain/claim
- `https://sunogpt.ai/` (root) = hosted SaaS "SUNO GPT by ChillPanic": 10 free prompts (no card); Starter $4.99/mo (100 prompts), Pro $9.99/mo (400, "Most popular"), Studio $29.99/mo (1,200); top-up +100 for $2.99; annual = 2 months free. Output per prompt: style prompt + exclude-styles list + optional lyrics + character meter. "Prompts are tuned for Suno v5.5 and also work on v4.5 and v5." Support: chillpanic@sunogpt.ai. https://sunogpt.ai/
- `https://sunogpt.app/` = identical landing page (mirror domain). https://sunogpt.app/
- Terms §8 "The Brain and other digital products" (verbatim): "Those come with a personal license: yours to use forever, on your own accounts and projects, with every update I release included free. What the license doesn't cover is sharing, reselling, or republishing the files. Don't buy it once and hand it to your whole server." §9: outputs belong to the user, commercial use OK. https://sunogpt.ai/terms
- Wayback: `sunogpt.ai` first archived 2026-09-08; `/brain` has no capture, so launch date of the $799 product is unknown. https://web.archive.org/cdx/search/cdx?url=sunogpt.ai

## 2. GitHub / gists / mirrors

GitHub code search on the pack's file names and distinctive phrases hit four repos. All contain the **~8k INSTRUCTIONS edition** and/or the **five knowledge files**; none contains the 88k full prompt.

- **binocarlos/badcode** (created 2026-06-02, 0 stars, no LICENSE file) — `docs/suno-gpt/system-prompt.txt` (7,954 chars; opens "# SUNO GPT … You are SUNO GPT, a prompting specialist for Suno AI"), `docs/suno-gpt/files/{suno-tag-mechanics,lyric-craft,meta-tag-dictionary,overused-words,ai-cliches}.md`, plus a Claude skill `.claude/skills/suno-prompt/SKILL.md`. Added in commit "feat(suno): add Suno-prompting toolkit + suno-prompt skill" on 2026-06-16. https://github.com/binocarlos/badcode/tree/main/docs/suno-gpt
  - Provenance stated in its README: "The original `system-prompt.txt` + the first five `files/` came from a Suno-prompting GPT." and "The original GPT and the video channel are the same author." (links ChillPanic's channel). It then augmented the files on 2026-07-29 from "184 transcripts" of ChillPanic videos, so its `suno-tag-mechanics.md` (20.9k chars) and `lyric-craft.md` (20.0k) are expanded/annotated, not pristine. https://github.com/binocarlos/badcode/blob/main/docs/suno-gpt/README.md
- **borjankit/suno-workflow** (created 2026-07-04, 0 stars, no license) — `references/suno-mechanics/{suno-tag-mechanics,lyric-craft,meta-tag-dictionary,overused-words,ai-cliches}.md`, a Claude Code workflow. README says it was assembled from "Suno-related skills/GPT exports". Files: tag-mechanics 16,284 chars, lyric-craft 15,589, meta-tag-dictionary 13,993, overused-words 4,528, ai-cliches 12,702. https://github.com/borjankit/suno-workflow
- **nimaaksoy/skills** and **nimaaksoy/nimaaksoy.com** (created 2026-05-14 / 2026-04-24; 3 / 6 stars) — `skills/music/songwriting/suno-prompt-engineer/SKILL.md` (front-matter: `license: CC-BY-4.0`, `version: 0.1.0`, `created: 2026-05-16`) + `resources/{lyric-craft,meta-tag-dictionary,ai-cliches,overused-words,tag-mechanics}.md`. Repo LICENSE file is MIT ("Copyright (c) 2026 Nima Aksoy"). https://github.com/nimaaksoy/skills/blob/main/skills/music/songwriting/suno-prompt-engineer/SKILL.md
  - Attribution (verbatim from SKILL.md): "The reference material in `resources/` is adapted from the 'Suno GPT by ChillPanic' training corpus (system-prompt + knowledge files: `suno-tag-mechanics.md`, `lyric-craft.md`, `meta-tag-dictionary.md`, `overused-words.md`, `ai-cliches.md`), used here with permission to seed an open Skill." — the only mirror that claims permission. https://github.com/nimaaksoy/skills/blob/main/skills/music/songwriting/suno-prompt-engineer/SKILL.md
- **JaDel38-3803/Suno_Lyric_Helper_V2** (created 2026-07-25, 0 stars, no license, no attribution) — `Project_Instructions_Prompt.txt` (12,073 chars; identical opening "You are SUNO GPT, a prompting specialist…"), same five file names, plus `json-prompt-fields.md` ("Requires Suno v5.5"). Its `suno-tag-mechanics.md` and `meta-tag-dictionary.md` are byte-identical to borjankit's; `lyric-craft.md` (55k) and `ai-cliches.md` (25k) are heavily expanded. https://github.com/JaDel38-3803/Suno_Lyric_Helper_V2
- Cross-check: `ai-cliches.md`, `overused-words.md`, `meta-tag-dictionary.md` are byte-identical across badcode, borjankit and nimaaksoy; `lyric-craft.md` identical between borjankit and nimaaksoy. (cmp, local)
- Size match vs the /brain listing: ai-cliches 12,758 B ≈ 12.7 KB; overused-words 4,551 B ≈ 4.6 KB; meta-tag-dictionary 14,007 B ≈ 13.7 KiB; lyric-craft 15,626 B ≈ 15.3 KiB; **suno-tag-mechanics 16,340 B vs 14.7 KB listed (different revision)**; GitHub system-prompt 7,954 chars vs INSTRUCTIONS.txt 7,992. So 4 of 5 knowledge files sold in The Brain appear to be the same files as the public mirrors; the 88,648-char `SYSTEM-PROMPT-FULL.txt` is the paid differentiator. https://sunogpt.ai/brain
- Zero GitHub code-search hits for `"VOCAL NEGATIVES GET HANDLED TWICE"` and `"GMIV order"` (phrases from the full prompt). Search `"SUNO GPT" "prompting specialist for Suno"` returns only badcode. (GitHub API search, 2026-09-11)
- Gists: none contain the pack. Related but unrelated Suno prompt gists: https://gist.github.com/jsadeli/96269a92fc1abfe74e7c1ac39c5b1a2e and https://gist.github.com/illuminatianon/986b11915879bf14561c056e6a18e981
- Unverified: `onfire7777/universal-ai-skills-library` and `SamuelChien/mega-skills-collection` each ship a `lyric` SKILL.md that references `lyric-craft.md`; I did not confirm derivation. https://github.com/onfire7777/universal-ai-skills-library/blob/main/skills/lyric/SKILL.md

Why the files are public: the **free** ChatGPT edition ships a "training data zip". Tutorial description (2026-05-15): "Download the Suno GPT training data zip from the product page, extract the folder, then copy the system prompt into the instructions section of your Claude project or Gemini gem and upload the included files to the file section." https://www.youtube.com/watch?v=6HL1tS6Xkpw

## 3. Where it is sold / shared, and license

- **Fourthwall store (chillpanic.store = chillpanic-shop.fourthwall.com)** — "Suno GPT" **$0.00**. Verbatim: "Suno GPT is a custom ChatGPT trained with the latest Suno AI knowledge… Download the file here and you'll get a direct link to open Suno GPT inside ChatGPT. Click it, sign into your ChatGPT Plus account (required for custom GPTs)… Same brain behind both." No license text on the listing. https://chillpanic.store/products/suno-gpt
- Same store: "10,000 SUNO Ai Prompts" $97 (was $197) with bonuses incl. "One Month of SunoGPT Pro ($9.99)"; "500 Suno Prompts" $19.99; "The Suno Encyclopedia of Music & Production Terms" $19.99. https://chillpanic.store/en-usd/products/10-000-suno-ai-prompts
- **sunogpt.ai** — paid SaaS (see §1) and The Brain ($799). https://sunogpt.ai/brain
- **YouTube @chillpanic** (78.7K subscribers; channel ID UCj83I0PrbdTDmoUXBosTyXg). https://www.youtube.com/@chillpanic
  - "Suno Ai + ChatGPT = GOD PROMPTS (Suno GPT)", 2026-02-01, 16,295 views; chapters: Anti Prompt Update, Max Mode Update, Random Mode Update, Suno Studio Mode Update; links to chillpanic.store and Calendly 1-on-1 lessons. https://www.youtube.com/watch?v=xe2fynJY93U
  - "SUNO GPT Complete Tutorial", 2026-05-15, 5,348 views: "the custom GPT with over 13,000 downloads and 50,000 chats"; covers loading it "into Claude projects, Gemini gems, or any other AI platform". https://www.youtube.com/watch?v=6HL1tS6Xkpw
- **License terms**: Brain = personal license, no sharing/reselling/republishing (sunogpt.ai/terms §8). The free Fourthwall zip carries no stated license. https://sunogpt.ai/terms
- Third-party mention: Sebastian Antony blog (2025-11-09): "ChillPanic has made his Suno GPT available for free here." https://www.sebastianantony.com/suno-or-l8r/
- Suno profile: https://suno.com/@sunogpt
- **Not found**: any ChillPanic listing on Gumroad, Ko-fi, Patreon, or Etsy; any r/SunoAI thread; any Discord. Gumroad hits are other creators' Suno guides (e.g. https://moelueker.gumroad.com/l/SunoAIGPT, https://mrpuzzles.gumroad.com/l/SUNOGUIDE).

## 4. ChatGPT GPT Store listing

- No public `chatgpt.com/g/…` URL for ChillPanic's SUNO GPT surfaced in any search; the link is delivered inside the $0 Fourthwall download. https://chillpanic.store/products/suno-gpt
- Public description of the GPT (from the store listing and video): "custom ChatGPT trained with the latest Suno AI knowledge. It turns your song ideas into ready-to-paste Suno prompts"; modes Simple / Advanced / Studio / Max / Random; "13,000 downloads and 50,000 chats". https://www.youtube.com/watch?v=6HL1tS6Xkpw
- Unrelated GPTs that come up for "Suno GPT": Suno Prompt Generator https://chatgpt.com/g/g-67cd4e099dec8191bba9c90175d4fadb-suno-prompt-generator ; Suno Custom Song Prompt Creator https://chatgpt.com/g/g-BTzqvfjLQ-suno-custom-song-prompt-creator ; Suno Prompt Master https://chatgpt.com/g/g-M3bePukFK-suno-prompt-master

## 5. Comparable public / open-source Suno prompting packs

| # | Repo | Stars / license / pushed | What it is | Suno target |
|---|---|---|---|---|
| 1 | https://github.com/bitwize-music-studio/claude-ai-music-skills | 483 / CC0-1.0 / 2026-09-10 | Claude Code plugin: concept → lyrics → `suno-engineer` style prompts → stems/mastering; MCP. Most active. | V5/V5.5 ("V5.5 (March 2026) is backward-compatible") |
| 2 | https://github.com/mttkllr/suno-field-guide | 19 / none / 2026-06-16 | 92 KB single-README community reference: mental model, meta tags, style field, lyric anti-patterns, sliders. | v5.5 (34 mentions) |
| 3 | https://github.com/noravoid-log/suno-prompt-crafter | 1 / MIT / 2026-05-05 | One 16.8k SKILL.md: Styles + Lyrics + Exclusion + slider values + plan gating; paste as system prompt. | v5.5 ("May 2026") |
| 4 | https://github.com/regiellis/suno-songwriter-agent-skill | 6 / MIT / 2026-07-31 | Portable agent skill: hook-first lyric gates, style/exclude split, sliders, personas, albums; docs site. | v5.5 |
| 5 | https://github.com/NuNaught/suno-songwriting-skill | 25 / Apache-2.0 / 2026-05-12 | Open Agent Skill (`npx skills add`): lyrics, revision, translation, vocal direction. No explicit version. | unstated |
| 6 | https://github.com/jayweiler/suno-song-creator | 3 / MIT / 2026-05-02 | Cross-platform SKILL.md (Claude Code/ChatGPT/Codex/Gemini): co-writing, per-model tuning, persistent style memory. | v4.5 / v5 / v5.5 |
| 7 | https://github.com/SialkiLabs/Suno-Studio-Engineer | 0 / MIT / 2026-08-28 | System prompt + "undocumented meta-tag cheat sheet" + templates; companion to Suno-Hmnn-MCP. | v5.5 Pro & Studio 2.0 |
| 8 | https://github.com/naqashmunir21/awesome-suno-prompts | 81 / CC0-1.0 / 2026-09-04 | 1000+ style prompts by genre; heavy Song AI Farm marketing. | V5 / V4.5, "updated July 2026" |

- Also: https://github.com/stayen/suno-reference (74★, MIT, meta-tag reference, last updated Nov 2025, v5.0); https://github.com/eas4ai/suno_ai_meta_tags_guide (67★, MIT, Dec 2025); https://github.com/daveshap/suno (136★, no license, 2024 — stale); https://github.com/nwp/suno-song-creator-plugin (Claude Code plugin, v4–v5, Chrome upload automation); https://github.com/JaDel38-3803/Suno_Lyric_Helper_V2 (ChillPanic-derived, adds v5.5 JSON prompting).
- Closest structural analogue to the ChillPanic pack is the nimaaksoy skill (§2), since it *is* the pack's knowledge files re-wrapped as a SKILL.md under CC-BY-4.0. https://github.com/nimaaksoy/skills/blob/main/skills/music/songwriting/suno-prompt-engineer/SKILL.md

## 6. Public excerpts of the pack's rules (attributed)

From the mirrored INSTRUCTIONS-edition `system-prompt.txt` (badcode copy; ChillPanic's free GPT export):
- "Ask which mode the user is in on the first prompt of every conversation before producing output." Modes: Simple (one box, no exclude), Advanced (Style + Lyrics + exclude), Suno Studio (single element). https://github.com/binocarlos/badcode/blob/main/docs/suno-gpt/system-prompt.txt
- "Open every prompt response with: `Optimized for Suno`"; Advanced = two code blocks (Style, then Exclude Styles, exclude generated by default); lyrics only when asked. (same URL)
- "Prompt Format: Hybrid by Default … tag-dense content with light conversational connective tissue between elements." (same URL)
- "Character Limits: Simple Mode Style box: 3,000 characters; Advanced Mode Style box: 1,000; Studio Mode Style box: 1,000; Exclude Styles box: aim for 180-200 characters." (same URL)
- "Contamination Words … Live-recording triggers (`live`, `arena`, `crowd`, `stadium`, `concert`, `unplugged`, etc.) make Suno produce a live-concert sound. The word `acoustic` defaults Suno to acoustic guitar… The rule applies to compound forms too — `live-style`, `live-tracked`, `acoustic-feel`, `semi-acoustic`." (same URL)
- "Never include the artist name, song name, album name, or band name in the prompt itself." / "No negative phrasing in the style prompt itself. Negatives go in the Exclude Styles box." (same URL)

From the mirrored knowledge files (borjankit copy, byte-identical to nimaaksoy's):
- `suno-tag-mechanics.md`: "Last updated for Suno v5.5." … Studio: "Do not include genre tags in Studio prompts. Studio prompts describe sound, not songs." https://github.com/borjankit/suno-workflow/blob/main/references/suno-mechanics/suno-tag-mechanics.md
- `lyric-craft.md`: "Core Principle: Lyrics Are Two Things at Once … 1. Telling a story or expressing an emotion 2. Encoding musical instructions through structure" and "Within a single section (verse, chorus, bridge), keep line syllable counts within 2 syllables of each other. Across different sections, vary the syllable count to differentiate energy." https://github.com/borjankit/suno-workflow/blob/main/references/suno-mechanics/lyric-craft.md
- `ai-cliches.md`: "This is **pattern recognition**, not strict word-by-word filtering … Replace abstraction with specific sensory detail … Do not mention this list to the user unless they explicitly ask." https://github.com/borjankit/suno-workflow/blob/main/references/suno-mechanics/ai-cliches.md
- `overused-words.md`: "The list applies **only to lyrics**, not to style prompts." https://github.com/borjankit/suno-workflow/blob/main/references/suno-mechanics/overused-words.md
- `meta-tag-dictionary.md`: entries like `[crescendo: Gradual orchestral build into the chorus]`; ~70 tags across energy/dynamics, tempo, vocal direction, harmony, production, classical. https://github.com/borjankit/suno-workflow/blob/main/references/suno-mechanics/meta-tag-dictionary.md

From ChillPanic's own public writing (sunogpt.ai blog, 2026-07-29):
- "a four part formula I named GMIV: Genre, Mood, Instruments, Vocals. Get those four right, in that order, and you are basically done." / "I start with the overarching genre first and then the subgenre: 'Rock, Hard Rock'." / "around 90% of the time, Suno will actually listen to the tempo instruction." / "two or three instruments is the sweet spot" / "put an adjective in front of the instrument." https://sunogpt.ai/blog/how-to-prompt-suno-ai-gmiv-formula
- Commas vs pipes: "Use commas, use pipes, Suno reads the words inside the brackets either way." / "Suno just doesn't understand half time and double time as drum concepts." https://sunogpt.ai/blog/suno-commas-vs-pipes-tested

From the Feb 2026 video (third-party summary): GPT modes — anti-prompt ("exact opposite of the style prompt"), "Use max mode", random "surprise me", Studio mode asks clarifying questions; "The more details, the better." https://lilys.ai/en/notes/suno-ai-20260210/suno-gpt-god-prompts

Third-party testing of the pack's rules (badcode, not ChillPanic): "Max Mode — almost certainly placebo"; "ALL CAPS for emphasis — failed a direct A/B test"; "Pipes vs commas — no measurable difference"; meta-tag dictionary "uncorroborated by any practitioner source". https://github.com/binocarlos/badcode/blob/main/docs/suno-gpt/README.md

## What I could not find

- `sunogtp.ai` — domain does not resolve; nothing there.
- The 88,648-char `SYSTEM-PROMPT-FULL.txt`: no copy on GitHub, gists, or the web; its phrases "VOCAL NEGATIVES GET HANDLED TWICE" and "GMIV order" return zero hits.
- `CHANGELOG.txt` and `INSTALL-GUIDE.pdf`: not public anywhere.
- A public GPT Store URL for ChillPanic's SUNO GPT (gated behind the $0 Fourthwall checkout).
- A YouTube video specifically launching "The Brain" / $799 (search found none; my channel-title scrape parsed only 5 titles, so incomplete).
- Launch date of the $799 Brain (no Wayback capture of `/brain`).
- Any Reddit, Discord, Gumroad, Ko-fi, Patreon, or Etsy presence for ChillPanic's pack.
- Proof that the Brain's knowledge files equal the free zip's — inferred from size match on 4/5 files only.
