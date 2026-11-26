class Solution:
    def canAliceWin(self, n: int) -> bool:
        x, t = 10, 0
        while n >= x:
            n -= x
            x -= 1
            t = (t + 1) % 2
        return t % 2 == 1
