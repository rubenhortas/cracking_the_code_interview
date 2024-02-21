def get_rotated_matrix(matrix: list) -> list:
    rows = len(matrix)

    for i in range(rows):
        for j in range(i, rows):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(rows):
        for j in range(int(rows / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][rows - 1 - j]
            matrix[i][rows - 1 - j] = temp

    return matrix
