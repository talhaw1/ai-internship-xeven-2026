# Task 1: Advanced Login System
# This program validates credentials and age using logical operators

print("--- Secure Portal Login ---")

# 1. Collecting User Input
username = input("Enter username: ")
password = input("Enter password: ")
age_input = input("Enter your age: ")

try:
    # 2. Type Conversion: Convert age string to integer for comparison
    age = int(age_input)

    # 3. Defining Logic Conditions (Comparison Operators)
    is_user_valid = len(username) >= 5
    is_pass_valid = len(password) >= 8
    is_age_valid = age >= 18

    # 4. Logical Validation (Logical 'and' & 'not')
    # Access is only granted if ALL conditions are True
    if is_user_valid and is_pass_valid and is_age_valid:
        print("\n✅ Access Granted! Welcome to the portal.")
    else:
        print("\n❌ Access Denied. Please review the errors below:")
        
        # 5. Specific Error Reporting (Using 'not' for clarity)
        if not is_user_valid:
            print("- Username must be at least 5 characters.")
        
        if not is_pass_valid:
            print("- Password must be at least 8 characters.")
            
        if not is_age_valid:
            print("- You must be 18 years or older to enter.")

# 6. Graceful Error Handling for Type Conversion
except ValueError:
    print("\n❌ Error: Age must be entered as a whole number (e.g., 25).")