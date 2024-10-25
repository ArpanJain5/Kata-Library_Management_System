import unittest
from library_management.library import Library  # Import the Library class from the main code

class TestLibrary(unittest.TestCase):

    def test_add_book(self):
        """Test adding a book to the library."""
        library = Library()
        library.add_book(1,"The Jungle Book", "Rudyard Kipling", 3)
        self.assertIn(1, library.books)  # Check if the book is added
        self.assertEqual(library.books[1], ["The Jungle Book", "Rudyard Kipling", 3])  # Verify book details

    def test_view_books(self):
        """Test viewing all books in the library."""
        library = Library()
        library.add_book(1, "The Jungle Book", "Rudyard Kipling", 3)
        self.assertEqual(len(library.books), 1)  # Should have 1 book in the library

    def test_borrow_book_success(self):
        """Test borrowing a book successfully."""
        library = Library()
        library.add_book(1, "The Jungle Book", "Rudyard Kipling", 3)
        library.borrow_book(1)
        self.assertEqual(library.books[1][2], 2)  # Copies should decrease by 1

if __name__ == "__main__":
    unittest.main()