{
    "id": 1,
    "first": "Trayan",
    "last": "Iliev",
    "address": {
        "country": "BG",
        "city": "Sofia",
        "street": "Jamaes Bouchier Blvd., 42"
    },
    "phones": [
        {
            "type": "work",
            "number": "+3592895423"
        },
        {
            "type": "mobile",
            "number": "+359885167243"
        },
    ]
}


class Phone:
    def __init__(self, number, type='MOBILE'):
        self.number = number
        self.type = type

    def __str__(self):
        return f'{self.type}: {self.number}'


class Contact:
    last_id = 0

    @classmethod
    def __get_next_id(cls):
        cls.last_id += 1
        return cls.last_id

    def __init__(self, first: str, last: str, address: str, phones: list[Phone] = None):
        # self.id = self.__class__.__get_next_id()
        # self.id = Contact.__get_next_id()
        self.id = self.__get_next_id()
        self.first = first
        self.last = last
        self.address = address
        self.phones = [] if phones is None else phones

    def __str__(self):
        result = ''
        phones_str = ', '.join([f'{ph.type}: {ph.number}' for ph in self.phones])
        result += f'| {self.id:>3d} | ' \
                  f'{self.first + " " + self.last:<15.15s} | ' \
                  f'{self.address:<40.40s} | ' \
                  f'{phones_str:50.50s} |'
        return result

if __name__ == '__main__':
    contacts = [
        Contact('Trayan', 'Iliev', 'Sofia, 1000', [Phone('+3592 891234', 'HOME'), Phone('+35989 123456')]),
        Contact('Georgi', 'Hristov', 'Plodiv, Pet tepeta, 17}', [Phone('+35988 654321')]),
        Contact('Mary', 'Smith', 'London', [Phone('+59 8956661234', 'HOME')]),
        Contact('John', 'Smith', 'London'),
    ]

    for contact in contacts:
        print(contact)
