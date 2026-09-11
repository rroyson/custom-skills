#!/usr/bin/env python3
"""Deterministic checks for a Suno song file or plain lyrics.

Usage: check_lyrics.py [song.md | lyrics.txt] [--loose] [--words PATH] [--self-test]

song.md: reads the STYLE / EXCLUDE STYLES / LYRICS fenced blocks (labelled by the heading above each fence).
lyrics.md: the text under its `## Lyrics` heading, from the first section tag.
Any other file (or stdin) is treated as lyrics only.
--loose skips the syllable-spread check (hip-hop, spoken word).
Exit 1 when any ERROR is found.

ponytail: syllables and rhymes are spelling heuristics (~85% right). They flag, a human decides.
Multisyllabic and assonant rhymes (hip-hop) read as unrhymed here, so a clean run is not proof of rhyme quality.
"""
import argparse
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_WORDS = os.path.join(HERE, "..", "words.txt")
VOWELS = "aeiouy"
FENCE = re.compile(r"^\s*(```|~~~)")
TAG = re.compile(r"^\s*\[([^\]]+)\]\s*$")
CUE_SPLIT = re.compile(r"\s*[:|]\s*|\s+[-–—]\s+")  # dash needs spaces so Pre-Chorus and half-spoken survive
SYL_EXCEPTIONS = {"every": 2, "everything": 3, "everyone": 3, "everybody": 4, "family": 2, "different": 2,
                  "interesting": 3, "favorite": 2, "business": 2, "evening": 2, "camera": 2, "chocolate": 2,
                  "comfortable": 3, "temperature": 3, "restaurant": 2, "literally": 3, "basically": 3,
                  "actually": 3, "probably": 2, "memory": 3, "fire": 1, "hour": 1, "our": 1, "poem": 2}
DIRECTION = re.compile(
    r"\b(whisper\w*|soft\w*|spoken|fade\w*|instrumental|solo|quiet\w*|loud\w*|build\w*|"
    r"slow\w*|gentl\w*|scream\w*|shout\w*|ad-?lib\w*|x\d|harmon\w*|backing)\b", re.I)


# ---------- word lists ----------
def load_words(path):
    lists = defaultdict(list)
    section = None
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            m = re.match(r"^\[(.+)\]$", line)
            if m:
                section = m.group(1).strip().lower()
                continue
            if section:
                lists[section].append(line.lower())
    return lists


def entry_regex(entry):
    parts = [re.escape(w) + r"(?:s|es|ed|ing|d)?" for w in entry.split()]
    return re.compile(r"\b" + r"\s+".join(parts) + r"\b", re.I)


# ---------- text helpers ----------
def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    if w in SYL_EXCEPTIONS:
        return SYL_EXCEPTIONS[w]
    if len(w) <= 3:
        return 1
    n = len(re.findall(r"[aeiouy]+", w))
    if n <= 1:
        return 1
    if w.endswith("le") and w[-3] not in VOWELS:
        pass  # ta-ble, lit-tle: the e is syllabic
    elif w.endswith("e") and w[-2] not in VOWELS:
        n -= 1
    elif w.endswith("es") and w[-3] not in VOWELS and not w.endswith(("les", "ses", "zes", "ches", "shes", "xes", "ges")):
        n -= 1
    elif w.endswith("ed") and w[-3] not in VOWELS and not w.endswith(("ted", "ded")):
        n -= 1
    return max(1, n)


def rime(word):
    """(nucleus, coda) of the last syllable, from spelling."""
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return ("", "")
    if len(w) > 3 and w.endswith("e") and w[-2] not in VOWELS and not (w.endswith("le") and w[-3] not in VOWELS):
        w = w[:-1]
    groups = list(re.finditer(r"[aeiouy]+", w))
    if not groups:
        return (w, "")
    last = groups[-1]
    return (last.group(), w[last.end():])


def sung_text(line):
    return re.sub(r"\([^)]*\)", " ", line)


