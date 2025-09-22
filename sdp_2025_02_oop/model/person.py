class Person:
    # __next_id = 0

    # @staticmethod
    # def get_next_id():
    #     __class__.__next_id += 1
    #     return __class__.__next_id

    # @classmethod
    # def get_next_id(cls):
    #     cls.__next_id += 1
    #     return cls.__next_id

    def __init__(self, name = None, address = None, phone = None, email = None, pid = None):
        self.id = pid
        self.email = email
        self.phone = phone
        self.address = address
        self.name = name

    def name(self):
        return self.name

    def name(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return f'ID: {self.id}, Name: {self.name}, Addr:{self.address}, Phone: {self.phone}, Email: {self.email}'