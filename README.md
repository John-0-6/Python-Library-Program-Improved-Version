# Library Management System (Python)

A **console-based Library Management System** built in **Python**.  
This system allows managing books, searching, borrowing, returning, deleting books, and persisting library data using JSON files.

---

## Features

- Add new **Books** with auto-generated IDs
- Display all books in the library
- Search books by **Title**
- Borrow books using their **Book ID**
- Return borrowed books
- Delete books from the library
- **Persistent storage** using JSON (`books.json`) ✅
- Automatically loads saved data when the program starts
- Input validation for invalid menu choices and incorrect input formats

---

## OOP Concepts Used

- Classes & Objects (`Book`, `LibraryManager`, `FileManager`)
- Encapsulation (private object state managed through class methods)
- Class methods (`from_dict`) for recreating objects from JSON data
- Manager class (`LibraryManager`) for handling all library operations
- Service class (`FileManager`) for file handling and data persistence
- Separation of concerns:
  - `Book` handles book data
  - `LibraryManager` manages library operations
  - `FileManager` handles saving and loading
  - `main` handles the user interface
- Collections: `list` for storing book objects
- JSON serialization using dictionaries (`to_dict()`)

---

## Technologies Used

- Python 3
- Built-in `json` module
- Console input/output (`input`, `print`)
- File handling (`open`, `json.load`, `json.dump`)
- Object-Oriented Programming (OOP)

---

## How It Works

1. The program automatically loads saved books from `books.json`.
2. The main menu provides the following options:
   1. Add Book
   2. Display Books
   3. Find Book
   4. Borrow Book
   5. Return Book
   6. Delete Book
   7. Save & Exit

3. Every new book is assigned a unique **Book ID** automatically.
4. Users can search books by **Title**.
5. Books can be borrowed and returned using their **Book ID**.
6. Deleted books are permanently removed from the library.
7. All changes are automatically saved to `books.json`.

---

## Usage

### Clone the repository

```bash
  git clone https://github.com/John-0-6/Library-Management-System-Python.git
  cd Library-Management-System-Python
```

---

### Run the program

```bash
  python main.py
```

---

## File Structure

```text
Library-Management-System-Python/
│
├── main.py
├── Book.py
├── LibraryManager.py
├── FileManager.py
└── books.json
```

---

## Menu Example

```text
1. Add Book
2. Display Books
3. Find Book
4. Borrow Book
5. Return Book
6. Delete Book
7. Save & Exit
```

---

## Example Output

```text
ID: 1 | Title: Harry Potter | Author: J.K. Rowling | Year: 1997 | Status: Available

Book borrowed successfully.

ID: 1 | Title: Harry Potter | Author: J.K. Rowling | Year: 1997 | Status: Borrowed
```

---

## Future Improvements

- Edit book information
- Search books by author
- Sort books by title or publication year
- Display available books only
- Multiple user accounts
- Due dates and overdue tracking
- SQLite database support
- Graphical User Interface (PyQt or Tkinter)

---
