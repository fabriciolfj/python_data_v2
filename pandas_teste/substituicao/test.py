import pandas as pd
import numpy as np

data = pd.Series([1., -999, 2., -999, -1000, 3.])

result = data.replace({-999: np.nan, -1000: 0})

print(result)