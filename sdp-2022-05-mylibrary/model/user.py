import uuid

class User:
    def __init__(self, fname = None, lname = None, username = None, password = None, role=None, active = True, id = None):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password
        self.role = role
        self.active = active

    def __str__(self):
        return f"| {self.id!s:>28} | {self.fname + ' ' + self.lname:<25} | {self.username!s:<12} " \
               f"| {self.password!s:<12} | {self.role!s:^6} | {self.active!s:^5} |"

if __name__ == '__main__':
    ivan = User('Ivan', 'Petrov', 'ivan', 'ivan123', 'Admin')
    petar = User('Petar', 'Hristov', 'peter', 'petar123', 'User')
    john = User('John', 'Doe', 'john', 'john123', 'Admin')
    jane = User('Jane', 'Doe', 'jane', 'jane123', 'Admin')
    sam = User('Sam', 'Neuman', 'sam', 'sam123', 'User')
    persons = [ivan, petar, john, jane, sam]
    for person in persons:
        print(person.__str__())
