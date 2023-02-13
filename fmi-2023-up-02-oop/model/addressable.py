class Addressable:
    def __init__(self, address, street, city, country="BG"):
        self.address = address
        self.street = street
        self.city = city
        self.country = country

    def __repr__(self):
        return f'{self.country}, {self.city}, {self.street} {self.address}'

    def get_label(self):
        return f'To: {self}'