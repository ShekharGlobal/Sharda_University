import pandas as pd

df = pd.DataFrame({"Name": ["Amit", "Riya", "John"], "Marks": [80, None, 70]})
print("Before dropna():")
print(df)
df = df.dropna()
print("After dropna():")
print(df)
