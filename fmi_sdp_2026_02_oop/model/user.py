import bcrypt

class User:
    db_filename = 'users'
    # @staticmethod
    # def get_filename():
    #     return User.db_filename
    @classmethod
    def get_filename(cls):
        return cls.db_filename
    def __init__(self, username=None, password=None, email=None,
                 fname=None, lname=None, roles=None, id=None):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.email = email
        self.username = username
        self.password = password
        self.roles = roles

    @property
    def password(self):
        return self.__password.decode(encoding='utf-8')
    @password.setter
    def password(self, password):
        self.__password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt( 12 ))

    def __repr__(self):
        return (f"User: {self.id}, {self.username}, {self.fname}, {self.lname}, "
                f"{self.email}, {self.password}, {self.roles}")