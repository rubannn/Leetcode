class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count, pred = 0, -inf
        for x, y in points:
            if x > pred:
                count += 1
                pred = y
        return count
