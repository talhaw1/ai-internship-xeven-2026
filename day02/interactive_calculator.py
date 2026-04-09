"""
Task 2: Interactive Calculator (Basic)
Demonstrating input(), output, type casting, and error handling.
Author: Talha (2026)
"""

try:
    # 1. Collect Data & Convert to Float (allows decimals like 5.5)
    first_number = float(input("Enter First Number: "))
    second_number = float(input("Enter Second Number: "))

    # 2. Output with f-strings and clear formatting
    print(f"\n--- Interactive Calculator Results ---")
    print(f"The sum of {first_number} and {second_number} is: {first_number + second_number}")
    print(f"The difference of {first_number} and {second_number} is: {first_number - second_number}")
    print(f"The product of {first_number} and {second_number} is: {first_number * second_number}")

    # 3. Handle Division by Zero safely
    if second_number != 0:
        print(f"The quotient of {first_number} and {second_number} is: {first_number / second_number}")
    else:
        print("The quotient: Error (Cannot divide by zero)")

except ValueError:
    # This runs if the user types letters instead of numbers
    print("Error: Invalid input! Please enter numeric values only (e.g., 10 or 10.5).")

except Exception as e:
    # A catch-all for any other unexpected errors
    print(f"An unexpected error occurred: {e}")
# This forces the program to wait for you before closing
input("\nExecution finished. Press Enter to close...")