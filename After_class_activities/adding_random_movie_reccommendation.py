import random
import time
import pandas as pd

from textblob import TextBlob
from colorama import Fore, init


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

init(autoreset=True)

try:
    df = pd.read_csv("imdb_top_1000.csv")

except FileNotFoundError:
    print(Fore.RED + "Error: 'imdb_top_1000.csv' not found.")
    raise SystemExit

df = df[[
    "Series_Title",
    "Genre",
    "Overview",
    "IMDB_Rating"
]]

df.dropna(inplace=True)

df["Features"] = df["Genre"] + " " + df["Overview"]

vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["Features"])

genres = sorted({
    g.strip()
    for xs in df["Genre"].str.split(",")
    for g in xs
})

def dots():

    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

    print()

def sentiment(text):

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive 😊"

    elif polarity < 0:
        return "Negative 😞"

    else:
        return "Neutral 😐"

def show_movie(movie):

    print(Fore.CYAN + "\n==============================")
    print(Fore.YELLOW + "Movie Recommendation")
    print(Fore.CYAN + "==============================")

    print(Fore.GREEN + f"Title: {movie['Series_Title']}")
    print(Fore.WHITE + f"Genre: {movie['Genre']}")
    print(Fore.WHITE + f"IMDb Rating: {movie['IMDB_Rating']}")

    print(Fore.MAGENTA + "\nOverview:")
    print(movie["Overview"])

    print(Fore.BLUE + "\nSentiment:")
    print(sentiment(movie["Overview"]))

    print(Fore.CYAN + "==============================")

def get_genre():

    print(Fore.GREEN + "\nAvailable Genres:\n")

    for i, genre in enumerate(genres, 1):
        print(f"{i}. {genre}")

    while True:

        choice = input(
            Fore.YELLOW +
            "\nEnter genre number or name: "
        ).strip()

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(genres):
                return genres[choice - 1]

        else:

            choice = choice.title()

            if choice in genres:
                return choice

        print(Fore.RED + "Invalid genre. Try again.")

def get_rating():

    while True:

        rating = input(
            Fore.YELLOW +
            "Minimum IMDb rating (or press Enter to skip): "
        )

        if rating == "":
            return None

        try:
            return float(rating)

        except ValueError:
            print(Fore.RED + "Invalid rating.")

def ai_recommendation():

    genre = get_genre()

    mood = input(
        Fore.YELLOW +
        "How are you feeling today? "
    ).strip()

    rating = get_rating()

    print(Fore.BLUE + "\nFinding the best movie", end="")
    dots()

    query = genre + " " + mood

    query_vector = vectorizer.transform([query])

    similarity = cosine_similarity(
        query_vector,
        tfidf_matrix
    ).flatten()

    df_copy = df.copy()

    df_copy["Similarity"] = similarity

    if rating is not None:
        df_copy = df_copy[
            df_copy["IMDB_Rating"] >= rating
        ]

    if len(df_copy) == 0:
        print(Fore.RED + "No movies found.")
        return

    df_copy = df_copy.sort_values(
        by="Similarity",
        ascending=False
    )

    movie = df_copy.iloc[0]

    show_movie(movie)

def random_recommendation():

    print(Fore.BLUE + "\nChoosing a random movie", end="")
    dots()

    movie = df.sample(1).iloc[0]

    show_movie(movie)

print(Fore.CYAN + "===================================")
print(Fore.YELLOW + " Movie Recommendation System ")
print(Fore.CYAN + "===================================")

name = input(
    Fore.YELLOW +
    "\nWhat is your name? "
).strip()

print(
    Fore.GREEN +
    f"\nWelcome {name}!"
)

while True:

    print(Fore.CYAN + "\n===================================")
    print(Fore.YELLOW + "Choose an Option")
    print(Fore.CYAN + "===================================")

    print("1. AI Recommendation")
    print("2. Random Recommendation")
    print("3. Exit")

    choice = input(
        Fore.YELLOW +
        "\nEnter your choice: "
    ).strip()

    if choice == "1":

        ai_recommendation()

    elif choice == "2":

        random_recommendation()

    elif choice == "3":

        print(
            Fore.GREEN +
            f"\nThanks for using the Movie Recommendation System, {name}!"
        )

        print(Fore.GREEN + "Enjoy your movie! 🍿🎬")

        break

    else:

        print(
            Fore.RED +
            "Invalid choice. Please try again."
        )

    while True:

        again = input(
            Fore.YELLOW +
            "\nWould you like another recommendation? (yes/no): "
        ).strip().lower()

        if again == "yes":
            break

        elif again == "no":

            print(
                Fore.GREEN +
                f"\nGoodbye {name}! Have a great day! 👋"
            )

            raise SystemExit

        else:

            print(
                Fore.RED +
                "Please enter yes or no."
            )