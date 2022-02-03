from dao.user_repository import UserRepository
from entity.user import User
from exception.credentials_exception import CredentialsException


class LoginController:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self._logged_user = None

    def register(self, user: User) -> User:
        # TODO validate user
        return self.user_repository.create(user)

    def login(self, username: str, password: str) -> User:
        user = self.user_repository.find_by_username(username)
        if user is not None and user.password == password:
            self._logged_user = user
            return user
        raise CredentialsException("Invalid username or password. Try again.")

    def logout(self) -> User:
        self._logged_user = None

    def get_logged_user(self) -> User | None:
        return self._logged_user
