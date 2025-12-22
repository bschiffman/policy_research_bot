from fetch_sources import fetch_all_sources
from summarize import test_openai_call

def main():
    print("✅ Bot started successfully")

    items = fetch_all_sources()
    print(f"📄 Fetched {len(items)} papers")

    for item in items:
        print(f"[{item['topic']}] {item['title']}")
        print(f"🔗 {item['link']}\n")

    print("🤖 OpenAI test response:")
    print(test_openai_call())

if __name__ == "__main__":
    main()
