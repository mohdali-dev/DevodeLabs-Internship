# =========================================
# Rule-Based AI Chatbot
# Internship Project 1
# Developed by Muhammad Ali
# =========================================

print("=" * 50)
print("🤖 Welcome to the AI Rule-Based Chatbot")
print("Type 'help' to see available commands.")
print("Type 'bye' to exit the chatbot.")
print("=" * 50)


# Continuous chatbot loop
while True:

    # Take user input
    user_input = input("\nYou: ").strip().lower()

    # Greeting responses
    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! 👋 Nice to meet you.")

    # Asking chatbot name
    elif user_input in ["your name", "who are you"]:
        print("Bot: I am a Rule-Based AI Chatbot created in Python.")

    # Asking chatbot condition
    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking 😊")

    # Help command
    elif user_input == "help":
        print("\n📌 Available Commands:")
        print("- hello / hi / hey")
        print("- how are you")
        print("- your name")
        print("- time")
        print("- date")
        print("- joke")
        print("- bye")

    # Time response
    elif user_input == "time":
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Bot: Current time is {current_time}")

    # Date response
    elif user_input == "date":
        from datetime import datetime
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")

    # Joke response
    elif user_input == "joke":
        print("Bot: Why do programmers prefer dark mode?")
        print("Bot: Because light attracts bugs 😂")

    # Exit condition
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a wonderful day 🚀")
        break

    # Empty input handling
    elif user_input == "":
        print("Bot: Please type something.")

    # Default response
    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Type 'help' to see available commands.")
