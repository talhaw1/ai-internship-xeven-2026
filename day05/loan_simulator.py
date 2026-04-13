"""
Simple Decision Tree Simulator for Loan Approval

This program simulates a decision tree using conditional statements.
It takes user input and follows decision rules step-by-step.
"""

try:
    # Taking input from user
    age = int(input("Enter your age: "))
    income = float(input("Enter your annual income: "))
    credit_score = int(input("Enter your credit score: "))

    print("\n--- Decision Tree Path ---")

    # Root Node: Check age
    if age < 18:
        print("Step 1: Age < 18 → Reject")
        print("Loan Denied (Applicant is underage)")

    else:
        print("Step 1: Age >= 18 → Passed")

        # Second Node: Check income
        if income < 30000:
            print("Step 2: Income < 30000 → Reject")
            print("Loan Denied (Income too low)")

        else:
            print("Step 2: Income >= 30000 → Passed")

            # Third Node: Check credit score
            if credit_score < 600:
                print("Step 3: Credit Score < 600 → Reject")
                print("Loan Denied (Poor credit score)")

            else:
                print("Step 3: Credit Score >= 600 → Passed")
                print("Loan Approved!")

except ValueError:
    print("Invalid input! Please enter numeric values.")