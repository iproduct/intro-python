import uuid


class Repository:
    def __init__(self):
        self.items = {}

    def create(self, item):
        item.id = uuid.uuid1()
        self.items[item.id] = item
        return item

    def update(self, item):
        if item.id not in self.items:
            return None
        self.items[item.id] = item
        return item

    def delete_by_id(self, id):
        if id in self.items:
            old = self.items[id]
        else:
            return None
        del self.items[id]
        return old

    def find_all(self):
        return self.items.values()

    def find_by_id(self, id):
        if id not in self.items:
           return None
        return self.items[id]

    def count(self):
        len(self.items)