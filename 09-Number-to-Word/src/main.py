from constants import UNDER_20, TENS, ABOVE_100


def num_to_word(num: int) -> str:
    """ 
    Convert a number to its word representation.

    :param num: _descriptions_
    :type num: int
    :return: _descriptions_
    :rtype: str

    >>> num_to_word(0)
    'Zero'
    >>> num_to_word(10)
    'Ten'
    >>> num_to_word(128)
    'One Hundred Twenty Eight'
    """

    if num < 20:
        return UNDER_20[num]
    elif num < 100:
        remainder = num % 10
        if remainder == 0:
            return TENS[num // 10]
        return TENS[num // 10] + " " + UNDER_20[remainder]

    pivot = max([key for key in ABOVE_100 if key <= num])
    p1 = num_to_word(num // pivot)
    p2 = ABOVE_100[pivot]

    if num % pivot == 0:
        return f'{p1} {p2}'
    
    return f"{p1} {p2} {num_to_word(num % pivot)}"


if __name__ == '__main__':
    print(num_to_word(128))
    print(num_to_word(28))
    print(num_to_word(1354))
    print(num_to_word(65872))
    print(num_to_word(10054698))
    print(num_to_word(1300))

    assert num_to_word(128) == "One Hundred Twenty Eight"
    assert num_to_word(28) == "Twenty Eight"
    print("All tests passed!")

