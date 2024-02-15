from enum import Enum

class PhoneType(Enum):
    MOBILE = 1
    HOME = 2
    WORK = 3

class Phone:
    def __init__(self, number: str ='', type: PhoneType = PhoneType.MOBILE):
        self.number = number
        self.type = type

    def __str__(self):
        return f'{self.type.name}: {self.number}'


class Contact:
    last_id = 0

    @classmethod
    def __get_next_id(cls):
        cls.last_id += 1
        return cls.last_id

    def __init__(self, first: str = "", last: str = "", address: str = "", phones: list[Phone] = None):
        # self.id = self.__class__.__get_next_id()
        # self.id = Contact.__get_next_id()
        self.id = self.__get_next_id()
        self.first = first
        self.last = last
        self.address = address
        self.phones = [] if phones is None else phones

    def __str__(self):
        result = ''
        phones_str = ', '.join([f'{ph.type.name}: {ph.number}' for ph in self.phones])
        result += f'| {self.id:>3d} | ' \
                  f'{self.first + " " + self.last:<15.15s} | ' \
                  f'{self.address:<40.40s} | ' \
                  f'{phones_str:50.50s} |'
        return result

if __name__ == '__main__':
    contacts = [
        Contact('Trayan', 'Iliev', 'Sofia, 1000', [Phone('+3592 891234', PhoneType.HOME), Phone('+35989 123456')]),
        Contact('Georgi', 'Hristov', 'Plodiv, Pet tepeta, 17}', [Phone('+35988 654321')]),
        Contact('Mary', 'Smith', 'London', [Phone('+59 8956661234', PhoneType.HOME)]),
        Contact('John', 'Smith', 'London'),
    ]

    for contact in contacts:
        print(contact)
