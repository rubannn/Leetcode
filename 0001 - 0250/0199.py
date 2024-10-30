# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        r_only = []

        def nodelevel(head: Optional[TreeNode], lvl: int):
            nonlocal r_only
            if head:
                if lvl == len(r_only):
                    r_only.append(head.val)
                nodelevel(head.right, lvl + 1)
                nodelevel(head.left, lvl + 1)
            return

        nodelevel(root, 0)
        return r_only
