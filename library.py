from book import Book


class Library:
    def __init__(self):
        self.books = []  # Initializes a new empty list to store books.

    def add_book(self, book):
        self.books.append(book)  # Adds a book object to the list of books.

    def list_books(self):
        for book in self.books:
            print(book)


# Example of how the implementation could look
if __name__ == "__main__":
    library = Library()
    while True:
        action = input("Enter 'add' to add a book, 'list' to list books, or 'quit' to exit: ")
        if action == 'quit':
            break
        elif action == 'add':
            # Prompts the user for book details, creates a new Book object, and adds it to the library.
            title = input("Enter title: ")
            author = input("Enter author: ")
            rating = float(input("Enter rating: "))
            genre = input("Enter genre: ")
            pages = int(input("Enter number of pages: "))
            synopsis = input("Enter synopsis: ")
            book = Book(title, author, rating, genre, pages, synopsis)
            library.add_book(book)
        elif action == 'list':
            library.list_books()  # Lists all books currently stored in the library.
