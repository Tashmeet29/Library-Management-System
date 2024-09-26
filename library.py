class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book["isbn"] == isbn:
                self.books.remove(book)  # Remove the borrowed book from available books
                return "Borrowed"
        return "Book not available"

    def return_book(self, book):
            self.books.append(book)  # Add the book back to available books

    def view_books(self):
        return self.books  # Return list of available books
