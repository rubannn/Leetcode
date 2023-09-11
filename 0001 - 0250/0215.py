def findKthLargest(self, nums: list, k: int) -> int:
    nums.sort()
    return nums[::-1][k-1]
