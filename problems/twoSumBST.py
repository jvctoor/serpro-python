# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        arr = breadthFirstSearch(root)
        map = {}
        for num in arr:
            resto = k - num
            if resto in map:
                return True
            map[num] = resto

        return False


def breadthFirstSearch(node):
    result = []
    queue = []
    queue.append(node)
    while len(queue) > 0:
        current = queue.pop(0)
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result
