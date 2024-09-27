import pandas as pd
import numpy as np

ts = pd.Series(np.random.standard_normal(4), index=pd.date_range('1/1/2000', periods=4, freq="M"))
print(ts)
print("==============")
print(ts.shift(2))
print("==============")
print(ts.shift(2, freq="M"))