def solve():
    n = int(input())
    segments = []
    for _ in range(n):
        a, b = map(int, input().split())
        segments.append((a, b))
    segments = sorted(segments, key=lambda x: x[0])
    ans = 0
    points = []
    curr_end = segments[0][1]
    covered_segments = set()
    for i, (a, b) in enumerate(segments[1:]):
        if a <= curr_end:
            curr_end = min(b, curr_end)
            if i == n - 2:
                ans += 1
                points.append(curr_end)
            continue
        if a > curr_end:
            ans += 1
            points.append(curr_end)
            curr_end = b
            if i == n - 2:
                ans += 1
                points.append(curr_end)
            continue
        if b > curr_end:
            continue
    return ans, points


if __name__ == "__main__":
    ans, points = solve()
    print(ans)
    print(" ".join(map(str, points)))
