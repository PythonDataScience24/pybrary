import gooeypie as gp


class LibraryGUI:
    def __init__(self, app, library_manager):
        self.app = app
        self.library_manager = library_manager

        self.tabs = gp.TabContainer(self.app)
        self.tab1 = gp.Tab(self.tabs, 'View Collection')
        self.tab2 = gp.Tab(self.tabs, 'Visualization')

        self.setup_tab1()
        self.setup_tab2()

        self.tabs.add(self.tab1)
        self.tabs.add(self.tab2)

        self.app.set_grid(1, 1)
        self.app.add(self.tabs, 1, 1, fill=True, stretch=True)

        self.load_data()

    def setup_tab1(self):
        self.tab1.set_grid(6, 4)

        # Create input fields for book details
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

        self.table = gp.Table(self.tab1, ['Title', 'Author', 'Year', 'Genre', 'Pages', 'Rating', 'Synopsis'])
        self.table.set_column_widths(60, 60, 60, 60, 60, 60, 60)
        self.table.height = 5
        self.table.add_event_listener('select', self.carry_over)
        self.tab1.add(self.table, 6, 1, column_span=4, fill=True, stretch=True)

        # Create buttons
        self.add_btn = gp.Button(self.tab1, 'Add Book', self.add_book)
        self.delete_btn = gp.Button(self.tab1, 'Delete Book', self.delete_book)
        self.search_btn = gp.Button(self.tab1, 'Search', self.search)
        self.clear_btn = gp.Button(self.tab1, 'Clear Fields', self.clear_fields)

        # Add buttons to tab1
        self.tab1.add(self.clear_btn, 5, 1)
        self.tab1.add(self.search_btn, 5, 2)
        self.tab1.add(self.add_btn, 5, 3)
        self.tab1.add(self.delete_btn, 5, 4)

    def setup_tab2(self):
        self.tab2.set_grid(1, 1)
        self.tab2.add(gp.Label(self.tab2, 'This is the second tab'), 1, 1, align='center', valign='middle')

    def clear_fields(self, event=None):
        self.title_inp.clear()
        self.author_inp.clear()
        self.year_inp.clear()
        self.genre_inp.clear()
        self.pages_inp.clear()
        self.rating_inp.clear()
        self.synopsis_inp.clear()
        self.load_data()

    def add_book(self, event):
        book_details = [
            self.title_inp.text, self.author_inp.text, self.year_inp.text, self.genre_inp.text,
            self.pages_inp.text, self.rating_inp.text, self.synopsis_inp.text
        ]

        if any(book_details):
            self.library_manager.add_book(book_details)
            self.clear_fields()

    def delete_book(self, event):
        selected_row = self.table.selected
        if selected_row:
            self.library_manager.delete_book(selected_row)
            self.load_data()

    def search(self, event):
        title_search = self.title_inp.text
        author_search = self.author_inp.text
        genre_search = self.genre_inp.text

        search_results = self.library_manager.search_books(title_search, author_search, genre_search)

        self.table.clear()
        for row in search_results:
            self.table.add_row(row)

    def carry_over(self, event):
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
        self.table.clear()
        for row in self.library_manager.full_library:
            self.table.add_row(row)