def words_of(line):
    return re.findall(r"[A-Za-z']+", sung_text(line))


def end_word(line):
    ws = words_of(line)
    return ws[-1].strip("'").lower() if ws else ""


# ---------- parsing ----------
def parse_blocks(text):
    blocks, lines, i, heading = {}, text.splitlines(), 0, ""
    while i < len(lines):
        m = FENCE.match(lines[i])
        if m:
            fence, j, body = m.group(1), i + 1, []
            while j < len(lines) and not lines[j].strip().startswith(fence):
                body.append(lines[j])
                j += 1
            blocks.setdefault(heading, "\n".join(body))
            i = j + 1
            continue
        if lines[i].strip():
            heading = re.sub(r"^[#*\s]+|[*:\s]+$", "", lines[i]).strip().upper()
        i += 1
    return blocks


def parse_sections(lyrics):
    sections, cur = [], {"name": "(untagged)", "tag": "", "tagline": 0, "lines": []}
    for n, raw in enumerate(lyrics.splitlines(), 1):
        m = TAG.match(raw)
        if m:
            if cur["lines"] or cur["tag"]:
                sections.append(cur)
            inner = m.group(1).strip()
            name = CUE_SPLIT.split(inner, 1)[0].strip()
            cur = {"name": name, "tag": inner, "tagline": n, "lines": []}
        elif raw.strip():
            cur["lines"].append((n, raw.rstrip()))
    if cur["lines"] or cur["tag"]:
        sections.append(cur)
    return sections


# ---------- checks ----------
def analyze_section(sec):
    ends = [end_word(t) for _, t in sec["lines"]]
    keys = [rime(w) for w in ends]
    letters, label = [None] * len(ends), 0
    for i in range(len(ends)):
        if letters[i] is not None or not keys[i][0]:
            continue
        partners = [j for j in range(i + 1, len(ends)) if keys[j] == keys[i]]
        if partners:
            letter = chr(ord("A") + label)
            label += 1
            letters[i] = letter
            for j in partners:
                letters[j] = letter
    scheme = "".join(l or "X" for l in letters)
    slant = 0
    for i in range(len(ends)):
        for j in range(i + 1, min(i + 3, len(ends))):
            (n1, c1), (n2, c2) = keys[i], keys[j]
            if letters[i] and letters[i] == letters[j]:
                continue
            if n1 and n2 and ((n1 == n2 and c1 != c2) or (c1 and c1 == c2 and n1 != n2)):
                slant += 1
    counts = [sum(syllables(w) for w in words_of(t)) for _, t in sec["lines"]]
    return ends, letters, scheme, slant, counts


