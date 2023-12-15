#!/usr/bin/env python3

"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
"""


def one_away(str1: str, str2: str) -> bool:
    str1_length = len(str1)
    str2_length = len(str2)

    if str2_length == str1_length:
        return _has_only_one_replaced(str1, str2)
    elif str2_length == str1_length + 1:
        return _hasOnlyOneInseredtOrRemoved(str1, str2, str1_length, str2_length)
    elif str2_length == str1_length - 1:
        return _hasOnlyOneInseredtOrRemoved(str2, str1, str2_length, str1_length)
    else:
        return False


def _has_only_one_replaced(str1: str, str2: str) -> bool:
    has_difference = False

    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            if has_difference:
                return False
            else:
                has_difference = True

    return True


def _hasOnlyOneInseredtOrRemoved(str1: str, str2: str, str1_length: int, str2_length: int) -> bool:
    index1 = 0
    index2 = 0

    while index2 < str2_length and index1 < str1_length:
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1

    return True
