books = [
    (1, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1999, 22.7),
    (2, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 9.4),
    (3, "Awesome Python 2 ed.", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1999, 22.7),
    (4, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011,
     135.9)
]


def format(books: list[tuple]) -> str:
    return '\n'.join(map(lambda book:
                         '| {0:4d} | {1:15.15s} | {2:30.30s} | {3:20.20s} | {4:15.15s} | {5:4d} | {6:8.2f} |'
                         .format(*book), books))


if __name__ == '__main__':
    print(format(books))
    print()
    books.sort(key=lambda book: (book[6], book[1]))
    print(format(books))

