from typing import List, Dict
from project.user import User


class Library:
  
    def __init__(self) -> None:
        self.user_records: List[User] = []
        self.books_available: Dict[str: List[str]] = {}  # {author: [book1, book2 ...]
        self.rented_books: Dict[str: Dict[str: int]] = {}  # {username1: book1: day_left, username2: book2: day_left...}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:

        if book_name in self.books_available[author]:

            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username not in self.rented_books:
                self.rented_books.update({user.username: {book_name: days_to_return}})

            self.rented_books[user.username][book_name] = days_to_return

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        return f'The book "{book_name}" is already rented and will be available in {self.rented_books[user.username][book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> str or None:

        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        self.rented_books[user.username].pop(book_name)
