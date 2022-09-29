import random
import uuid

from model.user import User


class Repository:
    def __init__(self):
        self._entities = {}

    def findAll(self):
        return self._entities.values()

    def findById(self, id):
        return self._entities[id]

    def create(self, user):
        if user.id is None:
            user.id = str(uuid.uuid4())
        self._entities[user.id] = user
        return user

    # TODO implement update and delete methods

    def __len__(self):
        return len(self._entities)

    def __iter__(self):
        for id in self._entities:
            yield self._entities[id]


if __name__ == '__main__':
    ivan = User('Ivan', 'Petrov', 'ivan', 'ivan123', 'Admin')
    petar = User('Petar', 'Hristov', 'peter', 'petar123', 'User')
    john = User('John', 'Doe', 'john', 'john123', 'Admin')
    jane = User('Jane', 'Doe', 'jane', 'jane123', 'Admin')
    sam = User('Sam', 'Neuman', 'sam', 'sam123', 'User')
    users = [ivan, petar, john, jane, sam]

    user_repo = Repository()
    for user in users:
        user_repo.create(user)
    # all_users = user_repo.findAll()

    for user in user_repo:
        print(user)
