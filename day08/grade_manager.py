"""
Student Grade Manager

Features:
- Add student
- Remove student
- Update grade
- Calculate average
- Find highest & lowest
- Sort students by grade
- Filter using list comprehension
"""

# Initial Data
student_names = ["Ali", "Ahmed", "Sara", "Zain", "Ayesha"]
student_grades = [85, 70, 92, 60, 78]


# 🔹 Add Student
def add_student(name, grade):
    student_names.append(name)
    student_grades.append(grade)
    print(f"{name} added successfully.")


# 🔹 Remove Student
def remove_student(name):
    if name in student_names:
        index = student_names.index(name)
        student_names.pop(index)
        student_grades.pop(index)
        print(f"{name} removed successfully.")
    else:
        print("Student not found.")


# 🔹 Update Grade
def update_grade(name, new_grade):
    if name in student_names:
        index = student_names.index(name)
        student_grades[index] = new_grade
        print(f"{name}'s grade updated.")
    else:
        print("Student not found.")


# 🔹 Get Average
def get_average():
    return sum(student_grades) / len(student_grades)


# 🔹 Highest & Lowest
def get_highest_lowest():
    max_grade = max(student_grades)
    min_grade = min(student_grades)

    max_index = student_grades.index(max_grade)
    min_index = student_grades.index(min_grade)

    print(f"Highest: {student_names[max_index]} ({max_grade})")
    print(f"Lowest: {student_names[min_index]} ({min_grade})")


# 🔹 Sort by Grade (Descending)
def sort_students():
    combined = list(zip(student_names, student_grades))
    combined.sort(key=lambda x: x[1], reverse=True)

    print("\nTop 3 Performers:")
    for name, grade in combined[:3]:
        print(f"- {name}: {grade}")


# 🔹 Filter Above/Below Average
def filter_students():
    avg = get_average()

    above_avg = [student_names[i] for i in range(len(student_grades)) if student_grades[i] >= avg]
    below_avg = [student_names[i] for i in range(len(student_grades)) if student_grades[i] < avg]

    print(f"\nAverage Grade: {avg:.2f}")
    print("Above Average:", above_avg)
    print("Below Average:", below_avg)


# 🔥 Demo Execution

print("\n--- Initial Data ---")
print(student_names)
print(student_grades)

add_student("Talha", 88)
update_grade("Ali", 90)
remove_student("Zain")

print("\nAverage:", get_average())

get_highest_lowest()
sort_students()
filter_students()