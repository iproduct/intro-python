import sys

from model import *
from model.sample_books import find_most_expensive_book, books

if __name__ == '__main__':
    # print(sys.path)
    # print([x for x in dir(sample_books) if not x.startswith("__")])
    # for book in books:
    #     print(book)
    # find_most_expensive_book(books)

    # Book class demo
    books_list: list[book.Book] = []
    for book_tuple in books:
        books_list.append(book.Book(*book_tuple))
    for book in books_list:
        print(book)
