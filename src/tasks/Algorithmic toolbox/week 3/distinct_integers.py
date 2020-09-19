def solve():
    n = int(input())
    numbers = set()
    curr_n = n
    if n == 1:
        return {1}

    for i in range(1, n):
        if i + 1 <= curr_n - i:
            numbers.add(i)
            curr_n -= i
        else:
            numbers.add(curr_n)
            break
    return numbers


if __name__ == "__main__":
    numbers = solve()
    print(len(numbers))
    print(" ".join(map(str, numbers)))