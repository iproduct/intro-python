from datetime import date, datetime

class Person:
    """Models a phisical person"""
    _next_id = 0

    @classmethod
    def get_next_id(cls):
        cls._next_id += 1
        return cls._next_id

    def __init__(self, fn, name, bdate, course=1):
        self._id = self.__class__.get_next_id()
        self._name = name
        self.birth_date = datetime.strptime(bdate, '%d.%m.%Y').date()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or (today.month == self.birth_date.month and today.day < self.birth_date.day):
            age -= 1
        return age

class Student(Person):
    """Models a student in learning management system"""

    def __init__(self, fn, name, bdate, course=1):
        self.fn = fn
        self.course = course

    def __str__(self):
        return f'| {self._id:>3d} | {str(self.fn):>8s} | {self._name:30s} | {self.birth_date.strftime("%d.%m.%Y"):10s} | {self.get_age():3d} | {self.course:6d} |'
    def __repr__(self):
        return f'Student({self._id}, {str(self.fn)}, {self._name}, {self.birth_date.strftime("%d.%m.%Y")}, {self.get_age()}, {self.course})'


def print_students(students):
    print(f'| {"ID":>3s} | {"FN":^8s} | {"Name":^30s} | {"Birth Date":^10s} | {"Age":^3s} | {"Course":^6s} |')
    for student in students:
        print(student)


if __name__ == '__main__':
    students = [
        Student('65300', 'Georgi Petrov', '23.07.1999'),
        Student('65301', 'Hristina Dimitrova', '07.05.2005', 2),
        Student('65305', 'Ivan Genov', '21.09.1982', 2),
    ]
    print_students(students)