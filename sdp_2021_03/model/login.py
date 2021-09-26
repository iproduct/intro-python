from typing import  NamedTuple

class Login(NamedTuple):
    email: str = ''
    password: str = ''

if __name__ == '__main__':
    login = Login('ivanp@abv.bg', 'ivanp123')
    print(login)
    # login.password = 'newpass'
    # object.__setattr__(login, 'password', 'newpass')
    login2 = login._replace(password='newpass')
    print(f'login: {login}')
    print(f'login2: {login2}')