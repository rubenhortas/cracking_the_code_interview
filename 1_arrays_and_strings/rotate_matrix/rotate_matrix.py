def get_rotated_matrix(matrix: list[list[object]]) -> list[list[object]]:
    rows = len(matrix)
    columns = len(matrix[0]) if rows > 0 else 0

    return [[matrix[row][col] for row in reversed(range(rows))] for col in range(columns)]
