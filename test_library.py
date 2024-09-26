from library import Library

def test_add_book():
    library = Library()
    book = {"isbn": "1234567890", "title": "Python Basics", "author": "John Doe", "year": 2021}
    library.add_book(book)
    assert book in library.books

def test_borrow_book():
    library = Library()
    book = {"isbn": "1234567890", "title": "Python Basics", "author": "John Doe", "year": 2021}
    library.add_book(book)

    # Borrow book using its ISBN
    assert library.borrow_book("1234567890") == "Borrowed"

    # Check that book is no longer available in library
    assert book not in library.books
