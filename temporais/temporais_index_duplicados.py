import pandas as pd
import numpy as np

dates = pd.DatetimeIndex(["2000-01-01", "2000-01-02", "2000-01-02", "2000-01-02", "2000-01-03"])
dup = pd.Series(np.arange(5), index=dates)
print(dup.index.is_unique)

group = dup.groupby(level=0)

print(group.count())