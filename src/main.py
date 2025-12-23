from fetch_sources import fetch_all_sources
from state import load_seen_items, save_seen_items
from summarize import summarize_item

def main():
    print("✅ Bot started successfully")

    # Load previously seen research items
    seen_items = load_seen_items()

    # Fetch research from all sources
    items = fetch_all_sources()
    print(f"📄 Fetched {len(items)} total items")

    # Filter out items that have already been sent
    new_items = [item for item in items if item["link"] not in seen_items]
    print(f"🆕 {len(new_items)} new items")

    if not new_items:
        print("ℹ️ No new research items today.")
        return

    for item in new_items:
        print(f"[{item['topic']}] {item['title']}")
        print(f"🔗 {item['link']}\n")

        # Generate summary using OpenAI
        summary = summarize_item(item)
        print(summary)
        print("-" * 60)

        # Mark item as seen
        seen_items.add(item["link"])

    # Persist updated state
    save_seen_items(seen_items)
    print("💾 Seen items updated successfully")


if __name__ == "__main__":
    main()
