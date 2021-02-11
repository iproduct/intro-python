

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


    # return result book
    return [title, authors, tags]

if __name__ == '__main__':
    library = []
    book = input_book()
    library.append(book)
    print(f"New book added: {library}")
