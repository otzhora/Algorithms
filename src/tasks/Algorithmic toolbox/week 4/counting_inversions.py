from typing import Any, List


def _merge(a: List[Any], left: int, mid: int, right: int):
    if right - left <= 1:
        return 0

    i = left
    j = mid
    k = 0
    c = [0] * (right - left)
    cnt = 0
    while i < mid and j < right:
        if a[i] <= a[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = a[j]
            j += 1
            cnt += mid - i
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
    return cnt


def _merge_sort(a: List[Any], left: int, right: int):
    if right - left <= 1:
        return 0

    mid = (left + right) // 2
    cnt = _merge_sort(a, left, mid)
    cnt += _merge_sort(a, mid, right)
    cnt += _merge(a, left, mid, right)
    return cnt


def solve(a):
    ans = _merge_sort(a, 0, len(a))
    return ans


if __name__ == "__main__":
    input()
    a = list(map(int, input().split()))
    print(solve(a))
