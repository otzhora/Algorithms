def solve(W, bars):
    n = len(bars)

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            dp[i][w] = dp[i-1][w]

            if bars[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - bars[i - 1]] + bars[i - 1])
    used = [0 for _ in range(n)]

    i = n
    w = W
    while i != 0 and w != 0:
        if bars[i - 1] <= w and dp[i - 1][w - bars[i - 1]] + bars[i - 1] > dp[i - 1][w]:
            used[i - 1] = True
            w -= bars[i - 1]
        i -= 1
    print(used)

    return dp[-1][-1]


if __name__ == "__main__":
    W, n = map(int, input().split())
    bars = list(map(int, input().split()))
    print(solve(W, bars))
