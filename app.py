from utils.response_generator import generate_response

print("Welcome to the Multilingual Healthcare Chatbot!")
print("Type 'exit' or 'quit' to end the chat.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Bot: Take care! Goodbye. 👋")
        break

    response = generate_response(user_input)
    print(f"Bot: {response}\n")
