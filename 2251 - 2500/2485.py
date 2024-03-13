class Solution:
    def pivotInteger(self, n: int) -> int:
        sn = n * (n + 1) // 2
        for k in range(1, n + 1):
            s = k * (k + 1) // 2
            if s == sn:
                return k
            sn -= k
        return -1
