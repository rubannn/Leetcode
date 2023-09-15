class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for x in nums:
            if x % 2 == 0:
                even_sum += x
        res = []
        for q in queries:
            if nums[q[1]] % 2 == 0:
                if q[0] % 2 == 0:
                    even_sum = even_sum + q[0]
                else:
                    even_sum = even_sum - nums[q[1]]
                nums[q[1]] += q[0]
            else:
                nums[q[1]] += q[0]
                if nums[q[1]] % 2 == 0:
                    even_sum += nums[q[1]]
            res.append(even_sum)
        return res
