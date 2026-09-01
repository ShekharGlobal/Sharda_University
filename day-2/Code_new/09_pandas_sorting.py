import pandas as pd

df = pd.DataFrame({"Name": ["Amit", "Riya", "John"], "Marks": [80, 90, 70]}, index=[2, 0, 1])
print("Sort by Marks:")
print(df.sort_values("Marks"))
print("Sort by Index:")
print(df.sort_index())
