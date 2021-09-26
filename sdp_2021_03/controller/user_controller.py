from typing import Optional

from dao import UserRepository
from model import User, Author, Admin
from model.login import Login


class UserController:
    def __init__(self, user_repo: UserRepository): # Dependency Injection (DI) - constructor based
        self.user_repo = user_repo
        self.logged_user = None

    def login(self, login: Login) -> bool:
        user = self.user_repo.find_user_by_email(login.email)
        if user != None and user.check_password(login.password):
            self.logged_user = user
            return True
        else:
            self.logged_user = None
            return False

    def get_logged_user(self) -> Optional[User]:
        return self.logged_user

if __name__ == '__main__':
    users = [
        Author('Ivan Petrov', 'ivanp@abv.bg', 'ivanp123'),
        Admin('Admin Admin', 'admin@mycompany.com', 'admin123', '35928976564'),
        Admin('Nadezda Hristova', 'nadia@mycompany.com', 'nadia123', '3592754632'),
    ]
    user_repo = UserRepository(users)
    print(f'Repository has {len(user_repo)} users.')
    user_repo.add_user(Author('Hrisitna Dimitrova', 'hrisitna@gmaIL.com', 'hristina', 'expert'))
    user_repo.add_user(Author('Ivan Pavlov', 'ivan@gmail.com', 'ivan123', 'professional'))

    for user in user_repo:
        print('+', user)
    print(f'Repository has {len(user_repo)} users.')

    user_controller = UserController(user_repo) # DI implementation
    login_successful = False
    login = Login()
    while not login_successful:
        email = input(f"Enter email [<Enter> for '{login.email}']:").strip()
        if email == '':
            email = login.email
        password = input('Enter password:')
        login = Login(email, password)
        if user_controller.login(login):
            print(f'You have successfully logged as: {user_controller.get_logged_user()}')
            login_successful = True
        else:
            print('Invalid email or password. Try again')


