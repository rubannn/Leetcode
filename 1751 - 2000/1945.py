class Solution:
    def getLucky(self, s: str, k: int) -> int:
        d = "".join([f"{ord(c) - ord('a') + 1}" for c in s])
        res = sum(int(c) for c in d)
        while k > 1:
            t = 0
            while res > 0:
                t += res % 10
                res //= 10
            res = t
            k -= 1
        return res
