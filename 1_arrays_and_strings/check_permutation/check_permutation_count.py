# Pythonic way using Counter

from collections import Counter


def is_permutation(str1: str, str2: str) -> bool:
    return Counter(str1) == Counter(str2)
