import numpy as np
import pandas as pd


def f1(x):
    return x.max() - x.min()


def f2(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])


def my_format(x):
    return f"{x:.2f}"


frame = pd.DataFrame(np.random.standard_normal((4, 3)),
                     columns=list("bde"),
                     index=["utah", "ohio", "texas", "oregon"])

np.abs(frame)

frame.apply(f1)

#olhando pra coluna
frame.apply(f1, axis="columns")
print(frame)

print(frame.apply(f2))

print(frame.map(my_format))
