# Sets
numbers = {10, 20, 20, 30, 40}

print(numbers)          # Duplicate 20 is removed

numbers.add(50)
print(numbers)

print(20 in numbers)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
