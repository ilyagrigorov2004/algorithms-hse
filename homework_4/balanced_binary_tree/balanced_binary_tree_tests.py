import pytest
from balanced_binary_tree import TreeNode, is_balanced


def test_balanced():
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert is_balanced(root) is True


def test_unbalanced():
    #        1
    #       / \
    #      2   2
    #     / \
    #    3   3
    #   / \
    #  4   4
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3))
    root.right = TreeNode(2)
    assert is_balanced(root) is False


def test_empty():
    assert is_balanced(None) is True


def test_single_node():
    assert is_balanced(TreeNode(1)) is True


def test_two_levels():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_balanced(root) is True


def test_only_left():
    # 1 -> 2 -> 3 -> 4 (только влево)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    assert is_balanced(root) is False


def test_only_right():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    assert is_balanced(root) is False


def test_difference_one():
    #     1
    #    / \
    #   2   3
    #  /
    # 4
    # Высота левого = 2, правого = 1. Разница = 1 (сбалансировано)
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4))
    root.right = TreeNode(3)
    assert is_balanced(root) is True


def test_difference_two():
    #     1
    #    / \
    #   2   3
    #  /
    # 4
    # /
    # 5
    # Высота левого = 3, правого = 1. Разница = 2 (не сбалансировано)
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4, TreeNode(5)))
    root.right = TreeNode(3)
    assert is_balanced(root) is False


def test_deep_imbalance():
    #        1
    #       / \
    #      2   3
    #     /     \
    #    4       5
    #   /
    #  6
    # Корень (1) сбалансирован. Но узел 2 — нет (разница 2).
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4, TreeNode(6)))
    root.right = TreeNode(3, None, TreeNode(5))
    assert is_balanced(root) is False