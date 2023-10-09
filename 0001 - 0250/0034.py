class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(nums, target):
            first, last = 0, len(nums) - 1
            while not (first > last):
                mid = (first + last) // 2
                if nums[mid] < target:
                    first = mid + 1
                else:
                    last = mid - 1
            return first

        if len(set(nums)) == 1 and target == nums[0]:
            return [0, len(nums)-1]
        left = bs(nums, target - 0.5)
        right = bs(nums, target + 0.5)
        print(left, right)
        return [-1, -1] if left == right else [left, right-1]
