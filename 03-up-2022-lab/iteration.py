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
    (9, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011, 135.9)
]

def find_most_expensive_book(book: list[tuple[int, str, str,str, int, float]]) -> tuple[int, str, str,str, int, float]:
    #TODO implement me
    return None


if __name__ == '__main__':
    print(find_most_expensive_book(books))