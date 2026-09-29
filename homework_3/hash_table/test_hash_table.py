import pytest
from hash_table import HashTable


# ========== БАЗОВЫЕ ТЕСТЫ ==========

def test_insert_and_get():
    """Вставка и получение одного элемента"""
    ht = HashTable()
    ht.insert("apple", 5)
    assert ht.get("apple") == 5


def test_insert_multiple():
    """Вставка нескольких элементов"""
    ht = HashTable()
    ht.insert("apple", 5)
    ht.insert("banana", 3)
    ht.insert("orange", 7)
    assert ht.get("apple") == 5
    assert ht.get("banana") == 3
    assert ht.get("orange") == 7


def test_update_existing():
    """Обновление существующего ключа"""
    ht = HashTable()
    ht.insert("apple", 5)
    ht.insert("apple", 10)
    assert ht.get("apple") == 10
    assert ht.count == 1


def test_get_missing():
    """Поиск несуществующего ключа"""
    ht = HashTable()
    assert ht.get("missing") is None


def test_delete():
    """Удаление существующего ключа"""
    ht = HashTable()
    ht.insert("apple", 5)
    assert ht.delete("apple") is True
    assert ht.get("apple") is None
    assert ht.count == 0


def test_delete_missing():
    """Удаление несуществующего ключа"""
    ht = HashTable()
    assert ht.delete("missing") is False


# ========== ГРАНИЧНЫЕ СЛУЧАИ ==========

def test_empty_table():
    """Пустая таблица"""
    ht = HashTable()
    assert ht.count == 0
    assert ht.get("anything") is None


def test_single_element():
    """Таблица с одним элементом"""
    ht = HashTable(size=1)
    ht.insert("a", 1)
    assert ht.get("a") == 1


def test_empty_string_key():
    """Пустая строка как ключ"""
    ht = HashTable()
    ht.insert("", 42)
    assert ht.get("") == 42


def test_none_key():
    """None как ключ"""
    ht = HashTable()
    ht.insert(None, 42)
    assert ht.get(None) == 42


def test_int_keys():
    """Целочисленные ключи"""
    ht = HashTable()
    for i in range(10):
        ht.insert(i, i * 10)
    for i in range(10):
        assert ht.get(i) == i * 10


def test_tuple_keys():
    """Кортежи как ключи"""
    ht = HashTable()
    ht.insert((1, 2), "a")
    ht.insert((3, 4), "b")
    assert ht.get((1, 2)) == "a"
    assert ht.get((3, 4)) == "b"


def test_negative_keys():
    """Отрицательные ключи"""
    ht = HashTable()
    ht.insert(-1, "minus")
    ht.insert(-100, "big minus")
    assert ht.get(-1) == "minus"
    assert ht.get(-100) == "big minus"


# ========== КОЛЛИЗИИ ==========

def test_collision():
    """Все ключи в одну ячейку (size=1)"""
    ht = HashTable(size=1)
    ht.insert("a", 1)
    ht.insert("b", 2)
    ht.insert("c", 3)
    assert ht.get("a") == 1
    assert ht.get("b") == 2
    assert ht.get("c") == 3
    assert ht.count == 3


def test_collision_update():
    """Обновление при коллизии"""
    ht = HashTable(size=1)
    ht.insert("a", 1)
    ht.insert("b", 2)
    ht.insert("a", 10)
    assert ht.get("a") == 10
    assert ht.get("b") == 2
    assert ht.count == 2


def test_collision_delete():
    """Удаление при коллизии"""
    ht = HashTable(size=1)
    ht.insert("a", 1)
    ht.insert("b", 2)
    ht.insert("c", 3)
    ht.delete("b")
    assert ht.get("a") == 1
    assert ht.get("b") is None
    assert ht.get("c") == 3
    assert ht.count == 2


def test_collision_delete_first():
    """Удаление первого элемента в цепочке"""
    ht = HashTable(size=1)
    ht.insert("a", 1)
    ht.insert("b", 2)
    ht.delete("a")
    assert ht.get("a") is None
    assert ht.get("b") == 2


