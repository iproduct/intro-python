
book = tuple[int, str, str, list[str], str, int, float]
SAMPLE_BOOKS = [
    (1, "Learning Python", "", ["Марк Лътз", "Дейвид Асър"], "O'Reily", 1997, 22.7),
    (2, "Think Python", "An Introduction to Software Design", ["Алън Б. Дауни"], "O'Reily", 2002, 9.4),
    (3, "Python Cookbook", "Recipes for Mastering Python 3", ["Браян К. Джоунс", "Дейвид М. Баазли"], "O'Reily", 2011, 62.6)
]

def create_book_repository(json_filename: str)-> list[book]:
    # TODO write you code here - load books from json file or in case of exception use SAMPLE_BOOKS
    pass

if __name__ == "__main__":
    book_repo = create_book_repository()
    for book in book_repo:
        print(book)
