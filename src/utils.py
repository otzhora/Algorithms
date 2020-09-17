import random
from typing import List


def generate_random_list(n: int, left: int, right: int) -> List[int]:
    """
    Generate random list
    :param n: number of elements in list
    :param left: left bound
    :param right: right bound
    :return: list of random integers within bounds
    """
    assert n >= 1, f"number of elements ({n}) should be greater than 0"
    assert left < right, f"left bound ({left}) should be smaller than" \
                         f" right bound ({right})"
    return [random.randint(left, right) for _ in range(n)]
