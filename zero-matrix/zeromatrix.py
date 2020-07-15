"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""
    rows_to_zero = set()
    cols_to_zero = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                rows_to_zero.add(row)
                cols_to_zero.add(col)
    for row in rows_to_zero:
        for col in range(len(matrix[row])):
            matrix[row][col] = 0
    for row in range(len(matrix)):
        if row not in rows_to_zero:
            for col in cols_to_zero:
                matrix[row][col] = 0
    return matrix


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** TESTS PASSED! YOU'RE DOING GREAT!\n")
