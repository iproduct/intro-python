from entity.book import Book

if __name__ == '__main__':
    b1 = Book("Think Python", "An Introduction to Software Design", ("Allen B. Downey",), "1491939362",
              "O'Reily", 2002, 9.7, "Software engineering", ("python", "introduction", "programming", "oop"),
              "If you want to learn how to program, working with Python is an excellent way to start. "
              "This hands-on guide takes you through the language a step at a time, beginning with basic "
              "programming concepts before moving on to functions, recursion, data structures, and "
              "object-oriented design. This second edition and its supporting code have been updated "
              "for Python 3.")
    b2 = Book("Learning Python", "5th Edition", ("Mark Lutz",), "1449355730",
              "O'Reily", 2013, 45.47, "Software engineering", ("python", "learning", "programming"),
              "Get a comprehensive, in-depth introduction to the core Python language with this hands-on book. "
              "Based on author Mark Lutz’s popular training course, this updated fifth edition will help you quickly "
              "write efficient, high-quality code with Python. It’s an ideal way to begin, whether you’re new to "
              "programming or a professional developer versed in other languages.")
    b3 = Book("Python Cookbook", "Recipes for mastering Python 3", ("David Beazley",), "1449340377",
              "O'Reily", 2013, 28.24, "Software engineering", ("python", "cookbook", "programming", "examples"),
              "If you need help writing programs in Python 3, or want to update older Python 2 code, this book is "
              "just the ticket. Packed with practical recipes written and tested with Python 3.3, this unique "
              "cookbook is for experienced Python programmers who want to focus on modern tools and idioms.")
    books = (b1, b2, b3)
    for book in books:
        print(book)
