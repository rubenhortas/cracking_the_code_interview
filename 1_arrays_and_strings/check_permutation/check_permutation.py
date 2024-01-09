def is_permutation(str1: str, str2: str) -> bool:
    # Time complexity: O(n)
    # Auxiliary space: O(1)
    counter = [0] * 128

    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        position = ord(str1[i])
        counter[position] = counter[position] + 1

    for i in range(len(str2)):
        position = ord(str2[i])
        counter[position] = counter[position] - 1

        if counter[position] < 0:
            return False

    return True
