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


# Menu functions
def add_book(library):
    new_book = input_book()
    library.append(new_book)
    save_to_file("library.csv", library)


def list_books(library):
    print("-" * 122)
    print(
        f'| {"Заглавие":20.20} | {"Под-загалвие":20.20} | {"Автори":30.30} | {"Тагове":20.20} | {"Година":6.6} | {"Език":7.7} |')
    print("-" * 122)
    for book in library:
        print(
            f'| {book[0]:20.20} | {book[1]:20.20} | {", ".join(book[2]):30.30} | {", ".join(book[3]):20.20} | {book[4]:6.6} | {book[5]:7.7} |')
    print("-" * 122)


def exit_from_program(library):
    # save_to_file("library.csv", library)
    pass


def list_new_books(library):
    """
    Print the most recent book (the book with most recent year field)
    :param library: the book library list
    """

    pass # TODO: Your code here ...


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
        ("Изход", exit_from_program),
    ]
    while True:
        print()
        for i in range(len(main_menu)):
            print(f"{i + 1}: {main_menu[i][0]}")

        option = int(input("Изберете опция:"))
        main_menu[option - 1][1](library)
        if option == len(main_menu):
            break

    print("Good bye!")
    # book = input_book()
    # library.append(book)
    # print(f"New book added: {library}")
    # # write to csv file
    # save_to_file("library.csv", library)
