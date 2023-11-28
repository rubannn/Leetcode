from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def last_nodes(root, res=[]):
            if not root:
                return

            if not (root.left or root.right):
                res.append(root.val)
                return

            last_nodes(root.left, res)
            last_nodes(root.right, res)

        last1, last2 = [], []
        last_nodes(root1, last1)
        last_nodes(root2, last2)
        return last1 == last2
