def get_rotated_matrix(matrix: list) -> list:
    n = len(matrix)

    result = [[0] * n for i in range(n)]

    for i, j in zip(range(n), reversed(range(n))):
        for k in range(n):
            result[k][i] = matrix[j][k]

    return result
