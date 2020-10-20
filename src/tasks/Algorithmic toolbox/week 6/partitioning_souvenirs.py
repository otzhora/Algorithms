def solve(w):
    s = sum(w)
    if s % 3 != 0:
        return 0
    W = s // 3

    d = [[False] * (W + 1) for _ in range(len(w))]

    n = len(w)

    for i in range(n):
        d[i][0] = True

    for j in range(1, W + 1):
        d[0][j] = w[0] == j

    for i in range(1, n):
        for j in range(1, W + 1):
            if d[i - 1][j]:
                d[i][j] = d[i - 1][j]
            elif j >= w[i]:
                d[i][j] = d[i - 1][j - w[i]]

    return int(d[len(w) - 1][W])


if __name__ == "__main__":
    input()
    a = list(map(int, input().split()))
    print(solve(a))
