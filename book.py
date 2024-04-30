class Book:
    def __init__(self, title, author, rating, genre, pages, synopsis):
        self.title = title
        self.author = author
        self.rating = rating
        self.genre = genre
        self.pages = pages
        self.synopsis = synopsis

    def __repr__(self):
        return f"{self.title} by {self.author}, Rating: {self.rating}, Genre: {self.genre}, Pages: {self.pages}"
