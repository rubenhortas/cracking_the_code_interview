#!/usr/bin/env python3
import copy
import unittest

import rotate_matrix
import rotate_matrix_pythonic
import rotate_matrix_alternative
import rotate_matrix_swap_index_by_index
import rotate_matrix_double_swap

from utils import print_matrix


def _print_matrices(matrix: list, rotated_matrix: list, expected_result: list) -> None:
    print('Matrix:')
    print_matrix(matrix)

    print('Rotated matrix:')
    print_matrix(rotated_matrix)

    print('Expected result:')
    print_matrix(expected_result)


class TestRotateMatrix(unittest.TestCase):

    def setUp(self):
        self.data = [
            ([
                 ['o', 'o', 'o'],
                 ['*', '*', '*'],
                 ['x', 'x', 'x']
             ],
             [
                 ['x', '*', 'o'],
                 ['x', '*', 'o'],
                 ['x', '*', 'o']
             ]),
            ([
                 ['00', '01', '02'],
                 ['10', '11', '12'],
                 ['20', '21', '22']
             ],
             [
                 ['20', '10', '00'],
                 ['21', '11', '01'],
                 ['22', '12', '02'],
             ]),
            ([
                 ['a', 'a', 'a'],
                 ['b', 'b', 'b'],
                 ['c', 'c', 'c']
             ],
             [
                 ['c', 'b', 'a'],
                 ['c', 'b', 'a'],
                 ['c', 'b', 'a']
             ])
        ]

    def test_rotate_matrix(self):
        for matrix, expected_result in self.data:
            rotated_matrix = rotate_matrix.get_rotated_matrix(matrix)
            # _print_matrices(matrix, rotated_matrix, expected_result)
            self.assertEqual(expected_result, rotated_matrix)

    def test_rotate_matrix_pythonic(self):
        for matrix, expected_result in self.data:
            rotated_matrix = rotate_matrix_pythonic.get_rotated_matrix(matrix)
            # _print_matrices(matrix, rotated_matrix, expected_result)
            self.assertEqual(expected_result, rotated_matrix)

    def test_rotate_matrix_alternative(self):
        for matrix, expected_result in self.data:
            rotated_matrix = rotate_matrix_alternative.get_rotated_matrix(matrix)
            # _print_matrices(matrix, rotated_matrix, expected_result)
            self.assertEqual(expected_result, rotated_matrix)

    def test_rotate_matrix_swap_index_by_index(self):
        for matrix, expected_result in self.data:
            # original_matrix = copy.deepcopy(matrix)
            rotated_matrix = rotate_matrix_swap_index_by_index.get_rotated_matrix(matrix)
            # _print_matrices(original_matrix, rotated_matrix, expected_result)
            self.assertEqual(expected_result, rotated_matrix)

    def test_rotate_matrix_double_swap(self):
        for matrix, expected_result in self.data:
            # original_matrix = copy.deepcopy(matrix)
            rotated_matrix = rotate_matrix_double_swap.get_rotated_matrix(matrix)
            # _print_matrices(original_matrix, rotated_matrix, expected_result)
            self.assertEqual(expected_result, rotated_matrix)
