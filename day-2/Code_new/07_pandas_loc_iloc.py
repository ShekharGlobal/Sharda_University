import pandas as pd

df = pd.DataFrame({"Name": ["Amit", "Riya", "John"], "Marks": [80, 90, 70]})
print("Using loc:", df.loc[1, "Name"])
print("Using iloc:", df.iloc[1, 0])
