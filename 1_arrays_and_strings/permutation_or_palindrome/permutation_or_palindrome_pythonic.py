#!/usr/bin/env python3

from collections import Counter


def is_permutation_of_palindrome(string: str) -> bool:
    normalized_string = string.replace(' ', '').lower()
    counts = Counter(normalized_string)
    odd_chars = 0

    for c in counts:
        if counts[c] % 2 != 0:
            # In a palindrome of even length all characters have to appear an even number of times.
            if len(normalized_string) % 2 == 0:
                return False
            else:
                odd_chars = odd_chars + 1

                # In a palindrome of odd length all characters have to appear an even number of times,
                # except for one character, which will appear once.
                if odd_chars > 1:
                    return False

    return True
