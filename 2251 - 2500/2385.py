from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def nodes(node):
            if not node:
                return
            if node.left:
                btree[node.val].append(node.left.val)
                btree[node.left.val].append(node.val)
            if node.right:
                btree[node.val].append(node.right.val)
                btree[node.right.val].append(node.val)
            nodes(node.left)
            nodes(node.right)

        btree = defaultdict(list)
        nodes(root)
        infected = set()
        stack = btree[start]
        infected.add(start)
        res = 0
        while stack:
            t = stack.copy()
            for node in t:
                infected.add(node)
                for el in btree[node]:
                    if el not in infected:
                        stack.append(el)
            stack = stack[len(t) :]
            res += 1
        return res
