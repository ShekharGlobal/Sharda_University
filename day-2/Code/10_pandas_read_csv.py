import pandas as pd
#Read this CSV and turn it into a DataFrame so I can analyze the data.
df = pd.read_csv("expenses.csv")

print(df)

print(df.head())
print(df.shape)
print(df["Amount"])
print(df["Amount"].mean())
print(df[df["Amount"] > 300])