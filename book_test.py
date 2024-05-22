import unittest
from library_manager import LibraryManager


class TestLibraryManager(unittest.TestCase):

    def setUp(self):
        self.manager = LibraryManager()
        self.manager.full_library = [
            ["The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "Novel"],
            ["To Kill a Mockingbird", "Harper Lee", "Fiction", "Novel"],
            ["1984", "George Orwell", "Fiction", "Dystopian"],
            ["The Catcher in the Rye", "J.D. Salinger", "Fiction", "Novel"]
        ]

    def test_search_books_by_title(self):
        result = self.manager.search_books("The gREAT Gatsby", "", "")
        expected = [["The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "Novel"]]
        self.assertEqual(result, expected, "Should find 'The Great Gatsby' by title")

    def test_search_books_by_author(self):
        result = self.manager.search_books("", "HARPER Lee", "")
        expected = [["To Kill a Mockingbird", "Harper Lee", "Fiction", "Novel"]]
        self.assertEqual(result, expected, "Should find 'To Kill a Mockingbird' by author")

    def test_search_books_by_genre(self):
        result = self.manager.search_books("", "", "dystopian")
        expected = [["1984", "George Orwell", "Fiction", "Dystopian"]]
        self.assertEqual(result, expected, "Should find '1984' by genre")

    def test_search_books_no_match(self):
        result = self.manager.search_books("Nonexistent Title😀", "", "")
        expected = []
        self.assertEqual(result, expected, "Should return an empty list when no match is found")

# The following two tests were added additionally since we ran into problems with these two functions
    def test_add_book(self):
        new_book = ["Brave New World", "Aldous Huxley", "Fiction", "Dystopian"]
        self.manager.add_book(new_book)
        self.assertIn(new_book, self.manager.full_library, "Should add 'Brave New World' to the library")

    def test_delete_book(self):
        book_to_delete = ["1984", "George Orwell", "Fiction", "Dystopian"]
        self.manager.delete_book(book_to_delete)
        self.assertNotIn(book_to_delete, self.manager.full_library, "Should delete '1984' from the library")


if __name__ == '__main__':
    unittest.main()
