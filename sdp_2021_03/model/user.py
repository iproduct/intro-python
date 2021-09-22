class User:
    next_id = 0

    # @staticmethod
    # def increment_next_id():
    #     User.next_id += 1

    @classmethod
    def increment_next_id(cls):
        cls.next_id += 1

    def __init__(self, name, email, password, role = 'user'):
        self.__class__.increment_next_id()
        self.id = self.__class__.next_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Email: {self.email}, Role: {self.role}'

    def __repr__(self):
        return f'User[ ID: {self.id}, Name: {self.name}, Email: {self.email}, Role: {self.role}]'

    def check_password(self, password: str) -> bool:
        return password == self.password

if __name__ == '__main__':
    users = [
        User('Ivan Petrov', 'ivanp@abv.bg', 'ivanp123'),
        User('Admin Admin', 'admin@mycompany.com', 'admin123', 'admin'),
        User('Nadezda Hristova', 'nadia@mycompany.com', 'nadia123', 'admin'),
        ]
    for user in users:
        print(user.id, user.name)

    print(users[0].check_password('ivanp123')) # True
    print(users[0].check_password('ivanpetrov')) # False