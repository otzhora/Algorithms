def solve(n):
    if n == 1:
        return 0, [n]
    elif n <= 3:
        return 1, [1, n]

    dp = [0 for _ in range(n + 1)]
    prev_number = [0 for _ in range(n + 1)]
    dp[2] = 1
    dp[3] = 1
    prev_number[1] = 1
    prev_number[2] = 1
    prev_number[3] = 1

    for i in range(4, n+1):
        if i % 3 == 0:
            if dp[i // 3] < dp[i - 1]:
                dp[i] = dp[i // 3] + 1
                prev_number[i] = i // 3
            else:
                dp[i] = dp[i - 1] + 1
                prev_number[i] = i - 1
        elif i % 2 == 0:
            if dp[i // 2] < dp[i - 1]:
                dp[i] = dp[i // 2] + 1
                prev_number[i] = i // 2
            else:
                dp[i] = dp[i - 1] + 1
                prev_number[i] = i - 1
        else:
            dp[i] = dp[i - 1] + 1
            prev_number[i] = i - 1

    path = [n]
    curr = n
    while curr != 1:
        curr = prev_number[curr]
        path.append(curr)

    return dp[-1], reversed(path)


if __name__ == "__main__":
    n = int(input())
    ans, path = solve(n)
    print(ans)
    print(" ".join(map(str, path)))
