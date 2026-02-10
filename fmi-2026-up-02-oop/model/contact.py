import datetime
import time


class Contact:
    def __init__(self, first_name, last_name, email, phone, address, created, modified, id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.created = created or time.now()
        self.modified = modified or time.now()
        self.id = id

    def __repr__(self):
        return f"<Contact {self.id}: {self.first_name} {self.last_name}, {self.email}, {self.phone}, {self.address}, {self.created}, {self.modified}>"

    def __str__(self):
        return (f"| {self.id: 4s} | {self.first_name:14.14s} | {self.last_name:14.14s} | {self.email:25.25s} | {self.phone:15.15s} |"
                f" {self.address:30.30s} | {self.created.strftime('%d.%m.%Y %H:%M:%S'):19.19s} | {self.modified.strftime('%d.%m.%Y %H:%M:%S'):19.19s} |")


if __name__ == "__main__":
    lc = [
        Contact('Trayan', 'Iliev',  't_iliev@gmial.com', '0887543211','Sofia, J.Bouchier 5'),
        Contact('Jane', 'Smith', 'jsmith@gmial.com', '0883456211', 'London'),
    ]