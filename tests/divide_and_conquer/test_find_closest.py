import random

from pytest import approx

from src.divide_and_conquer.closest_points import (find_closest_naive,
                                                   find_closest_points)
from src.utils import generate_random_list


def test_closest():
    x = generate_random_list(200, -10000, 10000)
    y = generate_random_list(200, -10000, 10000)
    points = [[x[i], y[i]] for i in range(200)]

    assert approx(find_closest_naive(points), find_closest_points(points))


if __name__ == "__main__":
    test_closest()
