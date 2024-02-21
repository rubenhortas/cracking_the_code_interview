#!/usr/bin/env python3

import unittest

import rotate_matrix
import rotate_matrix_pythonic

from utils import print_matrix


class TestRotateMatrix(unittest.TestCase):
    def setUp(self):
        self.data = [
            ([
                 ['o', 'o', 'o', 'o'],
                 ['*', '*', '*', '*'],
                 ['x', 'x', 'x', 'x']
             ],
             [
                 ['x', '*', 'o'],
                 ['x', '*', 'o'],
                 ['x', '*', 'o'],
                 ['x', '*', 'o']
             ]),
            ([
                 ['00', '01', '02', '03'],
                 ['10', '11', '12', '13'],
                 ['20', '21', '22', '23']
             ],
             [
                 ['20', '10', '00'],
                 ['21', '11', '01'],
                 ['22', '12', '02'],
                 ['23', '13', '03']
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
        for matrix, result in self.data:
            rotated_matrix = rotate_matrix.get_rotated_matrix(matrix)
            if matrix:
                print('Matrix:')
                print_matrix(matrix)
                print('Rotated matrix:')
                print_matrix(rotated_matrix)
                print('Expected result:')
                print_matrix(result)
            self.assertEqual(rotated_matrix, result)

    def test_rotate_matrix_pythonic(self):
        for matrix, result in self.data:
            rotated_matrix = rotate_matrix_pythonic.get_rotated_matrix(matrix)
            if matrix:
                print('Matrix:')
                print_matrix(matrix)
                print('Rotated matrix:')
                print_matrix(rotated_matrix)
                print('Expected result:')
                print_matrix(result)
            self.assertEqual(rotated_matrix, result)