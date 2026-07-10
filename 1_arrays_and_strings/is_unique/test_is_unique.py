#!/usr/bin/env python3

import unittest

import is_unique_count
import is_unique_counter
import is_unique_set
import is_unique_without_structures

import is_unique


class TestIsUnique(unittest.TestCase):
    def setUp(self) -> None:
        self.unique = "abcdefghij"
        self.not_unique = "abcdefabcd"

    def test_is_unique(self) -> None:
        self.assertTrue(is_unique.is_unique(self.unique))
        self.assertFalse(is_unique.is_unique(self.not_unique))

    def test_is_unique_count(self) -> None:
        self.assertTrue(is_unique_count.is_unique(self.unique))
        self.assertFalse(is_unique_count.is_unique(self.not_unique))

    def test_is_unique_counter(self) -> None:
        self.assertTrue(is_unique_counter.is_unique(self.unique))
        self.assertFalse(is_unique_counter.is_unique(self.not_unique))

    def test_is_unique_set(self) -> None:
        self.assertTrue(is_unique_set.is_unique(self.unique))
        self.assertFalse(is_unique_set.is_unique(self.not_unique))

    def test_is_unique_without_structures(self) -> None:
        self.assertTrue(is_unique_without_structures.is_unique(self.unique))
        self.assertFalse(is_unique_without_structures.is_unique(self.not_unique))
