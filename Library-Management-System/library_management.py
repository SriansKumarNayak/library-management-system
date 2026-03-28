import json
class Book:

    book_id_counter = 101

    def __init__(self, title, author):
        self.book_id = Book.book_id_counter
        self.title = title
        self.author = author
        self.status = "Available"
        Book.book_id_counter += 1

    def display(self):
        print(f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {self.status}")

def save_books():
    data = []

    for book in books:
        data.append({
            "book_id" : book.book_id,
            "title" : book.title,
            "author" : book.author,
            "status" : book.status
        })
        
    with open("books.json", "w") as file:
        json.dump(data, file, indent=4)

def load_books():
    try:
        with open("books.json", "r") as file:
            data = json.load(file)

            for item in data:
                b = Book(item(["title"], item["author"]))
                b.book_id = item["book_id"]
                b.status = item["status"]
                books.append(b)

            if books:
                Book.book_id_counter = books[-1].book_id + 1

    except (FileNotFoundError, json.JSONDecodeError):
        pass

books = []
load_books()

while True:
    print("\n===== Library Management System =====\n")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            break
        except ValueError:
            print("\nChoose from the number (1-5) only...\n")

    if choice == 1:
        print("\n===== Add Books =====\n")
        while True:
            title = input("Enter Title: ").strip()
            if title:
                break
            else:
                print("\nTitle cannot be empty...\n")

        while True:
            author = input("Enter Name of Auhtor: ").strip()
            if author:
                break
            else:
                print("\nAuthor cannot be empty...\n")

        books.append(Book(title, author))
        save_books()
        print("----------------------------------")
        print("Book added successfully!")
        print(f"Book ID: {books[-1].book_id}")
        print(f"Title: {books[-1].title}")
        print(f"Author: {books[-1].author}")
        print("----------------------------------")

    elif choice == 2:
        if not books:
            print("No Record Found!")
        else:
            print("\n--- Book Records ---\n")
            print("----------------------------------------------------------------------")
            for book in books:
                book.display()
                print("----------------------------------------------------------------------") 

    elif choice == 3:
        print("\n===== Issue Book =====\n")
        matches = []
        while True:
            search_title = input("Enter Title to Issue: ").strip()
            if search_title:
                break
            else:
                print("\nTitle cannot be empty!\n")
            
        for book in books:
            if book.title.lower() == search_title.lower():
                matches.append(book)
                
        if not matches:
            print("No book found with that title")
        else:
            print("\nMatches Found: ")
            print("----------------------------------------------------------------------")
            for book in matches:
                book.display()
                print("----------------------------------------------------------------------")
            print("\n")
            while True:    
                try:
                    ID_input = int(input("Enter Book ID to Issue (or type '0' to cancle): "))
                    if ID_input == 0:
                        break
                    ID = ID_input
                except ValueError:
                    print("Invalid ID!")
                    continue

                found = False
                for book in matches:
                    if book.book_id == ID:
                        if book.status == "Issued":
                            print("Book is already Issued")
                        else:
                            book.status = "Issued"
                            save_books()
                            print(f"\nBook Issued Successfully! (ID: {book.book_id})\n")
                        found = True
                        break
                if found:
                    break   
                else:
                    print("\nInvalid Book ID selected.\n")
                

    elif choice == 4:
        print("\n===== Return Book =====\n")
        while True:    
            try:
                ID_input = int(input("Enter Book ID to Return (or type '0' to cancle): "))
                if ID_input == 0:
                    break
                ID = ID_input
            except ValueError:
                print("Invalid ID!")
                continue
        
            found = False
            for book in books:
                if book.book_id == ID:
                    if book.status == "Available":
                        print("\nBook is already available.\n")
                    else:
                        book.status = "Available"
                        save_books()
                        print("\nBook Returned Successfully!")
                    found = True
                    break
            if found:
                break
            else:
                print("\nInvalid Book ID selected.\n")
        
    elif choice == 5:
        print("\nExiting Program... Goodbye!\n")
        break

    else:
        print("\nInvalid choice! Please select from 1 to 5.\n")