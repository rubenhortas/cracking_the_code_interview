#!/usr/bin/env python3

import unittest

import check_permutation
import check_permutation_sorting
import check_permutation_count


class TestCheckPermutation(unittest.TestCase):
    def setUp(self):
        self.string1 = 'check permutations'
        self.data = [
            ('permutations check', True),
            ('p3rmut4t10n5 ch3ck', False),
            ('permutations check ', False)
        ]

    def test_check_is_permutation(self):
        for string, result in self.data:
            self.assertEqual(check_permutation.is_permutation(self.string1, string), result)

    def test_is_permutation_sorting(self):
        for string, result in self.data:
            self.assertEqual(check_permutation_sorting.is_permutation(self.string1, string), result)

    def test_is_permutation_count(self):
        for string, result in self.data:
            self.assertEqual(check_permutation_count.is_permutation(self.string1, string), result)
