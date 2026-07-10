# Pythonic way using count


def is_unique(string: str) -> bool:
    return all(string.count(char) <= 1 for char in string)
