# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def getnodes(tree, lvl, side, start):
            res = []
            if tree:
                res.append({side: tree.val})
                if tree.left:
                    res += getnodes(tree.left, lvl + 1, side+'L', tree.val)
                if tree.right:
                    res += getnodes(tree.right, lvl + 1, side+'R', tree.val)
            return res

        vinfo = dict()
        for item in getnodes(root, 0, '~', None):
            for k, v in item.items():
                vinfo[k] = [v]
        mx = max(map(len, vinfo.keys()))
        for x in sorted(vinfo.keys(), key=lambda x: -len(x)):
            if len(x) != mx:
                if vinfo.get(x+'L', -1) != -1:
                    vinfo[x] += vinfo[x+'L']
                if vinfo.get(x+'R', -1) != -1:
                    vinfo[x] += vinfo[x+'R']
        return sum(int(sum(vinfo[x]) // len(vinfo[x])) == vinfo[x][0] for x in vinfo.keys())
