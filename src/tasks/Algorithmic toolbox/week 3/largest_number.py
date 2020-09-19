def is_greater(s1, s2):
    return s1 + s2 > s2 + s1


def solve():
    n = int(input())
    s = input().split()

    ans = []
    while len(s):
        max_s = s[0]
        for si in s[1:]:
            if is_greater(si, max_s):
                max_s = si
        ans.append(max_s)
        s.remove(max_s)

    return "".join(ans)


if __name__ == "__main__":
    print(solve())