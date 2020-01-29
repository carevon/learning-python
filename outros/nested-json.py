import requests
import pandas as pd
from pprint import pprint

url = "https://www.qnt.io/api/results?pID=gifgif&mID=54a309ae1c61be23aba0da62&key=54a309ac1c61be23aba0da3f"

response = requests.get(url)
results = response.json()["results"]

# pprint(results)

# 1
df = pd.DataFrame.from_dict(results)
# print(df.head(2))

# 2
df = pd.concat([df.drop(["content_data"], axis=1), df["content_data"].apply(pd.Series)], axis=1)
df = pd.concat([df.drop(["parameters"], axis=1), df["parameters"].apply(pd.Series)], axis=1)
# print(df.head(2))

df["tags"] = df["tags"].apply(lambda x: ", ".join(x))
# print(df.head(2)["tags"])

df = df[["rank", "tags", "embedLink", "mu", "sigma", "index"]]
print(df.head(2))

escritor = pd.ExcelWriter('output.xlsx')
df.to_excel(escritor, 'Sheet1')
escritor.save()