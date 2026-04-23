def pattern_generator():
    # --- 1. Pyramid Pattern ---
    print("--- 1. Star Pyramid ---")
    rows = 5
    for i in range(1, rows + 1):
        # Print spaces to center the pyramid
        print(" " * (rows - i), end="")
        # Print stars
        print("*" * (2 * i - 1))
    print()

    # --- 2. Multiplication Table (Nested Loops) ---
    print("--- 2. Multiplication Table (1-5) ---")
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i * j:3}", end=" ")
        print()  # New line after each row
    print()

    # --- 3. Matrix Operations ---
    print("--- 3. Matrix Operations ---")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Transpose Matrix (Rows become Columns)
    # Using nested loop logic
    transpose = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transpose[j][i] = matrix[i][j]
    
    print("Transposed Matrix:")
    for row in transpose:
        print(row)

    # Diagonal Elements
    diagonal = [matrix[i][i] for i in range(len(matrix))]
    print(f"\nMain Diagonal: {diagonal}")

    # --- 4. Simple ASCII Art (Checkerboard) ---
    print("\n--- 4. ASCII Checkerboard ---")
    size = 6
    for row in range(size):
        for col in range(size):
            if (row + col) % 2 == 0:
                print("##", end="")
            else:
                print("  ", end="")
        print()

if __name__ == "__main__":
    pattern_generator()