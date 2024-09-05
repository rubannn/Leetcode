class Solution:
    # variant 1
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sum_x = mean * (n + m) - sum(rolls)
        if sum_x <= 0 or sum_x > 6 * n or sum_x < n:
            return []
        else:
            mn = sum_x // n
            res = []
            while n > 1:
                res.append(mn)
                sum_x -= mn
                n -= 1
            if sum_x > 0:
                res.append(sum_x)
                i = 0
                while res[-1] > 6:
                    res[i] += 1
                    res[-1] -= 1
                    i += 1
            return res

    # variant 2
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sum_x = mean * (n + m) - sum(rolls)
        if sum_x > 6 * n or sum_x < n:
            return []
        else:
            res = [sum_x // n] * n
            for x in range(sum_x % n):
                res[x] += 1
            return res
