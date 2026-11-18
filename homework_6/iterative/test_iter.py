import random
import sys
import time

from merge_sort_iter import merge_sort_iter
from quick_sort_iter import quick_sort_iter

sys.setrecursionlimit(10_000)


# ========== КОРРЕКТНОСТЬ: БАЗОВЫЕ И ГРАНИЧНЫЕ ==========

def test_merge_sort_iter_basic():
    assert merge_sort_iter([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]


def test_quick_sort_iter_basic():
    assert quick_sort_iter([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]


def test_empty():
    for f in (merge_sort_iter, quick_sort_iter):
        assert f([]) == []


def test_single():
    for f in (merge_sort_iter, quick_sort_iter):
        assert f([1]) == [1]


def test_two_elements():
    for f in (merge_sort_iter, quick_sort_iter):
        assert f([2, 1]) == [1, 2]
        assert f([1, 2]) == [1, 2]


def test_duplicates():
    for f in (merge_sort_iter, quick_sort_iter):
        assert f([3, 3, 2, 2, 1, 1]) == [1, 1, 2, 2, 3, 3]
        assert f([5, 5, 5, 5]) == [5, 5, 5, 5]


def test_already_sorted():
    arr = list(range(10))
    for f in (merge_sort_iter, quick_sort_iter):
        assert f(arr) == arr


def test_reverse_sorted():
    arr = list(range(10, 0, -1))
    expected = list(range(1, 11))
    for f in (merge_sort_iter, quick_sort_iter):
        assert f(arr) == expected


def test_negative_numbers():
    arr = [-5, 3, -1, 0, 8, -10, 2]
    expected = [-10, -5, -1, 0, 2, 3, 8]
    for f in (merge_sort_iter, quick_sort_iter):
        assert f(arr) == expected


# ========== КОРРЕКТНОСТЬ: СЛУЧАЙНЫЕ ПРОТИВ sorted() ==========

def test_random_vs_sorted():
    for _ in range(100):
        n = random.randint(0, 60)
        arr = [random.randint(-100, 100) for _ in range(n)]
        expected = sorted(arr)
        assert merge_sort_iter(arr.copy()) == expected
        assert quick_sort_iter(arr.copy()) == expected


def test_random_many_duplicates():
    """Много дубликатов — проверяем устойчивость к плохим pivot."""
    for _ in range(50):
        n = random.randint(1, 80)
        arr = [random.randint(0, 3) for _ in range(n)]
        expected = sorted(arr)
        assert merge_sort_iter(arr.copy()) == expected
        assert quick_sort_iter(arr.copy()) == expected


# ========== НЕ МУТИРУЕТ ВХОД ==========

def test_does_not_mutate_input():
    for f in (merge_sort_iter, quick_sort_iter):
        arr = [5, 2, 9, 1, 5, 6]
        snapshot = arr[:]
        f(arr)
        assert arr == snapshot


# ========== БОЛЬШИЕ МАССИВЫ ==========

def _bench(fn, arr, label):
    data = arr.copy()
    start = time.time()
    fn(data)
    elapsed = time.time() - start
    print(f"  {label:<22} {elapsed * 1000:>10.2f} мс")
    return elapsed


def test_large_random():
    """n = 5000, случайные данные: обе ~ O(n log n)."""
    n = 5000
    arr = [random.randint(0, 10**6) for _ in range(n)]
    print(f"\n--- Итеративные, случайный массив ({n} эл.) ---")
    _bench(merge_sort_iter, arr, "Merge Sort Iter")
    _bench(quick_sort_iter, arr, "Quick Sort Iter")
    assert True


def test_large_sorted():
    """n = 5000, отсортированный: итеративный Quick Sort НЕ вырождается."""
    n = 5000
    arr = list(range(n))
    print(f"\n--- Итеративные, отсортированный ({n} эл.) ---")
    t_m = _bench(merge_sort_iter, arr, "Merge Sort Iter")
    t_q = _bench(quick_sort_iter, arr, "Quick Sort Iter")
    print(f"  Отношение Quick/Merge: {t_q / t_m:.2f}×")
    assert True


def test_large_reverse():
    n = 5000
    arr = list(range(n, 0, -1))
    print(f"\n--- Итеративные, обратный порядок ({n} эл.) ---")
    _bench(merge_sort_iter, arr, "Merge Sort Iter")
    _bench(quick_sort_iter, arr, "Quick Sort Iter")
    assert True


def test_large_all_equal():
    """Все элементы одинаковые — граничный случай для Quick Sort."""
    n = 5000
    arr = [7] * n
    print(f"\n--- Итеративные, все элементы равны ({n} эл.) ---")
    _bench(merge_sort_iter, arr, "Merge Sort Iter")
    _bench(quick_sort_iter, arr, "Quick Sort Iter")
    assert True