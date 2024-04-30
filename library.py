from book import Book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

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
            title = input("Enter title: ")
            author = input("Enter author: ")
            rating = float(input("Enter rating: "))
            genre = input("Enter genre: ")
            pages = int(input("Enter number of pages: "))
            synopsis = input("Enter synopsis: ")
            book = Book(title, author, rating, genre, pages, synopsis)
            library.add_book(book)
        elif action == 'list':
            library.list_books()
