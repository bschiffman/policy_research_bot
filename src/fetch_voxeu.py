import feedparser

VOXEU_RSS_URL = "https://voxeu.org/rss.xml"

def fetch_voxeu_papers(limit=10):
    """
    Fetch latest VoxEU columns (opinion / policy commentaries).
    Returns a list of dicts compatible with main.py:
    - title
    - link
    - authors
    - source
    - summary
    """
    feed = feedparser.parse(VOXEU_RSS_URL)
    papers = []

    for entry in feed.entries[:limit]:
        papers.append({
            "title": entry.title,
            "link": entry.link,
            "authors": entry.get("author", "Unknown"),
            "source": "VoxEU (columns / policy commentary)",
            "summary": entry.get("summary", ""),
        })
    return papers
