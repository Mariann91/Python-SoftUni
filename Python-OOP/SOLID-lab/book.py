from typing import List


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book) -> None:
        self.books.append(book)

    def find_book(self, title) -> Book or str:
        try:
            return [book for book in self.books if book.title == title][0]
          
        except IndexError:
            return "Book doesn't not exists in the library"
