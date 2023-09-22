class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s, res = set(), []
        for x in nums:
            if x in s:
                res.append(x)
            s.add(x)
        return res
