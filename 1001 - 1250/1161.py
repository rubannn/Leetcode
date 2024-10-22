# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
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
        dc = sorted(dc.items(), key=lambda x: -x[1])
        return dc[0][0]
