from typing import Any, List


def compute_lcs(a: List[Any], b: List[Any]):
    """
    Compute the length of the longest common subsequence of two sequences.
    :param a: sequence one
    :param b: sequence two
    :return: length of the longest common subsequence
    """
    dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]
