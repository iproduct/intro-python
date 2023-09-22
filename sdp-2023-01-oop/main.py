from datetime import date, datetime

class Student:
    """Models a student in learning management system"""

    def __init__(self, fn, name, bdate, course=1):
        self.fn = fn
        self.name = name
        self.birth_date = datetime.strptime(bdate, '%d.%m.%Y').date()
        self.course = course

    def __str__(self):
        return f'| {str(self.fn):>8s} | {self.name:30s} | {self.birth_date.strftime("%d.%m.%Y"):10s} | {self.get_age():3d} | {self.course:6d} |'

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or (today.month == self.birth_date.month and today.day < self.birth_date.day):
            age -= 1
        return age

def print_students(students):
    print(f'| {"FN":^8s} | {"Name":^30s} | {"Birth Date":^10s} | {"Age":^3s} | {"Course":^6s} |')
    for student in students:
        print(student)


if __name__ == '__main__':
    students = [
        Student('65300', 'Georgi Petrov', '23.07.1999'),
        Student('65301', 'Hristina Dimitrova', '07.05.2005', 2),
        Student('65305', 'Ivan Genov', '21.09.1982', 2),
    ]
    print_students(students)