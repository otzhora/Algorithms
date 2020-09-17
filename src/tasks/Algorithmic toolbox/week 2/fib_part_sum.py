def part_sum(n):
    fibs = [0] * 64
    fibs[1] = 1
    period = 60
    for i in range(2, 62):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
        fibs[i] %= 10

    rem = 0
    for i in range(0, n % period + 1):
        rem += fibs[i] % 10

    return rem % 10


def solution():
    m, n = list(map(int, input().split()))
    if m != 0:
        pl = part_sum(m-1)
    else:
        pl = 0
    pr = part_sum(n)

    ans = pr - pl
    if ans < 0:
        ans += 10

    print(ans)


if __name__ == "__main__":
    solution()
