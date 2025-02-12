from model.student import Student


class StudentRepository:
    def __init__(self, students=None):
        self.__students = students if students is not None else []
    def add(self, student):
        self.__students.append(student)
    @property
    def students(self):
        return self.__students
    @students.setter
    def students(self, students):
        self.__students = students
    def __len__(self):
        return len(self.__students)
    def __iter__(self):
        return iter(self.__students)


if __name__ == '__main__':
    course1_repo = StudentRepository()
    course2_repo = StudentRepository()
    george = Student('George', '0PH23235', 1)
    course1_repo.add(george)
    trayan = Student('Trayan Iliev', '0MI12345', 2)
    course2_repo.add(trayan)
    print(course1_repo.students)
    print(course2_repo.students)
    print(course2_repo._StudentRepository__students)



