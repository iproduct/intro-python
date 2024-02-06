# books are modeled as list of (book_id, title, subtitle, authors, publisher, year, price) tuples
books = [
    (1, "Learning Python", "", "Mark Lutz, David Aser", "O'Reily", 1999, 22.7),
    (2, "Think Python", "An Introduction to Software Design", "Alan Dawny", "O'Reily", 2002, 9.4),
    (3, "Python Cookbook", "Recipes for Mastering Python 3", "Brian Jones, David Basly", "O'Reily", 2011, 135.9),
]

# bond is modeled as a list of (book_id, quantity) tuples
bond = [(1, 1), (2, 5), (3, 2)]

def list_books(books):
    result = ''
    for book in books:
        result += "| {:>3d} | {:<15.15s} | {:<15.15s} | {:<20.20s} | {:<12.12s} | {:>4d} | {:>7.2f} | \n".format(*book)
    return result

def prepare_bond(bond, books_dict):
    result = ''
    sum = 0
    for i, pos in enumerate(bond):
        book = books_dict[pos[0]]
        price = book[6] * pos[1] # unit_price * quantity
        result += "| {:>2d} | {:<15.15s} | {:>7.2f}  | {:>3d} | {:>7.2f} |\n"\
            .format(i, book[1], book[6], pos[1], price)
        sum += price
    result += f"{' ' * 22} Total without VAT: {sum:>7.2f}\n"
    result += f"{' ' * 22}               VAT: {0.2 * sum:>7.2f}\n"
    result += f"{' ' * 22}             Total: {1.2 * sum:>7.2f}\n"
    return result

if __name__ == '__main__':
    print(list_books(books))
    # preapre books dict for efficient retrieval of books by ID
    books_dict = dict()
    for book in books:
        books_dict[book[0]] = book

    print(prepare_bond(bond, books_dict))