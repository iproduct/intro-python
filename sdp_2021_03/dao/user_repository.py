from typing import Optional
from model import User

class UserRepository:
    """
    CRUD functionality for User models (entities)
    """
    def __init__(self, users: list[User]):
        self.users = users

    def __len__(self):
        return len(self.users)

    def __iter__(self):
        for user in self.users:
            yield user

    # def __iter__(self):
    #     self.position = 0
    #     return self
    #
    # def __next__(self):
    #     if self.position < len(self.users):
    #         result =  self.users[self.position]
    #         self.position += 1
    #         return result
    #     else:
    #         raise StopIteration

    def add_user(self, new_user: User) -> User:
        self.users.append(new_user)
        return new_user

    def find_all_users(self) -> list[User]:
        return self.users

    def find_user_by_email(self, email: str) -> Optional[User]:
        for user in self.users:
            if user.email == email:
                return user
        else:
            return None

