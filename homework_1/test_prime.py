import pytest
from prime import prime_count, is_prime


def test_is_prime_true():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(11) is True


def test_is_prime_false():
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(15) is False


def test_prime_count_10():
    assert prime_count(10) == 4


def test_prime_count_1():
    assert prime_count(1) == 0


def test_prime_count_2():
    assert prime_count(2) == 0


def test_prime_count_100():
    assert prime_count(100) == 25


def test_prime_count_zero():
    assert prime_count(0) == 0


def test_prime_count_negative():
    assert prime_count(-5) == 0
