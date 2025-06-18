class Solution:
    def maxDiff(self, num: int) -> int:
        snum = str(num)
        nums = []
        for d in "0123456789":
            for c in snum:
                x = int(snum.replace(c, d))
                if len(str(x)) == len(snum) and x > 0:
                    nums.append(x)
        nums.sort()
        return nums[-1] - nums[0]
