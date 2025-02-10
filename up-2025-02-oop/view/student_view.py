from model.student import Student
from model.student_repository import StudentRepository


class StudentView:
    def __init__(self, student_repo: StudentRepository):
        self.student_repo = student_repo

    def input(self):
        s = Student()
        # input name with validation
        while True:
            s.name = input('Name: ').strip()
            if s.name:
                break
            print('Name cannot be blank.')

        # input fn with validation
        while True:
            s.fn = input('FN: ').strip()
            if len(s.fn) > 4:
                break
            print('FN should be at least 5 characters long.')

        # input semester with validation
        while True:
            try:
                s.semester = int(input('Semester: '))
            except ValueError:
                print('Semester should be a number.')
            if 1 <= len(s.semester) <= 10:
                break
            print('Valid semesters are between 1 and 10.')

        self.student_repo.add(s)

