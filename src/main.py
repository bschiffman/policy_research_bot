from summarize import test_openai_call

def main():
    print("✅ Bot started successfully")

    items = fetch_nber_papers()
    print(f"📄 Fetched {len(items)} NBER papers")

    for item in items:
        print(f"- {item['title']}")

    result = test_openai_call()
    print("🤖 OpenAI response:")
    print(result)

if __name__ == "__main__":
    main()
