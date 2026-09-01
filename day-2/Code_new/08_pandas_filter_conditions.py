import pandas as pd

df = pd.DataFrame({"Name": ["Amit", "Riya", "John", "Neha"], "Marks": [80, 90, 65, 75], "Branch": ["CS", "IT", "CS", "ECE"]})
print("isin():")
print(df[df["Branch"].isin(["CS", "IT"])])
print("between():")
print(df[df["Marks"].between(70, 85)])
print("query():")
print(df.query("Marks > 80"))
