import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.standard_normal((100, 4)))
print(data)
##col = data[2], col[col.abs()> 3] para coluna
print("======================")
result = data[(data.abs() > 3).any(axis="columns")]
print(result)