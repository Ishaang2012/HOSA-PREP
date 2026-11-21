"""Build chapter summaries and chapter quizzes from shared book files.

Each book lives in tools/books/<slug>.py and defines BOOK:

BOOK = {
    "titles": ["Exact title as listed in data/events.js", ...],  # every event listing this title gets the book
    "edition": "9th edition (2022)",                              # edition the chapter list comes from
    "source": "Publisher's table of contents (cengage.com)",
    "chapters": [(number, "Title", ["paragraph", ...], ["key point", ...]), ...],
    "quizzes": [((1, 2, 3), [(chapter, question, correct, [3 wrong], explanation), ...]), ...],
}

Checks: chapter numbers are unique, every quiz covers 3 chapters (the last may cover fewer)
that exist in the book, every question's chapter is one of its quiz's chapters, options are
distinct, and no question repeats. Answer positions are shuffled with a fixed seed per quiz.

Writes data/books/<event-id>.js (summaries, quizzes and bookInfo keyed by the book's position in
that event's `books` list) and registers it in index.html.
Usage: python3 tools/build_books.py            (builds every book and every event that uses one)
"""
import collections
import importlib.util
import json
import os
import random
import sys
import zlib

sys.path.insert(0, os.path.dirname(__file__))
from build_content import ROOT, load_events, register_scripts  # noqa: E402

BOOK_DIR = os.path.join(ROOT, "tools", "books")


def load_books():
    books = {}
    for f in sorted(os.listdir(BOOK_DIR)):
        if not f.endswith(".py"):
            continue
        spec = importlib.util.spec_from_file_location("book_" + f[:-3], os.path.join(BOOK_DIR, f))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        books[f[:-3]] = m.BOOK
    return books


def check(slug, b):
    nums = [c[0] for c in b["chapters"]]
    assert len(nums) == len(set(nums)), f"{slug}: duplicate chapter numbers"
    for n, title, paras, keys in b["chapters"]:
        assert title and paras and keys, f"{slug}: chapter {n} is missing a summary or key points"
    seen = set()
    for chs, rows in b.get("quizzes", []):
        assert 1 <= len(chs) <= 3 and all(c in nums for c in chs), f"{slug}: bad quiz chapters {chs}"
        assert len(rows) >= 10, f"{slug}: quiz {chs} has only {len(rows)} questions"
        for ch, q, right, wrong, expl in rows:
            assert ch in chs, f"{slug}: question for chapter {ch} is in quiz {chs}: {q}"
            assert len(wrong) == 3 and len({right, *wrong}) == 4, f"{slug}: options not 4 distinct: {q}"
            assert q not in seen, f"{slug}: duplicate question: {q}"
            seen.add(q)


def build_quiz(slug, chs, rows):
    rng = random.Random(zlib.crc32(f"{slug}:{chs}".encode()))
    rows = rows[:]
    rng.shuffle(rows)
    # Spread correct answers evenly over A-D, in a shuffled order.
    slots = [i % 4 for i in range(len(rows))]
    rng.shuffle(slots)
    out = []
    for (ch, q, right, wrong, expl), slot in zip(rows, slots):
        others = list(wrong)
        rng.shuffle(others)
        opts = others[:slot] + [right] + others[slot:]
        out.append({"q": q, "options": opts, "answer": slot, "explanation": expl, "chapter": ch})
    return {"chapters": list(chs), "questions": out}


def main():
    books = load_books()
    by_title = {}
    for slug, b in books.items():
        check(slug, b)
        for t in b["titles"]:
            by_title[t] = slug
    used = collections.Counter()
    scripts = []
    for ev in load_events().values():
        summaries, quizzes, info = {}, {}, {}
        for i, meta in enumerate(ev.get("books") or []):
            slug = by_title.get(meta["title"])
            if not slug:
                continue
            b = books[slug]
            used[slug] += 1
            summaries[i] = [{"number": n, "title": t, "summary": p, "keyPoints": k} for n, t, p, k in b["chapters"]]
            quizzes[i] = [build_quiz(slug, chs, rows) for chs, rows in b.get("quizzes", [])]
            info[i] = {"edition": b["edition"], "source": b["source"], "chapters": len(b["chapters"])}
        if not summaries:
            continue
        rel = f"data/books/{ev['id']}.js"
        os.makedirs(os.path.join(ROOT, "data", "books"), exist_ok=True)
        key = json.dumps(ev["id"])
        js = (f"// Chapter summaries and quizzes for {ev['name']}. Built by tools/build_books.py from tools/books/\n"
              "window.CONTENT = window.CONTENT || {};\n"
              f"window.CONTENT[{key}] = window.CONTENT[{key}] || {{}};\n")
        for name, val in (("summaries", summaries), ("quizzes", quizzes), ("bookInfo", info)):
            js += f"window.CONTENT[{key}].{name} = " + json.dumps(val, indent=1, ensure_ascii=False) + ";\n"
        open(os.path.join(ROOT, rel), "w", encoding="utf-8").write(js)
        scripts.append(rel)
        print(f"{ev['name']}: " + ", ".join(
            f"book {i + 1} ({len(summaries[i])} chapters, {len(quizzes[i])} quizzes)" for i in summaries))
    register_scripts(scripts)
    for slug in books:
        if not used[slug]:
            print(f"WARNING: {slug} matches no event book title")


if __name__ == "__main__":
    main()
