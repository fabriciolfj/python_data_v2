import re
from sys import flags

import pandas as pd

data = {"Dave": "dave@google.com", "Steve": "steve@google.com", "Rob": "rob@google.com"}

data = pd.Series(data)
print(data)


print(data.str.contains("google"))

pattern = r"([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})$"

match = data.str.findall(pattern, flags=re.IGNORECASE).str[0]
print("=============")
print(match)
print("=============")
print(match.str.get(1))