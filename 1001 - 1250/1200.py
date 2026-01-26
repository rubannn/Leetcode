from collections import defaultdict
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        dc = defaultdict(list)
        for i in range(len(arr) - 1):
            dc[arr[i + 1] - arr[i]].append([arr[i], arr[i + 1]])
        return dc[min(dc.keys())]
