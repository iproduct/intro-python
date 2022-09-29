import json

from dao.repository import Repository


class JsonRepository(Repository):
    def __init__(self, db_filename, entity_clases_dict):
        super().__init__()
        self.db_filename = db_filename
        self.entity_classes_dict = entity_clases_dict

    def save(self):
        with open(self.db_filename, 'wt', encoding='utf-8') as f:
            json.dump(list(self.findAll()), f, indent=4, default=dumper)

    def load(self):
        with open(self.db_filename, 'rt', encoding='utf-8') as f:
            users = json.load(f, object_hook=object_hook_factory(self.entity_classes_dict))
            for user in users:
                self.create(user)



# Helpers
def dumper(obj):
    try:
        return obj.to_json()
    except:
        result = dict(obj.__dict__)
        result.update({"_class": obj.__class__.__name__})
        return result

def object_hook_factory(entity_classes_dict): #HOF, closure
    def obj_hook(jsdict):
        cls_name = jsdict['_class']
        cls = entity_classes_dict[cls_name]
        obj = cls()
        del jsdict['_class']
        obj.__dict__ = jsdict
        return obj
    return obj_hook
