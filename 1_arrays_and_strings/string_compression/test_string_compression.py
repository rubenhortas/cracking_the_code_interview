#!/usr/bin/env python3

import unittest

import string_compression_pythonic

import string_compression


class TestStringCompression(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [("aabcccccaaa", "a2b1c5a3"), ("bcda", "bcda"), ("aaa", "a3")]

    def test_string_compression(self) -> None:
        for string, expected_result in self.data:
            self.assertEqual(expected_result, string_compression.get_compressed_string(string))

    def test_string_compression_pythonic(self) -> None:
        for string, expected_result in self.data:
            self.assertEqual(expected_result, string_compression_pythonic.get_compressed_string(string))
