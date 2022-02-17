from controller.book_controller import BookController
from controller.login_controller import LoginController
from dao.book_repository import BookRepository
from dao.json_repository import entity_class
from dao.user_repository import UserRepository
from entity.book import Book
from entity.user import User
from view.main_menu_commands import RegisterCommand, LoginCommand, LogoutCommand, GetLoggedUserCommand
from view.menu import MenuItem, Menu

if __name__ == '__main__':
    # b1 = Book(None, "Think Python", "An Introduction to Software Design", ("Allen B. Downey", "Mark Lutz"), "1491939362",
    #           "O'Reily", 2002, 9.7, "Software engineering", ("python", "introduction", "programming", "oop"),
    #           "If you want to learn how to program, working with Python is an excellent way to start. "
    #           "This hands-on guide takes you through the language a step at a time, beginning with basic "
    #           "programming concepts before moving on to functions, recursion, data structures, and "
    #           "object-oriented design. This second edition and its supporting code have been updated "
    #           "for Python 3.")
    # b2 = Book(None, "Learning Python", "5th Edition", ("Mark Lutz",), "1449355730",
    #           "O'Reily", 2013, 45.47, "Software engineering", ("python", "learning", "programming"),
    #           "Get a comprehensive, in-depth introduction to the core Python language with this hands-on book. "
    #           "Based on author Mark Lutz’s popular training course, this updated fifth edition will help you quickly "
    #           "write efficient, high-quality code with Python. It’s an ideal way to begin, whether you’re new to "
    #           "programming or a professional developer versed in other languages.")
    # b3 = Book(None, "Python Cookbook", "Recipes for mastering Python 3", ("David Beazley",), "1449340377",
    #           "O'Reily", 2013, 28.24, "Software engineering", ("python", "cookbook", "programming", "examples"),
    #           "If you need help writing programs in Python 3, or want to update older Python 2 code, this book is "
    #           "just the ticket. Packed with practical recipes written and tested with Python 3.3, this unique "
    #           "cookbook is for experienced Python programmers who want to focus on modern tools and idioms.")
    # books = (b1, b2, b3)

    books_repo = BookRepository("books.json", Book)
    # for book in books:
    #     books_repo.create(book)
    #
    # for book in books_repo.find_all():
    #     print(book)
    #
    # print("\nBook titles containing 'Python':")
    # for book in books_repo.find_by_title("Python"):
    #     print(book)
    #
    # print("\nBook titles containing 'learning':")
    # for book in books_repo.find_by_title("learning"):
    #     print(book)
    #
    # print("\nBook authors containing 'Lutz':")
    # for book in books_repo.find_by_author("Lutz"):
    #     print(book)

    book_controller = BookController(books_repo)

    # for book in books:
    #     book_controller.add_book(book)
    #
    # for book in book_controller.get_all_books():
    #     print(book)
    #
    # books_repo.save()

    # Book JSON repository demo
    entity_class = Book
    books_repo.load()

    it = iter(books_repo)
    try:
        while True:
            # it.__next__()
            print(next(it))
    except StopIteration:
        pass
    print()
    for book in books_repo:
        print(book)

    # # Login demo
    # user_repo = UserRepository("users.json", User)
    # entity_class = User
    # user_repo.load()
    # for user in user_repo.find_all():
    #     print(user)
    #
    # login_controller = LoginController(user_repo)
    # # login_controller.register(User(None, "Deafult", "Admin", "admin", "admin", "ADMIN"))
    # MAIN_MENU_ITEMS = [
    #     MenuItem("Register new user", RegisterCommand(login_controller)),
    #     MenuItem("Login", LoginCommand(login_controller)),
    #     MenuItem("Logout", LogoutCommand(login_controller)),
    #     MenuItem("Show logged user", GetLoggedUserCommand(login_controller)),
    # ]
    # main_menu = Menu(MAIN_MENU_ITEMS)
    # main_menu.show()
    # print("Good bye!")