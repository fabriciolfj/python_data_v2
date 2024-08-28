import json
import sys

import pandas as pd

obj = """
    { "name" : "Wes",
    "siblings" : [
        {"name": "Scott", "age" : 34},
        {"name": "Katie", "age" : 42}
        ]
    }
"""

asjson = json.loads(obj)
print(asjson)


siblings = pd.DataFrame(asjson['siblings'], columns=['name', 'age'])
print(siblings)

data = pd.read_json("example.json")
data.to_json(sys.stdout)