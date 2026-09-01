import pandas as pd

df = pd.DataFrame({
    "Category": ["Food", "Travel", "Food", "Shopping"],
    "Amount": [250, 500, 150, 1200]
})

print("Dataset:")
print(df)

print("\nTotal Expense:")
print(df["Amount"].sum())

print("\nAverage Expense:")
print(df["Amount"].mean())

print("\nHighest Expense:")
print(df["Amount"].max())

print("\nExpenses above 300:")
print(df[df["Amount"] > 300])

print("\nCategory-wise Expense:")
print(df.groupby("Category")["Amount"].sum())