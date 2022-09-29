from dao.json_repository import JsonRepository
from model.user import User

if __name__ == '__main__':
    # ivan = User('Ivan', 'Petrov', 'ivan', 'ivan123', 'Admin')
    # petar = User('Petar', 'Hristov', 'peter', 'petar123', 'User')
    # john = User('John', 'Doe', 'john', 'john123', 'Admin')
    # jane = User('Jane', 'Doe', 'jane', 'jane123', 'Admin')
    # sam = User('Sam', 'Neuman', 'sam', 'sam123', 'User')
    # users = [ivan, petar, john, jane, sam]
    #
    user_repo = JsonRepository('users.json', User)
    user_repo.load()
    # for user in users:
    #     user_repo.create(user)
    # all_users = user_repo.findAll()


    for user in user_repo:
        print(user)

    # user_repo.save()
