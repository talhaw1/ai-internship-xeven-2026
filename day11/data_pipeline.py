"""
Data Processing Pipeline (1000 Records)
Uses: for loop, enumerate(), zip(), continue, break
"""

import random

# 🔹 Generate 1000 records
names = [f"User{i}" for i in range(1000)]
ages = [random.randint(18, 60) for _ in range(1000)]
salaries = [random.randint(30000, 100000) for _ in range(1000)]

# 🔹 Introduce some invalid & critical data
names[50] = None          # invalid (missing)
salaries[120] = None      # invalid (missing)
ages[300] = -10           # critical error

# 🔹 Validate matching lengths
if not (len(names) == len(ages) == len(salaries)):
    print("Data length mismatch! Cannot process.")
else:
    total_records = len(names)

    print("\n--- Processing 1000 Records ---")

    for index, (name, age, salary) in enumerate(zip(names, ages, salaries), start=1):

        print(f"Processing record {index} of {total_records}")

        # 🔹 Skip invalid records
        if name is None or salary is None:
            print("Invalid record Skipping")
            continue

        # 🔹 Critical error → STOP pipeline
        if age < 0:
            print("Critical error (invalid age) Stopping pipeline")
            break

        # 🔹 Transformation (example)
        bonus = salary * 0.10
        updated_salary = salary + bonus

        # (Optional: limit output to avoid flooding console)
        if index <= 125:
            print(f"{name} | Age: {age} | Updated Salary: {updated_salary}")