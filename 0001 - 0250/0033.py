def search(self, nums: list[int], target: int) -> int:
    first, last = 0, len(nums) - 1
    while first <= last:
        mid = (first + last) // 2
        if nums[mid] == target:
            return mid
        if nums[first] <= nums[mid]:
            if nums[first] <= target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1
        else:
            if nums[mid] < target <= nums[last]:
                first = mid + 1
            else:
                last = mid - 1
    return -1
