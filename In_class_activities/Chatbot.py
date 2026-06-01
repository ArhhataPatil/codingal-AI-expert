import re, random
from colorama import Fore, Style, init
init(autoreset=True)

destinations={
    "beaches":["Maldives", "Bali", "Hawaii", "Phuket", "Boracay"],
    "mountains":["Swiss Alps", "Rocky Mountains", "Himalayas", "Mount Fuji", "Andes"],
    "cities":["Paris", "New York", "Tokyo", "Rome", "Seoul"]
}

jokes={
    "jokes":["Why did the computer show up late to work? It had a hard drive.",
            "Did you hear about the octopus who stopped printing? It ran out of ink!",
            "What do you call a sleepy little computer? A naptop!",
            "Why did the smartphone go to therapy? It lost its sense of touch!",
            "Why did the computer go to the doctor? It had a virus!"]
}

def show_help():
    print(f"I can:")
    print(f"If you want some beach reccomendations, type 'recommend/ suggest'")
    print(f"If you want to hear a joke type 'joke'")
    print(f"If you want to exit, type 'exit'")
    print(f"If you want to see this message again type 'help'")
    print(f"I f you want packing tips, type 'packing'")

def normalize_input(user_input):
    return re.sub(r"\s+", " ", user_input.strip().lower())





def chat():
    print(f"Hi! I am an AI chat bot. I can help you with many things!")
    name=input(f"What is your name? ")
    print(f"Nice to meet you {name}!")
    show_help()

    while True:
        user_input= input(f"{name}: ")
        user_input= normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            pass
        elif "joke" in user_input or "funny" in user_input:
            pass
        elif "packing" in user_input or "tips" in user_input:
            pass
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "quit" in user_input:
            print(f"Goodbay {name}! It was nice chatting with you. Have a great day!")
            break

if __name__ == " __main__":
    chat()
