import gooeypie as gp
import csv

pybrary = gp.GooeyPieApp('pybrary')

# Create tab container
tabs = gp.TabContainer(pybrary)

# Create tabs
tab1 = gp.Tab(tabs, 'View Collection')
tab2 = gp.Tab(tabs, 'Visualization')

#region Tab1
tab1.set_grid(8, 4)

def clear_fields():

    # Clear input fields
    title_inp.clear()
    author_inp.clear()
    year_inp.clear()
    pages_inp.clear()
    genre_inp.clear()
    rating_inp.clear()
    synopsis_inp.clear()

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
    collection.add_row([title, author, year, genre, pages, rating, synopsis])

    clear_fields()
    save_data()
    
def delete_book(event):

    collection.remove_selected()

    clear_fields()
    save_data()

def save_data():
    try:
        with open('library.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(collection.data)
    except Exception as e:
        print(f"Error saving data: {e}")

def load_data():
    try:
        with open('library.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                collection.add_row(row)
    except FileNotFoundError:
        pass  # It's okay if the file doesn't exist

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
synopsis_lbl = gp.Label(tab1, 'Synopsis:')
synopsis_inp = gp.Textbox(tab1, 70)

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
tab1.add(synopsis_lbl, 4, 1)
tab1.add(synopsis_inp, 5, 1, column_span=4)

collection = gp.Table(tab1, ['Title', 'Author', 'Year', 'Genre', 'Pages', 'Rating', 'Synopsis'])
collection.set_column_widths(60,60,60,60,60,60,60)
tab1.add(collection, 6, 1, column_span=4, fill=True, stretch=True)

# Create buttons
add_btn = gp.Button(tab1, 'Add Book', add_book)
delete_btn = gp.Button(tab1, 'Delete Book', delete_book)

# Add buttons to tab1
tab1.add(add_btn, 4, 3)
tab1.add(delete_btn, 4, 4)
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
load_data()

# Run the app
pybrary.run()
