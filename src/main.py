from summarize import test_openai_call

def main():
    print("✅ Bot started successfully")

    result = test_openai_call()
    print("🤖 OpenAI response:")
    print(result)

if __name__ == "__main__":
    main()
