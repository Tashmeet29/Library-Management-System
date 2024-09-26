from library import Library

def test_add_book():
    library = Library()
    book = {"isbn": "1234567890", "title": "Python Basics", "author": "John Doe", "year": 2021}
    library.add_book(book)
    assert book in library.books
