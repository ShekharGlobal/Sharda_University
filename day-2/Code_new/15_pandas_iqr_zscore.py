import pandas as pd

marks = pd.Series([50, 55, 60, 65, 70, 75, 200])
Q1 = marks.quantile(0.25)
Q3 = marks.quantile(0.75)
IQR = Q3 - Q1
print("Q1 =", Q1)
print("Q3 =", Q3)
print("IQR =", IQR)
mean = marks.mean()
std = marks.std()
z = (marks - mean) / std
print("Mean =", mean)
print("Standard deviation =", std)
print("Z-scores:")
print(z)
