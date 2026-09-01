import pandas as pd

students = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Amit", "Riya", "John"]})
marks = pd.DataFrame({"ID": [1, 2, 3], "Marks": [80, 90, 70]})
print("merge():")
print(pd.merge(students, marks, on="ID"))
print("concat():")
df1 = pd.DataFrame({"Name": ["Amit", "Riya"]})
df2 = pd.DataFrame({"Name": ["John", "Neha"]})
print(pd.concat([df1, df2], ignore_index=True))
print("join():")
left = students.set_index("ID")
right = marks.set_index("ID")
print(left.join(right))
