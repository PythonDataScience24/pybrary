import csv


class Librarian:
    """handles the books for the library
        is responsible for manipulation of books (add, delete, overwrite)
    """

    def __init__(self, main_app, library_manager):
        self.library_manager = library_manager
        self.app = main_app

    def add_book(self, title, author, year, genre, pages, rating, synopsis):
        if self.check_inputs(title, author, year, genre, pages, rating, synopsis):
            return
        book_details = [title, author, year, genre, pages, rating, synopsis]
        self.library_manager.add_book(book_details)

    def overwrite_book(self, title, author, year, genre, pages, rating, synopsis, selected_index):
        if self.check_inputs(title, author, year, genre, pages, rating, synopsis):
            return
        book_details = [title, author, year, genre, pages, rating, synopsis]
        self.library_manager.full_library[selected_index] = book_details
        self.save_data()

    def delete_book(self, book_details):
        self.library_manager.delete_book(book_details)
        self.save_data()

    def check_inputs(self, title, author, year, genre, pages, rating, synopsis):
        # make sure every field has input
        if not (title.strip() != '' or author.strip() != '' or year or pages or genre or rating or synopsis.strip()):
            self.app.alert("Invalid input", "Please fill in all fields", "error")
            return True
        # check numeric input
        try:
            if not self.is_valid_int(year):
                self.app.alert("Invalid input", "You've entered non-numbers in Year. Please enter valid numbers.",
                               "error")
                return True
            if not self.is_valid_int(pages):
                self.app.alert("Invalid input", "You've entered non-numbers in Pages. Please enter valid numbers.",
                               "error")
                return True
            if not self.is_valid_float(rating):
                self.app.alert("Invalid input", "You've entered non-numbers in Rating. Please enter valid numbers.",
                               "error")
                return True
            if not (1 <= float(rating) <= 5):
                self.app.alert("Invalid input", "Invalid rating: Please enter a number between 1 and 5.", "error")
                return True
        except ValueError as e:
            self.app.alert('Error', str(e), 'error')
            return True

    def save_data(self):
        """Saves the library data to a CSV file."""
        try:
            with open('library.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(self.library_manager.full_library)
        except Exception as e:
            print(f"Error saving data: {e}")

    @staticmethod
    def is_valid_int(value):
        """Checks if the value is a valid integer."""
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_float(value):
        """Checks if the value is a valid float."""
        try:
            float(value)
            return True
        except ValueError:
            return False
