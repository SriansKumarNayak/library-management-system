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


books = []

while True:
    print("\n===== Library Management System =====\n")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    while True:
        try:
            choice = int(input("Enter choice (1-5): "))
            break
        except ValueError:
            print("\nChoose from the number (1-5) only...\n")

    # ADD BOOK
    if choice == 1:
        print("\n--- Add Book ---")
        print("---------------------------------")

        while True:
            title = input("Enter Book Title: ").strip()
            if title:
                break
            print("\nTitle cannot be empty!\n")

        while True:
            author = input("Enter Author Name: ").strip()
            if author:
                break
            print("\nAuthor name cannot be empty!\n")

        books.append(Book(title, author))

        print("\n---------------------------------")
        print("✅ Book Added Successfully!")
        print(f"ID     : {books[-1].book_id}")
        print(f"Title  : {books[-1].title}")
        print(f"Author : {books[-1].author}")
        print("---------------------------------")

    elif choice == 2:
        if not books:
            print("No Record Found!")
        else:
            print("\n--- Book Records ---")
            print("--------------------------------------------------")
            for book in books:
                book.display()
                print("--------------------------------------------------")

    elif choice == 3:
        print("\n--- Issue Book ---")
        print("--------------------------------------------------")

        title = input("Enter Book Title: ").strip().lower()

        matches = []
        for book in books:
            if book.title.lower() == title:
                matches.append(book)

        if not matches:
            print("No book found with that title.")
        else:
            print("\nMatching Books:")
            print("--------------------------------------------------")
            for book in matches:
                book.display()
            print("--------------------------------------------------")

            try:
                book_id = int(input("Enter Book ID to issue: "))
            except ValueError:
                print("Invalid ID!")
                continue

            found = False
            for book in matches:
                if book.book_id == book_id:
                    if book.status == "Issued":
                        print("Book is already issued!")
                    else:
                        book.status = "Issued"
                        print(f"Book issued successfully! (ID: {book.book_id})")
                    found = True
                    break

            if not found:
                print("Invalid Book ID selected.")

    elif choice == 4:
        print("\n--- Return Book ---")
        print("--------------------------------------------------")

        try:
            book_id = int(input("Enter Book ID to return: "))
        except ValueError:
            print("Invalid ID!")
            continue

        found = False
        for book in books:
            if book.book_id == book_id:
                if book.status == "Available":
                    print("Book is already available!")
                else:
                    book.status = "Available"
                    print("Book returned successfully!")
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == 5:
        print("\nExiting program...\n")
        break

    else:
        print("\nInvalid choice! Please select from 1 to 5.\n")