from dao.json_repository import JsonRepository
from dao.repository import Repository
from entity.user import User
from util.func_utils import find_first


class UserRepository(JsonRepository):
    def find_by_username(self, username: str)-> User | None:
        return find_first(lambda u: u.username == username, self.find_all())