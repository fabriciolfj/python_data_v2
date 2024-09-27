from datetime import datetime

import pandas as pd
import numpy as np

from temporais.example_1 import datestrs

longer_ts = pd.Series(np.random.standard_normal(1000),
                      index=pd.date_range("2000-01-01", periods=1000))
print(longer_ts)
print("=============")
print(longer_ts["2001-05"])
print("=============")
print(longer_ts[datetime(2001, 5, 4):])
print("=============")
print(longer_ts[datetime(2001, 5, 2):datetime(2001, 5, 5)])
print("=============")
print(longer_ts.truncate(after=datetime(2001, 5, 4)))

