import json
import os
from datetime import date


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
            json.dump(self.current_test, f, indent=4,
                      default=lambda obj: obj.isoformat() if isinstance(obj, date) else obj.__dict__)