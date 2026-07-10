def get_response(user):
    user = user.lower()

    if user == "hello" or user == "hi":
        return "Hello, how can I help you?"

    elif user == "how are you":
        return "I am doing great! Thanks for asking."

    elif user == "bye" or user == "goodbye":
        return "Goodbye."

    else:
        return "Sorry, I don't understand."


# Optional: Keep this so you can still test from the terminal
if __name__ == "__main__":
    while True:
        user = input("You: ")
        response = get_response(user)
        print("ChatBot:", response)
        if user.lower() == "bye":
            break