def check_lyrics(lyrics, lists, loose=False):
    F = []
    lyrics = lyrics.replace("’", "'")
    sections = parse_sections(lyrics)
    all_lines = [(n, t) for s in sections for (n, t) in s["lines"]]
    total = len(all_lines)
    chars = len(lyrics)
    nwords = sum(len(words_of(t)) for _, t in all_lines)

    # length
    if chars > 5000:
        F.append(("ERROR", "length", f"{chars} chars, over Suno's 5,000 limit"))
    elif chars > 3000:
        F.append(("WARN", "length", f"{chars} chars, over the 3,000 target; Suno rushes or skips"))
    if total > 60:
        F.append(("WARN", "length", f"{total} lyric lines, over 60"))
    elif 0 < total < 30:
        F.append(("INFO", "length", f"{total} lyric lines; under 40 may run short"))
    F.append(("INFO", "length", f"{chars} chars, {total} lines, {nwords} words"))

    # tags
    tagged = [s for s in sections if s["tag"]]
    if not tagged:
        F.append(("WARN", "tags", "no [Section] tags found"))
    else:
        if sections[-1]["tag"].strip().lower() != "end":
            F.append(("WARN", "tags", "last tag is not [End]; Suno may trail on"))
        for s in tagged:
            if len(s["tag"].split()) > 8:
                F.append(("WARN", f"L{s['tagline']}", f"long bracket text may be sung: [{s['tag']}]"))
            cues = CUE_SPLIT.split(s["tag"])[1:]
            ncues = sum(len([c for c in part.split(",") if c.strip()]) for part in cues)
            if ncues > 3:
                F.append(("WARN", f"L{s['tagline']}", f"{ncues} cues in one tag; keep to 3"))
    for n, t in all_lines:
        if "[" in t or "]" in t:
            F.append(("WARN", f"L{n}", "bracket inside a lyric line; tags go on their own line"))
        for p in re.findall(r"\(([^)]*)\)", t):
            if DIRECTION.search(p):
                F.append(("WARN", f"L{n}", f"parentheses are sung; '({p})' reads as a direction"))
        if re.search(r"\d", re.sub(r"'\d\d\b", "", t)):
            F.append(("WARN", f"L{n}", "digits in lyric; spell numbers out"))

    # words
    tier1 = [(e, entry_regex(e)) for e in lists.get("tier1", [])]
    tier2 = [(e, entry_regex(e)) for e in lists.get("tier2", [])]
    homographs = set(lists.get("homographs", []))
    hits2 = []
    for idx, (n, t) in enumerate(all_lines):
        for e, rx in tier1:
            if rx.search(t):
                F.append(("ERROR", f"L{n}", f"tier-1 '{e}': {t.strip()}"))
        for e, rx in tier2:
            if rx.search(t):
                hits2.append((idx, n, e))
                F.append(("INFO", f"L{n}", f"tier-2 '{e}'"))
        for w in words_of(t):
            if w.lower() in homographs:
                F.append(("INFO", f"L{n}", f"homograph '{w}': make the pronunciation unambiguous"))
    seen = set()
    for a in range(len(hits2)):
        for b in range(a + 1, len(hits2)):
            if 0 < hits2[b][0] - hits2[a][0] <= 3 and (hits2[a][1], hits2[b][1]) not in seen:
                seen.add((hits2[a][1], hits2[b][1]))
                F.append(("WARN", f"L{hits2[a][1]}-L{hits2[b][1]}",
                          f"tier-2 cluster '{hits2[a][2]}' + '{hits2[b][2]}'; one of them is wallpaper"))
    if len(hits2) >= 5:
        F.append(("WARN", "words", f"{len(hits2)} tier-2 words in one song"))

    # rhyme, syllables, structure
    lazy = set()
    for pair in lists.get("rhyme-pairs", []):
        if "/" in pair:
            a, b = pair.split("/", 1)
            lazy.add(frozenset((a.strip(), b.strip())))
    schemes, perfect_lines, choruses, finals = {}, 0, [], []
    for s in sections:
        if not s["lines"]:
            continue
        ends, letters, scheme, slant, counts = analyze_section(s)
        name = s["name"]
        perfect_lines += sum(1 for l in letters if l)
        F.append(("INFO", name, f"scheme {scheme}, slant pairs {slant}, syllables {'-'.join(map(str, counts))}"))
        if len(s["lines"]) >= 3 and set(scheme) != {"X"}:
            schemes[name] = scheme
        for i in range(len(ends)):
            for j in range(i + 1, len(ends)):
                if letters[i] and letters[i] == letters[j]:
                    if ends[i] == ends[j]:
                        F.append(("WARN", name, f"same end word twice: '{ends[i]}'"))
                    elif frozenset((ends[i], ends[j])) in lazy:
                        F.append(("WARN", name, f"lazy rhyme pair {ends[i]}/{ends[j]}"))
        if not loose and len(counts) >= 2 and max(counts) - min(counts) > 3 \
                and not re.search(r"rap|spoken|talk", s["tag"], re.I):
            F.append(("WARN", name, f"syllable spread {min(counts)}-{max(counts)}; craft target is within two"))
        lname = name.lower()
        if lname in ("chorus", "hook"):
            choruses.append([t.strip().lower() for _, t in s["lines"]])
        elif lname.startswith("final") and ("chorus" in lname or "hook" in lname):
            finals.append([t.strip().lower() for _, t in s["lines"]])
    if len(schemes) >= 2 and len(set(schemes.values())) == 1:
        F.append(("WARN", "rhyme", f"every section uses {next(iter(schemes.values()))}; vary the scheme between sections"))
    verse_schemes = {v for k, v in schemes.items() if k.lower().startswith("verse")}
    chorus_schemes = {v for k, v in schemes.items() if "chorus" in k.lower() and not k.lower().startswith("pre")}
    for sch in verse_schemes & chorus_schemes:
        F.append(("WARN", "rhyme", f"verse and chorus share scheme {sch}; give the chorus its own"))
    if total and perfect_lines / total > 0.6:
        F.append(("WARN", "rhyme", f"{perfect_lines * 100 // total}% of line endings are perfect rhymes; add slant or unrhymed lines"))
    if len(choruses) > 1 and any(c != choruses[0] for c in choruses[1:]):
        F.append(("WARN", "structure", "choruses differ; paste the chorus text identically and vary the cue instead"))
    for f in finals:
        if choruses:
            diff = sum(1 for a, b in zip(choruses[0], f) if a != b) + abs(len(choruses[0]) - len(f))
            if diff > 2:
                F.append(("WARN", "structure", f"final chorus changes {diff} lines; keep the hook, change at most two"))
    return F


