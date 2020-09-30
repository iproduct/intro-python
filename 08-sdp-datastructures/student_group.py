# import student
from student import Student

class StudentGroup:
    def __init__(self, name, students):
        self.__name = name
        self.__students = students
        self.__index = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, value):
        self.__students = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == len(self.students):
            raise StopIteration
        student = self.students[self.__index]
        self.__index += 1
        return student

if __name__ == '__main__':
    sg1 = StudentGroup('Student Group 1', [
        Student('7009122345', 'Dimitar', 'Georgiev', 'Plovdiv', '+359889675432',
                     ['Algebra', 'SDP', 'Calculus', 'Internet Programming']),
        Student('7609223412', 'Dimitar', 'Atanasov', 'Sofia 1000', '+359889675432',
                ['Algebra', 'SDP', 'Calculus', 'Practical Robotics']),
        Student('6009052345', 'Elena', 'Petkova', 'Sofia, Graf Ignatiev, 23', '+359889675432',
                ['Algebra', 'SDP', 'Calculus', 'Differential Equations']),
        Student('8009122345', 'Gergana', 'Georgieva', 'Ruse', '+359889675432',
                ['Algebra', 'SDP', 'Calculus']),
        Student('9001172345', 'Stefan', 'Hristov', 'Varna', '+359889675432',
                ['Algebra', 'SDP', 'Calculus', 'Python Programming']),
    ])

    # test iteratior
    for student in sg1:
        print(student)