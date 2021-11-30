from dataclasses import field, make_dataclass
from datetime import datetime, timezone

import dill
import pandas as pd
import numpy as np

if __name__ == '__main__':
    fields = [('float_val', float, field(default=np.nan)),
              ('df', pd.DataFrame, field(default_factory=pd.DataFrame)),
              ('int_val', int, field(default_factory=int)),
              ('time_val', datetime, field(default=datetime.now(timezone.utc)))]

    Aclass = make_dataclass('Aclass', fields)
    Aclass.__module__ = __name__ # provide name for pickling the class

    an_instance=Aclass()

    dill.dump(an_instance, open('test.pkl', 'wb'))
    dill.load(open('test.pkl', 'rb'))