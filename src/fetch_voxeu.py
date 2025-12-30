import feedparser

CEPR_FEEDS = {
    "vox_content": "https://cepr.org/rss/vox-content",
    "discussion_papers": "https://cepr.org/rss/discussion-paper",
    "news": "https://cepr.org/rss/news"
}

def fetch_voxeu_papers(limit=10):
    items = []

    for topic, url in CEPR_FEEDS.items():
        feed = feedparser.parse(url)
        print(f"RSS '{topic}' contains {len(feed.entries)} entries")  # debug

        for entry in feed.entries:
            item = {
                "title": entry.title,
                "link": entry.link,
                "authors": entry.get("author", "Unknown"),
                "source": f"CEPR ({topic})",
            }
            items.append(item)

    # Sort by newest first if desired
    items.sort(key=lambda x: x.get("published_parsed", None), reverse=True)

    # Slice to limit
    return items[:limit]
