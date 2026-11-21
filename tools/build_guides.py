"""Build study guides for events judged without a written test.

Each guide lives in tools/guides/<event_id_with_underscores>.py and defines GUIDE:

GUIDE = {
    "overview": "What the event is and what wins it.",
    "facts": [("Label", "Value"), ...],                 # quick facts from the guideline
    "rounds": [("Round One: ...", ["rule", ...]), ...],  # how the event runs, in order
    "rubrics": [{"title": "...", "total": 105,           # total printed on the official rating sheet
                 "sections": [("Content", [("Criterion", max_points), ...]), ...]}],
    "tips": ["..."], "mistakes": ["..."], "checklist": ["..."],
}

The builder checks that each rubric's criteria add up to its official total, writes
data/guides/<id>.js and registers the script in index.html.
Usage: python3 tools/build_guides.py <event-id> [...]   (or no arguments to build all)
"""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build_content import ROOT, load_events, register_scripts, write_js  # noqa: E402

GUIDE_DIR = os.path.join(ROOT, "tools", "guides")


def load(event_id):
    path = os.path.join(GUIDE_DIR, event_id.replace("-", "_") + ".py")
    spec = importlib.util.spec_from_file_location("guide_" + event_id.replace("-", "_"), path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.GUIDE


def build(event_id):
    ev = load_events()[event_id]
    assert not ev["hasTest"], f"{event_id} has a written test; guides are for non-test events"
    g = load(event_id)
    for key in ("overview", "facts", "rounds", "rubrics", "tips", "mistakes", "checklist"):
        assert g.get(key), f"{event_id}: missing {key}"
    rubrics = []
    for r in g["rubrics"]:
        total = sum(p for _, items in r["sections"] for _, p in items)
        assert total == r["total"], f"{event_id}: rubric '{r['title']}' adds to {total}, official total is {r['total']}"
        rubrics.append({
            "title": r["title"], "total": r["total"], "note": r.get("note", ""), "pill": r.get("pill", ""),
            "sections": [{"name": n, "items": [{"criterion": c, "points": p} for c, p in items]} for n, items in r["sections"]],
        })
    out = {
        "overview": g["overview"],
        "facts": [{"label": a, "value": b} for a, b in g["facts"]],
        "rounds": [{"title": t, "steps": s} for t, s in g["rounds"]],
        "rubrics": rubrics,
        "tips": g["tips"], "mistakes": g["mistakes"], "checklist": g["checklist"],
    }
    rel = f"data/guides/{event_id}.js"
    write_js(rel, event_id, "guide", out, f"{ev['name']} study guide, from the 2026-27 guidelines. Built by tools/build_guides.py")
    register_scripts([rel])
    print(f"{ev['name']}: guide with {len(out['rounds'])} rounds, {len(rubrics)} rubric(s) "
          f"({', '.join(str(r['total']) for r in rubrics)} pts), {len(out['tips'])} tips, {len(out['checklist'])} checklist items")


if __name__ == "__main__":
    ids = sys.argv[1:] or sorted(f[:-3].replace("_", "-") for f in os.listdir(GUIDE_DIR) if f.endswith(".py"))
    for eid in ids:
        build(eid)
