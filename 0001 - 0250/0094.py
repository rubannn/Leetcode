# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def treeview(node, tpath):
            if not node:
                return
            treeview(node.left, tpath)
            tpath.append(node.val)
            treeview(node.right, tpath)

        path = []
        treeview(root, path)
        return path
