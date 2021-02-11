

def input_book():
    # input title
    while True:
        title = input("Въведете заглавие:")
        if len(title) >= 3:
            break
        else:
            print("Грешка - заглавието трябва да бъде с дължина поне 3 символа.")

    # input authors - comma separated
    while True:
        answer = input("Въведете автори (разделени със запетайки):")
        if len(answer) >= 3:
            authors = answer.split(",")
            i = 0
            while i < len(authors):
                authors[i] = authors[i].strip()
                i += 1
            break
        else:
            print("Грешка - автори трябва да бъде с дължина поне 3 символа.")

    # input tags - comma separated, each tag should be at least 2 characters long

    # return result book
    return [title, authors, tags]

if __name__ == '__main__':
    library = []
    book = input_book()
    library.append(book)
    print(f"New book added: {library}")
