from enum import Enum

from entity.person import Person


class Role(Enum):
    USER = 1
    ADMIN = 2

    @classmethod
    def from_json(cls, prop_dict):
        return cls[prop_dict['name']]

    def to_json(self):
        return {
            'name': self.name,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }


class User(Person):
    def __init__(self, f_name=None, l_name=None, age=None, username=None, password=None, role=Role.USER, id_=None):
        Person.__init__(self, f_name, l_name, age, id_)
        self.username = username
        self.password = password
        self.role = role

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
