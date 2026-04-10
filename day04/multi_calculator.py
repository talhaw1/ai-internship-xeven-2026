# Task 2: Multi-Operation Calculator
# Practicing arithmetic operators, type conversion, and error handling

print("--- Python Power Calculator ---")

try:
    # 1. User Input & Type Conversion
    # We use float() so the calculator can handle both decimals and whole numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Available Operations: +, -, *, /, %, **")
    operation = input("Choose an operation: ")

    # 2. Performing Operations based on selection
    result = None
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        # 3. Handling Division by Zero
        if num2 == 0:
            print("❌ Error: Cannot divide by zero!")
        else:
            result = num1 / num2
    elif operation == "%":
        # Modulus: Returns the remainder
        result = num1 % num2
    elif operation == "**":
        # Exponentiation: num1 raised to the power of num2
        result = num1 ** num2
    else:
        print("❌ Error: Invalid operation selection.")

    # 4. Displaying the Result with Formatting
    if result is not None:
        # We use f-strings to format to 1 decimal place for a clean look
        print(f"\nResult: {num1:.1f} {operation} {num2:.1f} = {result:.1f}")

# 5. Handling non-numeric inputs
except ValueError:
    print("❌ Error: Please enter valid numeric values.")