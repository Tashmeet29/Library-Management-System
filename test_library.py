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
    
def test_return_book():
    library = Library()
    book = {"isbn": "1234567890", "title": "Python Basics", "author": "John Doe", "year": 2021}

    # Borrow and then return book
    library.add_book(book)
    library.borrow_book("1234567890")
    library.return_book(book)

    # Check that book is back in available books list
    assert book in library.books

def test_view_available_books():
    library = Library()
    book1 = {"isbn": "1234567890", "title": "Python Basics", "author": "John Doe", "year": 2021}
    book2 = {"isbn": "0987654321", "title": "Advanced Python", "author": "Jane Smith", "year": 2022}

    library.add_book(book1)
    library.add_book(book2)

    available_books = library.view_books()

    # Check that both books are listed as available
    assert book1 in available_books
    assert book2 in available_books
