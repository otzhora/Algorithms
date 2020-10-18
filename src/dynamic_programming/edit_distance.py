def compute_edit_distance(s1: str, s2: str):
    """
    Compute edit distance between two strings
    :param s1: first string
    :param s2: second string
    :return: edit distance
    """
    assert len(s1) >= 1 and len(s2) >= 1, "You should pass string with length > 0"

    dp = [[i + j if i == 0 or j == 0 else 0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    dp[0][0] = 0

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1, dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1)
    return dp[-1][-1]
