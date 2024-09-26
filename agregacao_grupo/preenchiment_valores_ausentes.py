import pandas as pd
import numpy as np

states = [
    "ohio", "new york", "vermont", "florida",
    "oregon", "nevada", "california", "idaho"
]

group_key = ["east", "east", "east", "east",
             "west", "west", "west", "west"]

series = pd.Series(np.random.standard_normal(8), index=states)
series[["vermont", "nevada", "idaho"]] = np.nan

def fill_mean(group):
    return group.fillna(group.mean())

result = series.groupby(group_key).apply(fill_mean)
print(result)
print(result.groupby(group_key).size())

