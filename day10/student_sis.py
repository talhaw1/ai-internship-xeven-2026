"""
Student Information System (Production Version)

Features:
- Load existing data from JSON
- Add student (no overwrite)
- Update grades
- Calculate average
- Find top student
- Generate report
- Save updated data
"""

import json

# Global data store
students = {}


# 🔹 Load Data (SAFE)
def load_from_file(filename="students.json"):
    global students
    try:
        with open(filename, "r") as file:
            students = json.load(file)
        print("Data loaded successfully.")
    except FileNotFoundError:
        students = {}
        print("No existing file found. Starting fresh.")


# 🔹 Save Data
def save_to_file(filename="students.json"):
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)
    print("Data saved successfully.")


# 🔹 Add Student (NO OVERWRITE)
def add_student(student_id, name, age):
    if student_id in students:
        print(f"Student ID {student_id} already exists.")
    else:
        students[student_id] = {
            "name": name,
            "age": age,
            "grades": {}
        }
        print(f"Student {name} added.")


# 🔹 Update Grade
def update_grade(student_id, subject, score):
    if student_id in students:
        students[student_id]["grades"][subject] = score
        print(f"Grade updated for {students[student_id]['name']}")
    else:
        print("Student not found.")


# 🔹 Calculate Average
def get_student_average(student_id):
    if student_id in students:
        grades = students[student_id]["grades"].values()

        if len(grades) == 0:
            return 0

        return sum(grades) / len(grades)

    return None


# 🔹 Find Top Student
def find_top_student():
    top_student = None
    highest_avg = -1

    for student_id in students:
        avg = get_student_average(student_id)

        if avg is not None and avg > highest_avg:
            highest_avg = avg
            top_student = students[student_id]["name"]

    return top_student, highest_avg


# 🔹 Generate Report
def generate_report():
    report = []

    for student_id in students:
        avg = get_student_average(student_id)
        report.append((students[student_id]["name"], avg))

    # Sort by GPA descending
    report.sort(key=lambda x: x[1], reverse=True)

    print("\n--- Student Report ---")
    for name, avg in report:
        print(f"{name} - GPA: {avg:.2f}")


# 🔥 MAIN PROGRAM FLOW (IMPORTANT)

# Step 1: Load existing data
load_from_file()

# Step 2: Perform operations
add_student("S1", "Ali", 20)
add_student("S2", "Sara", 21)

update_grade("S1", "Math", 85)
update_grade("S1", "Physics", 90)

update_grade("S2", "Math", 95)
update_grade("S2", "Physics", 88)

# Step 3: Show results
print("\nAverage of S1:", get_student_average("S1"))

top, avg = find_top_student()
print(f"Top Student: {top} with GPA {avg:.2f}")

generate_report()

# Step 4: Save updated data
save_to_file()