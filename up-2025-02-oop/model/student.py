from model.person import Person

all_students = []


class Student(Person):
    # next_id = 0

    # @staticmethod
    # def get_next_id():
    #     __class__.next_id += 1
    #     return __class__.next_id

    # @classmethod
    # def get_next_id(cls):
    #     cls.next_id += 1
    #     return cls.next_id


    def __init__(self, name = None, address = None, phone = None, email = None, fn = None, semester = None, sid = None):
        # self.__class__.next_id += 1
        # self._id = self.__class__.get_next_id()
        super().__init__(name, address, phone, email, sid)
        self.semester = semester
        self.fn = fn

    def change_semester(self, new_semester):
        self.semester = new_semester

    def __str__(self):
        return f'{super().__str__()}, FN:{self.fn}, Sem: {self.semester}'

    def __repr__(self):
        return f'Student(ID: {self.id}, Name: {self.name}, FN:{self.fn}, Sem: {self.semester})'

if __name__ == '__main__':
    trayan = Student('Trayan Iliev','Sofia 1000', '0887453214', 'trayan@gmail.com',  '0MI12345', 2, )
    print(f'Trayan\'s ID: {trayan.id}')
    print(trayan)
    print(trayan.fn)
    trayan.change_semester(3)
    print(f'{id(trayan)}: {trayan}')

    george = Student('George', fn = '0PH23235', semester = 1)
    print(f'{id(george)}: {george}')

    all_students.append(trayan)
    all_students.append(george)

    print(all_students)
