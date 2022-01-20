from entity.book import Book

if __name__ == '__main__':
    b1 = Book("Think Python", "An Introduction to Software Design", ("Алън Б. Дауни",), "1491939362",
              "O'Reily", 2002, 9.7, "Software engineering", ("python", "introduction", "programming"),
              "If you want to learn how to program, working with Python is an excellent way to start. "
              "This hands-on guide takes you through the language a step at a time, beginning with basic "
              "programming concepts before moving on to functions, recursion, data structures, and "
              "object-oriented design. This second edition and its supporting code have been updated "
              "for Python 3.")
    print(b1)
