from math import log10


def karatsuba_multiply(x: int, y: int) -> int:
    """
    Multiply two long integers using Karatsuba multiplication. I assume that
    x >= 0 and y >= 0.
    """
    assert x >= 0
    assert y >= 0

    if x > 0:
        n = int(log10(x)) + 1
    else:
        n = 1

    if y > 0:
        m = int(log10(y)) + 1
    else:
        m = 1

    if n == 1 or m == 1:
        return x * y

    partition = min(m, n) // 2
    a = int(x // (10 ** partition))
    b = int(x % (10 ** partition))
    c = int(y // (10 ** partition))
    d = int(y % (10 ** partition))

    ac = karatsuba_multiply(a, c)
    bd = karatsuba_multiply(b, d)
    s3 = karatsuba_multiply(a + b, c + d)
    return 10 ** (2 * partition) * ac + 10 ** partition * (s3 - ac - bd) + bd
