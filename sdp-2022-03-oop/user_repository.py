from student import User

class UserRepoIterator:
    def __init__(self, user_repo):
        self._user_repo = user_repo
        self._next_index = -1
        self._values = self._user_repo.findAll()

    def __next__(self):
        if self._next_index == len(self._user_repo) - 1:
            raise StopIteration()
        self._next_index += 1
        return self._values[self._next_index]


class UserRepository:
    next_id = 0

    # @staticmethod
    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self):
        self._users = []

    def create(self, user):
        user.id = UserRepository.get_next_id()
        self._users.append(user)
        return user

    def findAll(self):
        return self._users

    def __len__(self):
        return len(self._users)

    # def __iter__(self):
    #     return UserRepoIterator(self)

    # def __iter__(self):
    #     return iter(self._users)

    def __iter__(self):
       for user in self._users:
           yield user


if __name__ == '__main__':
    john = User('John', 'Doe', 'john.doe@gmail.com', 48, 'john', 'john123', 'Admin')
    jane = User('Jane', 'Doe', 'jane.doe@gmail.com', 27, 'jane', 'jane123', 'Admin')
    sam = User('Sam', 'Neuman', 'sam@gmail.com', 42, 'sam', 'sam123', 'User')

    user_repo = UserRepository()
    user_repo.create(john)
    user_repo.create(jane)
    user_repo.create(sam)

    # all_users = user_repo.findAll()

    for user in user_repo:
        print(user)

    for user in user_repo:
        print(user)
