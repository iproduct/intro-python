class Person:
    def __init__(self, name = None, address = None, phone = None, email = None, idf = None):
        self.idf = idf
        self.email = email
        self.phone = phone
        self.address = address
        self.name = name

    def __str__(self):
        return f'ID: {self.idf}, Name: {self.name}, Addr:{self.address}, Phone: {self.phone}, Email: {self.email}'