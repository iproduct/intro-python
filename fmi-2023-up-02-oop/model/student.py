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
        self.__id = id
        names = name.strip().split(' ')
        fname = names[0]
        lname = names[-1]
        self.__fname = fname
        self.__lname = lname
        self.__age = age

    @property
    def id(self):
        print(f'Getting Id: {self.__id}')
        return self.__id

    @id.setter
    def id(self, value):
        print(f'Setting Id to: {value}')
        self.__id = value

    @property
    def age(self):
        print(f'Getting Age: {self.__age}')
        return self.__age

    @age.setter
    def age(self, value):
        print(f'Setting Age to: {value}')
        self.__Age = value

    @property
    def name(self):
        print(f'Getting Name: {self.__fname + " " + self.__lname}')
        return self.__fname + ' ' + self.__lname

    @name.setter
    def name(self, value):
        print(f'Setting Name to: {value}')
        names = value.strip().split(' ')
        self.__fname = names[0]
        self.__lname = names[-1]

    def __str__(self):
        return f'ID:{self.__id}, Name:{self.__fname} {self.__lname}, Age: {self.__age}'

    def __eq__(self, other):
        return self.__id == other.__id

    def __copy__(self):
        return Student(self.__id, self.__fname + ' ' + self.__lname, self.__age)

    def get_increment_age(self):
        """
        Incremnts and returns student's age
        :return: incremeted age
        """
        self.__age += 1
        return self.__age

    def set_name(self, new_name):
        names = new_name.strip().split(' ')
        fname = names[0]
        lname = names[-1]
        self.__fname = fname
        self.__lname = lname

    def set_age(self, new_age):
        self.__age = new_age

if __name__ == '__main__':
    s1 = Student(1, 'Ivan Petrov', 25)
    print(s1)
    print('Age:', s1.age)
    s1.age = 30
    s1.name = 'John Doe'
    print(s1.name)
    print(s1)
    print('Age after increment:', s1.get_increment_age())
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
    s4.id = 5
    print(s4.id)
    s4.get_increment_age()
    s4.set_name('John Petrov')
    print('Same student:', s1 == s4, s1 is s4)
    print(s1)
    print(s4)