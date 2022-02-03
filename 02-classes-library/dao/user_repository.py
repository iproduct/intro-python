from dao.repository import Repository
from entity.user import User
from util.fun_util import find


class UserRepository(Repository):
    def find_by_username(self, username: str) -> User:
        users_list = self.find_all()
        results = find(users_list, lambda user: user.username == username)
        return results
