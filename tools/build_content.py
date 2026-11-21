"""Build practice tests and flashcards for one event from tools/content/<event_id>.py.

Usage:  python3 tools/build_content.py <event-id> [<event-id> ...]

A content module defines:
  TOPICS = {"M": "The Mind", ...}          # code -> topic name exactly as in the event's testPlan
  EASY / MEDIUM / HARD = [(code, question, correct, [wrong, wrong, wrong], explanation), ...]
  FLASHCARDS = [("Section", "Description", [("front", "back"), ...]), ...]

Checks: each test has exactly the event's testQuestions (50); each topic's share of questions is
within one question of its official test-plan weight; no duplicate questions; 4 distinct options.
Writes data/tests/<id>.js and data/flashcards/<id>.js and registers both in index.html.
"""
import importlib.util, json, os, random, re, sys, zlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_events():
    src = open(os.path.join(ROOT, "data/events.js"), encoding="utf-8").read()
    arr = src[src.index("window.EVENTS = ") + len("window.EVENTS = "):].rstrip().rstrip(";")
    return {e["id"]: e for e in json.loads(arr)}


def load_module(event_id):
    path = os.path.join(ROOT, "tools/content", event_id.replace("-", "_") + ".py")
    spec = importlib.util.spec_from_file_location("content_" + event_id.replace("-", "_"), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_level(rows, ev, topics, seed, level):
    n = ev["testQuestions"]
    from collections import Counter
    assert len(rows) == n, f"{level}: {len(rows)} questions, need {n}; by topic: {dict(Counter(r[0] for r in rows))}"
    plan = {r["topic"]: r["pct"] for r in ev["testPlan"]}
    if plan and all(p is not None for p in plan.values()):
        for code, name in topics.items():
            assert name in plan, f"topic {name!r} is not in the official test plan"
            have = sum(1 for r in rows if r[0] == code)
            want = plan[name] * n / 100
            assert abs(have - want) < 1, f"{level}: {name} has {have} questions, plan says {want:g}"
    rng = random.Random(seed)
    rows = rows[:]
    rng.shuffle(rows)
    # Spread correct answers evenly over A-D, in random order.
    slots = [i % 4 for i in range(len(rows))]
    rng.shuffle(slots)
    out = []
    for (code, q, right, wrong, expl), slot in zip(rows, slots):
        assert code in topics, f"unknown topic code {code}"
        opts = list(wrong)
        assert len(opts) == 3 and right not in opts and len(set(opts)) == 3, f"bad options: {q}"
        rng.shuffle(opts)
        opts.insert(slot, right)
        out.append({"q": q, "options": opts, "answer": slot, "explanation": expl, "topic": topics[code]})
    return out


def register_scripts(paths):
    p = os.path.join(ROOT, "index.html")
    html = open(p, encoding="utf-8").read()
    start, end = "<!-- content:start -->", "<!-- content:end -->"
    if start not in html:
        html = html.replace('  <script src="js/app.js"></script>', f"  {start}\n  {end}\n  <script src=\"js/app.js\"></script>")
    block = html[html.index(start) + len(start):html.index(end)]
    existing = re.findall(r'src="([^"]+)"', block)
    # also keep tags that were added by hand before the markers existed
    for src in re.findall(r'<script src="(data/(?:tests|quizzes|flashcards|guides|books)/[^"]+)"></script>', html):
        if src not in existing:
            existing.append(src)
            html = html.replace(f'  <script src="{src}"></script>\n', "", 1)
    for s in paths:
        if s not in existing:
            existing.append(s)
    tags = "".join(f'\n  <script src="{s}"></script>' for s in sorted(existing))
    html = html[:html.index(start) + len(start)] + tags + "\n  " + html[html.index(end):]
    open(p, "w", encoding="utf-8").write(html)


def write_js(rel, event_id, key, value, comment):
    os.makedirs(os.path.dirname(os.path.join(ROOT, rel)), exist_ok=True)
    js = (f"// {comment}\n"
          "window.CONTENT = window.CONTENT || {};\n"
          f"window.CONTENT[{json.dumps(event_id)}] = window.CONTENT[{json.dumps(event_id)}] || {{}};\n"
          f"window.CONTENT[{json.dumps(event_id)}].{key} = " + json.dumps(value, indent=1, ensure_ascii=False) + ";\n")
    open(os.path.join(ROOT, rel), "w", encoding="utf-8").write(js)


def build(event_id):
    ev = load_events()[event_id]
    m = load_module(event_id)
    tests = {lvl: build_level(getattr(m, lvl.upper()), ev, m.TOPICS, zlib.crc32(f"{event_id}:{lvl}".encode()), lvl)
             for lvl in ["easy", "medium", "hard"]}
    qs = [q["q"] for t in tests.values() for q in t]
    dupes = {q for q in qs if qs.count(q) > 1}
    assert not dupes, f"duplicate questions: {dupes}"
    decks = []
    for section, desc, cards in m.FLASHCARDS:
        fronts = [c[0] for c in cards]
        assert len(fronts) == len(set(fronts)), f"duplicate flashcard in {section}"
        decks.append({"section": section, "description": desc, "cards": [{"front": f, "back": b} for f, b in cards]})
    scripts = [f"data/tests/{event_id}.js", f"data/flashcards/{event_id}.js"]
    write_js(scripts[0], event_id, "tests", tests,
             f"{ev['name']} practice tests: {ev['testQuestions']} questions each, weighted by the 2026-27 test plan. Built by tools/build_content.py")
    write_js(scripts[1], event_id, "flashcards", decks,
             f"{ev['name']} flashcards. Built by tools/build_content.py")
    register_scripts(scripts)
    pos = {lvl: "".join("ABCD"[q["answer"]] for q in t).count for lvl, t in tests.items()}
    print(f"{ev['name']}: 3 x {ev['testQuestions']} questions, {sum(len(d['cards']) for d in decks)} flashcards in {len(decks)} sections;",
          "answer spread", {lvl: [f(c) for c in "ABCD"] for lvl, f in pos.items()})


if __name__ == "__main__":
    for eid in sys.argv[1:]:
        build(eid)
