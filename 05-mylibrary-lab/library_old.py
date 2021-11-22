import json

books = []

id_sequence = 0

BOOKS_DB = "books.json"

def show_all_books():
    print_all_books(books)

def load_books_action():
    global books
    books = load_from_file(BOOKS_DB)
    print(f"{len(books)} books loaded successfully.")

main_menu = [
    ("Show All Books", show_all_books),
    ("Load from File", load_books_action),
    ("Exit", lambda: print("Thank you for using MYLibrary. Have nice Day!") or exit(0)),
]


def add_book(title, subtitle, authors, isbn, publisher, year, price, genre, tags, description=None):
    """Adds new book to the books collection"""
    global id_sequence
    id_sequence += 1
    books.append({
        "id": id_sequence,
        "title":title,
        "subtitle": subtitle,
        "authors": authors,
        "isbn": isbn,
        "publisher": publisher,
        "year": year,
        "price": price,
        "genre": genre,
        "tags": tags,
        "description": description
    })


def print_book(b):
    """Prints a book as table row"""
    print(
        f"| {b['id']:^3d} | {b['title']:<20.20s} | {b['subtitle']:<20.20s} | {', '.join(b['authors']):^25.25s} |"
        f"{b['isbn']:^10.10s} | {b['publisher']:^10.10s} | {b['year']:<4d} |"
        f"{b['price']:>7.2f} | {b['genre']:^15.15s} | {', '.join(b['tags']):^30.30s} |")

def print_all_books(books):
    """Prints a table with all books given"""
    for book in books:
        print_book(book)

def save_to_file(filename, books):
    """Save books data to JSON file"""
    with open(filename, "wt") as f:
        json.dump(books, f, indent=4)

def load_from_file(filename):
    """Load books data from JSON file"""
    with open(filename, "rt") as f:
        return json.load(f)

def show_menu(menu, title):
    print("\n"+title + ":")
    for i, option in enumerate(menu):
        print(f"{i + 1:^d}) {option[0]:<40.40s}")
    opt = int(input("Choose an option:"))
    try:
        result = menu[opt - 1][1]() # call the action function and check for exception
        if result:
            print(f"Error: {result}")
    except SystemExit:
        return False
    except BaseException as err:
        print(f"Error: {err}, {type(err)=}")
    return True

if __name__ == '__main__':
    # add_book("Head First Python", "A Brain-Friendly Guide", ["Paul Barry"], "1491919531",
    #          "O'Reilly UK Ltd.", 2016, 41.82, "Software Engineering",
    #          ["python", "introduction", "examples", "programming"],
    #          "Want to learn the Python language without slogging your way through how-to manuals? With Head First "
    #          "Python, you&;ll quickly grasp Python&;s fundamentals, working with the built-in data structures and "
    #          "functions. Then you&;ll move on to building your very own webapp, exploring database management, "
    #          "exception handling, and data wrangling. If you&;re intrigued by what you can do with context managers, "
    #          "decorators, comprehensions, and generators, it&;s all here. This second edition is a complete learning "
    #          "experience that will help you become a bonafide Python programmer in no time.")
    # add_book("Learning Python", "Powerful Object-Oriented Programming", ["Mark Lutz"], "1449355730",
    #          "O'Reilly UK Ltd.", 2013, 49.53, "Software Engineering",
    #          ["python", "programming", "oop"],
    #          "Get a comprehensive, in-depth introduction to the core Python language with this hands-on book. Based "
    #          "on author Mark Lutz's popular training course, this updated fifth edition will help you quickly write "
    #          "efficient, high-quality code with Python. It's an ideal way to begin, whether you're new to programming "
    #          "or a professional developer versed in other languages.")
    # print_all_books(books)
    # save_to_file(BOOKS_DB, books)
    # print("Loaded from file:")
    # loaded_books = load_from_file(BOOKS_DB)
    # print_all_books(loaded_books)
    # load_books_action()
    while show_menu(main_menu, "Main Menu"):
        pass

