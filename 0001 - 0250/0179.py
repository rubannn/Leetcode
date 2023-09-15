class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def qsort(arr):
            if len(arr) <= 1:
                return arr
            else:
                item = arr[0]
                left = [x for x in arr[1:] if x + item >= item + x]
                right = [x for x in arr[1:] if x + item < item + x]
                return qsort(left) + [item] + qsort(right)
        return str(int(''.join(qsort([str(x) for x in nums]))))
