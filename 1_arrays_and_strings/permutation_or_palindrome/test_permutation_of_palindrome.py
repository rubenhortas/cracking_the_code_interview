#!/usr/bin/env python3

import unittest

import permutation_of_palindrome
import permutation_or_palindrome_pythonic


class TestPermutationOfPalindrome(unittest.TestCase):
    def setUp(self):
        self.data = [
            ('Tact Coa', True),
            ('t a c t coapapa', True),
            ('Tact Coax', False),
            ('asdfadfadf', False)
        ]

    def test_is_permutation_of_palindrome(self):
        for string, expected_result in self.data:
            self.assertEqual(expected_result, permutation_of_palindrome.is_permutation_of_palindrome(string))

    def test_is_permutation_of_palindrome_pythonic(self):
        for string, expected_result in self.data:
            self.assertEqual(expected_result, permutation_or_palindrome_pythonic.is_permutation_of_palindrome(string))
