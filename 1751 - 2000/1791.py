from typing import List
from collections import defaultdict


class Solution:
    # variant 1
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()

    # variant 2
    def findCenter(self, edges: List[List[int]]) -> int:
        res = set(edges[0])
        for p in edges:
            res &= set(p)
        return list(res)[0]

    # variant 3
    def findCenter(self, edges: List[List[int]]) -> int:
        res = defaultdict(int)
        for a, b in edges:
            res[a] += 1
            res[b] += 1
        return max(res, key=res.get)
