from src.dynamic_programming.longest_common_subsequence import compute_lcs


def test_lcs():
    assert 2 == compute_lcs([2, 7, 5], [2, 5])
    assert 0 == compute_lcs([7], [1, 2, 3, 4])
    assert 2 == compute_lcs([2, 7, 8, 3], [5, 2, 8, 7])
