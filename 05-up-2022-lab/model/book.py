from model.publication import Publication
from model.sample_books import books


class Book(Publication):
    def __init__(self, id: int, title: str, subtitle: str, author: str, publisher: str, year: int, price: float):
        print((id, title, author, publisher, year))
        super().__init__(id, title, author, publisher, year)
        self.subtitle = subtitle
        self.price = price

    def __repr__(self):
        # book_attr_list = [f'{p[0]} = {p[1]}' for p in self.__dict__.items()]
        # book_attr_str = ', '.join(book_attr_list)
        return f"Book({super().__repr__()}, subtitle={self.subtitle}, price={self.price})"


if __name__ == '__main__':
    books_list: list[Book] = []
    for book_tuple in books:
        books_list.append(Book(*book_tuple))
    for book in books_list:
        print(book)
