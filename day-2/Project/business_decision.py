import pandas as pd
import numpy as np

# ============================================================
# DAY 2 - E-COMMERCE SALES ANALYSIS
# Business Decision Project
# ============================================================

# 1. Read the CSV file
# The provided CSV uses TAB as the separator.
df = pd.read_csv("ecommerce_sales_day2.csv", sep="\t")

print("=" * 60)
print("E-COMMERCE SALES ANALYSIS")
print("=" * 60)

# ------------------------------------------------------------
# 2. Understand the dataset
# ------------------------------------------------------------

print("\n1. FIRST 5 RECORDS")
print(df.head())

print("\n2. DATASET SIZE")
print("Rows, Columns:", df.shape)

print("\n3. COLUMN NAMES")
print(df.columns.tolist())

print("\n4. DATA INFORMATION")
df.info()

# ------------------------------------------------------------
# 3. Check data quality
# ------------------------------------------------------------

print("\n5. MISSING VALUES")
print(df.isnull().sum())

print("\n6. DUPLICATE RECORDS")
print("Number of duplicates:", df.duplicated().sum())

# ------------------------------------------------------------
# 4. Clean the data
# ------------------------------------------------------------

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing City
df["City"] = df["City"].fillna("Unknown")

# Fill missing Price with average price
df["Price"] = df["Price"].fillna(df["Price"].mean())

# ------------------------------------------------------------
# 5. Create Revenue
# Revenue = Quantity × Price
# ------------------------------------------------------------

df["Revenue"] = df["Quantity"] * df["Price"]

print("\n7. DATA AFTER CLEANING")
print(df.head())

# ------------------------------------------------------------
# 6. Overall business performance
# ------------------------------------------------------------

total_revenue = df["Revenue"].sum()
average_order = df["Revenue"].mean()
highest_order = df["Revenue"].max()
lowest_order = df["Revenue"].min()

print("\n" + "=" * 60)
print("BUSINESS PERFORMANCE")
print("=" * 60)

print(f"Total Revenue       : ₹{total_revenue:,.2f}")
print(f"Average Order Value : ₹{average_order:,.2f}")
print(f"Highest Order Value : ₹{highest_order:,.2f}")
print(f"Lowest Order Value  : ₹{lowest_order:,.2f}")

# ------------------------------------------------------------
# 7. Product analysis
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("PRODUCT ANALYSIS")
print("=" * 60)

product_sales = df.groupby("Product")["Revenue"].sum()
product_sales = product_sales.sort_values(ascending=False)

print(product_sales)

best_product = product_sales.idxmax()

print("\nBest Product:", best_product)
print("Business Decision:")
print(f"Consider giving '{best_product}' more inventory and marketing attention.")

# ------------------------------------------------------------
# 8. City analysis
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("CITY ANALYSIS")
print("=" * 60)

city_sales = df.groupby("City")["Revenue"].sum()
city_sales = city_sales.sort_values(ascending=False)

print(city_sales)

best_city = city_sales.idxmax()

print("\nBest City:", best_city)
print("Business Decision:")
print(f"Consider targeted marketing and better product availability in {best_city}.")

# ------------------------------------------------------------
# 9. Category analysis
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("CATEGORY ANALYSIS")
print("=" * 60)

category_sales = df.groupby("Category")["Revenue"].sum()
category_sales = category_sales.sort_values(ascending=False)

print(category_sales)

best_category = category_sales.idxmax()

print("\nBest Category:", best_category)
print("Business Decision:")
print(f"Prioritize the '{best_category}' category while investigating weaker categories.")

# ------------------------------------------------------------
# 10. High-value orders
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("HIGH-VALUE ORDERS")
print("=" * 60)

high_value_orders = df[df["Revenue"] > 50000]

print(high_value_orders[
    ["Order_ID", "Product", "City", "Quantity", "Price", "Revenue", "Customer"]
])

print("\nBusiness Decision:")
print("High-value orders may require additional customer-service and delivery attention.")

# ------------------------------------------------------------
# 11. Top 5 orders
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("TOP 5 ORDERS")
print("=" * 60)

top_orders = df.sort_values("Revenue", ascending=False).head(5)

print(top_orders[
    ["Order_ID", "Product", "City", "Revenue", "Customer"]
])

# ------------------------------------------------------------
# 12. Top customers
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("TOP 5 CUSTOMERS")
print("=" * 60)

customer_sales = df.groupby("Customer")["Revenue"].sum()
customer_sales = customer_sales.sort_values(ascending=False)

print(customer_sales.head(5))

print("\nBusiness Decision:")
print("Top customers can be targeted with loyalty programs and personalized offers.")

# ------------------------------------------------------------
# 13. NumPy demonstration
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("NUMPY ANALYSIS")
print("=" * 60)

revenue_array = np.array(df["Revenue"])

print("Total using NumPy :", np.sum(revenue_array))
print("Average using NumPy:", np.mean(revenue_array))
print("Maximum using NumPy:", np.max(revenue_array))
print("Minimum using NumPy:", np.min(revenue_array))

# ------------------------------------------------------------
# 14. Final Management Summary
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FINAL MANAGEMENT SUMMARY")
print("=" * 60)

print(f"1. Total Revenue       : ₹{total_revenue:,.2f}")
print(f"2. Average Order Value : ₹{average_order:,.2f}")
print(f"3. Best Product        : {best_product}")
print(f"4. Best City           : {best_city}")
print(f"5. Best Category       : {best_category}")
print(f"6. High-Value Orders   : {len(high_value_orders)}")

print("\nKEY LESSON:")
print("Data Science is not only about calculating numbers.")
print("We use data to discover insights and support business decisions.")

print("\nAnalyst statement:")
print("The data shows ______, therefore the business should ______.")