def check_style(style, lists):
    F, n = [], len(style)
    if n > 1000:
        F.append(("ERROR", "style", f"{n} chars, over 1,000"))
    elif n > 800:
        F.append(("WARN", "style", f"{n} chars, over the 800 target"))
    elif n < 200:
        F.append(("WARN", "style", f"{n} chars; underbuilt"))
    for e in lists.get("style-contamination", []):
        if re.search(r"\b" + re.escape(e) + r"\w*", style, re.I):
            F.append(("WARN", "style", f"'{e}' makes it sound like a concert recording; remove unless intended"))
    if re.search(r"\bacoustic\b", style, re.I):
        F.append(("INFO", "style", "'acoustic' pulls in acoustic guitar; fine if that is the arrangement"))
    if re.search(r"\b(no|without|not|never)\b", style, re.I):
        F.append(("WARN", "style", "negative phrasing; Suno reads 'no drums' as 'drums'"))
    return F


def check_exclude(ex):
    F, n = [], len(ex)
    if n > 1000:
        F.append(("ERROR", "exclude", f"{n} chars, over 1,000"))
    if re.search(r"(^|,)\s*(no|without)\b", ex, re.I):
        F.append(("WARN", "exclude", "use bare terms (piano), not 'no piano'"))
    terms = [t for t in ex.split(",") if t.strip()]
    if len(terms) > 10:
        F.append(("WARN", "exclude", f"{len(terms)} terms; 3-8 is the range"))
    return F


def lyrics_section(text):
    # lyrics.md workspace: skip Themes and the status line, start at the first [tag] under "## Lyrics"
    m = re.search(r"^##\s+Lyrics\s*$", text, re.M | re.I)
    if not m:
        return text
    rest = text[m.end():].splitlines()
    first = next((i for i, l in enumerate(rest) if TAG.match(l)), 0)
    return "\n".join(rest[first:])


def run(text, lists, loose=False):
    blocks = parse_blocks(text)
    lyrics = next((v for k, v in blocks.items() if "LYRIC" in k), None)
    if lyrics is None:
        lyrics = lyrics_section(text)
    F = check_lyrics(lyrics, lists, loose)
    style = next((v for k, v in blocks.items() if k.startswith("STYLE")), None)
    if style is not None:
        F += check_style(style, lists)
    ex = next((v for k, v in blocks.items() if k.startswith("EXCLUDE")), None)
    if ex is not None:
        F += check_exclude(ex)
    return F


