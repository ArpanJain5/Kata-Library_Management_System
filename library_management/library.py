class Library:
    def __init__(self):
        self.books = {}  # Dictionary initiated

    def add_book(self, book_id, title, author, copies):
        """Add a book to the library."""
        if book_id in self.books:
            self.books[book_id][2] += copies  # Update number of copies if book exists
        else:
            self.books[book_id] = [title, author, copies]  # Add new book

    def view_books(self):
        """View all books in the library."""
        return self.books  # Simply return the books dictionary
    
    def borrow_book(self, book_id):
        """Borrow a book from the library if available."""
        if book_id in self.books and self.books[book_id][2] > 0:
            self.books[book_id][2] -= 1  # Decrease available copies by 1
        else:
            "Book is not available in library"

    def return_book(self, book_id):
        """Return a borrowed book to the library."""
        if book_id in self.books:
            self.books[book_id][2] += 1  # Increase available copies by 1