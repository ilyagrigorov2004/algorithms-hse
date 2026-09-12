import pytest
from sum import max_even_sum


def test_all_even():
    assert max_even_sum([2, 4, 6]) == 12


def test_sum_even():
    assert max_even_sum([1, 2, 3]) == 6


def test_sum_odd():
    assert max_even_sum([5, 7, 13, 2, 14]) == 36


def test_single_odd():
    assert max_even_sum([3]) == 0


def test_single_even():
    assert max_even_sum([4]) == 4


def test_two_odd():
    assert max_even_sum([2, 5]) == 2


def test_empty():
    assert max_even_sum([]) == 0


def test_all_odd():
    assert max_even_sum([1, 3, 5]) == 8


def test_large_array():
    arr = [1] * 1000
    assert max_even_sum(arr) == 1000


def test_zero():
    assert max_even_sum([0]) == 0