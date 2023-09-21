class Solution:
    def findComplement(self, num: int) -> int:
        res, d = 0, 1
        for b in f'{num:b}'[::-1]:
            if b == '0':
                res += d
            d *= 2
        return res
