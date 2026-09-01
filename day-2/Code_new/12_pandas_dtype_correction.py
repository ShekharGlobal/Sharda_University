import pandas as pd

df = pd.DataFrame({"Marks": ["80", "90", "70"]})
print("Before conversion:")
print(df.dtypes)
df["Marks"] = pd.to_numeric(df["Marks"])
print("After conversion:")
print(df.dtypes)
