class Solution:
    # variant 1
    def singleNumber(self, nums: List[int]) -> List[int]:
        return [x for x in set(nums) if nums.count(x) == 1]

    # variant 2
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums += ["~"]
        res = []
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                res.append(nums[i])
                i += 1
                if len(res) == 2:
                    return res
        return res
