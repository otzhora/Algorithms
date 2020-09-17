from src.recursive.gcd import gcd


def test_gcd():
    assert 3 == gcd(357, 234)
    assert 61232 == gcd(3918848, 1653264)
