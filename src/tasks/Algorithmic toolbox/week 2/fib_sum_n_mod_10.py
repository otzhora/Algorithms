def solution():
    n = int(input())
    fibs = [0] * 64
    fibs[1] = 1
    period = 60
    for i in range(2, 62):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
        fibs[i] %= 10

    rem = 0
    for i in range(0, n % period + 1):
        rem += fibs[i] % 10

    print(rem % 10)


if __name__ == "__main__":
    solution()
