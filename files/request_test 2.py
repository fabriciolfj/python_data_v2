import requests
import pandas as pd

url = "https://api.github.com/repos/pandas-dev/pandasgit push origin main/issues"

resp = requests.get(url)

print(resp.raise_for_status())

data = resp.json()

print(data[0]['title'])

issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
print(issues)