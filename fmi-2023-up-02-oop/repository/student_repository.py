from student import Student


class StudentRepository:
    def __init__(self):
        self.students = []

    def __len__(self):
        return len(self.students)

    def __iter__(self):
        return iter(self.students)

    def add(self, student: Student):
        self.students.append(student)

    def find_all(self):
        return self.students

if __name__ == '__main__':
    repo = StudentRepository()
    repo.add(Student('Ivan Petrov', 25))
    repo.add(Student('Dimitar Georgiev', 30))
    repo.add(Student('Maria Petrova', 22))
    # all_students = repo.find_all()
    for student in repo:
        print(student)
    print('Number of students:', len(repo))