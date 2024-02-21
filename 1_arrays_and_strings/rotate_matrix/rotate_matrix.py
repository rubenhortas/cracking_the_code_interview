#!/usr/bin/env python3

def get_rotated_matrix(matrix: list) -> list:
    rotated_matrix = []
    rows = len(matrix)
    columns = len(matrix[0])

    for column in range(columns):
        row_ = []

        for row in reversed(range(rows)):
            row_.append(matrix[row][column])

        rotated_matrix.append(row_)

    return rotated_matrix
