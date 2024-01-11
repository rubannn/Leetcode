from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def nodes(node, mx, mn):
            if not node:
                return mx - mn
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            return max(nodes(node.left, mx, mn), nodes(node.right, mx, mn))

        return nodes(root, root.val, root.val)
