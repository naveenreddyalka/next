#!/usr/bin/env python3
"""Merge seed + inbox questions into company_latest_questions.json (newest first)."""
import json
import re
from datetime import date
from pathlib import Path

SCRIPTS = Path(__file__).parent
STORE = SCRIPTS / "company_latest_questions.json"
INBOX = SCRIPTS / "company_questions_inbox.json"
SEED_PATH = SCRIPTS / "company_questions_seed.py"

MAX_PER_COMPANY = 30


def norm(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def load_store():
    if STORE.exists():
        raw = json.loads(STORE.read_text(encoding="utf-8"))
        return {k: v for k, v in raw.items() if not k.startswith("_")}
    return {}


def load_inbox():
    if INBOX.exists():
        return json.loads(INBOX.read_text(encoding="utf-8"))
    return {}


def load_seed():
    ns = {}
    exec(SEED_PATH.read_text(encoding="utf-8"), ns)
    return ns.get("QUESTIONS", {})


def merge_questions(existing, incoming, today):
    seen = {norm(x["question"]) for x in existing}
    merged = list(existing)
    added = 0
    for item in incoming:
        key = norm(item["question"])
        if key in seen:
            continue
        entry = dict(item)
        entry.setdefault("added", today)
        merged.insert(0, entry)
        seen.add(key)
        added += 1
    return merged[:MAX_PER_COMPANY], added


def main():
    today = date.today().isoformat()
    store = load_store()
    seed = load_seed()
    inbox = load_inbox()
    all_slugs = set(seed) | set(inbox) | set(store)
    total_added = 0

    for slug in sorted(all_slugs):
        if slug.startswith("_"):
            continue
        existing = store.get(slug, [])
        incoming = list(inbox.get(slug, [])) + list(seed.get(slug, []))
        merged, added = merge_questions(existing, incoming, today)
        store[slug] = merged
        total_added += added
        if added:
            print(f"  +{added} {slug}")

    store["_meta"] = {"last_refresh": today, "max_per_company": MAX_PER_COMPANY}
    STORE.write_text(json.dumps(store, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"updated {STORE.name} (+{total_added} new questions)")


if __name__ == "__main__":
    main()
