from typing import Optional

from model import User

class UserController:
    def __init__(self, users: list[User]):
        self.users = users
        self.logged_user = None

    def get_user_by_email(self, email: str) -> Optional[User]:
        for user in self.users:
            if user.email == email:
                return user
        else:
            return None

    def login(self, email: str, password: str) -> bool:
        user = self.get_user_by_email(email)
        if user != None and user.check_password(password):
            self.logged_user = user
            return True
        else:
            self.logged_user = None
            return False

    def get_logged_user(self) -> Optional[User]:
        return self.logged_user

if __name__ == '__main__':
    users = [
        User('Ivan Petrov', 'ivanp@abv.bg', 'ivanp123'),
        User('Admin Admin', 'admin@mycompany.com', 'admin123', 'admin'),
        User('Nadezda Hristova', 'nadia@mycompany.com', 'nadia123', 'admin'),
    ]
    user_controller = UserController(users)
    email = input('Erter email:')
    password = input('Erter password:')
    if user_controller.login(email, password):
        print(f'You have successfully logged as: {user_controller.get_logged_user()}')
    else:
        print('Invalid email or password')