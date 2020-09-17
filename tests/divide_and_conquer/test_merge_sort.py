import random

from src.divide_and_conquer.merge_sort import merge_sort
from src.utils import generate_random_list


def test_merge_sort():
    for _ in range(20):
        n = random.randint(1, 10 ** 5)
        left = random.randint(-10 ** 5, 10 ** 5)
        right = random.randint(left + 1, 10 ** 5)
        a = generate_random_list(n, left, right)
        ans = sorted(a)
        merge_sort(a)
        assert a == ans
