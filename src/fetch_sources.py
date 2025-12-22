import feedparser

POLICY_RSS_FEED = "https://www.nber.org/papers.rss"

def fetch_nber_papers(limit=5):
    feed = feedparser.parse(POLICY_RSS_FEED)

    items = []
    for entry in feed.entries[:limit]:
        items.append({
            "title": entry.title,
            "summary": entry.get("summary", ""),
            "link": entry.link
        })

    return items
