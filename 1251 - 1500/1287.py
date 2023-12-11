class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        k = int(len(arr) / 4)
        for i in range(len(arr) - k):
            if i+k < len(arr) and arr[i] == arr[i+k]:
                return arr[i]
        return arr[0]
