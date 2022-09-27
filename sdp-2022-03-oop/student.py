class Person:
    next_id = 0
    def __init__(self, fname, lname, email, age):
        self.__class__.next_id += 1
        self.id = Person.next_id
        self.fname = fname
        self.lname = lname
        self.email = email
        self.age = age
    def __str__(self):
        return f"| {self.id:>3} | {self.fname + ' ' + self.lname:<25} | {self.email:<25} | {self.age:>3} |"

class User(Person):
    def __init__(self, fname, lname, email, age, username, password, role):
        super().__init__(fname, lname, email, age)
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f"{super().__str__()} {self.username:<12} | {self.password:<12} | {self.role:^6} |"

if __name__ == '__main__':
    ivan = Person('Ivan', 'Petrov', 'ivanp@abv.bg', 28)
    petar = Person('Petar', 'Hristov', 'peterh@gmail.com', 35)
    john = User('John', 'Doe', 'john.doe@gmail.com', 48, 'john', 'john123', 'Admin')
    jane = User('Jane', 'Doe', 'jane.doe@gmail.com', 27, 'jane', 'jane123', 'Admin')
    sam = User('Sam', 'Neuman', 'sam@gmail.com', 42, 'sam', 'sam123', 'User')
    persons = [ivan, petar, john, jane, sam]
    for person in persons:
        print(person.__str__())