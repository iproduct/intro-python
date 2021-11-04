def compare_str_ignore_case(s: str) -> str:
    return s.lower() # return lowercase of the string
    # return str.lower(s)


def book_by_title(book):
    return book[1] # return book title


def book_by_author(book):
    return book[3] # return book author


def book_by_price(book):
    return book[6] # return book price


def print_books(books):
    """
    prints all books formatted as table
    :param books: books to print
    :return: string containing books as table
    """
    # for each book print the book
    for b in books:
        print(
            f'| {b[0]:>3d} | {b[1]:20.20s} | {b[2]:20.20s} | {b[3]:^15.15s} | {b[4]:^15.15s} | {b[5]:4d} | {str(b[6]) if len(b) > 6 else "-   ":>7.7s} |')


if __name__ == '__main__':
    l = ['Orange', 'orange', 'banana', 'kiwi', 'mango', 'pineapple'] # sample fruits list
    l.sort(key=compare_str_ignore_case) # sorting fruits ignore case
    print(l)

    # sample books list containing each book as a tuple
    books = [
        (1, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1999, 22.7),
        (2, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 9.4),
        (3, "Python Crash Course, 2nd Edition", "A Hands-On, Project-Based Introduction to Programming", "Eric Matthes",
         "No Starch Press", 2014, 9.56),
        (4, "Python Pocket Reference", "Python in Your Pocket", "Mark Lutz", "O'Reily", 2002, 9.4),
        (5, "Python for Data Analysis", "Data Wrangling with Pandas, NumPy, and IPython", "Wes Mckinney", "O'Reily",
         2017, 30.75),
        (6, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011,
         135.9)
    ]

    # books_copy = books.copy()
    # books_copy = list(books)
    # books_copy = books[:]
    books_copy = [book for book in books if book[3][0] < 'z']

    books_copy.sort(key=book_by_price, reverse=True)
    print_books(books)
    print()
    print_books(books_copy)

    # tuples
    t = (2, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 9.4)
    newt = t + (["python", "introduction", "programming"],)
    print(newt, ", ", t is newt)
    print()
    books_without_price = []
    # calculate total books price
    suma = 0
    for book in books:
        (*la, price) = book
        books_without_price.append(la)
        suma += price
    print_books(books_without_price)
    print(f"Total price: {suma}\n")