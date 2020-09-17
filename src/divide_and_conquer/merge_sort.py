from typing import Any, List


def _merge(a: List[Any], left: int, mid: int, right: int):
    """
    Perform merge operation on an array
    :param a: array to merge
    :param left: left bound
    :param mid: mid bound
    :param right: right bound
    :return: None
    """
    if right - left <= 1:
        return

    i = left
    j = mid
    k = 0
    c = [0] * (right - left)
    while i < mid and j < right:
        if a[i] <= a[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = a[j]
            j += 1
        k += 1

    while i < mid:
        c[k] = a[i]
        i += 1
        k += 1

    while j < right:
        c[k] = a[j]
        j += 1
        k += 1

    for i in range(len(c)):
        a[left + i] = c[i]


def _merge_sort(a: List[Any], left: int, right: int):
    """
    Perform Merge Sort on an array within left and right
    bounds
    :param a: array to sort
    :param left: left bound
    :param right:  right bout
    :return: None
    """
    if right - left <= 1:
        return

    mid = (left + right) // 2
    _merge_sort(a, left, mid)
    _merge_sort(a, mid, right)
    _merge(a, left, mid, right)


def merge_sort(a: List[Any]):
    """
    Perform Merge Sort on the whole array
    :param a: array to sort
    :return: None
    """
    _merge_sort(a, 0, len(a))
