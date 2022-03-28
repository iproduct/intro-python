class Person:
    # nextId = 0
    # @staticmethod
    # def get_next_id():
    #     __class__.nextId += 1
    #     return __class__.nextId

    # @classmethod
    # def get_next_id(cls):
    #     cls.nextId += 1
    #     return cls.nextId

    def __init__(self, f_name, l_name, age, id = None):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

    def __str__(self):
        return f'{self.id}) {self.f_name} {self.l_name}: {self.age}'

    def get_formatted_str(self):
        return f'| {str(self.id):24s} | {self.f_name:15.15s} | {self.l_name:15.15s} | {self.age:3d} |'

if __name__ == "__main__":
    p1 = Person('Ivan', 'Petrov', 25)
    p2 = Person('Dimitar', 'Hristov', 35)
    p3 = Person('Maria', 'Georgieva', 27)
    persons = [p1, p2, p3]
    print(p1.f_name, p1.l_name, ": ", p1.age)
    print(p1)
    p1_mname = getattr(p1, "m_name", "<not available>")
    print(p1_mname)

    for p in persons:
        print(p.get_formatted_str())

    # print('Class Person.__dict__:', Person.__dict__)

