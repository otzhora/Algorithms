def solution():
    n, m = list(map(int, input().split()))
    fibs = [0] * (2 * 10 ** 5)
    fibs[1] = 1
    period = -1
    for i in range(2, 2 * 10 ** 5):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
        fibs[i] %= m
        if fibs[i] == 1 and fibs[i - 1] == 0:
            period = i - 1
            break

    if period != -1:
        print(fibs[n % period] % m)
    else:
        print(fibs[n] % m)



if __name__ == "__main__":
    solution()
