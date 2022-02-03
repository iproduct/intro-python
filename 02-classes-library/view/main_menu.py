from controller.login_controller import LoginController
from view.menu import Command


class LoginCommand(Command):
    def __init__(self, login_controller: LoginController):
        self.login_controller = login_controller

    def run(self) -> str:
        return "Not implemented"
