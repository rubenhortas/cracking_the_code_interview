def get_url(string: list, true_length: int) -> list:
    # Time complexity: O(n)
    # Auxiliary space: O(1)
    index = len(string)

    for i in reversed(range(true_length)):
        if string[i] == ' ':
            string[index - 3:index] = '%20'
            index = index - 3
        else:
            string[index - 1] = string[i]
            index = index - 1

    return string
