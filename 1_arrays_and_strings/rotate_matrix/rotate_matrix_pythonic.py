def get_rotated_matrix(matrix: list) -> list:
    return [list(reversed(row)) for row in zip(*matrix)]
