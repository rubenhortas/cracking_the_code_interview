def get_rotated_matrix(matrix: list) -> list:
    rotated_matrix = []
    rows = len(matrix)
    n = len(matrix)

    for column in range(n):
        row_ = []

        for row in reversed(range(rows)):
            row_.append(matrix[row][column])

        rotated_matrix.append(row_)

    return rotated_matrix
