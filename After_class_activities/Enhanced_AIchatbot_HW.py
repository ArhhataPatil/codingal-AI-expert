while True:

    print("Hello, I am an AI chatbot. What is your name?")
    name = input()

    print(f"Nice to meet you, {name}. How are you feeling today?")
    print("1. Happy")
    print("2. Sad")
    print("3. Excited")
    print("4. Anxious")
    print("5. Tired")
    print("6. Angry")

    feeling = input().lower()

    if feeling == "happy" or feeling == "1":
        print(f"That's great to hear, {name}! Keep smiling!")

    elif feeling == "sad" or feeling == "2":
        print(f"I'm sorry to hear that, {name}. Remember, it's okay to feel sad sometimes. Take care of yourself!")

    elif feeling == "excited" or feeling == "3":
        print(f"That's wonderful, {name}! Enjoy the excitement and make the most of it!")

    elif feeling == "anxious" or feeling == "4":
        print(f"I'm sorry to hear that, {name}. Try to take deep breaths and find ways to relax. You're not alone!")

    elif feeling == "tired" or feeling == "5":
        print(f"It sounds like you could use some rest, {name}. Make sure to take care of yourself and get some sleep!")

    elif feeling == "angry" or feeling == "6":
        print(f"I'm sorry to hear that, {name}. Try to find healthy ways to manage your anger, such as taking a walk or talking to someone you trust.")

    else:
        print(f"I'm not sure how to respond to that, {name}. But I'm here to listen if you want to talk more about it!")

    print("Do you want to repeat the conversation? (yes/no)")
    repeat = input().lower()

    if repeat == "yes":
        print("Restarting conversation...")

    else:
        print(f"Bye, {name}! It was nice chatting to you. Have a great day!")
        break