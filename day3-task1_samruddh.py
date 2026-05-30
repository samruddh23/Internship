def main():
    print("=== Number Pattern Generator ===")
    n = int(input("Enter a value for n: "))
    
    # --- Pattern 1: Right triangle of stars ---
    print("\n1. Right Triangle of Stars:")
    # Outer loop handles the rows
    for i in range(1, n + 1):
        # Inner loop handles columns (printing '*' i times)
        for j in range(i):
            print("*", end=" ")
        print()  # Newline after each row

    # --- Pattern 2: Inverted triangle of numbers ---
    print("\n2. Inverted Triangle of Numbers:")
    # Outer loop counts backward from n down to 1
    for i in range(n, 0, -1):
        # Inner loop prints numbers from 1 up to current row index i
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    # --- Pattern 3: Pascal's triangle first n rows ---
    print("\n3. Pascal's Triangle (First n rows):")
    # We will use lists as an accumulator to build successive rows
    row = []
    for i in range(n):
        # Format padding for centered triangle appearance
        print(" " * (n - i), end="")
        
        # Build the current row based on the previous row's layout
        next_row = [1] * (i + 1)
        for j in range(1, i):
            next_row[j] = row[j - 1] + row[j]
        
        row = next_row
        
        # Print the accumulated row contents
        for num in row:
            print(num, end=" ")
        print()

    # --- Pattern 4: Prime numbers up to n ---
    print(f"\n4. Prime Numbers up to {n}:")
    # Loop through integers starting from 2
    for num in range(2, n + 1):
        # Check factors up to the square root of the number for efficiency
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break  # Not a prime, exit the inner loop immediately
        else:
            # The else block executes ONLY if the inner loop finishes without breaking
            print(num, end=" ")
    print("\n\n=================================")

if __name__ == "__main__":
    main()

Output:
=== Number Pattern Generator ===
Enter a value for n: 4

1. Right Triangle of Stars:
* 
* * 
* * * 
* * * * 

2. Inverted Triangle of Numbers:
1 2 3 4 
1 2 3 
1 2 
1 

3. Pascal's Triangle (First n rows):
    1 
   1 1 
  1 2 1 
 1 3 3 1 

4. Prime Numbers up to 4:
2 3 

=================================
