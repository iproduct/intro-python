import json
import re
from datetime import date


class Persistable:
    def __init__(self, file_name, cls):
        self.file_name = file_name
        self.cls = cls

    def append(self, item):
        raise NotImplementedError('Method append(self, item) should be overriden by descendants')

    def save(self):
        items = [item.__dict__ for item in iter(self)]
        with open(self.file_name, 'wt', encoding="utf-8") as f:
            json.dump(items, f, indent=4, default=lambda obj: obj.isoformat() if isinstance(obj, date) else obj.__dict__)

    def load(self):
        with open(self.file_name, 'rt', encoding="utf-8") as f:
            items = json.load(f)
        for item in items:
            for key in item:
                if re.match('^\\d{4}-\\d{2}-\\d{2}$', str(item[key])) is not None:
                    item[key] = date.fromisoformat(item[key])
            obj = self.cls()
            obj.__dict__ = item
            self.append(obj)

