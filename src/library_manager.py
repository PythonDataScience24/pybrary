import csv


class LibraryManager:
    def __init__(self):
        self.full_library = []
        self.load_csv()

    def add_book(self, book_details):
        self.full_library.append(book_details)
        self.save_data()

    def overwrite_book(self, book_details, index):
        if index < len(self.full_library):
            self.full_library[index] = book_details
            self.save_data()

    def delete_book(self, book_details):
        if book_details in self.full_library:
            self.full_library.remove(book_details)
            self.save_data()

    def search_books(self, title_search, author_search, genre_search, year_search, pages_search, rating_search, synopsis_search):
        title_search = title_search.lower()
        author_search = author_search.lower()
        genre_search = genre_search.lower()
        year_search = year_search.lower()
        pages_search = pages_search.lower()
        rating_search = rating_search.lower()
        synopsis_search = synopsis_search.lower()

        search_results = [
            row for row in self.full_library if
            (not title_search or title_search in row[0].lower()) and
            (not author_search or author_search in row[1].lower()) and
            (not genre_search or genre_search in row[3].lower()) and
            (not year_search or year_search in row[2].lower()) and
            (not pages_search or pages_search in row[4].lower()) and
            (not rating_search or rating_search in row[5].lower()) and
            (not synopsis_search or synopsis_search in row[6].lower())
        ]

        return search_results

    def load_csv(self):
        try:
            with open('library.csv', 'r', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    self.full_library.append(row)
        except FileNotFoundError:
            pass  # It's okay if the file doesn't exist

    def save_data(self):
        try:
            with open('library.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(self.full_library)
        except Exception as e:
            print(f"Error saving data: {e}")
