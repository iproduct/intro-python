import datetime

class Person(object):
    def __init__(self, ssn, first_name, last_name, address= None, phone=None):
        self.__ssn = ssn
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__phone = phone

    @property
    def ssn(self):
        return self.__ssn

    @ssn.setter
    def ssn(self, value):
        self.__ssn = value

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def age(self):
        year2digits = int(self.ssn[:2])
        if year2digits < 30:
            year_born = 2000 + year2digits
        else:
            year_born = 1900 + year2digits
        month_born = int(self.ssn[2:4])
        day_born = int(self.ssn[4:6])
        now = datetime.datetime.now()
        years = now.year - year_born
        if(month_born < now.month or (month_born == now.month and day_born <= now.day)):
            years += 1
        return years

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    def __str__(self):
        return f'Person[ssn={self.ssn}, first={self.first_name}, last={self.last_name}, age={self.age}, ' \
               f'address={self.address}, phone={self.phone}]'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.ssn == other.ssn;
        return False;


class Student(Person):
    """Student class represents a student participating in courses"""
    def __init__(self, ssn, first_name, last_name, address= None, phone=None, courses=[]):
        # Person.__init__(self, ssn, first_name, last_name, age, address= None, phone=None)
        super().__init__(ssn, first_name, last_name, address= None, phone=None)
        self.__courses = courses

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        self.__courses = value;

    def __str__(self): # method overiding
        # return f'Student[{Person.__str__(self)}, courses={self.__courses}]'
        return f'Student[{super().__str__()}, courses={self.__courses}]'
        # return f'Person[ssn={self.ssn}, name={self.first_name}, last={self.last_name}, age={self.age}, ' \
        #        f'address={self.address}, phone={self.phone}]'


if __name__ == '__main__':
    p1 = Person('9009212345', 'Ivan', 'Petrov')
    print(p1.__str__())
    print(p1.__dir__())
    p2 = Person('7009122345', 'Dimitar', 'Georgiev', 'Sofia 1000', '+359889675432')
    print(p2)
    p3 = Person('7009122345', 'Dimitar', 'Georgiev', 'Plovdiv', '+359889675432')
    print(p3)
    print(f'p1 == p2: {p1 == p2}')
    print(f'p2 == p3: {p2 == p3}')
    s3 = Student('7009272345', 'Dimitar', 'Georgiev', 'Plovdiv', '+359889675432', ['Algebra', 'SDP', 'Calculus'])
    print(s3.__str__())
    print(f'Age: {s3.age}')
