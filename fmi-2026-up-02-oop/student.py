class Student(object):
    next_id = 0

    # @staticmethod
    # def get_next_id():
    #     Student.next_id += 1
    #     return Student.next_id

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self, fn, first_name, last_name, course):
        self.id = self.get_next_id()
        self._fn = fn
        self.first_name = first_name
        self.last_name = last_name
        self.course = course

    @property
    def fn(self):
        return self._fn

    @fn.setter
    def fn(self, fn):
        self._fn = fn

    def __repr__(self):
        return f'{self.id}, FN:{self._fn}: {self.first_name} {self.last_name}, {self.course} course'

    def set_course(self, course):
        self.course = course


if __name__ == '__main__':
    ivan = Student('0MI8000023', 'Ivan', 'Petrov', 2)
    print(ivan)
    ivan.set_course(3)
    print(ivan)
    petar = Student('0MI8000024', 'Petar', 'Hristov', 1)
    print(petar)
    petar.set_course(2)
    petar.fn = '0CH8000092'
    print(petar)
    students = [ivan, petar]
    for student in students:
        print(f'| {student.id:2d} | {student.fn:9s} | {student.first_name:12s} | {student.last_name:12s} | {student.course:1d} |')
