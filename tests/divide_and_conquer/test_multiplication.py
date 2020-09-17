from src.divide_and_conquer.multiplication import karatsuba_multiply
from random import randint


def test_karatsuba():
    x, y = 1234, 5678
    assert x * y == karatsuba_multiply(x, y)

    x, y = 1235, 567
    assert x * y == karatsuba_multiply(x, y)

    x, y = 12345, 567
    assert x * y == karatsuba_multiply(x, y)

    n_tests = 100
    for _ in range(n_tests):
        x, y = randint(0, 10**6), randint(0, 10**6)
        assert x * y == karatsuba_multiply(x, y)


if __name__ == "__main__":
    test_karatsuba()
