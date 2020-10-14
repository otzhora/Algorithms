from bisect import bisect


def count_contains(coords, n_open, p):
    ins_point = bisect(coords, p)
    if ins_point >= len(n_open):
        return 0

    if coords[ins_point] > p:
        return n_open[ins_point - 1]

    return n_open[ins_point]


def solve(segs, points):
    n = len(segs)
    opens = sorted([seg[0] for seg in segs])
    closes = sorted([seg[1] + 1 for seg in segs])
    n_open = [0 for _ in range(3 * n)]
    coords = [0 for _ in range(3 * n)]
    n_open[0] = 1
    coords[0] = opens[0]

    i, j = 1, 0
    k = 1
    while i < n and j < n:
        if opens[i] < closes[j]:
            coords[k] = opens[i]
            n_open[k] = n_open[k - 1] + 1
            i += 1
        elif opens[i] == closes[j]:
            coords[k] = opens[i]
            n_open[k] = n_open[k - 1]
            i += 1
            j += 1
        else:
            coords[k] = closes[j]
            n_open[k] = n_open[k - 1] - 1
            j += 1
        k += 1

    while j < n:
        coords[k] = closes[j]
        n_open[k] = n_open[k - 1] - 1
        k += 1
        j += 1
    coords = coords[:k]
    n_open = n_open[:k]

    ans = [0 for _ in range(len(points))]
    for i, p in enumerate(points):
        ans[i] = count_contains(coords, n_open, p)
    return " ".join(map(str, ans))


if __name__ == "__main__":
    s, p = map(int, input().split())
    segs = [[i for i in map(int, input().split())] for _ in range(s)]
    points = list(map(int, input().split()))
    print(solve(segs, points))
