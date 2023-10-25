class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for a in range(len(nums)):
            k = 0
            for b in range(len(nums)):
                if nums[a] > nums[b]:
                    k += 1
            res.append(k)
        return res
