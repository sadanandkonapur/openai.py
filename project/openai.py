import openai

# 🔐 Set your OpenAI API key here
OPENAI_API_KEY = "your_api_key_here"  # Replace with your actual API key

def chat_with_gpt(prompt):
    """Send user question to OpenAI GPT and return the reply."""
    openai.api_key = OPENAI_API_KEY

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Change to "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"[Error] {str(e)}"

def main():
    print("🤖 ARsGPT Chatbot")
    print("Type your question and press Enter. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("ARsGPT: Goodbye! 👋")
            break

        response = chat_with_gpt(user_input)
        print("ARsGPT:", response + "\n")

if __name__ == "__main__":
    main()
