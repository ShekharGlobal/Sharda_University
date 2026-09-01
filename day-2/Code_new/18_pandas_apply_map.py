import pandas as pd

marks = pd.Series([80, 90, 70])
result = marks.map(lambda x: x + 5)
print("map() result:")
print(result)

df = pd.DataFrame({"Name": ["Amit", "Riya", "John"], "Marks": [80, 90, 70]})
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")
print("apply() result:")
print(df)
