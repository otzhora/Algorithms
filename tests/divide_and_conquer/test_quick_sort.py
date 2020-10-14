import random

from src.divide_and_conquer.quick_sort import quick_sort
from src.utils import generate_random_list


def test_merge_sort():
    for _ in range(20):
        n = random.randint(1, 10 ** 5)
        left = random.randint(-10 ** 5, 10 ** 5)
        right = random.randint(left + 1, 10 ** 5)
        a = generate_random_list(n, left, right)
        ans = sorted(a)
        quick_sort(a, 0, len(a) - 1)
        assert a == ans


if __name__ == "__main__":
    test_merge_sort()