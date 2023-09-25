from datetime import date, datetime

class Person:
    """Models a phisical person"""
    _next_id = 0

    @classmethod
    def get_next_id(cls):
        cls._next_id += 1
        return cls._next_id

    def __init__(self, name = None, bdate = None):
        self._id: str = self.__class__.get_next_id()
        self._name:str = name
        self.birth_date: date = datetime.strptime(bdate, '%d.%m.%Y').date() if bdate is not None else None

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or (today.month == self.birth_date.month and today.day < self.birth_date.day):
            age -= 1
        return age

    def __str__(self):
        return f'| {self.id:>3d} | {self.name:30s} | {self.birth_date.strftime("%d.%m.%Y"):10s} | {self.get_age():3d} |'

    def __repr__(self):
        return f'Person({self._id}, {self._name}, {self.birth_date.strftime("%d.%m.%Y")})'


if __name__ == '__main__':
    p1 = Person('Hristo Stoilov', '18.09.1985')
    print(p1)