import json
from Book import Book


class FileManager:


    # Append book.to_dict(), to make it a dictionary, to data[]. And then save json
    def save(self, library):
        data = []

        for book in library.books:
            data.append(book.to_dict())

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)


    # Load json file to data, then for each item in data convert into set, then loading it in the library.books[]
    def load(self, library):
        try:
            with open("books.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return

        library.books.clear()

        highest_id = 0

        for item in data:
            book = Book.from_dict(item)

            library.books.append(book)

            if book.id > highest_id:
                highest_id = book.id

        library.next_id = highest_id + 1