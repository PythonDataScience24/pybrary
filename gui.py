import gooeypie as gp
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class LibraryGUI:
    """Handles the GUI for the library application."""

    def __init__(self, main_app, library_manager, librarian):
        """
        Initializes the LibraryGUI with the given app and library manager.

        Args:
            pybary (GooeyPieApp): The main GooeyPie application.
            library_manager (LibraryManager): The manager for the library data.
        """
        self.app = main_app
        self.library_manager = library_manager
        self.librarian = librarian

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
        self.button_container = gp.Container(self.tab1)
        self.button_container.set_grid(1, 5)

        self.table = gp.Table(self.tab1, ['Title', 'Author', 'Year', 'Genre', 'Pages', 'Rating', 'Synopsis'])
        self.table.set_column_widths(60, 60, 60, 60, 60, 60, 60)
        self.table.height = 5

        self.overwrite_btn = gp.Button(self.button_container, 'Overwrite Book', self.overwrite_book)
        self.add_btn = gp.Button(self.button_container, 'Add Book', self.add_book)
        self.delete_btn = gp.Button(self.button_container, 'Delete Book', self.delete_book)
        self.search_btn = gp.Button(self.button_container, 'Search', self.search)
        self.clear_btn = gp.Button(self.button_container, 'Clear Fields', self.clear_fields)

        viz_categories = ['Topic', 'Author', 'Rating', 'Trends']
        self.visualize_dd = gp.Dropdown(self.tab2, viz_categories)
        self.visualize_dd.selected_index = 0
        self.visualize_btn = gp.Button(self.tab2, 'GO!', self.visualize)
        self.graph_container = gp.LabelContainer(self.tab2, 'Graph')
        self.graph_container.set_grid(1, 1)
        self.graph_canvas = None

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
        self.tab1.add(self.button_container, 5, 1, column_span=4)
        self.synopsis_container.add(self.synopsis_inp, 1, 1)
        self.button_container.add(self.clear_btn, 1, 1)
        self.button_container.add(self.search_btn, 1, 2)
        self.button_container.add(self.add_btn, 1, 3)
        self.button_container.add(self.delete_btn, 1, 4)
        self.button_container.add(self.overwrite_btn, 1, 5)
        self.table.add_event_listener('select', self.carry_over)
        self.tab1.add(self.table, 6, 1, column_span=4, fill=True, stretch=True)

    def setup_tab2(self):
        """Sets up the Visualization tab."""
        self.tab2.set_grid(4, 1)
        self.tab2.add(gp.Label(self.tab2, 'Visualizations and Analysis'), 1, 1, align='center')
        self.tab2.add(self.visualize_dd, 2, 1, align='center')
        self.tab2.add(self.visualize_btn, 3, 1, align='center')
        self.tab2.add(self.graph_container, 4, 1, fill=True, stretch=True)

    def visualize(self, event):
        """Handles visualization based on the selected category."""
        selected_category = self.visualize_dd.selected
        if selected_category == 'Topic':
            self.visualize_by_topic()
        elif selected_category == 'Author':
            self.visualize_by_author()
        elif selected_category == 'Rating':
            self.visualize_by_rating()
        elif selected_category == 'Trends':
            self.analyze_trends()

    def visualize_by_topic(self):
        """Visualizes the book collection by topic (genre)."""
        genres = {}
        for book in self.library_manager.full_library:
            genre = book[3]
            if genre in genres:
                genres[genre] += 1
            else:
                genres[genre] = 1

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(genres.keys(), genres.values(), color='skyblue')
        ax.set_xlabel('Genre')
        ax.set_ylabel('Number of Books')
        ax.set_title('Number of Books by Genre')
        plt.xticks(rotation=45)
        plt.tight_layout()

        self.display_graph(fig)

    def visualize_by_author(self):
        """Visualizes the book collection by Author."""
        authors = {}
        for book in self.library_manager.full_library:
            author = book[1]
            if author in authors:
                authors[author] += 1
            else:
                authors[author] = 1
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(authors.keys(), authors.values(), color='darkblue')
        ax.set_xlabel('Authors')
        ax.set_ylabel('Number of Books')
        ax.set_title('Number of Books by Author')
        plt.xticks(rotation=45)
        plt.tight_layout()

        self.display_graph(fig)

    def visualize_by_rating(self):
        """Visualizes the book collection by rating."""
        ratings = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
        for book in self.library_manager.full_library:
            rating = book[5]
            if rating in ratings:
                ratings[rating] += 1
            else:
                ratings[rating] = 1

        # Convert the dictionary to a pandas DataFrame to ensure the correct order
        ratings_df = pd.DataFrame(list(ratings.items()), columns=['Rating', 'Count'])
        ratings_df = ratings_df.sort_values(by='Rating')

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(ratings_df['Rating'], ratings_df['Count'], color='lightgreen')
        ax.set_xlabel('Rating')
        ax.set_ylabel('Number of Books')
        ax.set_title('Number of Books by Rating')
        plt.xticks(rotation=45)
        plt.tight_layout()

        self.display_graph(fig)

    def analyze_trends(self):
        """Analyzes trends in book ratings per author per year."""
        author_year_rating = {}
        for book in self.library_manager.full_library:
            author = book[1]
            year = book[2]
            rating = float(book[5])
            if (author, year) in author_year_rating:
                author_year_rating[(author, year)].append(rating)
            else:
                author_year_rating[(author, year)] = [rating]

        trends = {}
        for key, ratings in author_year_rating.items():
            trends[key] = sum(ratings) / len(ratings)

        authors = list(set([key[0] for key in trends.keys()]))
        years = list(set([key[1] for key in trends.keys()]))
        authors.sort()
        years.sort()

        fig, ax = plt.subplots(figsize=(12, 6))
        for author in authors:
            avg_ratings = [trends.get((author, year), 0) for year in years]
            ax.plot(years, avg_ratings, marker='o', label=author)

        ax.set_xlabel('Year')
        ax.set_ylabel('Average Rating')
        ax.set_title('Average Book Ratings per Author per Year')
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        self.display_graph(fig)

    def display_graph(self, fig):
        """Displays the given figure in the graph container."""
        if self.graph_canvas:
            self.graph_canvas.get_tk_widget().destroy()
        self.graph_canvas = FigureCanvasTkAgg(fig, master=self.graph_container)
        self.graph_canvas.draw()
        self.graph_canvas.get_tk_widget().pack(fill='both', expand=True)

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

        b = self.librarian.add_book(title, author, year, genre, pages, rating, synopsis)
        if b:
            self.clear_fields()

    def overwrite_book(self, event):
        selected_index = self.table.selected_row
        if selected_index is not None:
            title = self.title_inp.text
            author = self.author_inp.text
            year = self.year_inp.text
            genre = self.genre_inp.text
            pages = self.pages_inp.text
            rating = self.rating_inp.text
            synopsis = self.synopsis_inp.text

            self.librarian.overwrite_book(title, author, year, genre, pages, rating, synopsis, selected_index)
            self.load_data()

    def delete_book(self, event):
        """Deletes a book from the library."""
        selected_index = self.table.selected_row
        if selected_index is not None:
            title = self.title_inp.text
            author = self.author_inp.text
            year = self.year_inp.text
            genre = self.genre_inp.text
            pages = self.pages_inp.text
            rating = self.rating_inp.text
            synopsis = self.synopsis_inp.text
            book_details = [title, author, year, genre, pages, rating, synopsis]
            self.librarian.delete_book(book_details)
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
