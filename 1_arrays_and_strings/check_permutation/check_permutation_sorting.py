#!/usr/bin/env python3

def is_permutation(str1: str, str2: str) -> bool:
    # Time complexity: O(nlog(n))
    # Auxiliary space: O(1)
    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)
