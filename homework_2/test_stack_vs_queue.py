import pytest
from stack_vs_queue import Stack, Queue


# ========== ТЕСТЫ ДЛЯ СТЕКА ==========

def test_stack_empty():
    """Новый стек пуст"""
    s = Stack()
    assert s.empty() is True


def test_stack_push():
    """После push стек не пуст"""
    s = Stack()
    s.push(1)
    assert s.empty() is False


def test_stack_peek():
    """peek возвращает верхний элемент"""
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.peek() == 3


def test_stack_pop():
    """pop возвращает верхний и удаляет его"""
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.empty() is True


def test_stack_lifo():
    """Стек работает по принципу LIFO"""
    s = Stack()
    for i in range(1, 6):
        s.push(i)
    result = []
    while not s.empty():
        result.append(s.pop())
    assert result == [5, 4, 3, 2, 1]


def test_stack_pop_empty():
    """pop на пустом стеке возвращает None"""
    s = Stack()
    assert s.pop() is None


def test_stack_peek_empty():
    """peek на пустом стеке возвращает None"""
    s = Stack()
    assert s.peek() is None


def test_stack_single_element():
    """Стек с одним элементом"""
    s = Stack()
    s.push(42)
    assert s.peek() == 42
    assert s.pop() == 42
    assert s.empty() is True


# ========== ТЕСТЫ ДЛЯ ОЧЕРЕДИ ==========

def test_queue_empty():
    """Новая очередь пуста"""
    q = Queue()
    assert q.empty() is True


def test_queue_push():
    """После push очередь не пуста"""
    q = Queue()
    q.push(1)
    assert q.empty() is False


def test_queue_peek():
    """peek возвращает первый элемент"""
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    assert q.peek() == 1


def test_queue_pop():
    """pop возвращает первый и удаляет его"""
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.empty() is True


def test_queue_fifo():
    """Очередь работает по принципу FIFO"""
    q = Queue()
    for i in range(1, 6):
        q.push(i)
    result = []
    while not q.empty():
        result.append(q.pop())
    assert result == [1, 2, 3, 4, 5]


def test_queue_pop_empty():
    """pop на пустой очереди возвращает None"""
    q = Queue()
    assert q.pop() is None


def test_queue_peek_empty():
    """peek на пустой очереди возвращает None"""
    q = Queue()
    assert q.peek() is None


def test_queue_single_element():
    """Очередь с одним элементом"""
    q = Queue()
    q.push(42)
    assert q.peek() == 42
    assert q.pop() == 42
    assert q.empty() is True


def test_queue_push_after_empty():
    """Push после того, как очередь опустела (проверка tail)"""
    q = Queue()
    q.push(1)
    q.push(2)
    q.pop()
    q.pop()
    assert q.empty() is True
    q.push(3)               # ← важно: tail должен обновиться
    assert q.peek() == 3
    assert q.pop() == 3
    assert q.empty() is True


def test_queue_many_operations():
    """Много чередующихся операций"""
    q = Queue()
    q.push(1)
    q.push(2)
    assert q.pop() == 1
    q.push(3)
    assert q.pop() == 2
    q.push(4)
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.empty() is True