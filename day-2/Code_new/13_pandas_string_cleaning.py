import pandas as pd

df = pd.DataFrame({"Name": [" amit ", "RIYA", " john "]})
print("Before cleaning:")
print(df)
df["Name"] = df["Name"].str.strip().str.title()
print("After cleaning:")
print(df)
