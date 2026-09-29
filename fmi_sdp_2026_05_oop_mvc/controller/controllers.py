from enum import Enum
from json import dump, load
import uuid

from dao.abstract_repository import AbstractRepository
from dao.contact_json_repo import ContactJsonRepo
from model.contact import PhoneType, Phone, Contact
from view.menus import Menu, Item
from view.views import InputContactView, ShowContactsView


class MainController:
    def __init__(self, contact_repo: ContactJsonRepo, input_contact_view: InputContactView, show_contacts_view: ShowContactsView):
        self.contact_repository = contact_repo
        self.input_contact_view = input_contact_view
        self.show_contacts_view = show_contacts_view
        self.menu = self.create_menu()

    def create_menu(self):
        return Menu([
            Item("Print all contacts", self.show_contacts_handler),
            Item("Add contact", self.input_contact_handler),
            Item("Exit", self.exit_handler),
        ])

    def run(self):
        self.contact_repository.load_contacts()
        while True:
            handler = self.menu.show()
            handler()


    # Handlers
    def show_contacts_handler(self):
        self.show_contacts_view.show(self.contact_repository.find())

    def input_contact_handler(self):
        contact = self.input_contact_view.show()
        self.contact_repository.create(contact)
        self.contact_repository.save_contacts()

    def exit_handler(self):
        # self.save_contacts()
        print('Good bye - have a nice day!')
        exit(0)

