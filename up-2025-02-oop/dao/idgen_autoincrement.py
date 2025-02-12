from dao.id_generator import IdGenerator


class IdGenAutoincrement(IdGenerator):
    def __init__(self):
        self.next_id = 0
    def generate_id(self):
        self.next_id += 1
        return self.next_id
