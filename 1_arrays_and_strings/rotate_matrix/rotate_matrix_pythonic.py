Matrix = list[list[str]]


def get_rotated_matrix(matrix: Matrix) -> Matrix:
    return [list(reversed(row)) for row in zip(*matrix, strict=True)]
