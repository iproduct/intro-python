import json
from functools import reduce
from itertools import count

books = [
    (1, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1997, 22.7),
    (2, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 9.4),
    (3, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс, Дейвид М. Баазли", "O'Reily", 2011,
     62.6),
    (4, "Learning Python 2 ed.", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1998, 22.7),
    (5, "Think Python 2 ed.", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 19.4),
    (6, "Python Cookbook 2", "Recipes for Mastering Python 3", "Браян К. Джоунс, Дейвид М. Баазли", "O'Reily", 2015,
     56.7),
    (7, "Learning Python 3 ed.", "", "Марк Лътз, Дейвид Асър", "O'Reily", 2001, 28.9),
    (8, "Think Python 3 ed.", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 23.4),
    (9, "Python Cookbook 3 ed.", "Recipes for Mastering Python 3", "Браян К. Джоунс, Дейвид М. Баазли", "O'Reily", 2018,
     135.9)
]


def make_book(id, title, subtitle, authors, publisher, year, price):
    return {
        'id': id,
        'title': title,
        'subtitle': subtitle,
        'authors': [author.strip() for author in authors.split(',')],
        'publisher': publisher,
        'year': year,
        'price': price
    }


if __name__ == "__main__":
    books_dicts = map(lambda book_tuple: make_book(*book_tuple), books)
    # for book in books_dicts:
    #     print(book)
    # new_books = filter(lambda book: book['year'] > 2010, books_dicts) # selection
    # new_book_titles_years = map(lambda b: (b['id'], b['title'], b['year']), new_books) # projection
    # new_books_prices_sum = sum(map(lambda book: book['price'], new_books))
    # print(f"Sum of new books: {new_books_prices_sum:7.2f}")
    # authors = set((a for book in books_dicts for a in book['authors']))
    # counted_books = zip(count(1), map(lambda book: book['title'], books_dicts))
    # for cb in counted_books:
    #     print(f'{cb[0]} -> {cb[1]}')
    # print('All after 1995:', all( map(lambda book: book['year'] > 2000, books_dicts)))
    # print('All after 2017:', any( map(lambda book: book['year'] > 2017, books_dicts)))

    # print("Prices list:", reduce(lambda acc, book: acc + (', ' if len(acc) > 0 else '') + str(book['price']), books_dicts, ''))
    print(f"Prices sum: {reduce(lambda acc, book: acc + book['price'], books_dicts, 0):6.2f}")


