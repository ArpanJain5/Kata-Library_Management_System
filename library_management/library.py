class Library:
    def __init__(self):
        self.books = {}  # Dictionary initiated

    def add_book(self, book_id, title, author, copies):
        """Add a book to the library."""
        if book_id in self.books:
            self.books[book_id][2] += copies  # Update number of copies if book exists
        else:
            self.books[book_id] = [title, author, copies]  # Add new book
