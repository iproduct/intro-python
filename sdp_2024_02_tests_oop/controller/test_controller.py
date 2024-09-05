import json
import os
import uuid
from datetime import date, datetime
from enum import Enum


def dumper(obj):
    if isinstance(obj, datetime.datetime):
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


class TestController:
    def __init__(self, data_dir:str='tests'):
        self.data_dir = data_dir
        self.current_test = None

    def loadTest(self, id):
        with open(os.path.join(self.data_dir, f'test_{id}.json'), 'rt') as f:
            self.current_test = json.load(f)

    def saveTest(self):
        os.makedirs(self.data_dir,  exist_ok = True)
        with open(f'{self.data_dir}/test_{self.current_test.id}.json', 'wt') as f:
            json.dump(self.current_test, f, indent=4, default=dumper)