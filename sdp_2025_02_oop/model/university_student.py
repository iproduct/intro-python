from model.student import Student


class UniversityStudent(Student):
    def __init__(self, name = None, fn = None, semester = None, university = None):
        # Student.__init__(self, name, fn, semester)
        super().__init__(name, fn, semester)
        self.university = university

    def __str__(self):
        return super().__str__() + f', University: {self.semester}'

    def __repr__(self):
        return f'University Student({self.name}, {self.fn}, {self.semester}, {self.university})'

if __name__ == '__main__':
    us1 = UniversityStudent('John Smith', '0MI123456' ,5 , 'SU')
    print(us1)