def report(F):
    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    counts = defaultdict(int)
    for level, where, msg in sorted(F, key=lambda f: order[f[0]]):
        counts[level] += 1
        print(f"{level:5}  {where:<12} {msg}")
    print(f"--- {counts['ERROR']} errors, {counts['WARN']} warnings, {counts['INFO']} info")
    return counts["ERROR"]


# ---------- self-test ----------
SLOP = """[Verse 1]
Neon lights are calling out my name
Echoes of the night that feel the same
Shadows dancing through the pouring rain
Fire in my veins, I feel no pain
[Chorus]
We rise above, we're breaking free
Chasing dreams across the sea
Forever and always you and me
Together we will always be
[Verse 2]
Whispers in the dark, they call to me
In my mind I know we're meant to be
Rising like a phoenix from the fire
Burning bright with my desire
[Chorus]
We rise above, we're breaking free
Chasing dreams across the sea
Forever and always you and me
Together we'll always be
[Bridge]
(softly) I was born in 1993
Can you feel it? Yeah
[Outro]
"""

CLEAN = """[Verse 1 - hushed, close mic]
Your dad's old Ranger wouldn't catch
I pumped the gas the way you do
The dome light blinked, I struck a match
And gave the wheel a knock or two
[Chorus - belted, full band]
I'm learning how to wait
I've got nowhere to be
You said give it a second
And that's the one you gave me
[Verse 2 - a little louder]
It turned over on the fourth try
I let it idle in the yard
Your mother came out asking why
I told her that's the easy part
[Chorus - stacked harmonies]
I'm learning how to wait
I've got nowhere to be
You said give it a second
And that's the one you gave me
[Bridge - drums drop out, close vocal]
Her dad left it to her
The truck, the yard, the wait
She never learned to drive it
Somebody had to stay
[Final Chorus - bigger drums]
I'm learning how to wait
I've got nowhere to be
You said give it a second
And that's the one you gave me
[Outro - one guitar, slowing]
Engine off, windows down
I've got nowhere to be
[End]
"""


def self_test(lists):
    assert syllables("banana") == 3 and syllables("table") == 2 and syllables("smile") == 1
    assert syllables("walked") == 1 and syllables("wanted") == 2 and syllables("the") == 1
    assert rime("night") == rime("light") and rime("fire") == rime("desire")
    slop = run(SLOP, lists)
    levels = defaultdict(list)
    for lv, _, msg in slop:
        levels[lv].append(msg)
    assert len(levels["ERROR"]) >= 6, levels["ERROR"]
    joined = " | ".join(levels["WARN"])
    for needle in ("lazy rhyme", "digits", "parentheses", "[End]", "choruses differ"):
        assert needle in joined, f"missing WARN {needle!r} in: {joined}"
    clean = run(CLEAN, lists)
    bad = [f for f in clean if f[0] != "INFO"]
    assert not bad, bad
    ws = "# T\n\n## Themes\n\n- Core: the ceiling\n\n## Lyrics\n\nOnly the hook so far\n\n[Chorus]\nIt's hard to bring the ceiling down\n"
    assert lyrics_section(ws).startswith("[Chorus]"), lyrics_section(ws)
    assert lyrics_section("[Verse 1]\nplain") == "[Verse 1]\nplain"
    print("self-test OK: slop flagged, clean passes, lyrics.md section read")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?")
    ap.add_argument("--loose", action="store_true", help="skip syllable-spread check (hip-hop); sections tagged spoken/rap are skipped anyway")
    ap.add_argument("--words", default=DEFAULT_WORDS)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    lists = load_words(a.words)
    if a.self_test:
        self_test(lists)
        return 0
    text = open(a.path, encoding="utf-8").read() if a.path else sys.stdin.read()
    return 1 if report(run(text, lists, a.loose)) else 0


if __name__ == "__main__":
    sys.exit(main())
