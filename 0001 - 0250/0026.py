def removeDuplicates(self, nums: list[int]) -> int:
    res = []
    for x in nums:
        if x not in res:
            res.append(x)
    for i, x in enumerate(res):
        nums[i] = x
    return len(res)
