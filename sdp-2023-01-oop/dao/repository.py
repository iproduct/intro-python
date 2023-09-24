class Repository:
    """
    Implements CRUD entity lifecycle operations - DAO pattern
    """
    def __init__(self, initial_items=None):
        items_list = [] if initial_items is None else initial_items
        self.__items = {s.id: s for s in items_list}

    def __len__(self):
        return len(self.__items)

    def __iter__(self):
        return iter(self.__items.values())

    def find_all(self):             # Read
        return list(self.__items.values())

    def find_by_id(self, id):       # Read
        return self.__items[id]

    def append(self, item):         # Create
        self.__items[item.id] = item

    def update(self, new_item):     # Update
        self.__items[new_item.id] = new_item

    def delete_by_id(self, id):     # Delete
        deleted = self.__items.pop(id)
        return deleted
