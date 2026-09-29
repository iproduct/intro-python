from controller.controllers import MainController
from dao.contact_json_repo import ContactJsonRepo
from dao.id_generator import IdGeneratorUuid
from view.views import InputContactView, ShowContactsView

if __name__ == '__main__':
    input_contact_view = InputContactView()
    show_contacts_view = ShowContactsView()
    contact_repo = ContactJsonRepo(IdGeneratorUuid(), 'contacts.json')
    ctrl = MainController(contact_repo, input_contact_view, show_contacts_view)
    ctrl.run()