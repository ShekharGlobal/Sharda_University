import pandas as pd

df = pd.DataFrame({"Student": ["Amit", "Amit", "Riya", "Riya"], "Subject": ["Math", "Science", "Math", "Science"], "Marks": [80, 70, 90, 85]})
print("pivot():")
print(df.pivot(index="Student", columns="Subject", values="Marks"))
print("crosstab():")
print(pd.crosstab(df["Student"], df["Subject"]))
