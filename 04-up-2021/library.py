"""Home Library Information System

This script allows to manage books in home library and provides
Create-Read-Update-Delete (CRUD) functionality operations for books.

The system saves book information to CSV file 'library.csv' and
can load the books from this file in the start of next session.

This file can also be imported as a module and contains the following
functions:

    * input_book - inputs information for a new book in home library
    * load_from_file - loads books from given file
    * save_to_file - saves books to given file
    * write_book - write books in the library to console
    * prints_book - prints given books as formatted table to the console
    * add_book - inputs new book and adds the book to the given library list
    ...
    * main - the main function of the script
"""


import re

def input_book():
    # input title
    while True:
        title = input("Въведете заглавие:")
        if len(title) >= 3:
            break
        else:
            print("Грешка - заглавието трябва да бъде с дължина поне 3 символа.")

    # input subtitle
    subtitle = input("Въведете под-заглавие:")
    if subtitle == '':
        subtitle = ' '

    # input authors - comma separated
    while True:
        answer = input("Въведете автори (разделени със запетайки):")
        if len(answer) >= 3:
            authors = answer.split(",")
            i = 0
            while i < len(authors):
                authors[i] = authors[i].strip()
                if len(authors[i]) < 5:
                    authors.pop(i)
                else:
                    i += 1
            break
        else:
            print("Грешка - автори трябва да бъде с дължина поне 3 символа.")

    # input tags - comma separated, each tag should be at least 2 characters long
    while True:
        answer = input("Въведете тагове (разделени със запетайки):")
        if len(answer) >= 2:
            tags = answer.split(",")
            i = 0
            while i < len(tags):
                tags[i] = tags[i].strip()
                if len(tags[i]) < 2:
                    tags.pop(i)
                else:
                    i += 1
            break
        else:
            print("Грешка - тагове трябва да бъде с дължина поне 3 символа.")

    # input publishing year
    while True:
        year = input("Въведете година на издаване:")
        if re.match(r"[12][0-9]{3}", year):
            break
        else:
            print("Грешка - въведете валидна година: напр. 1995")

    # input language
    while True:
        language = input("1) Английски, 2) Български, 3) Немски, 4) Руски (<Enter> за Английски):")
        if re.match(r"[1-4]?", language):
            if language == "" or language == "1":
                language = "English"
            elif language == "2":
                language = "Bulgarian"
            elif language == "3":
                language = "Deutsch"
            elif language == "2":
                language = "Russian"
            break
        else:
            print("Грешка - въведете валидen избор")

    # return result book
    return [title, subtitle, authors, tags, year, language]


# File IO methods
def load_from_file(filename):
    table = []
    in_file = open(filename, "rt", encoding="utf-8")
    for line in in_file:
        line = line.strip()
        if line == '':
            continue
        record = []
        closing_quotes_index = -1
        open_quotes_index = line.find('"')

        while open_quotes_index >= 0:
            new_properties = line[closing_quotes_index + 1: open_quotes_index - 1].split(",")
            record.extend(new_properties)
            closing_quotes_index = line.find('"', open_quotes_index + 1)
            record.append(line[open_quotes_index + 1: closing_quotes_index])
            open_quotes_index = line.find('"', closing_quotes_index + 1)

        # parse props after last closing quote
        new_properties = line[closing_quotes_index + 2:].split(",")
        record.extend(new_properties)
        i = 0
        while i < len(record):
            if record[i] == '':
                del record[i]
            else:
                i += 1
        table.append(record)

    in_file.close()
    return table


def save_to_file(filename, library):
    out = open(filename, "wt", encoding="utf-8")
    for book in library:
        write_book(out, book)
    out.close()


def write_book(out, book):
    for i in range(len(book)):
        value = book[i]
        # print( type(value) )
        if isinstance(value, str):
            out.write(value)
        elif isinstance(value, list):
            list_str = ",".join(value)
            out.write(f'"{list_str}"')
        else:
            continue
        if i != len(book) - 1:
            out.write(",")
    out.write("\n")


def print_books(books):
    print("-" * 132)
    print(
        f'| {"Заглавие":20.20} | {"Под-загалвие":20.20} | {"Автори":30.30} | {"Тагове":30.30} | {"Година":6.6} | {"Език":7.7} |')
    print("-" * 132)
    for book in books:
        print(
            f'| {book[0]:20.20} | {book[1]:20.20} | {", ".join(book[2]):30.30} | {", ".join(book[3]):30.30} | {book[4]:6.6} | {book[5]:7.7} |')
    print("-" * 132)


# Menu functions
def add_book(library):
    new_book = input_book()
    library.append(new_book)
    save_to_file("library.csv", library)


def list_books(library):
    print_books(library)

def exit_from_program(library):
    # save_to_file("library.csv", library)
    pass


def list_new_books(library):
    """
    Print the most recent book (the book with most recent year field)
    :param library: the book library list
    """
    pass # TODO: Your code here ...


def list_by_tags(library):
    """
    Input tags and print the books that have at least one of tags
    :param library: the book library list
    """
    tags_str = input("Enter search tags:")
    tags = tags_str.split(",")
    for i in range(len(tags)):
        tags[i] = tags[i].strip()
    results = []
    for book in library:
        if set(tags).intersection(set(book[3])) != set():
            results.append(book)
    print_books(results)


def list_by_title(library):
    """
    Input tags title or part of it and find all books that have that title part
    :param library: the book library list
    """

    pass # TODO: Your code here ...

def dummy_func(library):
    pass

# def list_by_predicate(library, predicate):
#     """
#     List books satisfying given predicate function
#     :param library: list of books
#     :param predicate: function of book argument returning True or False
#     :return: list books filtered by predicate
#     """
#     # results = []
#     # for book in library:
#     #     if predicate(book):
#     #         results.append(book)
#     # return results
#     return filter(predicate, library)



def list_by_period(library):
    start = int(input("Start year:"))
    end = int(input("End year:"))
    # def is_published_in_period(book):
    #     return int(book[4]) >= start and int(book[4]) <= end
    print_books(filter(library, create_predicate_by_period(start, end)))


def create_predicate_by_period(start, end):
    # def is_published_in_period(book):
    #     return int(book[4]) >= start and int(book[4]) <= end
    return lambda book: int(book[4]) >= start and int(book[4]) <= end


if __name__ == '__main__':
    library = load_from_file("library.csv")
    for book in library:
        book[2] = book[2].split(",")
        book[3] = book[3].split(",")
    print(library)

    main_menu = [
        ("Добави книга", add_book),
        ("Покажи всички книги", list_books),
        ("Най-нови книги", list_new_books),
        ("Търсене по тагове", list_by_tags),
        ("Търсене по заглавие", list_by_title),
        ("Търсене по период", list_by_period),
        ("Изход", exit_from_program),
    ]
    while True:
        print()
        for i in range(len(main_menu)):
            print(f"{i + 1}: {main_menu[i][0]}")

        try:
            option = int(input("Изберете опция:"))
            main_menu[option - 1][1](library)
            if option == len(main_menu):
                print("Good bye!")
                break
        except ValueError:
            print("Invalid choice. Try again.")
        except IndexError:
            print(f"Invalid choice.Choose between 1 and {len(main_menu)}")


# print(f"__file__: {__file__}")
# print(f"__package__: {__package__}")
# print(f"__name__: {__name__}")
    # book = input_book()
    # library.append(book)
    # print(f"New book added: {library}")
    # # write to csv file
    # save_to_file("library.csv", library)
