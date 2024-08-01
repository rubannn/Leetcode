# https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ''
        for i, x in enumerate(nums):
            ans += '01'[x[i] == '0']
        return ans
