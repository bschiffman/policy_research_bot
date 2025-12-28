import requests
from datetime import datetime, timedelta

SEMANTIC_API = "https://api.semanticscholar.org/graph/v1/paper/search"

def fetch_semantic_papers(query, days_back=7, limit=5):
    since = (datetime.utcnow() - timedelta(days=days_back)).strftime("%Y-%m-%d")

    params = {
        "query": query,
        "limit": limit,
        "fields": "title,authors,abstract,year,venue,url",
    }

    r = requests.get(SEMANTIC_API, params=params)
    r.raise_for_status()

    papers = []
    for p in r.json().get("data", []):
        papers.append({
            "id": p["paperId"],
            "title": p["title"],
            "authors": ", ".join(a["name"] for a in p.get("authors", [])),
            "abstract": p.get("abstract", ""),
            "source": "Semantic Scholar",
            "url": p.get("url"),
            "link": p.get("url"),  # <--- add this line
            "year": p.get("year"),
        })

    return papers
