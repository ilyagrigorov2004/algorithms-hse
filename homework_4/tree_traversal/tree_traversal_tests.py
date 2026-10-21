import pytest
from tree_traversal import (
    TreeNode, insert,
    preorder, inorder, postorder,
    reverse_preorder, reverse_inorder, reverse_postorder
)


def create_tree(arr):
    """Вспомогательная функция для создания дерева"""
    root = None
    for x in arr:
        root = insert(root, x)
    return root


# ========== ТЕСТЫ ДЛЯ INSERT ==========

def test_insert_empty():
    """Вставка в пустое дерево"""
    root = insert(None, 5)
    assert root.val == 5
    assert root.left is None
    assert root.right is None


def test_insert_multiple():
    """Вставка нескольких элементов"""
    root = create_tree([8, 3, 10, 1, 6, 14])
    assert root.val == 8
    assert root.left.val == 3
    assert root.right.val == 10
    assert root.left.left.val == 1
    assert root.left.right.val == 6
    assert root.right.right.val == 14


def test_insert_duplicate():
    """Дубликаты игнорируются"""
    root = create_tree([5, 5, 5])
    assert root.val == 5
    assert root.left is None
    assert root.right is None


# ========== ТЕСТЫ ДЛЯ ОБХОДОВ ==========

def test_traversals():
    """Все 6 обходов на стандартном дереве"""
    # Дерево:
    #       8
    #      / \
    #     3   10
    #    / \
    #   1   6
    root = create_tree([8, 3, 10, 1, 6])

    assert preorder(root) == [8, 3, 1, 6, 10]
    assert inorder(root) == [1, 3, 6, 8, 10]
    assert postorder(root) == [1, 6, 3, 10, 8]

    assert reverse_preorder(root) == [8, 10, 3, 6, 1]
    assert reverse_inorder(root) == [10, 8, 6, 3, 1]
    assert reverse_postorder(root) == [10, 6, 1, 3, 8]


def test_traversals_empty():
    """Пустое дерево"""
    assert preorder(None) == []
    assert inorder(None) == []
    assert postorder(None) == []
    assert reverse_preorder(None) == []
    assert reverse_inorder(None) == []
    assert reverse_postorder(None) == []


def test_traversals_single():
    """Дерево из одного узла"""
    root = create_tree([42])
    assert preorder(root) == [42]
    assert inorder(root) == [42]
    assert postorder(root) == [42]


def test_inorder_sorted():
    """Главное свойство BST: inorder даёт отсортированный список"""
    arr = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    root = create_tree(arr)
    assert inorder(root) == sorted(arr)


def test_skewed_tree():
    """Вырожденное дерево (вставляем по возрастанию)"""
    root = create_tree([1, 2, 3, 4, 5])
    # Дерево выглядит как список: 1 -> 2 -> 3 -> 4 -> 5 (все вправо)
    assert inorder(root) == [1, 2, 3, 4, 5]
    assert preorder(root) == [1, 2, 3, 4, 5]