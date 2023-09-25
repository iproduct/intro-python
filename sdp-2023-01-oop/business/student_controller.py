import re

from dao.student_repository import StudentRepository
from exceptions.invalid_entity_data import InvalidEntityData
from model.student import Student


class StudentController:
    def __init__(self, student_repo: StudentRepository):
        self._student_repo: StudentRepository = student_repo

    def add_student(self, student: Student):
        self.validate_student(student)
        self._student_repo.append(student)

    def validate_student(self, student: Student):
        violations: list[str] = []
        name_len = len(student.name.strip())
        if  name_len < 5 or name_len > 40:
            violations.append(f'Student name should be between 5 and 40 characters long: "{student.name}"')
        if re.match(r'^(\d{5,6}|\dMI\d{7})$', student.fn) is None:
            violations.append(f'Faculty number should be in 5 or 6 digits OR "<digit>MI<7_digits>" format: "{student.fn}"')

        if len(violations) > 0:
            raise InvalidEntityData('Invalid student data', violations)

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
    controller.add_student(Student('68359', 'Atanas Georgiev', '18.11.1979', 4))