class Person:
    def __init__(self, name = None, address = None, phone = None, email = None, pid = None):
        self.id = pid
        self.email = email
        self.phone = phone
        self.address = address
        self.name = name

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Addr:{self.address}, Phone: {self.phone}, Email: {self.email}'