from dao.persistable import Persistable
from dao.repository import Repository
from model.student import Student, print_students


class StudentRepository(Repository, Persistable):
    def __init__(self, initial_students_list=None, file_name='students.json'):
        Repository.__init__(self, initial_students_list)
        Persistable.__init__(self, file_name, Student)
    def find_by_fn(self, fn: str) -> list[Student]:
        return [s for s in self.find_all() if s.fn == str(fn)]

    def find_by_name(self, name_part: str) -> list[Student]:
        return [s for s in self.find_all() if name_part.lower() in s.name.lower()]

if __name__ == '__main__':
    students = [
        Student('65300', 'Georgi Petrov', '23.07.1999'),
        Student('65301', 'Hristina Dimitrova', '07.05.2005', 2),
        Student('65305', 'Ivan Genov', '21.09.1982', 2),
        Student('65306', 'Georgi Genov', '21.09.1982', 3),
        Student('65307', 'Temenuzka Georgieva', '21.09.1982', 4),
    ]
    students[1].name = 'Hristina Dimitrova-Georgieva'
    repo = StudentRepository(students, 'students.json')
    repo.append(Student('68359', 'Atanas Petrov', '18.11.1979', 4))

    for student in repo:
        print(student)
    print(f'Number of students: {len(repo)}')

    print()
    print(repo.find_by_id(2))
    print()
    print(repo.find_by_fn('65305'))
    print()
    print_students(repo.find_by_name('Georgi'))

    print()
    print(repo.find_by_id(2).id)

    repo.save()

    repo_from_file = StudentRepository()
    repo_from_file.load()

    print_students(repo_from_file.find_all())

