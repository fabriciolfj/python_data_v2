import numpy as np

names = np.array(["Bob", "Will", "Joe", "Bob"])

result = np.unique(names)

print(result)

values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))