from fetch_sources import fetch_all_sources
from summarize import test_openai_call
from state import load_seen_items, save_seen_items

def main():
    print("✅ Bot started successfully")

    # Load previously seen items
    seen_items = load_seen_items()

    # Fetch all sources
    items = fetch_all_sources()
    print(f"📄 Fetched {len(items)} total items")

    # Filter out previously seen items
    new_items = [item for item in items if item["link"] not in seen_items]
    print(f"🆕 {len(new_items)} new items")

    for item in new_items:
        print(f"[{item['topic']}] {item['title']}")
        print(item["link"])
        print()

        # Mark as seen
        seen_items.add(item["link"])

    # Save updated state
    save_seen_items(seen_items)

