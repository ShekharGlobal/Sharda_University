import numpy as np

marks = np.array([35, 80, 45, 90, 25])
result = np.where(marks >= 40, "Pass", "Fail")
print("Marks:", marks)
print("Result:", result)
