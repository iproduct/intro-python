from datetime import datetime

class Contact:
    def __init__(self, first_name = '', last_name = '', phone_number = '', email = '', address = '',
                 created = None, modified = None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.created = created if created is not None else datetime.now()
        self.modified = modified if modified is not None else datetime.now()

    def __repr__(self):
        return f'Contact({self.first_name}, {self.last_name}, {self.phone_number}, {self.email}, {self.address}, {self.created}, {self.modified})'

    def __str__(self):
        return f'|{self.first_name:10.10s} | {self.last_name:10.10s} | {self.phone_number:10.10s} | {self.email:15.15s} | {self.address:15.15s} | {self.created.strftime("%d.%m.%Y"):10.10s} | {self.modified.strftime("%d.%m.%Y"):10.10s} |'


if __name__ == '__main__':
    lc = [
        Contact('Trayan', 'Iliev', '0887543211', 't_iliev@gmial.com', 'Sofia, J.Bouchier 5'),
        Contact('Jane', 'Smith', '0883456211', 'jsmith@gmial.com', 'London'),
    ]

    for contact in lc:
        print(contact)