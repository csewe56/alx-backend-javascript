def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle up to the nth row.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = []  # Initialize an empty list to hold the rows of Pascal's triangle

    for i in range(n):  # Iterate over the range of rows
        row = [1] * (i + 1)  # Start each row with 1's
        for j in range(1, i):  # Iterate over the columns of the current row
            # Each number is the sum of the two numbers directly above it
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)  # Add the current row to the triangle

    return triangle

# Testing the function
for row in pascal_triangle(5):
    print(row)

