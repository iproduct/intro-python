
class User:
    """Book library user"""
    def __init__(self, id = None, fname=None, lname=None, username=None, password=None, roles=["Reader"]):
       self.id = id
       self.fname = fname
       self.lname = lname
       self.username = username
       self.password = password
       self.roles = roles

    def __str__(self):
        return f"Name: {self.fname} {self.lname}, Username: {self.username}, Roles: {', '.join(self.roles)}"

class Admin(User):
    def __init__(self, id = None, fname=None, lname=None, username=None, password=None,
                 roles=["Admin"], books_added = [], users_added = []):
        # User.__init__(self, id, fname, lname, username, password, roles)
        super().__init__(id, fname, lname, username, password, roles)
        self.books_added = books_added
        self.users_added = users_added

    def __str__(self):
        # return f"{User.__str__(self)}, Books: {self.books_added}, Users: {self.users_added}"
        return f"{super().__str__()}, Books: {self.books_added}, Users: {self.users_added}"


if __name__ == "__main__":
    a1 = Admin(1, "Default", "Admin", "admin", "admin", books_added=["Python Intro", "Decorators in Python"])
    print(a1)