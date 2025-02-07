class Student:
    def __init__(self, name, fn, semester):
       self.name = name
       self.semester = semester
       self.fn = fn
    def change_semester(self, new_semester):
        self.semester = new_semester
    def __str__(self):
        return f'Student(Name: {self.name}, FN:{self.fn}, Sem: {self.semester})'

if __name__ == '__main__':
    trayan = Student('Trayan Iliev', '0MI12345', 2)
    print(trayan)
    print(trayan.fn)
    trayan.change_semester(3)
    print(trayan)