# Pythonic way using count

def is_unique(string: str) -> bool:
    for char in string:
        if string.count(char) > 1:
            return False

    return True
