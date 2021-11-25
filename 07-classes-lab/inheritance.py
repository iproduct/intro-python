
class Person:
    def __init__(self, ssn, name):
        self.ssn = ssn
        self.__name = name

    def __str__(self):
        return f"{self.ssn}: {self.__name}"

class User(Person):
    def __init__(self, ssn, name):
        Person.__init__(self, ssn, name)
        self.ssn = "User_" + str(ssn)
        self.__name = "User_" + name

    def __str__(self):
        return f"{self.ssn}: {self.__name} > from Person: {Person.__str__(self)}"

if __name__ == "__main__":
    # p1 = Person(7912247626, "John Smith")
    # print(p1)
    # print(p1.__name)

    u1 = User(7912247626, "John Smith")
    print(u1)
    # print(u1.__name)
    print(u1._User__name)
    print(u1._Person__name)