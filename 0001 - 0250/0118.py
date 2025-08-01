class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(numRows - 1):
            last = [1]
            for k in range(len(res[-1]) - 1):
                last += [res[-1][k] + res[-1][k + 1]]
            res.append(last + [1])
        return res
