import pytest
from validate import validate


def test_example_true():
    """Пример 1: можно получить popped"""
    assert validate([1, 2, 3, 4, 5], [1, 3, 5, 4, 2]) is True


def test_example_false():
    """Пример 2: нельзя получить popped"""
    assert validate([1, 2, 3], [3, 1, 2]) is False


def test_same_order():
    """pushed и popped совпадают"""
    assert validate([1, 2], [1, 2]) is True


def test_reverse_order():
    """pushed в прямом, popped в обратном"""
    assert validate([1, 2], [2, 1]) is True


def test_single_element():
    """Один элемент"""
    assert validate([1], [1]) is True


def test_empty():
    """Пустые массивы"""
    assert validate([], []) is True


def test_all_push_then_pop():
    """Сначала все push, потом все pop"""
    assert validate([1, 2, 3], [3, 2, 1]) is True


def test_impossible_case():
    """Невозможный случай: 1 должна быть забрана раньше 2, но 2 наверху"""
    assert validate([1, 2], [1, 2]) is True
    assert validate([1, 2, 3], [2, 3, 1]) is True


def test_large_array():
    """Большой массив — проверка производительности"""
    n = 10000
    pushed = list(range(n))
    popped = list(range(n))
    assert validate(pushed, popped) is True


def test_large_reverse():
    """Большой массив в обратном порядке"""
    n = 10000
    pushed = list(range(n))
    popped = list(range(n - 1, -1, -1))
    assert validate(pushed, popped) is True


def test_interleaved():
    """Чередование push и pop"""
    assert validate([1, 2, 3, 4], [2, 1, 4, 3]) is True


def test_impossible_interleaved():
    """Невозможное чередование"""
    assert validate([1, 2, 3, 4], [3, 1, 2, 4]) is False