import random
from typing import Any, List


def partition3(a: List[Any], l: int, r: int):
    """
    Perform 3-way partinion on an array a with bounds l, r
    :param a: array
    :param l: left bound
    :param r: right bound
    :return: indices i, j such that all a[k] < a[i] for k in range l, i - 1
                                    all a[k] == a[i] for k in range i, j
                                    all a[k] > a[j] for k in range j+1, r
    """
    i, j = l, l
    for k in range(l + 1, r + 1):
        if a[k] < a[i]:
            a[k], a[j + 1] = a[j + 1], a[k]
            a[j + 1], a[i] = a[i], a[j + 1]
            i += 1
            j += 1
        elif a[k] == a[j]:
            a[k], a[j + 1] = a[j + 1], a[k]
            j += 1
    return i, j


def quick_sort(a: List[Any], l: int, r: int):
    """
    Perform 3-way QuickSort on an array a with bounds l, r
    :param a: array to sort
    :param l: left bound
    :param r: right bound
    :return:
    """
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    i, j = partition3(a, l, r)
    quick_sort(a, l, i - 1)
    quick_sort(a, j + 1, r)
