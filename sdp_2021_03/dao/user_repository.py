from typing import Optional
from model import User

class UserRepository:
    def __init__(self, users: list[User]):
        self.users = users

    def get_user_by_email(self, email: str) -> Optional[User]:
        for user in self.users:
            if user.email == email:
                return user
        else:
            return None

