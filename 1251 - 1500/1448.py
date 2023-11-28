class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goods_count(node, cur_min) -> int:
            if not node:
                return 0
            mx = max(cur_min, node.val)
            return goods_count(node.left, mx) + goods_count(node.right, mx) + (node.val >= cur_min)

        return goods_count(root, root.val)
