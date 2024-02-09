#!/usr/bin/env python3

# noinspection PyShadowingNames
def get_rotated_matrix(matrix: list) -> list | None:
    rotated_matrix = []
    rows = len(matrix)
    columns = len(matrix[0])

    for column in range(columns):
        row_ = []

        for row in range(rows - 1, -1, -1):
            row_.append(matrix[row][column])

        rotated_matrix.append(row_)

    return rotated_matrix
