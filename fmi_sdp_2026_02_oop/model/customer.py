from model.user import User


class Customer(User):
    db_filename = 'customers'
    def __init__(self, *args, phone = None, address = None, credit_card = None, **kwargs):
        kwargs['roles'] = ['customer']
        super().__init__(*args, **kwargs)
        self.phone = phone
        self.address = address
        self.credit_card = credit_card

    def __repr__(self):
        return 'Customer' + super().__repr__()[4:] + f', {self.phone}, {self.address}, {self.credit_card}, file: {self.get_filename()}'
