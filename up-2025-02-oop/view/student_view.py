from model.student import Student
from dao.student_repository import StudentRepository


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
                continue
            if 1 <= s.semester <= 10:
                break
            print('Valid semesters are between 1 and 10.')

        self.student_repo.add(s)

if __name__ == '__main__':
    students_book = StudentRepository()
    george = Student('George', '0PH23235', 1)
    students_book.add(george)
    trayan = Student('Trayan Iliev', '0MI12345', 2)
    students_book.add(trayan)

    # create view using repository
    student_view = StudentView(students_book)
    student_view.input()
    for s in students_book:
        print(s)
    print(f'Total number of students: {len(students_book)}')