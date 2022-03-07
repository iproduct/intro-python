import uuid


class RepositoryIterator:
    def __init__(self, values: list):
        self._values = values
        self._next_index = -1

    def __next__(self):
        self._next_index += 1
        if self._next_index < len(self._values):
            return self._values[self._next_index]
        raise StopIteration()


class Repository:
    def __init__(self):
        self._items = {}

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

    # def __iter__(self):
    #     # self._values = self._items.values().__iter__()
    #     return RepositoryIterator(list(self._items.values()))
    #     # return iter(self._items.values())

    def __iter__(self):
        for item in list(self._items.values()):
            yield item

    def count(self):
        return len(self._items)

    def clear(self):
        self._items.clear()
