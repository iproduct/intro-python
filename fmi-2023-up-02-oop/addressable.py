class Addressable:
    def __init__(self, address, street, city, country="BG"):
        self.address = address
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street} {self.address}'