import re, random
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

destinations = {
    "beaches": ["Maldives", "Bali", "Hawaii", "Phuket", "Boracay"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Mount Fuji", "Andes"],
    "cities": ["Paris", "New York", "Tokyo", "Rome", "Seoul"]
}

jokes = [
    "Why did the computer show up late? It had a hard drive.",
    "Why did the smartphone go to therapy? It lost its sense of touch!",
    "What do you call a sleepy computer? A naptop!",
    "Why did the computer get a virus? It wasn’t updated!",
    "Why was the phone always tired? Too many apps running!"
]

weather_conditions = [
    "Sunny ☀️ 25°C",
    "Rainy 🌧️ 18°C",
    "Cloudy ☁️ 20°C",
    "Partly Cloudy ⛅ 21°C",
    "Windy 🌬️ 22°C"
]

news = [
    "AI is improving faster than expected.",
    "Scientists discover new renewable energy source.",
    "Space mission successfully launched.",
    "Tech companies invest more in green energy."
]

def menu():
    print(f"{Fore.CYAN}\n================== MAIN MENU ==================")
    print(f"{Fore.GREEN}recommend   --> Get travel recommendations")
    print(f"{Fore.YELLOW}joke        --> Hear a joke")
    print(f"{Fore.GREEN}packing     --> Get packing tips")
    print(f"{Fore.YELLOW}weather     --> Get today's weather")
    print(f"{Fore.GREEN}news        --> Get today's news")
    print(f"{Fore.YELLOW}time        --> Get current time")
    print(f"{Fore.GREEN}menu        --> Show this menu")
    print(f"{Fore.YELLOW}exit        --> Exit the chatbot")
    print(f"{Fore.CYAN}===============================================\n")

def normalize_input(user_input):
    return re.sub(r"\s+", " ", user_input.strip().lower())

def chat():
    print(f"{Fore.GREEN}Hi! I am your simple AI chatbot!")
    name = input("What is your name? ")

    print(f"{Fore.GREEN}Nice to meet you {name}!")
    menu()

    history = []

    while True:
        user_input = normalize_input(input(f"{Fore.WHITE}{name}: "))
        history.append(user_input)

        if "menu" in user_input:
            menu()

        elif "recommend" in user_input or "suggest" in user_input:
            print(f"{Fore.CYAN}Do you like beaches, mountains, or cities?")
            choice = input("Choice: ").lower()

            if choice in destinations:
                print(f"{Fore.GREEN}You should visit " +
                      random.choice(destinations[choice]))
            else:
                print(f"{Fore.RED}I don't know that category.")

        elif "joke" in user_input or "funny" in user_input:
            print(Fore.YELLOW + random.choice(jokes))

        elif "packing" in user_input or "tips" in user_input:
            print(f"{Fore.MAGENTA}Packing tip: Pack light and only what you need!")

        elif "weather" in user_input:
            print(f"{Fore.BLUE}Weather today: " + random.choice(weather_conditions))

        elif "news" in user_input:
            print(Fore.CYAN + random.choice(news))

        elif "time" in user_input:
            now = datetime.now()
            print(f"{Fore.GREEN}Current time: ")
            print(now)

        elif "exit" in user_input or "quit" in user_input:
            print(f"{Fore.GREEN}Goodbye {name}! See you next time!")
            break

        else:
            print(f"{Fore.RED}I didn't understand that. Type 'menu' to see options :).")

if __name__ == "__main__":
    chat()