from datetime import date, datetime

class Person:
    """Models a phisical person"""
    _next_id = 0

    @classmethod
    def get_next_id(cls):
        cls._next_id += 1
        return cls._next_id

    def __init__(self, name = None, bdate = None):
        self._id = self.__class__.get_next_id()
        self._name = name
        self.birth_date = datetime.strptime(bdate, '%d.%m.%Y').date() if bdate is not None else None

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

    def __str__(self):
        return f'| {self.id:>3d} | {self.name:30s} | {self.birth_date.strftime("%d.%m.%Y"):10s} | {self.get_age():3d} |'

    def __repr__(self):
        return f'Person({self._id}, {self._name}, {self.birth_date.strftime("%d.%m.%Y")})'


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


class Instructor(Person):
    def __init__(self, name, bdate, department, courses, emp_start_date):
        super().__init__(name, bdate)
        self.emp_start_date = datetime.strptime(emp_start_date, '%d.%m.%Y').date()
        self.courses = courses
        self.department = department

    def __str__(self):
        return f'{super().__str__()} {str(self.department):12s} | {", ".join(self.courses):30} | {self.get_experience_years():3d} |'
    def __repr__(self):
        return f'Instructor({self.id}, {str(self.fn)}, {self.name}, {self.birth_date}, {self.department}, {self.courses}, {self.emp_start_date})'

    def get_experience_years(self):
        today = date.today()
        exp = today.year - self.emp_start_date.year
        if today.month < self.emp_start_date.month or (
                today.month == self.emp_start_date.month and today.day < self.emp_start_date.day):
            exp -= 1
        return exp

def print_instructors(instructors):
    print(f'| {"ID":>3s} | {"Name":^30s} | {"Birth Date":^10s} | {"Age":^3s} | {"Department":^12s} | {"Courses":^30s} | {"Exp":^3s} |')
    for instructor in instructors:
        print(instructor)

if __name__ == '__main__':
    students = [
        Student('65300', 'Georgi Petrov', '23.07.1999'),
        Student('65301', 'Hristina Dimitrova', '07.05.2005', 2),
        Student('65305', 'Ivan Genov', '21.09.1982', 2),
    ]
    print_students(students)

    p1 = Person('Hristo Stoilov', '18.09.1985')
    print(p1)

    instructors = [
        Instructor('Georgi Petrov', '23.07.1999', 'IT', ['UP', 'SDP'], '01.09.2010'),
        Instructor('Hristina Dimitrova', '07.05.2005', 'IT', ['UP', 'SDP'], '01.03.2015'),
        Instructor('Ivan Genov', '21.09.1982', 'IT', ['UP', 'SDP'], '01.07.2003'),
    ]
    print()
    print_instructors(instructors)
