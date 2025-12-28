from fetch_sources import fetch_all_sources
from state import load_seen_items, save_seen_items
from summarize import summarize_item
from fetch_semantic_scholar import fetch_semantic_papers

def main():
    print("✅ Bot started successfully")

    # Load previously seen research items
    seen_items = load_seen_items()

    # Fetch research from all sources (primary)
    items = fetch_all_sources()
    print(f"📄 Fetched {len(items)} total items")

    # 🔁 FALLBACK LOGIC
    if len(items) == 0:
        print("⚠️ No items from primary sources — falling back to Semantic Scholar")
        items = fetch_semantic_papers(
            query="econometrics OR causal inference OR policy evaluation",
            days_back=7,
            limit=10,
        )
        print(f"📄 Fetched {len(items)} fallback items")

    # Filter out items that have already been sent
    new_items = [item for item in items if item["link"] not in seen_items]
    print(f"🆕 {len(new_items)} new items")

    if not new_items:
        print("ℹ️ No new research items today.")
        return

    for item in new_items:
        print(f"[{item['topic']}] {item['title']}")
        print(f"✍️ {item.get('authors', 'Unknown authors')}")
        print(f"🏷️ Source: {item.get('source', 'Unknown')}")
        print(f"🔗 {item.get('link', item.get('url'))}")

        # Generate summary using OpenAI
        summary = summarize_item(item)
        print(summary)
        print("-" * 60)

        # Mark item as seen
        seen_items.add(item.get('link', item.get('url')))

    # Persist updated state
    save_seen_items(seen_items)
    print("💾 Seen items updated successfully")


if __name__ == "__main__":
    main()
