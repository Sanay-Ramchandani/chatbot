import openai

# Set up your OpenAI API key
openai.api_key = 'your-api-key-here'

def create_chatbot():
    print("OpenAI GPT-based chatbot is ready.")
    return None  # No need for a chatbot instance

def chat_with_bot():
    print("Hello! I am OpenAI GPT-based bot. How can I assist you today?")
    print("Type 'exit' to end the chat.")

    while True:
        try:
            user_input = input("You: ")
            
            if user_input.lower() == 'exit':
                print("OpenAI Bot: Goodbye! Have a great day!")
                break

            # Get a response from OpenAI
            response = openai.Completion.create(
                engine="text-davinci-003",  # Or choose another model like 'gpt-3.5-turbo' if available
                prompt=user_input,
                max_tokens=150
            )
            bot_response = response.choices[0].text.strip()
            print(f"OpenAI Bot: {bot_response}")

        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    create_chatbot()
    chat_with_bot()
