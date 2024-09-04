from operator import index

import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=["Ohio", "Colorado", "New York"],
                    columns=["one", "two", "three", "four"])

data = data.rename(index={"Ohio": "INDIANA"},
            columns={"three": "peekaboo"})

print(data)
