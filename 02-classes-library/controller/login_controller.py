from dao.user_repository import UserRepository
from entity.user import User


class LoginController:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, user: User) -> User:
        # TODO validate user
        self.user_repository.create(user)

    def login(self, username: str, password: str) -> User:
