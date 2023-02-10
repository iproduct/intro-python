class Student:
    num_students = 0
    def __init__(self, name, age):
        self.__class__.num_students += 1
        self.id = Student.num_students
        self.name = name
        self.age = age

    def __str__(self):
        return f'ID:{self.id}, Name:{self.name}, Age: {self.age}'

    def get_increment_age(self):
        self.age += 1
        return self.age

    def set_age(self, new_age):
        self.age = new_age

if __name__ == '__main__':
    s1 = Student('Ivan Petrov', 25)
    print(s1)
    print('Age:', s1.age)
    s1.age = 30
    print(s1)
    print('Age after increment:', s1.get_increment_age())
    print(s1)
    s1.set_age(40)
    print(s1)
    s2 = Student('Dimitar Georgiev', 30)
    s3 = Student('Maria Petrova', 22)
    students = [s1, s2, s3]
    for s in students:
        print(s)