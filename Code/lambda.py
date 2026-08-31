# Lambda functions
square = lambda x: x * x

print(square(5))

add = lambda a, b: a + b
print(add(10, 20))

# Useful with sorted()
students = [
    {"name": "Amit", "marks": 82},
    {"name": "Priya", "marks": 95},
    {"name": "Rahul", "marks": 76}
]

students_sorted = sorted(students, key=lambda s: s["marks"], reverse=True)

for student in students_sorted:
    print(student["name"], student["marks"])
