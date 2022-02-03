from dao.user_repository import UserRepository
from entity.user import User
from exception.InvalidUsernameOrPasswordException import InvalidUsernameOrPasswordException


class LoginController:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self._logged_user = None

    def register(self, user: User) -> User:
        # TODO validate user
        self.user_repository.create(user)

    def login(self, username: str, password: str) -> User:
        user = self.user_repository.find_by_username(username)
        if user.password == password:
            self.logged_user = user
            return user
        raise InvalidUsernameOrPasswordException("Invalid username or password")

    def logout(self) -> User:
        self._logged_user = None

    def get_logged_user(self):
        return self._logged_user
