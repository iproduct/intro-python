from typing import Optional

from dao import UserRepository
from model import User

class UserController:
    def __init__(self, user_repo: UserRepository): # Dependency Injection (DI) - constructor based
        self.user_repo = user_repo
        self.logged_user = None

    def login(self, email: str, password: str) -> bool:
        user = self.user_repo.get_user_by_email(email)
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
    user_repo = UserRepository(users)
    user_controller = UserController(user_repo) # DI implementation
    login_successful = False
    while not login_successful:
        email = input('Erter email:')
        password = input('Erter password:')
        if user_controller.login(email, password):
            print(f'You have successfully logged as: {user_controller.get_logged_user()}')
            login_successful = True
        else:
            print('Invalid email or password. Try again')


