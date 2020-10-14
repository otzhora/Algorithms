import math
from bisect import bisect_left, bisect_right
from typing import List, Union


def dist(p1: List[Union[int, float]], p2: List[Union[int, float]]) -> float:
    """
    Calculate distance between two points
    :param p1: point 1
    :param p2: point 2
    :return: distance between points
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def _find(points: List[List[Union[int, float]]],
          left_idx: int,
          right_idx: int,
          x: List[Union[int, float]]) -> float:
    """
    Find two closest points in an array of points. For more info see
    "Finding the closest pair of points: Section 33.4 @ Thomas H. Cormen,
    Charles E. Leiserson, Ronald L. Rivest, Clifford Stein - Introduction to Algorithms (3rd Edition). MIT Press. 2009."
    :param points: an array of points
    :param left_idx: the left border that we are currently considering
    :param right_idx: the right border that we are currently considering
    :param x: x coordinates of points in sorted order
    :return: minimum distance between two points in an array
    """
    if right_idx - left_idx <= 3:
        buf_ans = 1e9 + 100
        for i in range(left_idx, right_idx):
            for j in range(left_idx, right_idx):
                if i != j:
                    buf_ans = min(buf_ans, dist(points[i], points[j]))

        return buf_ans

    mid = (right_idx + left_idx) // 2
    d1 = _find(points, left_idx, mid, x)
    d2 = _find(points, mid, right_idx, x)
    d = min(d1, d2)

    S = (points[mid][0] + points[mid + 1][0]) / 2
    left_bound = bisect_left(x, S - d, left_idx, right_idx)
    right_bound = bisect_right(x, S + d, left_idx, right_idx)
    right_bound = min(right_idx, right_bound)

    points_y = sorted([p for p in points[left_bound: right_bound]], key=lambda x: x[1])

    d_hat = 1e9 + 100
    for i in range(len(points_y)):
        for j in range(i + 1, min(i + 7, len(points_y))):
            d_hat = min(d_hat, dist(points_y[i], points_y[j]))

    return min(d, d_hat)


def find_closest_points(points: List[List[Union[int, float]]]) -> float:
    """
    Find two closest points in an array of points. For more info see
    "Finding the closest pair of points: Section 33.4 @ Thomas H. Cormen,
    Charles E. Leiserson, Ronald L. Rivest, Clifford Stein - Introduction to Algorithms (3rd Edition). MIT Press. 2009."
    :param points: an array of points
    :return: minimum distance between two points in an array
    """
    points = sorted(points, key=lambda x: x[0])
    x = [p[0] for p in points]
    return _find(points, 0, len(points), x)


def find_closest_naive(points: List[List[Union[int, float]]]) -> float:
    """
    Find two closest points in an array of points using a naive algorithm
    :param points: an array of points
    :return: minimum distance between two points in an array
    """
    ans = 1e9 + 100
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                ans = min(ans, dist(points[0], points[1]))
    return ans
