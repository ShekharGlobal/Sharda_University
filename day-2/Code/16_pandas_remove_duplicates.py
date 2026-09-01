import pandas as pd


data = {
    "Category": ["Food", "Travel", "Food"],
    "Amount": [250, 500, 250]
}

df = pd.DataFrame(data)

print(df)

df = df.drop_duplicates()

print(df)
