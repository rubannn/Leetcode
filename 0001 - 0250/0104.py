from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def mxDepth(node):
            if node is None:
                return 0
            else:
                left_depth = mxDepth(node.left)
                right_depth = mxDepth(node.right)
                return max(left_depth, right_depth) + 1
        return mxDepth(root)
