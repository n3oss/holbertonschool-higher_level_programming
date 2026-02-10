#!/usr/bin/python3
"""pyhton doc"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Start each row with 1
        row = [1]
        # Get reference to the previous row
        prev_row = triangle[i - 1]

        # Calculate the middle elements
        # They are the sum of the two elements above them
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        # End each row with 1
        row.append(1)
        # Add the completed row to our triangle
        triangle.append(row)

    return triangle
