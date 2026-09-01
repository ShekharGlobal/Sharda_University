import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
matrix = arr.reshape(2, 3)
print("Reshaped:")
print(matrix)
print("Ravel:", matrix.ravel())
print("Flatten:", matrix.flatten())
