class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    #дубликат — ничего не делаем
    return root


def preorder(root):
    result = []

    def _walk(node):
        if node is None: return
        result.append(node.val)
        _walk(node.left)
        _walk(node.right)
    _walk(root)
    return result


def inorder(root):
    result = []

    def _walk(node):
        if node is None:
            return
        _walk(node.left)
        result.append(node.val)
        _walk(node.right)
    _walk(root)
    return result


def postorder(root):
    result = []

    def _walk(node):
        if node is None: return
        _walk(node.left)
        _walk(node.right)
        result.append(node.val)
    _walk(root)
    return result


def reverse_preorder(root):
    result = []

    def _walk(node):
        if node is None: return
        result.append(node.val)
        _walk(node.right)
        _walk(node.left)
    _walk(root)
    return result


def reverse_inorder(root):
    result = []

    def _walk(node):
        if node is None: return
        _walk(node.right)
        result.append(node.val)
        _walk(node.left)
    _walk(root)
    return result


def reverse_postorder(root):
    result = []

    def _walk(node):
        if node is None:
            return
        _walk(node.right)
        _walk(node.left)
        result.append(node.val)
    _walk(root)
    return result
