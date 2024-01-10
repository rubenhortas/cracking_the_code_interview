# Pythonic way using Counter

from collections import Counter


def is_unique(string: str) -> bool:
    counter = Counter(string)

    for char in counter:
        if counter[char] > 1:
            return False

    return True
