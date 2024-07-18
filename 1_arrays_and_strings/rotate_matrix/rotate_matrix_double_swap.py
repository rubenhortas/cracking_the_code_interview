def get_rotated_matrix(matrix: list):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n - 1 - j]
            matrix[i][n - 1 - j] = temp

    return matrix
