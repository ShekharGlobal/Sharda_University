import pandas as pd
import numpy as np

# 1. Read CSV
df = pd.read_csv("ecommerce_sales_day2.csv", sep="\t")

# 2. Display first 5 rows
print("First 5 rows:")
print(df.head())

# 3. Understand the dataset
print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

# 4. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 5. Remove duplicate records
df = df.drop_duplicates()

# 6. Fill missing City
df["City"] = df["City"].fillna("Unknown")

# 7. Fill missing Price
df["Price"] = df["Price"].fillna(df["Price"].mean())

# 8. Create Revenue
df["Revenue"] = df["Quantity"] * df["Price"]

print("\nData after cleaning:")
print(df.head())

# 9. Total Revenue
print("\nTotal Revenue:")
print(df["Revenue"].sum())

# 10. Average Revenue
print("\nAverage Revenue:")
print(df["Revenue"].mean())

# 11. Highest Revenue
print("\nHighest Revenue:")
print(df["Revenue"].max())

# 12. Orders above ₹10,000
print("\nOrders above ₹10,000:")
print(df[df["Revenue"] > 10000])

# 13. Sort by Revenue
print("\nTop 5 orders:")
print(df.sort_values("Revenue", ascending=False).head())

# 14. Product-wise Revenue
print("\nProduct-wise Revenue:")
print(df.groupby("Product")["Revenue"].sum())

# 15. City-wise Revenue
print("\nCity-wise Revenue:")
print(df.groupby("City")["Revenue"].sum())

# 16. Category-wise Revenue
print("\nCategory-wise Revenue:")
print(df.groupby("Category")["Revenue"].sum())