import requests
from pandas.io.json import json_normalize

url = "https://think.cs.vt.edu/corgis/datasets/json/airlines/airlines.json"
resp = requests.get(url=url)

df = json_normalize(resp.json())
# Writing Excel File:
df.to_excel('Airlines.xlsx')