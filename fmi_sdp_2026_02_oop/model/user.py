import bcrypt

from dao.entity import Entity


class User[IDType] (Entity[IDType]):
    db_filename = 'users'

    # @staticmethod
    # def get_filename():
    #     return User.db_filename
    @classmethod
    def get_filename(cls):
        return cls.db_filename

    def __init__(self, username: str|None = None, password: str|None = None, email: str|None = None,
                 fname: str|None= None, lname: str|None = None, roles: list[str] | str|None = None, uid: IDType = None):
        self.id = uid
        self.fname = fname
        self.lname = lname
        self.email = email
        self.username = username
        self.password = password
        self.roles = roles if roles is not None else []

    @property
    def password(self) -> str:
        return self.__password.decode(encoding='utf-8')

    @password.setter
    def password(self, password: str):
        self.__password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12))

    def __repr__(self) -> str:
        return (f"User: {self.id}, {self.username}, {self.fname}, {self.lname}, "
                f"{self.email}, {self.password}, {self.roles}")
