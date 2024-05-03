#!/usr/bin/env python3

import unittest

from one_away import one_away


class TestOneAway(unittest.TestCase):
    def setUp(self):
        self.data = [
            ('pale', 'ple', True),
            ('pales', 'pale', True),
            ('pale', 'bale', True),
            ('pale', 'bae', False)
        ]

    def test_one_away(self):
        for str1, str2, expected_result in self.data:
            self.assertEqual(expected_result, one_away(str1, str2))
