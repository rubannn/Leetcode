# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def bfs(node):
            if not node:
                return
            if low <= node.val <= high:
                self.res += node.val
            bfs(node.right)
            bfs(node.left)

        self.res = 0
        bfs(root)
        return self.res
