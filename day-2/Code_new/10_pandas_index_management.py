import pandas as pd

df = pd.DataFrame({"Name": ["Amit", "Riya", "John"], "Marks": [80, 90, 70]})
print("Original:")
print(df)
df = df.set_index("Name")
print("After set_index():")
print(df)
df = df.reset_index()
print("After reset_index():")
print(df)
