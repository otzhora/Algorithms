def solution():
    n = int(input())
    fibs = [0] * 64
    fibs[1] = 1
    period = 60
    for i in range(2, 64):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
        fibs[i] %= 10

    f1 = fibs[n % period] % 10
    f2 = fibs[(n + 1) % period] % 10
    print(f1 * f2 % 10)


if __name__ == "__main__":
    solution()
