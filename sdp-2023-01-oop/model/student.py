from model.person import Person

class Student(Person):
    """Models a student in learning management system"""

    def __init__(self, fn = None, name = None, bdate = None, course=1):
        super().__init__(name, bdate)
        self.fn = fn
        self.course = course

    def __str__(self):
        return f'{super().__str__()} {str(self.fn):>8s} | {self.course:6d} |'
    def __repr__(self):
        return f'Student({self.id}, {str(self.fn)}, {self.name}, {self.birth_date.strftime("%d.%m.%Y")}, {self.course})'


def print_students(students):
    print(f'| {"ID":>3s} | {"Name":^30s} | {"Birth Date":^10s} | {"Age":^3s} | {"FN":^8s} | {"Course":^6s} |')
    for student in students:
        print(student)


if __name__ == '__main__':
    students = [
        Student('65300', 'Georgi Petrov', '23.07.1999'),
        Student('65301', 'Hristina Dimitrova', '07.05.2005', 2),
        Student('65305', 'Ivan Genov', '21.09.1982', 2),
    ]
    print_students(students)