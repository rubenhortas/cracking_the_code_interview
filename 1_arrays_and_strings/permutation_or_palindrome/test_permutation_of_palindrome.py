#!/usr/bin/env python3

import unittest
from typing import override

import permutation_or_palindrome_pythonic

import permutation_or_palindrome


class TestPermutationOfPalindrome(unittest.TestCase):
    data: list[tuple[str, bool]] = []  # noqa ruff012

    @override
    def setUp(self) -> None:
        self.data = [("Tact Coa", True), ("t a c t coapapa", True), ("Tact Coax", False), ("asdfadfadf", False)]

    def test_is_permutation_of_palindrome(self) -> None:
        for string, expected_result in self.data:
            self.assertEqual(expected_result, permutation_or_palindrome.is_permutation_or_palindrome(string))

    def test_is_permutation_of_palindrome_pythonic(self) -> None:
        for string, expected_result in self.data:
            self.assertEqual(expected_result, permutation_or_palindrome_pythonic.is_permutation_of_palindrome(string))
