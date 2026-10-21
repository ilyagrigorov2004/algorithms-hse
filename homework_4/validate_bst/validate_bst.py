class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validate_bst(root):
    answer = []

    def _walk(node):
        if node is None:
            return
        _walk(node.left)
        answer.append(node.val)
        _walk(node.right)

    _walk(root)

    for i in range(len(answer) - 1):
        if answer[i] >= answer[i+1]:
            return False
    return True
