import gooeypie as gp
import csv

pybrary = gp.GooeyPieApp('pybrary')

full_library = []

# Create tab container
tabs = gp.TabContainer(pybrary)

# Create tabs
tab1 = gp.Tab(tabs, 'View Collection')
tab2 = gp.Tab(tabs, 'Visualization')

#region Tab1
tab1.set_grid(6, 4)

def clear_fields(event):

    # Clear input fields
    title_inp.clear()
    author_inp.clear()
    year_inp.clear()
    pages_inp.clear()
    genre_inp.clear()
    rating_inp.clear()
    synopsis_inp.clear()

    # Reset search
    load_data()

def add_book(event):
    # Get input values
    title = title_inp.text
    author = author_inp.text
    year = year_inp.text
    pages = pages_inp.text
    genre = genre_inp.text
    rating = rating_inp.text
    synopsis = synopsis_inp.text

    # If all fields are empty, do nothing
    if not (title or author or year or pages or genre or rating or synopsis.strip()):
        return

    # Add new row to table
    full_library.append([title, author, year, genre, pages, rating, synopsis])

    clear_fields(event)
    save_data()
    
def delete_book(event):

    selected_row = table.selected
    if selected_row:
        full_library.remove(selected_row)
        save_data()
        clear_fields(event)

def save_data():
    try:
        with open('library.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(full_library)
    except Exception as e:
        print(f"Error saving data: {e}")

def load_csv():
    table.clear()
    try:
        with open('library.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                full_library.append(row)
    except FileNotFoundError:
        pass  # It's okay if the file doesn't exist

def load_data():
    table.clear()
    for row in full_library:
        table.add_row(row)

def search(event):
    # Fetch data to search with
    title_search = title_inp.text
    author_search = author_inp.text
    year_search = year_inp.text
    genre_search = genre_inp.text
    pages_search = pages_inp.text
    rating_search = rating_inp.text
    synopsis_search = synopsis_inp.text

    search_results = []

    for row in full_library:
        if ((not title_search or title_search in row[0]) and
            (not author_search or author_search in row[1]) and
            (not year_search or year_search in row[2]) and
            (not genre_search or genre_search in row[3]) and
            (not pages_search or pages_search in row[4]) and
            (not rating_search or rating_search in row[5]) and
            (not synopsis_search or synopsis_search in row[6])):
            search_results.append(row)

    table.clear()

    for row in search_results:
        table.add_row(row)

def carry_over(event):
    selected_row = table.selected
    if selected_row:
        title_inp.text = selected_row[0]
        author_inp.text = selected_row[1]
        year_inp.text = selected_row[2]
        genre_inp.text = selected_row[3]
        pages_inp.text = selected_row[4]
        rating_inp.text = selected_row[5]
        synopsis_inp.text = selected_row[6]

# Create input fields for book details
title_lbl = gp.Label(tab1, 'Title:')
title_inp = gp.Input(tab1)
author_lbl = gp.Label(tab1, 'Author:')
author_inp = gp.Input(tab1)
year_lbl = gp.Label(tab1, 'Year:')
year_inp = gp.Input(tab1)
genre_lbl = gp.Label(tab1, 'Genre:')
genre_inp = gp.Input(tab1)
pages_lbl = gp.Label(tab1, 'Page Count:')
pages_inp = gp.Input(tab1)
rating_lbl = gp.Label(tab1, 'Rating:')
rating_inp = gp.Input(tab1)
synopsis_container = gp.LabelContainer(tab1, 'Synopsis:')
synopsis_container.set_grid(1, 1)
synopsis_inp = gp.Textbox(synopsis_container, 70)


# Add input fields to tab1
tab1.add(title_lbl, 1, 1)
tab1.add(title_inp, 1, 2)
tab1.add(author_lbl, 1, 3)
tab1.add(author_inp, 1, 4)
tab1.add(year_lbl, 2, 1)
tab1.add(year_inp, 2, 2)
tab1.add(genre_lbl, 2, 3)
tab1.add(genre_inp, 2, 4)
tab1.add(pages_lbl, 3, 1)
tab1.add(pages_inp, 3, 2)
tab1.add(rating_lbl, 3, 3)
tab1.add(rating_inp, 3, 4)
tab1.add(synopsis_container, 4, 1, column_span=4)
synopsis_container.add(synopsis_inp, 1, 1)

table = gp.Table(tab1, ['Title', 'Author', 'Year', 'Genre', 'Pages', 'Rating', 'Synopsis'])
table.set_column_widths(60,60,60,60,60,60,60)
table.height = 5
table.add_event_listener('select', carry_over)
# Create a copy of the full library for searching
tab1.add(table, 6, 1, column_span=4, fill=True, stretch=True)

# Create buttons
add_btn = gp.Button(tab1, 'Add Book', add_book)
delete_btn = gp.Button(tab1, 'Delete Book', delete_book)
search_btn = gp.Button(tab1, 'Search', search)
clear_btn = gp.Button(tab1, 'Clear Fields', clear_fields)

# Add buttons to tab1
tab1.add(clear_btn, 5, 1)
tab1.add(search_btn, 5, 2)
tab1.add(add_btn, 5, 3)
tab1.add(delete_btn, 5, 4)
#endregion

#region Initialize tab2
tab2.set_grid(1, 1)
tab2.add(gp.Label(tab2, 'This is the second tab'), 1, 1, align='center', valign='middle')
#endregion

# Add tabs to TabContainer
tabs.add(tab1)
tabs.add(tab2)

# Add TabContainer to main window
pybrary.set_grid(1, 1)
pybrary.add(tabs, 1, 1, fill=True, stretch=True)

# Load data when program starts
load_csv()
load_data()

# Run the app
pybrary.run()
