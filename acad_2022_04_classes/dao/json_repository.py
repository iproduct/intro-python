import json

from dao.repository import Repository


class JsonRepository(Repository):
    def __init__(self, idGenerator, db_filename):
        super().__init__(idGenerator)
        self.db_filename = db_filename

    def save(self):
        with open(self.db_filename, 'wt', encoding='utf-8') as f:
            json.dump(list(self.find_all()), f, indent=4, default=dumper)


# Helpers
def dumper(obj):
    try:
        return obj.to_json()
    except AttributeError:
        return obj.__dict__


