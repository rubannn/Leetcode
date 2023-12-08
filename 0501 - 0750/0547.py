from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(v):
            visit[v] = not visit[v]
            for j in range(n):
                if not visit[j] and isConnected[v][j]:
                    dfs(j)

        res, n = 0, len(isConnected)
        visit = [False] * n
        for i in range(n):
            if not visit[i]:
                res += 1
                dfs(i)
        return res


sol = Solution()
tests = [
    ([[1,1,0],[1,1,0],[0,0,1]], 2),
    ([[1,0,0],[0,1,0],[0,0,1]], 3),
    ([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]], 1),
]
for t, ans in tests:
    print(sol.findCircleNum(t) == ans)