def test_collision_delete_last():
    """Удаление последнего элемента в цепочке"""
    ht = HashTable(size=1)
    ht.insert("a", 1)
    ht.insert("b", 2)
    ht.delete("b")
    assert ht.get("a") == 1
    assert ht.get("b") is None


# ========== RESIZE ==========

def test_resize():
    """Расширение таблицы"""
    ht = HashTable(size=4)
    for i in range(100):
        ht.insert(f"key{i}", i)
    for i in range(100):
        assert ht.get(f"key{i}") == i
    assert ht.count == 100


def test_resize_collisions():
    """Расширение при коллизиях"""
    ht = HashTable(size=1)
    for i in range(50):
        ht.insert(i, i * 2)
    for i in range(50):
        assert ht.get(i) == i * 2


def test_resize_preserves_values():
    """Resize сохраняет все значения"""
    ht = HashTable(size=4)
    for i in range(10):
        ht.insert(f"key{i}", i)
    assert ht.get("key0") == 0
    assert ht.get("key5") == 5
    assert ht.get("key9") == 9


def test_resize_twice():
    """Двойной resize"""
    ht = HashTable(size=2)
    for i in range(200):
        ht.insert(i, i)
    for i in range(200):
        assert ht.get(i) == i


# ========== СМЕШАННЫЕ ОПЕРАЦИИ ==========

def test_mixed_operations():
    """Чередование операций"""
    ht = HashTable()
    ht.insert("a", 1)
    ht.insert("b", 2)
    ht.insert("c", 3)
    ht.delete("b")
    ht.insert("d", 4)
    ht.insert("a", 10)

    assert ht.get("a") == 10
    assert ht.get("b") is None
    assert ht.get("c") == 3
    assert ht.get("d") == 4
    assert ht.count == 3


def test_many_operations():
    """Много операций"""
    ht = HashTable(size=4)

    # Вставляем 1000 элементов
    for i in range(1000):
        ht.insert(f"key{i}", i)

    # Удаляем каждый второй
    for i in range(0, 1000, 2):
        ht.delete(f"key{i}")

    # Проверяем оставшиеся
    for i in range(1, 1000, 2):
        assert ht.get(f"key{i}") == i
    for i in range(0, 1000, 2):
        assert ht.get(f"key{i}") is None

    assert ht.count == 500


def test_delete_all():
    """Удаление всех элементов"""
    ht = HashTable()
    for i in range(10):
        ht.insert(f"key{i}", i)
    for i in range(10):
        ht.delete(f"key{i}")
    assert ht.count == 0
    for i in range(10):
        assert ht.get(f"key{i}") is None


def test_reinsert_after_delete():
    """Повторная вставка после удаления"""
    ht = HashTable()
    ht.insert("a", 1)
    ht.delete("a")
    ht.insert("a", 2)
    assert ht.get("a") == 2
    assert ht.count == 1


# ========== СТРЕСС-ТЕСТЫ ==========

def test_stress_insert_get():
    """Стресс: 10000 вставок и поисков"""
    ht = HashTable()
    n = 10000
    for i in range(n):
        ht.insert(f"key{i}", i)
    for i in range(n):
        assert ht.get(f"key{i}") == i
    assert ht.count == n


def test_stress_with_collisions():
    """Стресс: много коллизий (size=1)"""
    ht = HashTable(size=1)
    n = 100
    for i in range(n):
        ht.insert(i, i)
    for i in range(n):
        assert ht.get(i) == i


def test_stress_mixed():
    """Стресс: смешанные операции"""
    ht = HashTable(size=4)
    n = 5000
    for i in range(n):
        ht.insert(i, i * 2)
    for i in range(0, n, 3):
        ht.delete(i)
    for i in range(n):
        if i % 3 == 0:
            assert ht.get(i) is None
        else:
            assert ht.get(i) == i * 2