import openai

# Set your OpenAI API key
OPENAI_API_KEY = "your_api_key_here"

def chat_with_gpt(prompt):
    """Sends user input to ChatGPT and returns the response."""
    openai.api_key = OPENAI_API_KEY
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Change to "gpt-4" if you have access
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    
    except Exception as e:
        return f"Error: {e}"

# Main chatbot loop
if __name__ == "__main__":
    print("ARsGPT: bye! Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["hi", "bye", "hello broo"]:
            print("ARsGPT: hello broo!")
            break
        
        response = chat_with_gpt(user_input)
        print("ARsGPT:", response)
