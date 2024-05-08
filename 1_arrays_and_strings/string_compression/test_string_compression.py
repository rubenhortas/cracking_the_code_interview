#!/usr/bin/env python3

import unittest

import string_compression
import string_compression_pythonic


class TestStringCompression(unittest.TestCase):
    def setUp(self):
        self.data = [
            ('aabcccccaaa', 'a2b1c5a3'),
            ('bcda', 'bcda'),
            ('aaa', 'a3')
        ]

    def test_string_compression(self):
        for string, expected_result in self.data:
            self.assertEqual(expected_result, string_compression.get_compressed_string(string))

    def test_string_compression_pythonic(self):
        for string, expected_result in self.data:
            self.assertEqual(expected_result, string_compression_pythonic.get_compressed_string(string))
