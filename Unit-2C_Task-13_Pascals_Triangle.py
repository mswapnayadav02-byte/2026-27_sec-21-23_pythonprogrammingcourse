n = int(input("Enter the number of rows for Pascal's Triangle: "))
for i in range(n):
    # Print leading spaces for formatting
    print(" " * (n - i - 1), end="")
    
    # Calculate and print the values in the current row
    value = 1
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)  # Update value using binomial coefficient formula
    
    print()  # Move to the next line after each row