from typing import Union

Book = tuple[int, str, str, str, str, int, float]


def sum(a, b):
    return (a, b)


def times(a: str, b: int) -> str:
    return a * b


def times2(a, b):
    return a * b


# def get_book_title(book: Book) -> str:
#     print("get_book_title", "->", book)
#     return book[1]


def get_titles(books: list[Book]) -> map:
    return map(lambda book: book[1], books)


if __name__ == '__main__':
    x, y = sum(3, 5)
    print(x, y, type(x), type(y))
    print(times(3.5, 3))
    print(times("abc", 5))

    # lists
    books = [
        (1, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1999, 22.7),
        (2, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 9.4),
        (3, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011),
        (4, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1999, 22.7),
        (5, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 9.4),
        (6, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011),
        (7, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1999, 22.7),
        (8, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 9.4),
        (9, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily",
         2011,
         135.9)
    ]
    i = 0
    for title in get_titles(books):
        print(title)
        i += 1
        if i == 2:
            break
