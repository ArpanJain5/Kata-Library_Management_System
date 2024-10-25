# Library Management System:

This project is a simple Library Management System built using Python. It allows users to add books, borrow books, return them, and view available books. The system ensures clean code, follows Test-Driven Development (TDD), and adheres to best practices.


# Features:

Add Books: Add books to the library with a unique book ID, title, author, and the number of copies.
Borrow Books: Borrow a book if it's available.
Return Books: Return a previously borrowed book.
View Available Books: View all books currently available in the library.


# Requirements:

pytest==6.2.4


# Installation and Setup

1. Clone the repository:
```
    git clone https://github.com/ArpanJain5/Kata.git
```
2. Navigate to the project directory:
```
    cd Kata
```
3. Install any dependencies (if needed):
```
    pip install -r requirements.txt
```


# Usage:
To add a book:
```
library.add_book(book_id, title, author, copies)
```

To run the unit tests:
```
python -m unittest discover
```


#Testing
The project follows TDD, so tests for each feature are written in test_library.py.
Run all tests using:
```
python -m unittest discover
```
