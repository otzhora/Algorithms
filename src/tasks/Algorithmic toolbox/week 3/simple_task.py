def solve():
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    stops = sorted(stops)
    stops.append(d)
    ans = 0
    possible_dist = m
    for i in range(1, n + 1):
        if stops[i] > possible_dist >= stops[i - 1]:
            possible_dist = stops[i - 1] + m
            ans += 1
    if possible_dist < d:
        return -1
    return ans


if __name__ == "__main__":
    print(solve())
