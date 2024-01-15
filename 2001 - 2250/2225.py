from typing import List


class Solution:
    # variant 1 - 1363 ms, 71.3 MB
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = set()
        loss1, loss2 = set(), set()
        for x, y in matches:
            win.add(x)
            if y in loss1:
                loss2.add(y)
            else:
                loss1.add(y)
        return [sorted(win - loss1), sorted(loss1 - loss2)]

    # variant 2 - 1623 ms, 81.3 MB
    def findWinners2(self, matches: List[List[int]]) -> List[List[int]]:
        dc = dict()
        for x, y in matches:
            if dc.get(x, None) is None:
                dc[x] = {"win": [], "loss": 0}
            dc[x]["win"].append(y)
            if dc.get(y, None) is None:
                dc[y] = {"win": [], "loss": 0}
            dc[y]["loss"] += 1
        res = [set(), set()]
        for k in dc:
            t = dc[k]["loss"]
            if t in (0, 1):
                res[t].add(k)
        return [sorted(res[0]), sorted(res[1])]


tests = [
    (
        [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]],
        [[1, 2, 10], [4, 5, 7, 8]],
    ),
    (
        [[2, 3], [1, 3], [5, 4], [6, 4]],
        [[1, 2, 5, 6], []]
    ),
]

sol = Solution()
for t, ans in tests[:]:
    print(sol.findWinners(t), ans)
