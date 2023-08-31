class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        x = y = p = 0
        v = ((0, 1), (1, 0), (0, -1), (-1, 0))
        fill = -1
        res = [[fill for _ in range(n)] for _ in range(m)]
        while head:
            res[x][y] = head.val
            head = head.next
            vx, vy = v[p]
            if not ((0 <= x + vx < m) and (0 <= y + vy < n)
                    and (res[x + vx][y + vy] == fill)):
                p = (p + 1) % 4
            x += v[p][0]
            y += v[p][1]
        return res
