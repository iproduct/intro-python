from controller.login_controller import LoginController
from entity.user import User
from exception import credentials_exception
from exception.credentials_exception import CredentialsException
from view.menu import Command, MenuItem


class LoginCommand(Command):
    def __init__(self, login_controller: LoginController):
        self.login_controller = login_controller

    def run(self) -> str:
        username = input("Enter username:")
        password = input("Enter password:")
        try:
            user = self.login_controller.login(username, password)
        except CredentialsException as ex:
            return str(ex)
        return f"Hello, {user.first_name} {user.last_name} [{user.username}]!"

class LogoutCommand(Command):
    def __init__(self, login_controller: LoginController):
        self.login_controller = login_controller

    def run(self) -> str:
        self.login_controller.logout()
        return f"You have successfully logged out."

class GetLoggedUserCommand(Command):
    def __init__(self, login_controller: LoginController):
        self.login_controller = login_controller

    def run(self) -> str:
        user = self.login_controller.get_logged_user()
        if user is not None:
            return f"You are logged as: {user.first_name} {user.last_name} [{user.username}]."
        else:
            return "No user logged in."

class RegisterCommand(Command):
    def __init__(self, login_controller: LoginController):
        self.login_controller = login_controller

    def run(self) -> str:
        first_name = input("Enter first name:")
        last_name = input("Enter last name:")
        username = input("Enter username:")
        password = input("Enter password:")
        user = self.login_controller.register(User(None, first_name, last_name, username, password))
        return f"You are successfully registered as: {user.first_name} {user.last_name} [{user.username}]."

