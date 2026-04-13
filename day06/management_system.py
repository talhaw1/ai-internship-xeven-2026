"""
Student Management System using Lists
"""

# Initial list of students
students = ["Ali", "Ahmed", "Sara", "Zain", "Ayesha"]

print("Initial Students:", students)

# Add students
students.append("Talha")  # Add at end
print("\nAfter append:", students)

students.insert(2, "Usman")  # Add at index 2
print("After insert:", students)

# Remove students
students.remove("Ahmed")  # Remove by value
print("\nAfter remove:", students)

students.pop()  # Remove last student
print("After pop:", students)

# Slicing first 3 students
first_three = students[:3]
print("\nFirst 3 students:", first_three)

# Sort list
students.sort()
print("\nSorted students:", students)