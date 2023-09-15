class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        x = 0
        while arr[x] < arr[x + 1]:
            x += 1
        return x
