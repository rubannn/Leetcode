class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while True:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
            if left + 1 == right or left == right:
                if target <= nums[left]:
                    return left
                elif target > nums[right]:
                    return right + 1
                return left + 1
