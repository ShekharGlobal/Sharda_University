# Student Record Management
# Day-1 capstone-style practice

import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    roll_no = input("Roll number: ").strip()
    name = input("Name: ").strip()
    course = input("Course: ").strip()

    while True:
        try:
            marks = float(input("Marks: "))
            if 0 <= marks <= 100:
                break
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Enter a valid number.")

    students.append({
        "roll_no": roll_no,
        "name": name,
        "course": course,
        "marks": marks
    })

    print("Student added.")


def view_students(students):
    if not students:
        print("No students found.")
        return

    for student in students:
        print(
            f"{student['roll_no']} | "
            f"{student['name']} | "
            f"{student['course']} | "
            f"{student['marks']}"
        )


def search_student(students):
    roll_no = input("Enter roll number: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:
            print(student)
            return

    print("Student not found.")


def calculate_average(students):
    if not students:
        print("No students available.")
        return

    total = sum(student["marks"] for student in students)
    average = total / len(students)

    print(f"Average marks: {average:.2f}")


def main():
    students = load_students()

    while True:
        print("\n=== Student Record Management ===")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Calculate average")
        print("5. Save and exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            calculate_average(students)
        elif choice == "5":
            save_students(students)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
