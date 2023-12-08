from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def treeview(node):
            if node and not node.left and not node.right:
                return f'{node.val}'
            elif node is None:
                return ''
            else:
                return f"{node.val}({treeview(node.left)}){f'({treeview(node.right)})' if node.right else ''}"
        return treeview(root)
