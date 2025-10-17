def get_response(user_text):
    user_text = user_text.lower()
    if "hello" in user_text or "hi" in user_text:
        return "Hey there! How are you?"
    elif "how are you" in user_text:
        return "I'm good! 😄"
    elif "your name" in user_text:
        return "I'm AnjaliBot 🤖"
    elif "bye" in user_text:
        return "Bye! Have a great day ❤️"
    else:
        return "I didn't understand that."

# Example test
while True:
    msg = input("You: ")
    if msg.lower() == "bye":
        print("Bot: Bye!")
        break
    print("Bot:", get_response(msg))
