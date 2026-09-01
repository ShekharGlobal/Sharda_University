import pandas as pd

df = pd.DataFrame({
    "Category": ["Food", "Travel", "Food", "Travel"],
    "Amount": [250, 500, 150, 300]
})

print(df.groupby("Category")["Amount"].sum())
print(df.groupby("Category")["Amount"].mean())