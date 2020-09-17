def solution():
    n = int(input())
    fibs = [0] * (n + 3)
    fibs[1] = 1
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]

    print(fibs[n])


if __name__ == "__main__":
    solution()