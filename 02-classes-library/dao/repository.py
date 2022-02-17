import uuid


class Repository:
    def __init__(self):
        self._items = {}
        self._values = None

    def create(self, item):
        item.id = str(uuid.uuid1())
        self._items[item.id] = item
        return item

    def update(self, item):
        if item.id not in self._items:
            return None
        self._items[item.id] = item
        return item

    def delete_by_id(self, id):
        if id in self._items:
            old = self._items[id]
        else:
            return None
        del self._items[id]
        return old

    def find_all(self) -> list:
        return list(self._items.values())

    def find_by_id(self, id):
        if id not in self._items:
           return None
        return self._items[id]

    def __iter__(self):
        # self._values = self._items.values().__iter__()
        self._values = iter(self._items.values())
        return self

    def __next__(self):
        return next(self._values)

    def count(self):
        return len(self._items)