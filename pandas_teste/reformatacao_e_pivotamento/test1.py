import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.arange(6).reshape((2, 3)),
    index=pd.Index(["ohio", "colorado"], name="state"),
    columns=pd.Index(["one", "two", "three"],
                   name="number")
)

print(data)
print("===========")
result = data.stack(level="number")
print(result)
print("===========")
print(result.unstack(level="state"))