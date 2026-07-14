from LibraryManager import LibraryManager
from FileManager import FileManager

library = LibraryManager()
file_manager = FileManager()
file_manager.load(library)


# Main menu
def menu():
    print("1. Add Book")
    print("2. Display Books")
    print("3. Find Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Save & Exit")


# Add book title, book author, and book year
def add_book():
    title = input("Title: ").capitalize()
    author = input("Author: ").capitalize()
    year = int(input("Year: "))

    library.add_book(title, author, year)


# Search book, with book title
def find_book():
    title = input("Title: ").capitalize()

    book = library.find_book(title)

    if book:
        print(book)
    else:
        print("Book not found.")


# Borrow book, with book ID
def borrow_book():
    book_id = int(input("ID: "))

    library.borrow_book(book_id)


# Return book, with book ID
def return_book():
    book_id = int(input("ID: "))

    library.return_book(book_id)


# Delete book, with book ID
def delete_book():
    book_id = int(input("ID: "))

    library.delete_book(book_id)


# Save library
def save():
    file_manager.save(library)


# Main program
def main():
    while True:
        menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter a valid choice. (Numbers 1-7 ONLY)")
            continue

        if choice < 1 or choice > 7:
            print("Enter a valid choice. (Numbers 1-7 ONLY)")
            continue

        match choice:
            # Add book
            case 1:
                add_book()
                save()

            # Display all books
            case 2:
                library.display_books()


            # Search book
            case 3:
                find_book()


            # Borrow book
            case 4:
                borrow_book()
                save()


            # Return book
            case 5:
                return_book()
                save()


            # Delete book
            case 6:
                delete_book()
                save()


            # Save and exit
            case 7:
                save()
                break


if __name__ == "__main__":
    main()