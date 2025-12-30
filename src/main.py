from fetch_sources import fetch_all_sources
from state import load_seen_items, save_seen_items
from summarize import summarize_item
from fetch_voxeu import fetch_voxeu_papers
#from fetch_semantic_scholar import fetch_semantic_papers

def main():
    print("✅ Bot started successfully")

    # Load previously seen research items
    seen_items = load_seen_items()

    # Fetch research from all sources (primary)
    items = fetch_all_sources()
    print(f"📄 Fetched {len(items)} total items")

    # Filter out items that have already been sent
    new_items = [item for item in items if item["link"] not in seen_items]
    print(f"🆕 {len(new_items)} new items")

    if not new_items:
        print("ℹ️ No new research items today.")
    # 🔁 FALLBACK LOGIC
    if len(new_items) == 0:
        print("⚠️ No items from primary sources — falling back to VoxEU")
        vox_items = fetch_voxeu_papers(limit=100)
        print(f"📄 Fetched {len(vox_items)} VoxEU items")

        new_items = [
            item for item in vox_items
            if item["link"] not in seen_items
        ]

    print(f"🆕 {len(new_items)} new VoxEU items")
    to_summarize = new_items[:4]
    print(f"📌 Summarizing {len(to_summarize)} items today (limit 4)")

    for item in to_summarize:
        print(f"[{item['source']}] {item['title']}")
        print(f"✍️ {item.get('authors', 'Unknown authors')}")
        print(f"🔗 {item['link']}")
        if item["source"].lower().startswith("voxeu"):
            print("📝 Note: This is commentary (policy column), not peer-reviewed research.")
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
