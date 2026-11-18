import random
import time

import pytest

from quickselect import find_kth_largest


# ========== ПРИМЕРЫ ИЗ ЗАДАНИЯ ==========

def test_example_1():
    """nums = [3,2,1,5,6,4], k = 2 → 5"""
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5


def test_example_2():
    """nums = [3,2,3,1,2,4,5,5,6], k = 4 → 4"""
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


# ========== БАЗОВЫЕ И ГРАНИЧНЫЕ ==========

def test_single_element():
    assert find_kth_largest([42], 1) == 42


def test_two_elements():
    assert find_kth_largest([2, 1], 1) == 2
    assert find_kth_largest([2, 1], 2) == 1
    assert find_kth_largest([1, 2], 1) == 2
    assert find_kth_largest([1, 2], 2) == 1


def test_k_equals_one_is_max():
    assert find_kth_largest([1, 5, 3, 2, 4], 1) == 5


def test_k_equals_n_is_min():
    assert find_kth_largest([1, 5, 3, 2, 4], 5) == 1


def test_already_sorted_ascending():
    arr = list(range(1, 101))
    assert find_kth_largest(arr, 1) == 100
    assert find_kth_largest(arr, 50) == 51
    assert find_kth_largest(arr, 100) == 1


def test_already_sorted_descending():
    arr = list(range(100, 0, -1))
    assert find_kth_largest(arr, 1) == 100
    assert find_kth_largest(arr, 50) == 51
    assert find_kth_largest(arr, 100) == 1


def test_negative_numbers():
    arr = [-5, 3, -1, 0, 8, -10, 2]
    # sorted: [-10, -5, -1, 0, 2, 3, 8]
    assert find_kth_largest(arr, 1) == 8
    assert find_kth_largest(arr, 7) == -10
    assert find_kth_largest(arr, 3) == 2


def test_all_negative():
    arr = [-3, -1, -7, -2, -5]
    assert find_kth_largest(arr, 1) == -1
    assert find_kth_largest(arr, 5) == -7


# ========== ДУБЛИКАТЫ ==========

def test_all_equal():
    assert find_kth_largest([7] * 10, 1) == 7
    assert find_kth_largest([7] * 10, 5) == 7
    assert find_kth_largest([7] * 10, 10) == 7


def test_many_duplicates():
    arr = [2, 2, 2, 3, 3]
    # sorted: [2, 2, 2, 3, 3]
    assert find_kth_largest(arr, 1) == 3
    assert find_kth_largest(arr, 2) == 3
    assert find_kth_largest(arr, 3) == 2
    assert find_kth_largest(arr, 5) == 2


def test_example_with_duplicates_bruteforce():
    """Сверяем все k для массива с дубликатами."""
    arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    exp = sorted(arr, reverse=True)  # [6,5,5,4,3,3,2,2,1]
    for k in range(1, len(arr) + 1):
        assert find_kth_largest(arr.copy(), k) == exp[k - 1]


# ========== НЕ МУТИРУЕТ ВХОД ==========

def test_does_not_mutate_input():
    arr = [3, 2, 1, 5, 6, 4]
    snap = arr[:]
    find_kth_largest(arr, 2)
    assert arr == snap


# ========== СЛУЧАЙНЫЕ ПРОТИВ sorted() ==========

def test_random_vs_sorted_small():
    for _ in range(200):
        n = random.randint(1, 50)
        arr = [random.randint(-50, 50) for _ in range(n)]
        k = random.randint(1, n)
        expected = sorted(arr)[n - k]
        assert find_kth_largest(arr.copy(), k) == expected


def test_random_large():
    for _ in range(30):
        n = random.randint(100, 500)
        arr = [random.randint(-10**6, 10**6) for _ in range(n)]
        k = random.randint(1, n)
        expected = sorted(arr)[n - k]
        assert find_kth_largest(arr.copy(), k) == expected


def test_random_few_distinct_values():
    """Много повторов — проверяем устойчивость к плохому pivot."""
    for _ in range(100):
        n = random.randint(1, 200)
        arr = [random.randint(0, 3) for _ in range(n)]
        k = random.randint(1, n)
        expected = sorted(arr)[n - k]
        assert find_kth_largest(arr.copy(), k) == expected


# ========== НЕТРИВИАЛЬНЫЕ СЛУЧАИ ==========

def test_median_of_odd_and_even():
    assert find_kth_largest([5, 3, 1, 4, 2], 3) == 3   # медиана [1..5]
    assert find_kth_largest([4, 1, 3, 2], 2) == 3      # верхняя медиана
    assert find_kth_largest([4, 1, 3, 2], 3) == 2      # нижняя медиана


def test_palindromic_array():
    """Симметричный массив — проверка работы partition."""
    arr = list(range(50)) + list(range(49, -1, -1))
    n = len(arr)
    exp = sorted(arr, reverse=True)
    for k in (1, 10, n // 2, n - 1, n):
        assert find_kth_largest(arr.copy(), k) == exp[k - 1]


def test_already_split_good_pivot():
    """Массив, где все элементы по одну сторону от pivot-середины."""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
    assert find_kth_largest(arr, 1) == 100
    assert find_kth_largest(arr, 10) == 1


def test_alternating_extremes():
    """Массив, чередующий минимумы и максимумы."""
    arr = []
    lo, hi = 0, 1000
    for _ in range(50):
        arr.append(lo); lo += 1
        arr.append(hi); hi -= 1
    n = len(arr)
    exp = sorted(arr, reverse=True)
    for k in (1, 25, 50, 75, 100):
        assert find_kth_largest(arr.copy(), k) == exp[k - 1]


def test_k_out_of_range_raises():
    """k должен быть в [1, n] — контрактное поведение."""
    with pytest.raises((ValueError, IndexError)):
        find_kth_largest([1, 2, 3], 0)
    with pytest.raises((ValueError, IndexError)):
        find_kth_largest([1, 2, 3], 4)


# ========== БЕНЧМАРКИ ==========

def test_benchmark_all_equal_large():
    """
    Все элементы равны — регресс на квадратичность partition.
    Схема Хоара + ветка `else: return a[target]` в quickselect
    должны давать O(n) за один проход.
    """
    n = 50_000
    arr = [7] * n
    t0 = time.time()
    res = find_kth_largest(arr, n // 2)
    elapsed = time.time() - t0
    print(f"\nall-equal n={n}: {elapsed:.4f}s")
    assert res == 7
    assert elapsed < 2.0, (
        f"quickselect на all-equal работает {elapsed:.1f}s — "
        f"похоже на квадратичную деградацию (проверьте partition)"
    )


def test_benchmark_linear_scaling():
    """
    t(2n)/t(n) ≈ 2 для O(n), а не ≈ 4 для O(n²).
    Широкий порог — из-за шума на малых временах.
    """
    random.seed(0)

    def measure(n):
        arr = [random.randint(0, 10**6) for _ in range(n)]
        data = arr.copy()
        t0 = time.time()
        find_kth_largest(data, n // 2)
        return time.time() - t0

    t1 = measure(100_000)
    t2 = measure(200_000)
    ratio = t2 / t1
    print(f"\nscaling t(2n)/t(n) = {ratio:.2f}")
    assert ratio < 2.8