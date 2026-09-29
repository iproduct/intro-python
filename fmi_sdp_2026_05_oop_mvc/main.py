from controller.controllers import MainController
from view.views import InputContactView, ShowContactsView

if __name__ == '__main__':
    input_contact_view = InputContactView()
    show_contacts_view = ShowContactsView()
    ctrl = MainController('contacts.json', input_contact_view, show_contacts_view)
    ctrl.run()