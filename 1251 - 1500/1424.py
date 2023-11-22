from typing import List

class Solution:
    # good solution
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diags = dict()
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diags[i + j] = [nums[i][j]] + diags.get(i + j, [])

        res = []
        for k in sorted(diags.keys()):
            res += diags[k]
        return res

    # Time Limit Exceeded for bigData
    def findDiagonalOrder_not_correct_for_all_tests(self, nums: List[List[int]]) -> List[int]:
        res = []
        n = len(nums)
        k = sum(len(r) for r in nums)
        rows = list(range(n))[::-1]
        row = rows.pop()
        while True:
            if nums[row]:
                res.append(nums[row][0])
                nums[row] = nums[row][1:]
                if (k := k - 1) == 0:
                    break

            if row == 0:
                row = rows.pop() if rows else (n - 1)
            else:
                row -= 1
                while row > -1 and nums[row] == []:
                    row -= 1

                if row < 0:
                    row = rows.pop() if rows else (n - 1)
                    while not nums[row]:
                        row -= 1
        return res

tests = [
    {'nums': [[1,2,3],[4,5,6],[7,8,9]], 'res': [1,4,2,7,5,3,8,6,9]},
    {'nums': [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]], 'res': [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]},
    {'nums': [[1,2,3],[4],[5,6,7],[8],[9,10,11]], 'res': [1,4,2,5,3,8,6,9,7,10,11]},
    {'nums': [[20,17,13,14],[12,6],[3,4]], 'res': [20,12,17,3,6,13,4,14]},
    {'nums': [[1,36,9,7,4,20,1,7],[11,27,7,38,32,17,13],[35,16,7,7,21,13],[5,40,27,37,26],[12,17,2,3,17,9,6,4],
              [29,5,19,37,4,7,34,32,9],[13,34,20,24,32]],
     'res': [1,11,36,35,27,9,5,16,7,7,12,40,7,38,4,29,17,27,7,32,20,13,5,2,37,21,17,1,34,19,3,26,13,13,7,20,37,17,24,4,9,32,7,6,34,4,32,9]},
    {'nums': [[14,12,19,16,9],[13,14,15,8,11],[11,13,1]], 'res': [14,13,12,11,14,19,13,15,16,1,8,9,11]},
    {'nums': [[13,9,16,10,4],[34,24,8,36,10,29,24,2,26,3],[5,39,13,31,2,27,1],[24,18,7,15,25,14],[12,25,19,40,2,35,35,10,23,21],[27,5,39,35,6,34],[29,22,20,39,19,9,14,38,38],[39,12,33,5,7,30,39],[39,33,8,33,15,7,14,11]],
     'res': [13,34,9,5,24,16,24,39,8,10,12,18,13,36,4,27,25,7,31,10,29,5,19,15,2,29,39,22,39,40,25,27,24,39,12,20,35,2,14,1,2,33,33,39,6,35,26,8,5,19,34,35,3,33,7,9,10,15,30,14,23,7,39,38,21,14,38,11]}
         ]

sol = Solution()
for items in tests[:]:
    nm = items['nums']
    rs = items['res']
    print(sol.findDiagonalOrder(nm) == rs)
