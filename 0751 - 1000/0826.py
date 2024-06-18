from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        jobs = sorted(zip(difficulty, profit))
        res = mx = i = 0
        for w in sorted(worker):
            while i < len(jobs) and jobs[i][0] <= w:
                mx = max(mx, jobs[i][1])
                i += 1
            res += mx
        return res


tests = [
    ([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7], 100),
    ([85, 47, 57], [24, 66, 99], [40, 25, 25], 0),
]
sol = Solution()
for d, p, w, ans in tests:
    print(sol.maxProfitAssignment(d, p, w), ans)
