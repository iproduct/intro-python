from person import Person
from student import Student

ADMIN = "Admin"
USER = "User"

class User(Person, Student):
    def __init__(self, id, name, age, username, password, role=USER):
        super().__init__(id, name, age)
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f'{super().__str__()}, Username: {self.username}, Pass: {self.password}, Role: {self.role}'

if __name__ == '__main__':
    p1 = Person(1, 'Ivan Petrov', 35)
    print(p1, type(p1))
    u2 = User(2, 'John Doe', 42, 'john', 'john123', ADMIN)
    u3 = User(3, 'Jane Doe', 29, 'jane', 'jane123')
    print(u2, type(u2))
    print(f'Is u2 User?: {isinstance(u2, User)}')
    print(f'Is u2 Person?: {isinstance(u2, Person)}')
    print(f'Is u2 object?: {isinstance(u2, object)}')
    print(f'Is u2 dict?: {isinstance(u2, dict)}')