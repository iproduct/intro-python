from book import Book
from book_repository import BookRepository
from book_repository_json import BookRepositoryJson, load_from_file

if __name__ == "__main__":
    b1 = Book(
        3,
        "Head First Python",
        "A Brain-Friendly Guide",
        ["Paul Barry"],
        "1491919531",
        "O'Reilly UK Ltd.",
        2016,
        41.82,
        "Software Engineering",
        [
            "python",
            "introduction",
            "examples",
            "programming"
        ],
        "Want to learn the Python language without slogging your way through how-to manuals? With Head First Python, you&;ll quickly grasp Python&;s fundamentals, working with the built-in data structures and functions. Then you&;ll move on to building your very own webapp, exploring database management, exception handling, and data wrangling. If you&;re intrigued by what you can do with context managers, decorators, comprehensions, and generators, it&;s all here. This second edition is a complete learning experience that will help you become a bonafide Python programmer in no time."
    )
    b2 = Book(
        4,
        "Head First Python",
        "A Brain-Friendly Guide",
        ["Paul Barry"],
        "1491919531",
        "O'Reilly UK Ltd.",
        2016,
        41.82,
        description="Want to learn the Python language without slogging your way through how-to manuals? With Head First Python, you&;ll quickly grasp Python&;s fundamentals, working with the built-in data structures and functions. Then you&;ll move on to building your very own webapp, exploring database management, exception handling, and data wrangling. If you&;re intrigued by what you can do with context managers, decorators, comprehensions, and generators, it&;s all here. This second edition is a complete learning experience that will help you become a bonafide Python programmer in no time."
    )
    # books = BookRepositoryJson()
    # books.load()
    # books.insert(b1)
    # books.insert(b2)
    #
    # for book in books.find_all():
    #     print(book)

    # books.persist()

    books = load_from_file("books.json")
    print(books)
