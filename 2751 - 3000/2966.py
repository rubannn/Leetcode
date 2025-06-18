class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(0, n, 3):
            arr = nums[i : i + 3]
            if arr[2] - arr[0] > k:
                return []
            res.append(arr)
        return res

    def divideArray2(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) // 3):
            elem = nums[3 * i : 3 * i + 3]
            if elem[2] - elem[0] > k:
                return []
            res.append(elem)
        return res
