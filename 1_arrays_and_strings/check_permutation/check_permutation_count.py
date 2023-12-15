#!/usr/bin/env python3

from collections import Counter

# Pythonic way using Counter

def is_permutation(str1: str, str2: str) -> bool:
    return Counter(str1) == Counter(str2)
