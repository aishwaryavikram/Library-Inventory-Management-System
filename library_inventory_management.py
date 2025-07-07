def initialise_inventory():
    library_inventory = {
        "B101" : {
            "title": "Harry Potter",
            "author" : "JK Rowling",
            "year_published" : 1999,
            "copies_available" : 5
        },
        "B102": {
            "title": "Introduction to Algorithms",
            "author": "Thomas H. Cormen",
            "year_published": 2009,
            "copies_available": 2
        },
        "B103": {
            "title": "Effective Java",
            "author": "Joshua Bloch",
            "year_published": 2017,
            "copies_available": 3
        },
        "B104" : {
            "title": "Harry Potter 2",
            "author" : "JK Rowling",
            "year_published" : 2001,
            "copies_available" : 8
        },
        
    }
    print(library_inventory)
    return library_inventory

def search_isbn(inventory):
    chose_isbn = input("Enter the ISBN that you want to search for: ")
    book = inventory.get(chose_isbn)
    if book:
        print(f"Book found for ISBN: {chose_isbn}")
        print(f" Titile: {book["title"]}")
        print(f" Author: {book["author"]}")
        print(f" Year Published: {book["year_published"]}")
        print(f" Copies Available: {book["copies_available"]}\n")
    else:
        print("Book with ISBN: {chose_isbn} is not in our databse.\n")

def search_author(inventory):
    chose_author = input("Enter the author name to search: ")
    matched_books = []
    for isbn,info in inventory.items():
        if chose_author ==  info["author"]:
            matched_books.append((isbn,info["title"]))
        if len(matched_books) == 0:
            print("There are no books by this author.")
        else:
            print(f"Books by {chose_author}: \n")
            for isbn, title in matched_books:
                print(f"ISBN :{isbn} | Title :{title}")
            print("That is all !\n")
    


def display_books(inventory):
    if len(inventory) == 0:
        print("There are no books in inventory.")
        return 
    
    print("\nAll books in the library:\n ")
    for isbn, info in inventory.items():
        print(f"ISBN: {isbn}")
        print(f" Titile: {info["title"]}")
        print(f" Author: {info["author"]}")
        print(f" Year Published: {info["year_published"]}")
        print(f" Copies Available: {info["copies_available"]}\n")
    print("That's all the books we have!\n")
    


def add_book(inventory):
    
    isbn = input("Enter new book's ISBN: ")
    if isbn in inventory:
        print(f"ISBN {isbn} already exists—cannot add duplicate")
        return
    
    title = input("Enter new book's title: ")
    author = input("Enter new book's author: ")
    try:
        year_published = int(input("Enter new book's year published(e.g. 2020): "))
    except :
        print("\nInvalid year. Please enter a valid published year only\n")
        return


    try:
        copies_available = int(input("Enter new book's number of copies available: "))
    except:
        print("\nError. Invalid value. Please enter a valid number.")
        return
    
    if copies_available > 0:
        inventory[isbn]={
            "title": title, 
            "author" : author,
            "year_published" : year_published,
            "copies_available" : copies_available
        }
    else: 
        print("\n Only positive number of copies available value accepted.")
        return
    print(f"Book {title} added under ISBN {isbn}.")



def  remove_book(inventory):
    removeBook = input("Enter the ISBN for the book you would like to remove.")
    if removeBook in inventory:
        title = inventory[removeBook]["title"]
        inventory.pop(removeBook)
        print(f"ISBN {removeBook} {title} removed from collection.")
    else:
        print(f"Cannot remove: ISBN not in collection.")
       
    


def update_copies(inventory):
    isbn_number = input("Enter ISBN number that you want to update the number of copies for.")
    if isbn_number in inventory:
        copies = input("What is the new number of copies available for this book?")
        if copies.isdecimal():
            inventory[isbn_number]["copies_available"] = copies
            print(f"Copies for ISBN {isbn_number} updated to {copies}.")
        else:
            print(f"Cannot update: ISBN {isbn_number} because not valid integer value of the book.")
            return

    else:
        print("Cannot update: ISBN {isbn_number} not found.")


def low_stock_books(inventory):
    lowstocknum = 0
    for isbn,book in inventory.items():
        lowStock = book["copies_available"]
        if lowStock < 3:
            lowstocknum+=1
            print(f"ISBN {isbn} | Title: {book["title"]} | Copies: {book["copies_available"]}")
    if lowstocknum == 0:
        print("All books have sufficient stock")



def total_books(inventory):
    totalBooks = 0
    for book in inventory.values():  
       
        totalBooks = totalBooks + book["copies_available"]
    if totalBooks > 0:
        print(f"Total books in inventory: {totalBooks}.")
    else:
        print("Collection is empty.")


        

def main():
    inventory = initialise_inventory()
    
    while True:
        print("Library Inventory Menu:")
        print("1. Display all books")
        print("2. Search by ISBN")
        print("3. Search by author")
        print("4. Add a new book")
        print("5. Update number of copies")
        print("6. Remove a book")
        print("7. List all ISBNs/titles/authors")
        print("8. List low-stock books")
        print("9. Show total book count")
        print("q. Quit")

        # ask user a question here
        choice = input("Choose your option: ")
        if choice == "1":
            display_books(inventory)
        elif choice == "2":
            search_isbn(inventory)
        elif choice == "3":
            search_author(inventory)
        elif choice == "4":
            add_book(inventory)
        elif choice == "5":
            update_copies(inventory)
        elif choice == "6":
            remove_book(inventory)
        elif choice == "7":
            initialise_inventory()
        elif choice == "8":
            low_stock_books(inventory)
        elif choice == "9":
            total_books(inventory)
        elif choice == "q":
            break
            

main()
