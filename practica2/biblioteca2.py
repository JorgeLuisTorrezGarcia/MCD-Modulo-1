class Item:
    def __init__(self, title:str, year:int):
        self.title = title
        self.year = year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")

class Book(Item):
    def __init__(self,title:str, year:int, author:str):
        super().__init__(title, year)
        self.author = author
        
    def display_info(self):
        print("     BOOK: ")
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Author: {self.author}")
        print(" ************************** \n")

class Magazine(Item):
    def __init__(self,title:str, year:int,issue_number:int):
        super().__init__(title,year)
        self.issue_number = issue_number
    
    def display_info(self):
        print("     Magazine: \n")
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Issue number: {self.issue_number}")
        print(" ************************** \n")

def main():


    items:list[Item] = []

    while True:
        print("Library System \n")
        print("1. Add a Book")
        print("2. Add a Magazine")
        print("3. Show all items")
        print("4. Exit")

        option= input("\n opcion: \n")

        if option == "1":
            print("Inter data: \n")
            title = input("Title: ")
            year = int(input("Year: "))
            author = input("Author: ")

            book_new = Book(title,year,author)
            items.append(book_new)

        elif option == "2":
            print("Enter data: \n")    
            title = input("Title: ")
            year = int(input("Year: "))
            issue_number = int(input("Issue Number: "))
            magazine_new = Magazine(title,year,issue_number)
            items.append(magazine_new)

        elif option == "3":
            print("ITEMS: \n")
            for item in items:
                item.display_info()

        elif option == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please try again.")

main()