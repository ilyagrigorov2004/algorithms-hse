import pytest
from two_sum import two_sum_hash, two_sum_brute


# ========== ТЕСТЫ ДЛЯ two_sum_hash ==========

def test_hash_example_1():
    assert two_sum_hash([1, 3, 4, 10], 7) == (1, 2)


def test_hash_example_2():
    assert two_sum_hash([5, 5, 1, 4], 10) == (0, 1)


def test_hash_two_elements():
    assert two_sum_hash([1, 2], 3) == (0, 1)


def test_hash_negative():
    assert two_sum_hash([-1, -2, -3, -4], -7) == (2, 3)


def test_hash_large():
    arr = list(range(1000))
    assert two_sum_hash(arr, 1997) == (998, 999)


def test_hash_first_pair():
    assert two_sum_hash([1, 2, 3, 4], 3) == (0, 1)


def test_hash_last_pair():
    assert two_sum_hash([1, 2, 3, 4], 7) == (2, 3)


def test_hash_zeros():
    assert two_sum_hash([0, 0], 0) == (0, 1)


def test_hash_duplicates():
    assert two_sum_hash([3, 3], 6) == (0, 1)


def test_hash_no_pair():
    assert two_sum_hash([1, 2, 3], 100) is None


# ========== ТЕСТЫ ДЛЯ two_sum_brute ==========

def test_brute_example_1():
    assert two_sum_brute([1, 3, 4, 10], 7) == (1, 2)


def test_brute_example_2():
    assert two_sum_brute([5, 5, 1, 4], 10) == (0, 1)


def test_brute_two_elements():
    assert two_sum_brute([1, 2], 3) == (0, 1)


def test_brute_negative():
    assert two_sum_brute([-1, -2, -3, -4], -7) == (2, 3)


def test_brute_no_pair():
    assert two_sum_brute([1, 2, 3], 100) is None


# ========== ОБА СПОСОБА ДАЮТ ОДИНАКОВЫЙ РЕЗУЛЬТАТ ==========

def test_both_same_result():
    test_cases = [
        ([1, 3, 4, 10], 7),
        ([5, 5, 1, 4], 10),
        ([1, 2], 3),
        ([-1, -2, -3, -4], -7),
        ([0, 0], 0),
        ([3, 3], 6),
    ]
    for arr, k in test_cases:
        assert two_sum_hash(arr, k) == two_sum_brute(arr, k)