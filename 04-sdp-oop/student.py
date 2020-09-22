import copy

class Student:
    """This class models an individual student"""
    num_students = 0
    def get_next_id():
        __class__.num_students = __class__.num_students + 1
        return __class__.num_students

    def __init__(self, ssn = None, first_name = None, last_name = None, age = 0, middle_name=None):
        self.ssn = ssn
        self.names = []
        self.names.append(first_name)
        if middle_name:
            self.names.append(middle_name)
        self.names.append(last_name)
        self.age = age
        # Student.num_students = Student.num_students + 1
        self.id = self.__class__.get_next_id()

    def __del__(self):
        print(f'Object {self.__str__()} will be destroyed.')

    def __str__(self):
        return f'ID: {self.id}, SSN: {self.ssn}, Name: {self.get_fullname()}, Age: {self.age}'

    def __len__(self):
        return len(self.names)

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.ssn == other.ssn

    def __copy__(self):
        newone = self.__class__.__new__()
        # newone = type(self)()
        newone.__dict__.update(self.__dict__)
        return newone

    def __deepcopy__(self, memodict={}):
        newone = type(self)()
        newone.__dict__.update(self.__dict__)
        newone.names = self.names.copy()
        return newone

    def get_fullname(self):
        return ' '.join(self.names)

def test():
    pass

if __name__ == '__main__':
    s1 = Student('6005112394', 'Ivan', 'Petrov', 65, 'Angelov')
    s2 = Student('9005112394','Dimtar', 'Georgiev', 35)
    s3 = Student('7005112394', 'John', 'Smith', 55)
    s4 = Student('8005114567', 'Vyara', 'Georgieva', 34)
    s5 = Student('8005114567', 'Vyara', 'Smith', 35)
    print(s1.get_fullname())
    print(s2.get_fullname())
    s1.age = s1.age + 1
    print(s1.age)
    print(s1.__getattribute__('age'))
    print(getattr(s1, 'age'))

    setattr(s1, 'birthday', '1990-07-14')
    print(hasattr(s1, 'birthday'))
    print(getattr(s1, 'birthday'))

    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    print(Student.__dict__['get_fullname'](s3))
    print(s1.__dict__)
    print(Student.__dict__)

    print('Number of names:', len(s1))
    print(f'{s1.get_fullname()} is older than {s2.get_fullname()}:', s1 > s2)
    print(f'{s1.get_fullname()} is older than {s3.get_fullname()}:', s1 > s3)
    print(f'{s4.get_fullname()} is same student as {s5.get_fullname()}:', s4 == s5)
    print(f'{s3.get_fullname()} is same student as {s5.get_fullname()}:', s3 == s5)

    s6 = copy.deepcopy(s4)
    print('!!!', s4, id(s4))
    s6.names[1] = 'Dimitrova'
    print('!!!', s6, id(s6))
    print('!!!', s4, id(s4))

    # remove s1 instace
    # del s1
    # print(s1.get_fullname())
    # print(s2.get_fullname())
    print('End of program.')
