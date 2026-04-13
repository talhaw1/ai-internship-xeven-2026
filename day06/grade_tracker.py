"""
Grade Tracker using Parallel Lists
"""

student_names = ["Ali", "Ahmed", "Sara", "Zain", "Ayesha"]
student_grades = [85, 45, 90, 60, 30]

# Highest grade
max_grade = max(student_grades)
max_index = student_grades.index(max_grade)

# Lowest grade
min_grade = min(student_grades)
min_index = student_grades.index(min_grade)

# Average grade
average = sum(student_grades) / len(student_grades)

# Passed students
print("\n--- Grade Report ---")

print(f"Highest Grade: {max_grade} (Student: {student_names[max_index]})")
print(f"Lowest Grade: {min_grade} (Student: {student_names[min_index]})")
print(f"Average Grade: {average:.2f}")

print("\nStudents who passed:")
for i in range(len(student_grades)):
    if student_grades[i] >= 50:
        print(f"{student_names[i]} - {student_grades[i]}")