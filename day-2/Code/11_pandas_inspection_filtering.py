
import pandas as pd

df = pd.read_csv("expenses.csv")

print(df.head())
print(df.shape)
print(df.columns)
df.info()
print(df.describe())
print(df[df["Amount"] > 300])
print(df.sort_values("Amount"))
print(df.sort_values("Amount", ascending=False))
print(df.sort_values("Amount", ascending=False).head(1))  #Which expense was the highest?