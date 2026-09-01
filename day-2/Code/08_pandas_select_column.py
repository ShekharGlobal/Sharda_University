import pandas as pd

data = {
    "Category": ["Food", "Travel", "Books"],
    "Amount": [250, 500, 300]
}

df = pd.DataFrame(data)

print(df["Amount"])