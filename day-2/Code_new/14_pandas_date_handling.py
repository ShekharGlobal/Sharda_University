import pandas as pd

df = pd.DataFrame({"Date": ["2026-01-10", "2026-02-15", "2026-03-20"]})
df["Date"] = pd.to_datetime(df["Date"])
print(df)
print("Year:")
print(df["Date"].dt.year)
print("Month:")
print(df["Date"].dt.month)
