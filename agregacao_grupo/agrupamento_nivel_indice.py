import pandas as pd
import numpy as np

columns = pd.MultiIndex.from_arrays([["US", "US", "US", "JP", "JP"],
                                     [1, 3, 5, 1, 3]],
                                    names=["city", "tenor"])

hier_df = pd.DataFrame(np.random.standard_normal((4, 5)), columns=columns)

print(hier_df.groupby(level="city", axis=1).count())