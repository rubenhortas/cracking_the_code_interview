def get_rotated_matrix(matrix: list) -> list:
    rows = len(matrix)
    columns = len(matrix[0])

    result = [[0] * rows for i in range(columns)]

    for i, j in zip(range(columns), reversed(range(rows))):
        for k in range(columns):
            result[k][i] = matrix[j][k]
    return result