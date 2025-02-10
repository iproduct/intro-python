all_students = []


class Student:
    next_id = 0

    # @staticmethod
    # def get_next_id():
    #     __class__.next_id += 1
    #     return __class__.next_id

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id


    def __init__(self, name = None, fn = None, semester = None):
        # self.__class__.next_id += 1
        self._id = self.__class__.get_next_id()
        self.name = name
        self.semester = semester
        self.fn = fn

    @property
    def id(self):
        return self._id

    def change_semester(self, new_semester):
        self.semester = new_semester

    def __repr__(self):
        return f'Student(ID: {self.id}, Name: {self.name}, FN:{self.fn}, Sem: {self.semester})'

if __name__ == '__main__':
    trayan = Student('Trayan Iliev', '0MI12345', 2)
    print(f'Trayan\'s ID: {trayan.id}')
    print(trayan)
    print(trayan.fn)
    trayan.change_semester(3)
    print(f'{id(trayan)}: {trayan}')

    george = Student('George', '0PH23235', 1)
    print(f'{id(george)}: {george}')

    all_students.append(trayan)
    all_students.append(george)

    print(all_students)
