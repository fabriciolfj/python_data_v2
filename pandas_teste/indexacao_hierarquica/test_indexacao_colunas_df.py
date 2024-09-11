import pandas as pd
import numpy as np

frame = pd.DataFrame(
    {
        "a": range(7),
        "b": range(7, 0, -1),
        "c": ["one", "one", "one", "two", "two", "two", "two"],
        "d": [0, 1, 2, 0, 1, 2, 3]
    }
)

print(frame)
print("=====================")
frame = frame.set_index(["c", "d"])
print(frame)