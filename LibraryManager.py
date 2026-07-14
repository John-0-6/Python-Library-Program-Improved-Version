from Book import Book

class LibraryManager:

    def __init__(self):
        self.books = []
        self.next_id = 1


    # Add book to books[]
    def add_book(self, title, author, year):
        if not self.books:
            self.next_id = 1

        book = Book(self.next_id, title, author, year)
        self.books.append(book)
        self.next_id += 1


    # Display all books
    def display_books(self):
        if not self.books:
            print("Library is empty.")
            return

        for book in self.books:
            print(book)


    # User search, by book title
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book

        return None


    # Reusable internal book search
    def search(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book

        return None


    # Makes the book.available to False, by book ID
    def borrow_book(self, book_id):
        book = self.search(book_id)

        if book is None:
            print("Book not found.")
            return

        if book.borrow():
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")


    # Makes the book.available = True, by book ID
    def return_book(self, book_id):
        book = self.search(book_id)

        if book is None:
            print("Book not found.")
            return

        if book.return_book():
            print("Book returned.")
        else:
            print("Book is already in the library.")

    # Deletes certain book, by book ID
    def delete_book(self, book_id):
        book = self.search(book_id)

        if book is None:
            print("Book not found.")
            return

        self.books.remove(book)
        print("Book deleted.")