from functools import reduce

books = [
    (1, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1999, 22.7),
    (2, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни","O'Reily", 2002, 9.7),
    (3, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011, 135.9)
    ]

def print_books(books, sort_key= None, reverse=False):
    if sort_key != None:
        books_copy = books.copy()
        books_copy.sort(key = sort_key, reverse = reverse)
    else:
        books_copy = books
    result = ""
    for book in books_copy:
        line = "| {:>d} | {:<15.15s} | {:<15.15s} | {:20.20s} | {:12.12s} | {:4d} | {:7.2f} |\n" \
            .format(*book)
        result += line
    return result, len(line) - 1

def sum_prices(acc, book):
    return acc + book[-1]

def get_price(book_tuple):
    return book_tuple[-1]

if __name__ == "__main__":
    result, line_len = print_books(books, get_price, reverse=True)
    print(result)
    total_price = reduce(sum_prices, books, 0)
    print('Total price: '.rjust(line_len - 7) + f"{total_price:>7.2f}")
    print('VAT: '.rjust(line_len - 7) + f"{total_price * 0.2:>7.2f}")
