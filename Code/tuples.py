# Tuples
student = ("Shekhar", 101, "Python")

print(student)
print(student[0])
print(student[1])

# Tuple unpacking
name, roll_no, course = student
print(name, roll_no, course)

# Tuple is immutable:
# student[0] = "Amit"   # This gives TypeError
