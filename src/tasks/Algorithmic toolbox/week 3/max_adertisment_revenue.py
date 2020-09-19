def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = sorted(a)
    b = sorted(b)
    return sum(a[i] * b[i] for i in range(n))


if __name__ == "__main__":
    print(solve())
