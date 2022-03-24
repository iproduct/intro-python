import json

books = [
    (1, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1997, 22.7),
    (2, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 9.4),
    (3, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс, Дейвид М. Баазли", "O'Reily", 2011,
     62.6),
    (4, "Learning Python 2 ed.", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1998, 22.7),
    (5, "Think Python 2 ed.", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 19.4),
    (6, "Python Cookbook 2", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011,
     56.7),
    (7, "Learning Python 3 ed.", "", "Марк Лътз, Дейвид Асър", "O'Reily", 2001, 28.9),
    (8, "Think Python 3 ed.", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 23.4),
    (9, "Python Cookbook 3 ed.", "Recipes for Mastering Python 3", "Браян К. Джоунс, Дейвид М. Баазли", "O'Reily", 2011,
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
    books_dicts = list(map(lambda book_tuple: make_book(*book_tuple), books))
    print(books_dicts)

