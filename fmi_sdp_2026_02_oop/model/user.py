class User:
    def __init__(self, username=None, password=None, email=None,
                 fname=None, lname=None, roles=None, id=None):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.email = email
        self.username = username
        self.password = password
        self.roles = roles

    def __repr__(self):
        return (f"User({self.id}, {self.username}, {self.fname}, {self.lname}, "
                f"{self.email}, {self.password}, {self.roles})")