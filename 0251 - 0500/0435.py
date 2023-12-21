class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count, t = 0, intervals[0][1]
        for x, y in intervals[1:]:
            if x >= t:
                t = y
            else:
                count += 1
        return count
