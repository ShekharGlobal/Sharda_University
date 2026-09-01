import pandas as pd

df = pd.DataFrame({
    "Category": ["Food", "Travel", "Books"],
    "Amount": [250, 500, 300]
})

df["Tax"] = df["Amount"] * 0.05

print(df)