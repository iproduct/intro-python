from student import Student, print_students


class StudentRepository:
    def __init__(self, initial_students_list=None):
        students_list = [] if initial_students_list is None else initial_students_list
        self.students = {s.id: s for s in students_list}

    def find_all(self):
        return list(self.students.values())

    def find_by_id(self, id):
        return self.students[id]
    def find_by_fn(self, fn):
        return [s for s in self.students.values() if s.fn == str(fn)]


if __name__ == '__main__':
    students = [
        Student('65300', 'Georgi Petrov', '23.07.1999'),
        Student('65301', 'Hristina Dimitrova', '07.05.2005', 2),
        Student('65305', 'Ivan Genov', '21.09.1982', 2),
    ]
    repo = StudentRepository(students)
    print_students(repo.find_all())

    print()
    print(repo.find_by_id(2))
    print()
    print(repo.find_by_fn(65305))
