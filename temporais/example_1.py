import numpy as np
from datetime import datetime
from datetime import timedelta

now  = datetime.now()
delta  = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)

print(delta)
print(delta.seconds)

print("===============")
data = timedelta(12)
print(data)
print("===============")
stamp = datetime(2011, 1, 3)
print(stamp.strftime("%Y-%m-%d"))
print("===============")
value = "2011-01-03"
print(datetime.strptime(value, "%Y-%m-%d"))

datestrs = ["7/6/2011", "8/6/2011"]
result = [datetime.strptime(x, "%m/%d/%Y") for x in datestrs]
print(result)