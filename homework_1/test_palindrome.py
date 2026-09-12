import pytest
from palindrome import palindrome


def test_true_cases():
    assert palindrome(121) is True
    assert palindrome(1221) is True
    assert palindrome(1) is True
    assert palindrome(5) is True
    assert palindrome(12321) is True


def test_false_cases():
    assert palindrome(31) is False
    assert palindrome(123) is False
    assert palindrome(10) is False
    assert palindrome(100) is False


def test_single_digit():
    for i in range(1, 10):
        assert palindrome(i) is True


def test_large_number():
    assert palindrome(123454321) is True
    assert palindrome(123456789) is False


def test_wrong_cases():
    assert palindrome(-121) == "Данное число не является целым положительным"
    assert palindrome(0) == "Данное число не является целым положительным"
    assert palindrome(-1) == "Данное число не является целым положительным"