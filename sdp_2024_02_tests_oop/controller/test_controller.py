import json
import os
import uuid
from datetime import date, datetime
from enum import Enum
from typing import Type

from model.answer import Answer
from model.question import Question, QuestionType
from model.test import Test


def dumper(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, Enum):
        return {
            '_class': obj.__class__.__name__,
            "value": obj.name
        }
    elif isinstance(obj, uuid.UUID):
        return {
            '_class': obj.__class__.__name__,
            "value": str(obj)
        }
    else:
        result = dict(obj.__dict__)
        result.update({"_class": obj.__class__.__name__})
        return result


def object_hook_factory(entity_classes_set: set[Type]): #HOF, closure
    entity_classes_dict = {cls.__name__: cls for cls in entity_classes_set}
    def obj_hook(jsondict): # callback
        cls_name = jsondict['_class']
        cls = entity_classes_dict[cls_name]
        if issubclass(cls, Enum):
            return cls[jsondict['value']]
        elif cls_name == uuid.UUID.__name__:
            return uuid.UUID(jsondict['value'])
        else:
            obj = cls()
            del jsondict['_class']
            obj.__dict__ = jsondict
            return obj
    return obj_hook

class TestController:
    def __init__(self, data_dir:str='tests'):
        self.data_dir = data_dir
        self.current_test = None

    def loadTest(self, id):
        with open(os.path.join(self.data_dir, f'test_{id}.json'), 'rt') as f:
            self.current_test = json.load(f, object_hook=object_hook_factory({Test, Question, Answer, QuestionType}))

    def saveTest(self):
        os.makedirs(self.data_dir,  exist_ok = True)
        with open(f'{self.data_dir}/test_{self.current_test.id}.json', 'wt') as f:
            json.dump(self.current_test, f, indent=4, default=dumper)