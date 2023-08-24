
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        else:
            return inOrder(root, [])


def inOrder(node, arr):
    if node.left:
        inOrder(node.left, arr)
    arr.append(node.val)
    if node.right:
        inOrder(node.right, arr)
    return arr