from copy import copy


class Student:
    """
    Models a student in e-learning system
    """
    num_students = 0

    @staticmethod
    def get_next_id():
        Student.num_students += 1
        return Student.num_students

    @classmethod
    def get_next_id(cls):
        cls.num_students += 1
        return cls.num_students

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f'ID:{self.id}, Name:{self.name}, Age: {self.age}'

    def __eq__(self, other):
        return self.id == other.id

    def __copy__(self):
        return Student(self.id, self.name, self.age)

    def get_increment_age(self):
        """
        Incremnts and returns student's age
        :return: incremeted age
        """
        self.age += 1
        return self.age

    def set_age(self, new_age):
        self.age = new_age

if __name__ == '__main__':
    s1 = Student(1, 'Ivan Petrov', 25)
    print(s1)
    print('Age:', s1.age)
    s1.age = 30
    print(s1)
    print('Age after increment:', s1.get_increment_age())
    print(s1)
    s1.set_age(40)
    print(s1)
    s2 = Student(2, 'Dimitar Georgiev', 30)
    s3 = Student(3, 'Maria Petrova', 22)
    students = [s1, s2, s3]
    for s in students:
        print(s)
    print()
    print(s1.__dict__)
    print(Student.__dict__)
    print()
    s4 = copy(s1)
    s4.get_increment_age()
    s4.name = 'John Petrov'
    print('Same student:', s1 == s4, s1 is s4)
    print(s1)
    print(s4)