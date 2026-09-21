books = []

def add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    year = int(input("Enter book year: "))
    rating = float(input("Enter book rating out of 5: "))
    review = input("Enter a short review: ")

    book = {
        "name": name,
        "author": author,
        "year": year,
        "rating": rating,
        "review": review
    }

    books.append(book)

    print(f"Book {name} added successfully!")


def view_books():
    if len(books) == 0:
        print("No books found.")
        return

    print("List of Books:")

    for i, book in enumerate(books, start=1):
        print(
            i,
            book["name"],
            "| Author:", book["author"],
            "| Year:", book["year"],
            "| Rating:", book["rating"]
        )


def search_book():
    name = input("Enter book name to search: ")
    found = False

    for book in books:
        if book["name"].lower() == name.lower():
            print("Book found:")
            print("\nName:", book["name"])
            print("Author:", book["author"])
            print("Year:", book["year"])
            print("Rating:", book["rating"])
            print("Review:", book["review"])

            found = True
            break

    if not found:
        print("Book not found.")


def check_review():
    name = input("Enter book name to check review: ")

    for book in books:
        if book["name"].lower() == name.lower():
            print("Book Review:")
            print("Name:", book["name"])
            print("Rating:", book["rating"])
            print("Review:", book["review"])

            if book["rating"] >= 4:
                print("This book has a good rating!")
            elif book["rating"] >= 3:
                print("This book has an okay rating.")
            else:
                print("This book has a low rating.")

            return

    print("Book not found.")


def highest_rated():
    if len(books) == 0:
        print("No books found.")
        return

    highest_book = books[0]

    for book in books:
        if book["rating"] > highest_book["rating"]:
            highest_book = book

    print("Highest Rated Book:")
    print("Name:", highest_book["name"])
    print("Author:", highest_book["author"])
    print("Rating:", highest_book["rating"])


while True:
    print("Library Management System")
    print("1. Add New Book")
    print("2. View All Books")
    print("3. Search for a Book")
    print("4. Check Book Review")
    print("5. Find Highest Rated Book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        check_review()

    elif choice == "5":
        highest_rated()

    elif choice == "6":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
