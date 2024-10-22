from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        dc = defaultdict(int)

        def nodelevel(head: Optional[TreeNode], lvl: int):
            nonlocal dc
            if head:
                dc[lvl] += head.val
                if head.left:
                    nodelevel(head.left, lvl + 1)
                if head.right:
                    nodelevel(head.right, lvl + 1)
            return

        nodelevel(root, 1)
        mx = sorted(dc.values())
        return -1 if k > len(mx) else mx[-k]
