from dao.json_repository import JsonRepository
from model.book import Book
from model.user import User

if __name__ == '__main__':
    ivan = User('Ivan', 'Petrov', 'ivan', 'ivan123', 'Admin')
    petar = User('Petar', 'Hristov', 'peter', 'petar123', 'User')
    john = User('John', 'Doe', 'john', 'john123', 'Admin')
    jane = User('Jane', 'Doe', 'jane', 'jane123', 'Admin')
    sam = User('Sam', 'Neuman', 'sam', 'sam123', 'User')
    users = [ivan, petar, john, jane, sam]
    #
    user_repo = JsonRepository('users.json', {"User": User})
    for user in users:
        user_repo.create(user)
    user_repo.save()
    user_repo.load()


    # all_users = user_repo.findAll()

    for user in user_repo:
        print(user)

    # Books demo
    user_repo = JsonRepository('books.json', {"User": User, "Book": Book})
