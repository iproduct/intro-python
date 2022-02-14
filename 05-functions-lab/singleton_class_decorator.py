from functools import wraps


def singleton(cls):
    """Make a class Singleton class (only one instance)"""
    @wraps(cls)
    def singleton_wrapper(*args, **kwargs):
        if not singleton_wrapper._instance:
            singleton_wrapper._instance = cls(*args, **kwargs)
        return singleton_wrapper._instance
    singleton_wrapper._instance = None
    return singleton_wrapper


User = str

@singleton
class UserRepository:
    def __init__(self):
        self.users = {}

    def create(self, user: User) -> User:
        self.users[user] = user
        return user

    def findAll(self):
        return self.users.values()

@singleton
class BookRepository:
    def __init__(self):
        self.books = {}

    def create(self, book: User) -> User:
        self.books[book] = book
        return book

    def findAll(self):
        return self.books.values()

if __name__ == "__main__":
    repo1 = UserRepository()
    repo2 = UserRepository()
    repo1.create("John")
    repo1.create("Jane")
    print(list(repo2.findAll()))

    repo3 = BookRepository()
    repo4 = BookRepository()
    repo3.create("Python101")
    repo3.create("Pyton201")
    print(list(repo4.findAll()))
