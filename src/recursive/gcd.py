def gcd(a: int, b: int) -> int:
    """
    Compute gcd of two integers using Euclidean Algorithm
    :param a: first integer
    :param b: second integer
    :return: gcd
    """
    if b == 0:
        return a
    return gcd(b, a % b)
