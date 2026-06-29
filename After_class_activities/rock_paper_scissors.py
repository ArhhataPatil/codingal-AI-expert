import random
import colorama 
from colorama import Fore, Style, init
init(autoreset=True)

def play_game():
    while True:
        print(Fore.CYAN + "=" * 60)
        print(Fore.MAGENTA + "🎮 ROCK • PAPER • SCISSORS 🎮".center(60))
        print(Fore.CYAN + "=" * 60)

        user = input(Fore.YELLOW + "👉 Enter a choice (rock, paper, scissors): " + Style.RESET_ALL)

        actions = ["rock", "paper", "scissors"]
        computer = random.choice(actions)

        print(Fore.BLUE + "🖥 Computer chose: " + Fore.MAGENTA + computer + Style.RESET_ALL)

        if user == computer:
            print(Fore.CYAN + "🤝 Both selected " + user + ". It's a tie!" + Style.RESET_ALL)

        elif user == "rock" and computer == "scissors":
            print(Fore.GREEN + "💥 Rock defeats scissors! You win! 🎉" + Style.RESET_ALL)

        elif user == "paper" and computer == "rock":
            print(Fore.GREEN + "📄 Paper defeats rock! You win! 🎉" + Style.RESET_ALL)

        elif user == "scissors" and computer == "paper":
            print(Fore.GREEN + "✂ Scissors defeats paper! You win! 🎉" + Style.RESET_ALL)

        elif user == "rock" and computer == "paper":
            print(Fore.RED + "📄 Paper defeats rock! You lose 😢" + Style.RESET_ALL)

        elif user == "paper" and computer == "scissors":
            print(Fore.RED + "✂ Scissors defeats paper! You lose 😢" + Style.RESET_ALL)

        elif user == "scissors" and computer == "rock":
            print(Fore.RED + "💥 Rock defeats scissors! You lose 😢" + Style.RESET_ALL)

        else:
            print(Fore.RED + "⚠ Invalid input. Please choose rock, paper, or scissors." + Style.RESET_ALL)

        replay = input(Fore.MAGENTA + "🔁 Play again? (yes/no): " + Style.RESET_ALL)

        if replay.lower() == "yes":
            continue
        else:
            print(Fore.BLUE + "👋 Thanks for playing! Goodbye!" + Style.RESET_ALL)
            break

play_game()