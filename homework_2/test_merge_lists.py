import pytest


# ========== КЛАСС ==========

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# ========== ФУНКЦИИ ==========

def merge(list1: ListNode | None, list2: ListNode | None):
    if list1 is None and list2:
        return list2
    elif list1 and list2 is None:
        return list1
    elif list1 is None and list2 is None:
        return None

    if list1.value <= list2.value:
        result_head = list1
        list1 = list1.next
    else:
        result_head = list2
        list2 = list2.next

    current = result_head
    while list1 and list2:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 or list2
    return result_head


def merge_two_lists_dummy(list1, list2):
    dummy = ListNode(None)
    current = dummy
    while list1 and list2:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 or list2
    return dummy.next


# ========== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==========

def create_list(arr):
    """Создаёт связный список из массива"""
    dummy = ListNode(0)
    current = dummy
    for x in arr:
        current.next = ListNode(x)
        current = current.next
    return dummy.next


def list_to_array(head):
    """Преобразует связный список в массив"""
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result


# ========== ТЕСТЫ ДЛЯ MERGE (без dummy) ==========

def test_merge_example():
    """Пример из условия"""
    l1 = create_list([1, 2, 4])
    l2 = create_list([1, 3, 4])
    result = merge(l1, l2)
    assert list_to_array(result) == [1, 1, 2, 3, 4, 4]


def test_merge_both_empty():
    """Оба списка пусты"""
    result = merge(None, None)
    assert result is None


def test_merge_first_empty():
    """Первый пуст, второй нет"""
    l2 = create_list([1, 2, 3])
    result = merge(None, l2)
    assert list_to_array(result) == [1, 2, 3]


def test_merge_second_empty():
    """Второй пуст, первый нет"""
    l1 = create_list([1, 2, 3])
    result = merge(l1, None)
    assert list_to_array(result) == [1, 2, 3]


def test_merge_single_elements():
    """Один элемент в каждом"""
    l1 = create_list([1])
    l2 = create_list([2])
    result = merge(l1, l2)
    assert list_to_array(result) == [1, 2]


def test_merge_single_elements_reverse():
    """Один элемент, но первый больше"""
    l1 = create_list([2])
    l2 = create_list([1])
    result = merge(l1, l2)
    assert list_to_array(result) == [1, 2]


def test_merge_all_smaller_first():
    """Все элементы первого меньше"""
    l1 = create_list([1, 2, 3])
    l2 = create_list([4, 5, 6])
    result = merge(l1, l2)
    assert list_to_array(result) == [1, 2, 3, 4, 5, 6]


def test_merge_all_smaller_second():
    """Все элементы второго меньше"""
    l1 = create_list([4, 5, 6])
    l2 = create_list([1, 2, 3])
    result = merge(l1, l2)
    assert list_to_array(result) == [1, 2, 3, 4, 5, 6]


def test_merge_equal_elements():
    """Все элементы равны"""
    l1 = create_list([1, 1, 1])
    l2 = create_list([1, 1, 1])
    result = merge(l1, l2)
    assert list_to_array(result) == [1, 1, 1, 1, 1, 1]


def test_merge_different_lengths():
    """Разные длины"""
    l1 = create_list([1, 5])
    l2 = create_list([2, 3, 4, 6])
    result = merge(l1, l2)
    assert list_to_array(result) == [1, 2, 3, 4, 5, 6]


def test_merge_interleaved():
    """Чередование"""
    l1 = create_list([1, 3, 5])
    l2 = create_list([2, 4, 6])
    result = merge(l1, l2)
    assert list_to_array(result) == [1, 2, 3, 4, 5, 6]


def test_merge_one_long_one_short():
    """Один список длиннее"""
    l1 = create_list([1, 2, 3, 4, 5])
    l2 = create_list([2])
    result = merge(l1, l2)
    assert list_to_array(result) == [1, 2, 2, 3, 4, 5]


def test_merge_negative_numbers():
    """Отрицательные числа"""
    l1 = create_list([-3, -1, 2])
    l2 = create_list([-2, 0, 3])
    result = merge(l1, l2)
    assert list_to_array(result) == [-3, -2, -1, 0, 2, 3]


