# Function scope
college = "Sharda University"   # Global variable

def show_student():
    name = "Shekhar"            # Local variable
    print(name)
    print(college)              # Global variable can be read here

show_student()

# print(name)  # NameError because name is local to the function
