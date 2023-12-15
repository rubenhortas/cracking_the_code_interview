#!/usr/bin/env python3

# Given two strings, write a method to decide if one is a permutation of the other.
# We will assume the following:
#   * Permutation is case-sensitive
#   * Whitespaces are significant
#   * ASCII encoding

def is_permutation(str1: str, str2: str) -> bool:
    # Time complexity: O(nlog(n))
    # Auxiliary space: O(1)
    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)
