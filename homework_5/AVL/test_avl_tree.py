import pytest
from avl_tree import AVLTree


@pytest.fixture
def avl():
    return AVLTree()


def inorder(root):
    """Вспомогательная функция для получения отсортированного списка"""
    result = []
    def _walk(node):
        if not node: return
        _walk(node.left)
        result.append(node.key)
        _walk(node.right)
    _walk(root)
    return result


def test_insert_basic(avl):
    root = None
    for key in [10, 20, 30, 40, 50, 25]:
        root = avl.insert(root, key)
    assert inorder(root) == [10, 20, 25, 30, 40, 50]


def test_avl_balancing(avl):
    """Проверка, что дерево балансируется (высота не растет линейно)"""
    root = None
    for i in range(1, 8):  # 1,2,3,4,5,6,7 (вставка по возрастанию)
        root = avl.insert(root, i)
    # Если дерево сбалансировано, высота должна быть 3 (log2(7) ~ 2.8)
    assert avl.get_height(root) == 3


def test_delete_leaf(avl):
    root = None
    for key in [10, 20, 30]:
        root = avl.insert(root, key)
    root = avl.delete(root, 10)
    assert inorder(root) == [20, 30]


def test_delete_node_with_one_child(avl):
    root = None
    for key in [10, 20, 30]:
        root = avl.insert(root, key)
    root = avl.delete(root, 20)
    assert inorder(root) == [10, 30]


def test_delete_node_with_two_children(avl):
    root = None
    for key in [10, 20, 30, 40, 50, 25]:
        root = avl.insert(root, key)
    root = avl.delete(root, 30)
    assert inorder(root) == [10, 20, 25, 40, 50]


def test_search_found(avl):
    root = None
    for key in [10, 20, 30]:
        root = avl.insert(root, key)
    node = avl.search(root, 20)
    assert node is not None
    assert node.key == 20


def test_search_not_found(avl):
    root = None
    for key in [10, 20, 30]:
        root = avl.insert(root, key)
    node = avl.search(root, 99)
    assert node is None


def test_insert_duplicates(avl):
    """Дубликаты не должны добавляться"""
    root = None
    root = avl.insert(root, 10)
    root = avl.insert(root, 10)
    assert inorder(root) == [10]


def test_empty_tree(avl):
    """Граничный случай: пустое дерево"""
    assert avl.search(None, 10) is None
    assert avl.delete(None, 10) is None