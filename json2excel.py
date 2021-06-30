import json
import pandas as pd
with open('skb_type1.json','w', encoding='UTF-8') as json_file:
    data = json.load(json_file)
    df = pd.DataFrame(data)
    df.to_excel('skb_type1.xlsx')