# Base class
class Item:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")


# Derived class: Book
class Book(Item):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def display_info(self):
        print("Book:")
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Author: {self.author}")
        print("-" * 20)


# Derived class: Magazine
class Magazine(Item):
    def __init__(self, title, year, issue_number):
        super().__init__(title, year)
        self.issue_number = issue_number

    def display_info(self):
        print("Magazine:")
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Issue Number: {self.issue_number}")
        print("-" * 20)


# List to store items
library_items = []

# Menu system
while True:
    print("\nLibrary System")
    print("1. Add a Book")
    print("2. Add a Magazine")
    print("3. Show all items")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter book title: ")
        year = input("Enter publication year: ")
        author = input("Enter author: ")

        book = Book(title, year, author)
        library_items.append(book)

    elif choice == "2":
        title = input("Enter magazine title: ")
        year = input("Enter publication year: ")
        issue = input("Enter issue number: ")

        magazine = Magazine(title, year, issue)
        library_items.append(magazine)

    elif choice == "3":
        if not library_items:
            print("No items in the library.")
        else:
            print("\nLibrary Items:")
            for item in library_items:
                item.display_info()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid option. Please try again.")
