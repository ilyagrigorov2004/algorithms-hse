import sys
import random
import time

from merge_sort import merge_sort
from quick_sort import quick_sort          # pivot = arr[0]
from quick_sort_mid import quick_sort_mid  # pivot = середина


sys.setrecursionlimit(10_000)


# ========== ТЕСТЫ НА КОРРЕКТНОСТЬ ==========

def test_merge_sort_basic():
    assert merge_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]


def test_quick_sort_basic():
    assert quick_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]


def test_quick_sort_mid_basic():
    assert quick_sort_mid([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]


def test_empty_and_single():
    for f in (merge_sort, quick_sort, quick_sort_mid):
        assert f([]) == []
        assert f([1]) == [1]


def test_already_sorted():
    arr = [1, 2, 3, 4, 5]
    for f in (merge_sort, quick_sort, quick_sort_mid):
        assert f(arr) == arr


def test_reverse_sorted():
    arr = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    for f in (merge_sort, quick_sort, quick_sort_mid):
        assert f(arr) == expected


def test_random_matches_sorted():
    for _ in range(20):
        arr = [random.randint(-50, 50) for _ in range(random.randint(0, 50))]
        expected = sorted(arr)
        assert merge_sort(arr.copy())     == expected
        assert quick_sort(arr.copy())     == expected
        assert quick_sort_mid(arr.copy()) == expected


# ========== БОЛЬШИЕ ТЕСТЫ ДЛЯ СРАВНЕНИЯ ВРЕМЕНИ ==========

def _bench(fn, arr, label):
    data = arr.copy()
    start = time.time()
    fn(data)
    elapsed = time.time() - start
    print(f"  {label:<20} {elapsed * 1000:>10.2f} мс")
    return elapsed


def test_huge_random_array():
    """Случайный массив: все три алгоритма ~ O(n log n)."""
    n = 1000
    arr = [random.randint(0, 100_000) for _ in range(n)]
    print(f"\n--- Случайный массив ({n} эл.) ---")
    _bench(merge_sort,     arr, "Merge Sort")
    _bench(quick_sort,     arr, "Quick Sort (arr[0])")
    _bench(quick_sort_mid, arr, "Quick Sort (mid)")
    assert True


def test_huge_sorted_array():
    """
    Отсортированный массив:
      - Merge Sort      → O(n log n)
      - Quick (arr[0])  → O(n²)  ← вырождение!
      - Quick (mid)     → O(n log n)
    """
    n = 1000
    arr = list(range(n))
    print(f"\n--- Отсортированный массив ({n} эл.) ---")
    t_merge = _bench(merge_sort,     arr, "Merge Sort")
    t_qs    = _bench(quick_sort,     arr, "Quick Sort (arr[0])")
    _bench(quick_sort_mid, arr, "Quick Sort (mid)")
    print(f"  Quick(arr[0]) медленнее Merge в {t_qs / t_merge:.1f}× раз")
    assert True


def test_huge_reverse_sorted_array():
    """Обратный порядок — для Quick(arr[0]) тоже худший случай."""
    n = 1000
    arr = list(range(n, 0, -1))
    print(f"\n--- Обратный порядок ({n} эл.) ---")
    _bench(merge_sort,     arr, "Merge Sort")
    _bench(quick_sort,     arr, "Quick Sort (arr[0])")
    _bench(quick_sort_mid, arr, "Quick Sort (mid)")
    assert True