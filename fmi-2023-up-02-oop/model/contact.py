class Contact:
    def __init__(self, name, phone, id=None):
        self.id = id
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.id if self.id is not None else "":<32s} | {self.name:<20.20s} | {self.phone:<15.15s}'

    def __eq__(self, other):
        return self.id == other.id
