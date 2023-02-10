class Person(object):
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Age: {self.age}'

    def __eq__(self, other):
        return self.id == other.id

