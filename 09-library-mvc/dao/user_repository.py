from dao.json_repository import JsonRepository
from entity.user import User
from util.fun_util import find


class UserRepository(JsonRepository):
    def find_by_username(self, username: str) -> User | None:
        users_list = self.find_all()
        results = find(lambda user: user.username == username, users_list)
        return results
