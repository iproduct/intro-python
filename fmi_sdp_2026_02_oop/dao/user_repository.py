from abc import ABC

from dao.abstract_repository import AbstractRepository
from model.user import User


class UserRepository[IDType](AbstractRepository[IDType, User], ABC):
    def find_by_username(self, username: str) -> User[IDType] | None:
        for user in self.find():
            if user.username == username:
                return user
        return None

    def find_by_email(self, email: str) -> User[IDType] | None:
        for user in self.find():
            if user.email == email:
                return user
        return None