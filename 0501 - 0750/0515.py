    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def getnodes(tree, lvl):
            res = []
            if tree:
                res.append((tree.val, lvl))
                if tree.left:
                    res += getnodes(tree.left, lvl + 1)
                if tree.right:
                    res += getnodes(tree.right, lvl + 1)
            return res
        rows = {}
        for x in getnodes(root, 0):
            rows[x[1]] = rows.get(x[1], []) + [x[0]]

        return [max(x) for x in rows.values()]
