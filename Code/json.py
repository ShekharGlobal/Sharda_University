# JSON file handling
import json

student = {
    "name": "Shekhar",
    "roll_no": 101,
    "course": "Python",
    "marks": 88
}

# Write JSON
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("JSON file created.")

# Read JSON
with open("student.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)
print("Student:", data["name"])
print("Marks:", data["marks"])
