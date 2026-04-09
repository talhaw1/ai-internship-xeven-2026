"""
Task 2: Grade Calculator with Feedback
Focus: Efficient range checking and input validation.
"""

try:
    # 1. Accept numeric grade
    score_input = input("Enter your numeric grade (0-100): ")
    score = float(score_input)

    # 2. Validate input range (0-100)
    if score < 0 or score > 100:
        print("Invalid Grade! Please enter a value between 0 and 100.")
    
    else:
        # 3. Assign letter grades and messages using efficient elif
        # Because we check from highest to lowest, we don't need 'score >= 90 and score <= 100'
        if score >= 90:
            grade = "A"
            message = "Excellent work! You've mastered this material."
        elif score >= 80:
            grade = "B"
            message = "Good job! You've shown a strong understanding."
        elif score >= 70:
            grade = "C"
            message = "Well done! You have a solid foundation, but keep practicing."
        elif score >= 60:
            grade = "D"
            message = "You passed, but there is significant room for improvement."
        else:
            grade = "F"
            message = "Unfortunately, you did not pass this time. Don't give up!"

        # 4. Final Output
        print(f"\n--- Grade Report ---")
        print(f"Score: {score}")
        print(f"Grade: {grade}")
        print(f"Feedback: {message}")

except ValueError:
    print("Error: Input must be a numeric value.")