"""
Task 1: Enhanced Age Verification System
Focus: Multi-category branching and input validation.
"""

try:
    # Collect Name and Age
    name = input("Please enter your name: ").strip()
    age_raw = input("Please enter your age: ")

    # Convert to integer (handles float strings like "25.0")
    age = int(float(age_raw))

    # --- Logic Gates ---
    
    # Check for invalid negative ages first
    if age < 0:
        print(f"Sorry {name}, negative ages are not possible. Please try again.")

    # Classification using if-elif-else
    elif age < 13:
        category = "Child"
        message = "Every day is a playground for you!"
    
    elif age <= 17: # Between 13 and 17
        category = "Teenager"
        message = "You have many opportunities ahead of you."
        
    elif age <= 64: # Between 18 and 64
        category = "Adult"
        message = "Keep working hard toward your goals."
        
    else: # 65 and above
        category = "Senior"
        message = "Your experience and wisdom are greatly valued."

    # Final Output
    if age >= 0:
        print(f"\nHello {name}! As a {category}, {message}")

except ValueError:
    # Runs if the user types letters or symbols instead of numbers
    print("Error: Invalid age. Please enter a numerical value (e.g., 21).")
    