class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dc = dict()
        for x in arr:
            dc[x] = dc.get(x, 0) + 1
        return len(dc.values()) == len(set(dc.values()))
