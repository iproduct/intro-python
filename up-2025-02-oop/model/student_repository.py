from model.student import Student


class StudentRepository:
    def __init__(self, students=None):
        self._students = students if students is not None else []
    def add(self, student):
        self._students.append(student)
    def get_all(self):
        return self._students


if __name__ == '__main__':
    course1_repo = StudentRepository()
    course2_repo = StudentRepository()
    george = Student('George', '0PH23235', 1)
    course1_repo.add(george)
    trayan = Student('Trayan Iliev', '0MI12345', 2)
    course2_repo.add(trayan)
    print(course1_repo.get_all())
    print(course2_repo.get_all())



