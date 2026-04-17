# Day 8: Task 3 - Data Cleaning Pipeline

def run_cleaning_pipeline():
    # 1. The Messy Dataset
    messy_data = ["  python ", "MACHINE LEARNING", None, "python", " Data Science ", "machine learning", None, "   PYTHON  ", "deep learning"]
    
    # Metrics: Before Cleaning
    initial_count = len(messy_data)
    initial_completeness = (len([x for x in messy_data if x is not None]) / initial_count) * 100

    print("--- 🛠️ Data Quality Report: BEFORE ---")
    print(f"Data: {messy_data}")
    print(f"Total Items: {initial_count}")
    print(f"Completeness: {initial_completeness:.1f}%")

    # --- 2. The Cleaning Steps (List Comprehensions) ---
    
    # Step A: Remove None values (Filter)
    step1 = [item for item in messy_data if item is not None]
    
    # Step B: Strip whitespace and normalize to Lowercase
    step2 = [item.strip().lower() for item in step1]
    
    # Step C: Remove Duplicates
    # While we could use set(), a list comprehension way is:
    final_data = []
    [final_data.append(x) for x in step2 if x not in final_data]

    # --- 3. Display Results & Metrics: AFTER ---
    unique_count = len(final_data)
    final_completeness = 100.0  # Since we removed None

    print("\n--- ✅ Data Quality Report: AFTER ---")
    print(f"Data: {final_data}")
    print(f"Unique Items: {unique_count}")
    print(f"Completeness: {final_completeness:.1f}%")
    
    # Summary of changes
    print(f"\nSummary: Reduced from {initial_count} items to {unique_count} clean items.")

if __name__ == "__main__":
    run_cleaning_pipeline()
       