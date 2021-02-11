

def input_book():
    while True:
        title = input("Въведете заглавие:")
        if len(title) >= 3:
            break
        else:
            print("Грешка - заглавието трябва да бъде с дължина поне 3 символа.")

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
    return [title, authors]

if __name__ == '__main__':
    library = []
    book = input_book()
    library.append(book)
    print(f"New book added: {library}")
