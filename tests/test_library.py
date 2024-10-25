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

if __name__ == "__main__":
    unittest.main()