class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    @staticmethod
    def format(book: Book) -> str:
        return book.content


class Printer:

    @staticmethod
    def get_book(book: Book, formatted_book: Formatter):
        formatter = formatted_book
        formatted_book = formatter.format(book)

        return formatted_book
      
