"""
List Slicing Practice
"""

numbers = list(range(1, 21))  # 1 to 20

print("Original List:", numbers)

# First 5 elements
print("\nFirst 5 elements:", numbers[:5])

# Last 5 elements
print("Last 5 elements:", numbers[-5:])

# Every 3rd element
print("Every 3rd element:", numbers[::3])

# Reverse list
print("Reversed list:", numbers[::-1])

# Middle 10 elements
print("Middle 10 elements:", numbers[5:15])