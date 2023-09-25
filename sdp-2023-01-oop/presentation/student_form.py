import re
from datetime import datetime

from business.student_controller import StudentController
from dao.student_repository import StudentRepository
from model.student import Student, print_students


class StudentForm:
    def __init__(self, controller: StudentController) -> None:
        self._student_controller = controller

    def execute(self):
        s = Student()
        while True:
            s.name  = input('Input name: ')
            if len(s.name) >= 5 and len(s.name) <=40:
                break
            else:
                print('Invalid name - should be between 5 and 40 chars long. Try again.')
        while True:
            s.fn  = input('Input FN: ')
            if re.match(r'^(\d{5,6}|\dMI\d{7})$', str(s.fn)) is not None:
                break
            else:
                print('Invalid faculty number. Try again.')
        while True:
            bdate  = input('Input birth date: ')
            if re.match(r'^\d{2}\.\d{2}\.\d{4}$', bdate) is not None:
                s.birth_date = datetime.strptime(bdate, '%d.%m.%Y').date()
                break
            else:
                print('Invalid date - ex.: "05.07.2003". Try again.')
        while True:
            try:
                course  = int(input('Student course: '))
            except ValueError:
                print('Invalid course should be a number between 1 and 4. Try again.')
            if course >= 1 and course <=4:
                s.course = course
                break
            else:
                print('Invalid course should be a number between 1 and 4. Try again.')

        self._student_controller.add_student(s)


if __name__ == '__main__':
    students = [
        Student('65300', 'Georgi Petrov', '23.07.1999'),
        Student('65301', 'Hristina Dimitrova', '07.05.2005', 2),
        Student('65305', 'Ivan Genov', '21.09.1982', 2),
        Student('65306', 'Georgi Genov', '21.09.1982', 3),
        Student('65307', 'Temenuzka Georgieva', '21.09.1982', 4),
    ]
    repo = StudentRepository(students, 'students.json')
    controller: StudentController = StudentController(repo)
    form = StudentForm(controller)
    form.execute()
    print_students(controller.get_all_students())