class Contact:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.id:3d} | {self.name:<20s} | {self.phone:<15s}'

    def __eq__(self, other):
        return self.id == other.id
