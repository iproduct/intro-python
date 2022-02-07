from functools import reduce
from itertools import count

Book = tuple[int, str, str, str, str, int, float]
books = [
    (1, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1997, 22.7),
    (2, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 9.4),
    (3, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011, 62.6),
    (4, "Learning Python 2", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1998, 22.7),
    (5, "Think Python 2", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 9.4),
    (6, "Python Cookbook 2", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011, 56.7),
    (7, "Learning Python 3", "", "Марк Лътз, Дейвид Асър", "O'Reily", 2001, 22.7),
    (8, "Think Python 3", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 9.4),
    (9, "Python Cookbook 3", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011, 135.9)
]

def after_year_2000(book: Book) -> bool:
    return book[-2] > 2000

if __name__ == '__main__':
    print(all(map(after_year_2000, books)))
    print(any(map(lambda book: not after_year_2000(book), books)))
    all_books_title_year = map(lambda book: (book[1], book[-2], book[-1]), books) # projection
    new_books_to_buy = filter( lambda book_year: book_year[1] > 2000, all_books_title_year) # selection
    new_books_to_buy_by_column = zip(*new_books_to_buy)
    # print(*new_books_to_buy_by_column)
    numbered_books = zip(count(1), *new_books_to_buy_by_column)
    numbered_books_list = list(numbered_books)
    print(*numbered_books_list, sep="\n")
    print("Total: ", sum(map(lambda book: book[-1], numbered_books_list)))
    print("Total: ", reduce(lambda acc, book: acc + book[-1], numbered_books_list, 0.0))
