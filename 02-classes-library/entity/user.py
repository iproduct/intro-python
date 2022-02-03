
class User:
    def __init__(self, id = None, first_name = None, last_name = None,
                 username = None, password = None, role="READER", active=True):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.role = role
        self.active = active

    def __str__(self):
        return f"| {self.id:>12.12s} | {self.first_name:<15.15s} | {self.last_name:<15.15s} | " \
               f"{self.username:<15.15s} | {self.password:<15.15s} | " \
               f"{self.role:<15.15s} | {self.active} |"