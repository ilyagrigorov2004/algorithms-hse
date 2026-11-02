import pytest
from permutations import permutations


def sort_permutations(perms):
    """Сортирует список перестановок для стабильного сравнения"""
    return sorted([tuple(p) for p in perms])


def test_permutations_basic():
    """Базовый пример из условия"""
    result = permutations([1, 2, 3])
    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    assert sort_permutations(result) == sort_permutations(expected)


def test_permutations_two():
    """Два элемента"""
    result = permutations([0, 1])
    expected = [[0,1],[1,0]]
    assert sort_permutations(result) == sort_permutations(expected)


def test_permutations_single():
    """Один элемент"""
    result = permutations([1])
    assert result == [[1]]


def test_permutations_empty():
    """Пустой список — возвращает список с одним пустым списком"""
    result = permutations([])
    assert result == [[]]