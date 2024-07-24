class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def getNewVal(x):
            return int("".join([f"{mapping[int(c)]}" for c in str(x)]))

        nums.sort(key=lambda a: getNewVal(a))
        return nums
