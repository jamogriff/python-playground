from faker import Faker
from library.user import User
from library.book import Book
from library.library import Library

class LibraryFactory:
    """Bootstraps a library instance with users and books."""

    @classmethod
    def make(self, name: str) -> Library:
        fake = Faker()
        library = Library(name)
        books = [Book(fake.isbn10(), fake.sentence(), fake.name()) for n in range(20)]
        book_with_multiple_copies = [Book('123456789', 'Prince Geno Overcomes Hercules', 'Jamison Griffith') for n in range(4)]
        
        for book in books:
            library.add_book(book)

        for book in book_with_multiple_copies:
            library.add_book(book)

        users = [User(fake.name()) for n in range(80)]

        for user in users:
            library.add_user(user)

        return library


