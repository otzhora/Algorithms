from src.dynamic_programming.edit_distance import compute_edit_distance


def test_edit_distance():
    assert 0 == compute_edit_distance("ab", "ab")
    assert 3 == compute_edit_distance("short", "ports")
    assert 5 == compute_edit_distance("editing", "distance")
