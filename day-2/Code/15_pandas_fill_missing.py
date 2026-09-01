
import pandas as pd

data = {
    "Category": ["Food", "Travel", "Books"],
    "Amount": [250, None, 300]
}

df = pd.DataFrame(data)
df["Amount"] = df["Amount"].fillna(0)

print(df)