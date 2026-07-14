class Book:


    def __init__(self,book_id, title, author, year, available=True):
        self.id = book_id
        self.title = title.capitalize()
        self.author = author.capitalize()
        self.year = year
        self.available = True


    # If self.available is True, make it False. Return True. Otherwise, False
    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False


    # If self.available is False, make it True. Return True. Otherwise, False
    def return_book(self):
        if not self.available:
            self.available = True
            return True
        return False


    # Book dictionary for saving
    def to_dict(self):
        return {
                "id": self.id,
                "title": self.title,
                "author": self.author,
                "year": self.year,
                "available": self.available,
        }


    # Converting json into set, and then load to library.books[]
    @classmethod
    def from_dict(cls, item):
        return cls(
            item["id"],
            item["title"],
            item["author"],
            item["year"],
            item["available"]
        )


    # Print format
    def __str__(self):
        status = "Available" if self.available else "Borrowed"

        return f"ID: {self.id} | Title:{self.title} | Author:{self.author} | Year:{self.year} | Status: {status}"