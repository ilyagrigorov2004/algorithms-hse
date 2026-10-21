import pytest
from validate_bst import TreeNode, validate_bst


# ========== ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ ==========

def build_tree(vals):
    """Создаёт дерево из списка, вставляя элементы по правилам BST"""

    def insert(root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = insert(root.left, val)
        elif val > root.val:
            root.right = insert(root.right, val)
        return root

    root = None
    for v in vals:
        root = insert(root, v)
    return root


# ========== ТЕСТЫ ==========

def test_valid_bst():
    """Корректное дерево поиска"""
    #       8
    #      / \
    #     3   10
    #    / \
    #   1   6
    root = TreeNode(8)
    root.left = TreeNode(3, TreeNode(1), TreeNode(6))
    root.right = TreeNode(10)
    assert validate_bst(root) is True


def test_valid_bst_large():
    """Большое корректное дерево"""
    root = build_tree([10, 5, 15, 2, 7, 12, 20])
    assert validate_bst(root) is True


def test_invalid_bst():
    """Некорректное дерево (правое поддерево меньше корня)"""
    #       5
    #      / \
    #     1   4
    #        / \
    #       3   6
    # 4 находится справа от 5, но 4 < 5. Не BST.
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4, TreeNode(3), TreeNode(6))
    assert validate_bst(root) is False


def test_invalid_deep():
    """Ошибка глубоко в дереве"""
    #       10
    #      /  \
    #     5    15
    #         /  \
    #        6    20   <-- 6 меньше 10, но справа!
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15, TreeNode(6), TreeNode(20))
    assert validate_bst(root) is False


def test_empty_tree():
    """Пустое дерево — валидный BST"""
    assert validate_bst(None) is True


def test_single_node():
    """Дерево из одного узла — валидный BST"""
    assert validate_bst(TreeNode(5)) is True


def test_duplicates():
    """Дубликаты нарушают строгое свойство BST"""
    root = TreeNode(5)
    root.left = TreeNode(5)
    assert validate_bst(root) is False


def test_duplicates_deep():
    """Дубликаты глубоко в дереве"""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(15)  # дубликат
    assert validate_bst(root) is False


def test_left_child_greater():
    """Левый ребёнок больше родителя"""
    root = TreeNode(5)
    root.left = TreeNode(10)
    assert validate_bst(root) is False


def test_right_child_smaller():
    """Правый ребёнок меньше родителя"""
    root = TreeNode(5)
    root.right = TreeNode(3)
    assert validate_bst(root) is False


def test_negative_numbers():
    """Отрицательные числа"""
    root = build_tree([0, -5, 5, -10, -2, 2, 10])
    assert validate_bst(root) is True


def test_negative_invalid():
    """Отрицательные числа, невалидное дерево"""
    root = TreeNode(0)
    root.left = TreeNode(5)  # слева больше
    assert validate_bst(root) is False


def test_skewed_right():
    """Вырожденное дерево вправо (1 -> 2 -> 3)"""
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert validate_bst(root) is True


def test_skewed_left():
    """Вырожденное дерево влево (3 -> 2 -> 1)"""
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    assert validate_bst(root) is True


def test_min_max_edge():
    """Значения на границах"""
    root = build_tree([0, -100, 100])
    assert validate_bst(root) is True
