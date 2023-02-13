from addressable import Addressable
from person import Person
from student import Student

ADMIN = "Admin"
USER = "User"

class User(Person, Addressable):
    def __init__(self, id, name, age, username, password, addr, role=USER):
        super().__init__(id, name, age)
        Addressable.__init__(self, addr.address, addr.street, addr.city, addr.country)
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f'{Person.__str__(self)}, Username: {self.username}, Pass: {self.password}, Role: {self.role}, Address:{Addressable.__repr__(self)}'

if __name__ == '__main__':
    p1 = Person(1, 'Ivan Petrov', 35)
    print(p1)
    u2 = User(2, 'John Doe', 42, 'john', 'john123', Addressable('1000', 'J. Bouchier', 'Sofia'), ADMIN)
    u3 = User(3, 'Jane Doe', 29, 'jane', 'jane123', Addressable('2000', 'J. Bouchier', 'Sofia'))
    print(u2)
    print(u2.city)
    print(u3)
    print(f'Is u2 User?: {isinstance(u2, User)}')
    print(f'Is u2 Person?: {isinstance(u2, Person)}')
    print(f'Is u2 Addresable?: {isinstance(u2, Addressable)}')
    print(f'Is u2 object?: {isinstance(u2, object)}')
    print(f'Is u2 dict?: {isinstance(u2, dict)}')
    print(u2.get_label())
    print(u2.say_hi())
