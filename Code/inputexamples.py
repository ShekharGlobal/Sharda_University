name = input("Enter student name: ")
branch = input("Enter branch: ")
cgpa = float(input("Enter CGPA: "))

# Deliberate error:
#print("CGPA: " + cgpa)

# Fixed using f-string
print("\n" + "=" * 30)
print("       STUDENT PROFILE")
print("=" * 30)
print(f"Name   : {name}")
print(f"Branch : {branch}")
print(f"CGPA   : {cgpa}")
print("=" * 30)

#Inside an f-string, anything inside {} is treated as a Python variable or expression