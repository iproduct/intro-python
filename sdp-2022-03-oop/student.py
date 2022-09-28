from datetime import datetime

class Person:

    def __init__(self, fname, lname, email, age):
        self.id = 0
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
        self._password = password
        self.role = role

    @property
    def password(self):
        # print(f"Password of user '{self.username}' was accessed on {datetime.now().isoformat(timespec='seconds')}")
        return self._password

    @password.setter
    def password(self, new_pass):
        # print(f"Password of user '{self.username}' was CHANGED on {datetime.now().isoformat(timespec='seconds')}")
        self._password = new_pass

    def __str__(self):
        return f"{super().__str__()} {self.username:<12} | {self.password:<12} | {self.role:^6} |"

# TODO: Implement class Student inheriting from User, with following attributes:
# fn, year, courses, grades (dict from course_id to the grade for the course)

# TODO: Implement class Course with following attributes:
# id, name, credits, description

print(__name__)

if __name__ == '__main__':
    ivan = Person('Ivan', 'Petrov', 'ivanp@abv.bg', 28)
    petar = Person('Petar', 'Hristov', 'peterh@gmail.com', 35)
    john = User('John', 'Doe', 'john.doe@gmail.com', 48, 'john', 'john123', 'Admin')
    jane = User('Jane', 'Doe', 'jane.doe@gmail.com', 27, 'jane', 'jane123', 'Admin')
    sam = User('Sam', 'Neuman', 'sam@gmail.com', 42, 'sam', 'sam123', 'User')
    persons = [ivan, petar, john, jane, sam]
    john.password = 'NEW_PASSS'
    for person in persons:
        print(person.__str__())
