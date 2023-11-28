class Solution:
    def numberOfWays(self, corridor: str) -> int:
        res, t, k, modulus = 0, 1, 0, 10**9 + 7

        for c in corridor:
            if c == 'S':
                t = (t + res) % modulus
                res = k
                k = t
                t = 0
            else:
                t = (t + res) % modulus

        return res
