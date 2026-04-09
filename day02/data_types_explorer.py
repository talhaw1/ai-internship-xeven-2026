"""
Script: data_types_explorer.py
Purpose: Explore Python's core data types and type conversion.
Part of the 30-Day AI Internship - Day 02 Practical Tasks.
"""

# --- 1. Demonstrating Data Types (PEP 8 naming) ---

# Integer: Whole numbers
student_id = 1001 

# Float: Decimal numbers
accuracy_score = 0.98 

# Boolean: Logical True/False
is_process_complete = True 

# String: Text data
project_title = "AI Internship Day 2" 

print("--- Step 1: Checking Original Types ---")
print(f"ID: {student_id} | Type: {type(student_id)}")
print(f"Score: {accuracy_score} | Type: {type(accuracy_score)}")
print(f"Status: {is_process_complete} | Type: {type(is_process_complete)}")
print(f"Title: {project_title} | Type: {type(project_title)}")
print("-" * 30)

# --- 2. Type Conversion (Casting) ---

print("\n--- Step 2: Demonstrating Type Conversion ---")

# int to str: Useful for labeling numbers
id_as_text = str(student_id)
print(f"Converted ID to String: '{id_as_text}' | New Type: {type(id_as_text)}")

# str to float: Essential for processing user math input
price_string = "19.99"
price_as_float = float(price_string)
print(f"Converted String to Float: {price_as_float} | New Type: {type(price_as_float)}")

# float to int: Truncating decimals
truncated_score = int(accuracy_score) 
print(f"Converted Float {accuracy_score} to Int: {truncated_score} (Notice the decimal is gone!)")