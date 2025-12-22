import feedparser

ARXIV_FEEDS = {
    "economics": "https://export.arxiv.org/rss/econ.GN",
    "econometrics": "https://export.arxiv.org/rss/econ.EM",
    "ai": "https://export.arxiv.org/rss/cs.AI",
    "ml": "https://export.arxiv.org/rss/cs.LG"
}

def fetch_one_from_feed(feed_url):
    feed = feedparser.parse(feed_url)

    if not feed.entries:
        return None

    entry = feed.entries[0]

    return {
        "title": entry.title,
        "summary": entry.get("summary", ""),
        "link": entry.link,
    }

def fetch_all_sources():
    items = []

    for topic, url in ARXIV_FEEDS.items():
        item = fetch_one_from_feed(url)
        if item:
            item["topic"] = topic
            items.append(item)

    return items
