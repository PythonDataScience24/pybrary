"""
GUI module for the pybrary application
"""

import gooeypie as gp
import csv
from popup import Popup


class LibraryGUI:
    """Handles the GUI for the library application."""

    def __init__(self, main_app, library_manager):
        """
        Initializes the LibraryGUI with the given app and library manager.

        Args:
            pybary (GooeyPieApp): The main GooeyPie application.
            library_manager (LibraryManager): The manager for the library data.
        """
        self.app = main_app
        self.library_manager = library_manager

        self.tabs = gp.TabContainer(self.app)
        self.tab1 = gp.Tab(self.tabs, 'View Collection')
        self.tab2 = gp.Tab(self.tabs, 'Visualization')

        # Define instance attributes
        self.title_lbl = gp.Label(self.tab1, 'Title:')
        self.title_inp = gp.Input(self.tab1)
        self.author_lbl = gp.Label(self.tab1, 'Author:')
        self.author_inp = gp.Input(self.tab1)
        self.year_lbl = gp.Label(self.tab1, 'Year:')
        self.year_inp = gp.Input(self.tab1)
        self.genre_lbl = gp.Label(self.tab1, 'Genre:')
        self.genre_inp = gp.Input(self.tab1)
        self.pages_lbl = gp.Label(self.tab1, 'Page Count:')
        self.pages_inp = gp.Input(self.tab1)
        self.rating_lbl = gp.Label(self.tab1, 'Rating:')
        self.rating_inp = gp.Input(self.tab1)
        self.synopsis_container = gp.LabelContainer(self.tab1, 'Synopsis:')
        self.synopsis_container.set_grid(1, 1)
        self.synopsis_inp = gp.Textbox(self.synopsis_container, 70)

        self.table = gp.Table(self.tab1, ['Title', 'Author', 'Year', 'Genre', 'Pages', 'Rating', 'Synopsis'])
        self.table.set_column_widths(60, 60, 60, 60, 60, 60, 60)
        self.table.height = 5

        self.add_btn = gp.Button(self.tab1, 'Add Book', self.add_book)
        self.delete_btn = gp.Button(self.tab1, 'Delete Book', self.delete_book)
        self.search_btn = gp.Button(self.tab1, 'Search', self.search)
        self.clear_btn = gp.Button(self.tab1, 'Clear Fields', self.clear_fields)

        self.setup_tab1()
        self.setup_tab2()

        self.tabs.add(self.tab1)
        self.tabs.add(self.tab2)

        self.app.set_grid(1, 1)
        self.app.add(self.tabs, 1, 1, fill=True, stretch=True)

        self.load_data()

    def setup_tab1(self):
        """Sets up the View Collection tab."""
        self.tab1.set_grid(6, 4)

        # Add input fields to tab1
        self.tab1.add(self.title_lbl, 1, 1)
        self.tab1.add(self.title_inp, 1, 2)
        self.tab1.add(self.author_lbl, 1, 3)
        self.tab1.add(self.author_inp, 1, 4)
        self.tab1.add(self.year_lbl, 2, 1)
        self.tab1.add(self.year_inp, 2, 2)
        self.tab1.add(self.genre_lbl, 2, 3)
        self.tab1.add(self.genre_inp, 2, 4)
        self.tab1.add(self.pages_lbl, 3, 1)
        self.tab1.add(self.pages_inp, 3, 2)
        self.tab1.add(self.rating_lbl, 3, 3)
        self.tab1.add(self.rating_inp, 3, 4)
        self.tab1.add(self.synopsis_container, 4, 1, column_span=4)
        self.synopsis_container.add(self.synopsis_inp, 1, 1)

        self.table.add_event_listener('select', self.carry_over)
        self.tab1.add(self.table, 6, 1, column_span=4, fill=True, stretch=True)

        # Add buttons to tab1
        self.tab1.add(self.clear_btn, 5, 1)
        self.tab1.add(self.search_btn, 5, 2)
        self.tab1.add(self.add_btn, 5, 3)
        self.tab1.add(self.delete_btn, 5, 4)

    def setup_tab2(self):
        """Sets up the Visualization tab."""
        self.tab2.set_grid(1, 1)
        self.tab2.add(gp.Label(self.tab2, 'This is the second tab'), 1, 1, align='center', valign='middle')

    def clear_fields(self, event=None):
        """Clears the input fields."""
        self.title_inp.clear()
        self.author_inp.clear()
        self.year_inp.clear()
        self.genre_inp.clear()
        self.pages_inp.clear()
        self.rating_inp.clear()
        self.synopsis_inp.clear()
        self.load_data()

    def add_book(self, event):
        """Adds a book to the library."""
        title = self.title_inp.text
        author = self.author_inp.text
        year = self.year_inp.text
        genre = self.genre_inp.text
        pages = self.pages_inp.text
        rating = self.rating_inp.text
        synopsis = self.synopsis_inp.text

        if not (title and author and year and pages and genre and rating and synopsis.strip()):
            Popup.show_error("All fields must be filled in.")
            return

        # Validate numeric inputs
        try:
            if not self.is_valid_int(year):
                raise ValueError("Invalid input: Please enter a valid integer for year.")
            if not self.is_valid_int(pages):
                raise ValueError("Invalid input: Please enter a valid integer for page count.")
            if not self.is_valid_float(rating):
                raise ValueError("Invalid input: Please enter a valid float for rating.")
            if not (1 <= float(rating) <= 5):
                raise ValueError("Invalid rating: Please enter a number between 1 and 5.")
        except ValueError as e:
            Popup.show_error(str(e))
            return

        book_details = [title, author, year, genre, pages, rating, synopsis]

        self.library_manager.add_book(book_details)
        self.clear_fields()

    def delete_book(self, event):
        """Deletes a book from the library."""
        selected_index = self.table.selected_row
        if selected_index is not None:
            del self.library_manager.full_library[selected_index]
            self.save_data()
            self.load_data()

    def search(self, event):
        """Searches for books in the library."""
        title_search = self.title_inp.text
        author_search = self.author_inp.text
        genre_search = self.genre_inp.text

        search_results = self.library_manager.search_books(title_search, author_search, genre_search)

        self.table.clear()
        for row in search_results:
            self.table.add_row(row)

    def carry_over(self, event):
        """Carries over the selected book details to the input fields."""
        selected_row = self.table.selected
        if selected_row:
            self.title_inp.text = selected_row[0]
            self.author_inp.text = selected_row[1]
            self.year_inp.text = selected_row[2]
            self.genre_inp.text = selected_row[3]
            self.pages_inp.text = selected_row[4]
            self.rating_inp.text = selected_row[5]
            self.synopsis_inp.text = selected_row[6]

    def load_data(self):
        """Loads the library data into the table."""
        self.table.clear()
        for row in self.library_manager.full_library:
            self.table.add_row(row)

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

    def save_data(self):
        """Saves the library data to a CSV file."""
        try:
            with open('library.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(self.library_manager.full_library)
        except Exception as e:
            print(f"Error saving data: {e}")
