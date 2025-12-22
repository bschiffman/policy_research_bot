import json
from pathlib import Path

SEEN_PATH = Path("data/seen_items.json")

def load_seen_items():
    if SEEN_PATH.exists():
        return set(json.loads(SEEN_PATH.read_text()))
    return set()

def save_seen_items(seen_items):
    SEEN_PATH.write_text(json.dumps(sorted(seen_items), indent=2))
