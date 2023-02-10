from person import Person

ADMIN = "Admin"
USER = "User"

class User(Person):
    def __init__(self, id, name, age, username, password, role=USER):
        super().__init__(id, name, age)
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f'{super().__str__()}, Username: {self.username}, Pass: {self.password}, Role: {self.role}'