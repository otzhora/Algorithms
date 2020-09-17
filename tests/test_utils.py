import random

from src.utils import generate_random_list


def test_generate_random_list():
    for _ in range(20):
        n = random.randint(1, 10**5)
        left = random.randint(-10**5, 10**5)
        right = random.randint(left + 1, 10**5)
        a = generate_random_list(n, left, right)
        assert len(a) == n
        assert min(a) >= left
        assert max(a) <= right
