from datetime import date, datetime
from model.person import Person

class Instructor(Person):
    def __init__(self, name = None, bdate = None, department = None, courses = None, emp_start_date = None):
        super().__init__(name, bdate)
        self.emp_start_date = datetime.strptime(emp_start_date, '%d.%m.%Y').date() if emp_start_date is not None else None
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
    instructors = [
        Instructor('Georgi Petrov', '23.07.1999', 'IT', ['UP', 'SDP'], '01.09.2010'),
        Instructor('Hristina Dimitrova', '07.05.2005', 'IT', ['UP', 'SDP'], '01.03.2015'),
        Instructor('Ivan Genov', '21.09.1982', 'IT', ['UP', 'SDP'], '01.07.2003'),
    ]
    print_instructors(instructors)
