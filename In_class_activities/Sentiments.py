import colorama 
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()
print(f"{Fore.BLUE} Welcome to sentiment spy: {Style.RESET_ALL}")
username=input(f"{Fore.BLACK}Please enter your name: {Style.RESET_ALL}")

if not username:
    username= "Mystery User"
conversation_history = []
print(f"Hello Agent{username}")
print(f"Type your sentence to analyze its sentiment. Type rest, history, or exit to quit.")

while True:
    user_input= input(f"-->")
    if not user_input:
        print(f"{Fore.RED}Please enter a valid sentence.{Style.RESET_ALL}")
        continue

    if user_input.lower()=="exit":
        print("Exiting sentiment spy. Goodbye {username}!")
        break
    elif user_input.lower()=="reset":
        conversation_history.clear()
        print("Conversation history cleared.")
        continue
    elif user_input.lower()=="history":
        if not conversation_history:
            print("No conversation history.")
        else:
            print("Conversation History:")
            for idx, (text, polarity, sentiment) in enumerate(conversation_history, start=1):
                if sentiment=="Positive":
                    color=Fore.GREEN
                elif sentiment=="Negative":
                    color=Fore.RED
                else:
                    color=Fore.ORANGE
                print(f"{idx}. {text} - {color}{sentiment} (Polarity: {polarity:.2f}){Style.RESET_ALL}")    

                continue

    polarity= TextBlob(user_input).sentiment.polarity

    if polarity>0.25:
        sentiment="Positive"
        color=Fore.GREEN

    elif polarity<-0.25:
        sentiment="Negative"
        color=Fore.RED

    else:
        sentiment="Neutral"
        color=Fore.ORANGE

    conversation_history.append((user_input, polarity, sentiment))
    print(f"{color}Sentiment: {sentiment} (Polarity: {polarity:.2f}){Style.RESET_ALL}")