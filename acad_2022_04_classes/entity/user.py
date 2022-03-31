from enum import Enum

from entity.person import Person


class Role(Enum):
    USER = 1
    ADMIN = 2
    def to_json(self):
        return self.name


class User(Person):
    def __init__(self, f_name, l_name, age, username, password, role=Role.USER, id_=None):
        Person.__init__(self, f_name, l_name, age, id_)
        self.username = username
        self.password = password
        self.role = role
        # self.__type_name = 'User'

    # @property
    # def username(self):
    #     return self._username
    #
    # @username.setter
    # def username(self, username):
    #     self._username = username
    #
    # @property
    # def password(self):
    #     return self._password
    #
    # @password.setter
    # def password(self, password):
    #     self._password = password
    #
    # @property
    # def role(self):
    #     return self._role
    #
    # @role.setter
    # def role(self, role):
    #     self._role = role

    def get_formatted_str(self):
        return f"{super().get_formatted_str()} {self.username:12.12s} | {self.password:12.12s} | {self.role:12.12s} |"

