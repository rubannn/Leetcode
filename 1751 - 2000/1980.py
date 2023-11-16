# https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans, p = '', 0
        for x in nums:
            ans += '01'[x[p] == '0']
            p += 1
        return ans
