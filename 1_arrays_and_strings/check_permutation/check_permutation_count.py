#!/usr/bin/env python3

from collections import Counter


# Given two strings, write a method to decide if one is a permutation of the other.
# We will assume the following:
#   * Permutation is case-sensitive
#   * Whitespaces are significant
#   * ASCII encoding

# Pythonic way using Counter

def is_permutation(str1: str, str2: str) -> bool:
    return Counter(str1) == Counter(str2)
