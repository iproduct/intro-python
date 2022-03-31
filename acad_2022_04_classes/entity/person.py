from functools import total_ordering


@total_ordering
class Person:
    # nextId = 0
    # @staticmethod
    # def get_next_id():
    #     __class__.nextId += 1
    #     return __class__.nextId

    # @classmethod
    # def get_next_id(cls):
    #     cls.nextId += 1
    #     return cls.nextId

    def __init__(self, f_name, l_name, age, id = None):
        self.id = id
        self._f_name = f_name
        self._l_name = l_name
        self.age = age
        self.__type_name='Person'

    def _get_f_name(self):
        # print(f"Called _get_f_name()")
        return self._f_name

    def _set_f_name(self, value):
        # print(f"Called _set_f_name({value})")
        self._f_name = value

    def _del_f_name(self):
        # print(f"Called _del_f_name()")
        del self._f_name

    f_name = property(_get_f_name, _set_f_name, _del_f_name, "Person's first name")

    @property
    def l_name(self):
        # print(f"Called @property l_name()")
        return self._l_name

    @l_name.setter
    def l_name(self, value):
        # print(f"Called @l_name.setter({value})")
        self._l_name = value

    @l_name.deleter
    def l_name(self):
        # print(f"Called @l_name.deleter()")
        del self._l_name

    def _is_valid_operand(self, other):
        return (hasattr(other, "f_name") and
                hasattr(other, "l_name"))

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.f_name.lower(), self.l_name.lower()) ==
                (other.f_name.lower(), other.l_name.lower()))

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.f_name.lower(), self.l_name.lower()) <
                (other.f_name.lower(), other.l_name.lower()))

    def __str__(self):
        return f'{self.id}) {self.f_name} {self.l_name}: {self.age}'

    def get_formatted_str(self):
        return f'| {str(self.id):24s} | {self.f_name:15.15s} | {self.l_name:15.15s} | {self.age:3d} |'

if __name__ == "__main__":
    p1 = Person('Ivan', 'Petrov', 25)
    p2 = Person('Dimitar', 'Hristov', 35)
    p3 = Person('Maria', 'Georgieva', 27)
    persons = [p1, p2, p3]
    print(p1.f_name, p1.l_name, ": ", p1.age)
    print(p1)
    p1_mname = getattr(p1, "m_name", "<not available>")
    print(p1_mname)

    for p in persons:
        print(p.get_formatted_str())

    # print('Class Person.__dict__:', Person.__dict__)