def test_merge_large():
    """Большие списки"""
    n = 1000
    l1 = create_list(list(range(0, 2 * n, 2)))   # чётные
    l2 = create_list(list(range(1, 2 * n, 2)))   # нечётные
    result = merge(l1, l2)
    assert list_to_array(result) == list(range(2 * n))


# ========== ТЕСТЫ ДЛЯ MERGE_DUMMY (с dummy) ==========

def test_merge_dummy_example():
    """Пример из условия"""
    l1 = create_list([1, 2, 4])
    l2 = create_list([1, 3, 4])
    result = merge_two_lists_dummy(l1, l2)
    assert list_to_array(result) == [1, 1, 2, 3, 4, 4]


def test_merge_dummy_both_empty():
    """Оба списка пусты"""
    result = merge_two_lists_dummy(None, None)
    assert result is None


def test_merge_dummy_first_empty():
    """Первый пуст"""
    l2 = create_list([1, 2, 3])
    result = merge_two_lists_dummy(None, l2)
    assert list_to_array(result) == [1, 2, 3]


def test_merge_dummy_second_empty():
    """Второй пуст"""
    l1 = create_list([1, 2, 3])
    result = merge_two_lists_dummy(l1, None)
    assert list_to_array(result) == [1, 2, 3]


def test_merge_dummy_single_elements():
    """Один элемент в каждом"""
    l1 = create_list([1])
    l2 = create_list([2])
    result = merge_two_lists_dummy(l1, l2)
    assert list_to_array(result) == [1, 2]


def test_merge_dummy_all_smaller_first():
    """Все элементы первого меньше"""
    l1 = create_list([1, 2, 3])
    l2 = create_list([4, 5, 6])
    result = merge_two_lists_dummy(l1, l2)
    assert list_to_array(result) == [1, 2, 3, 4, 5, 6]


def test_merge_dummy_all_smaller_second():
    """Все элементы второго меньше"""
    l1 = create_list([4, 5, 6])
    l2 = create_list([1, 2, 3])
    result = merge_two_lists_dummy(l1, l2)
    assert list_to_array(result) == [1, 2, 3, 4, 5, 6]


def test_merge_dummy_equal_elements():
    """Все элементы равны"""
    l1 = create_list([1, 1, 1])
    l2 = create_list([1, 1, 1])
    result = merge_two_lists_dummy(l1, l2)
    assert list_to_array(result) == [1, 1, 1, 1, 1, 1]


def test_merge_dummy_different_lengths():
    """Разные длины"""
    l1 = create_list([1, 5])
    l2 = create_list([2, 3, 4, 6])
    result = merge_two_lists_dummy(l1, l2)
    assert list_to_array(result) == [1, 2, 3, 4, 5, 6]


def test_merge_dummy_interleaved():
    """Чередование"""
    l1 = create_list([1, 3, 5])
    l2 = create_list([2, 4, 6])
    result = merge_two_lists_dummy(l1, l2)
    assert list_to_array(result) == [1, 2, 3, 4, 5, 6]


def test_merge_dummy_large():
    """Большие списки"""
    n = 1000
    l1 = create_list(list(range(0, 2 * n, 2)))
    l2 = create_list(list(range(1, 2 * n, 2)))
    result = merge_two_lists_dummy(l1, l2)
    assert list_to_array(result) == list(range(2 * n))


# ========== ТЕСТЫ: ОБА ВАРИАНТА ДАЮТ ОДИНАКОВЫЙ РЕЗУЛЬТАТ ==========

def test_both_variants_same_result():
    """Оба варианта дают одинаковый результат"""
    test_cases = [
        ([1, 2, 4], [1, 3, 4]),
        ([], []),
        ([], [1, 2]),
        ([1, 2], []),
        ([1], [2]),
        ([2], [1]),
        ([1, 1, 1], [1, 1, 1]),
        ([-3, -1], [-2, 0]),
    ]
    for arr1, arr2 in test_cases:
        l1 = create_list(arr1)
        l2 = create_list(arr2)
        result1 = list_to_array(merge(l1, l2))

        l1 = create_list(arr1)
        l2 = create_list(arr2)
        result2 = list_to_array(merge_two_lists_dummy(l1, l2))

        assert result1 == result2, f"Разные результаты для {arr1} и {arr2}"