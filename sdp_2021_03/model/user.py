from functools import total_ordering

# from decorators import trace_get_attributes
import decorators as dec

# @dec.trace_get_attributes
@total_ordering
class User:
    next_id = 0

    # @staticmethod
    # def increment_next_id():
    #     User.next_id += 1

    @classmethod
    def increment_next_id(cls):
        cls.next_id += 1

    def __init__(self, name, email, password, role = 'user'):
        self.__class__.increment_next_id()
        self.id = self.__class__.next_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Email: {self.email}, Role: {self.role}'

    def __repr__(self):
        return f'User[ ID: {self.id}, Name: {self.name}, Email: {self.email}, Role: {self.role}]'

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return (self.name, self.id) < (other.name, other.id)

    def check_password(self, password: str) -> bool:
        return password == self.password

class Author(User):
    def __init__(self, name, email, password, rank = 'beginner'):
        super().__init__(name, email, password, 'user')
        self.rank = rank
    def __str__(self):
        return f'Author({super().__str__()}, Rank: {self.rank})'

class Admin(User):
    def __init__(self, name, email, password, phone):
        super().__init__(name, email, password, 'admin')
        self.phone = phone
    def __str__(self):
        return f'Admin({super().__str__()}, Phone: {self.phone})'

default_admin = Admin('Admin Admin', 'admin@mycompany.com', 'admin123', '35928976564')

if __name__ == '__main__':
    users: list[User] = [
        Author('Ivan Petrov', 'ivanp@abv.bg', 'ivanp123'),
        Admin('Admin Admin', 'admin@mycompany.com', 'admin123', '35928976564'),
        Admin('Nadezda Hristova', 'nadia@mycompany.com', 'nadia123', '3592754632'),
        Admin('Admin Admin', 'admin2@mycompany.com', 'admin123', '3592897655'),

    ]

    for user in sorted(users):
        print(user)

    print(users[0].check_password('ivanp123')) # True
    print(users[0].check_password('ivanpetrov')) # False
    # print(users[0].__dict__)
    # print(User.__dict__)
