class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nm = Counter(nums)
        res = []
        while sum(nm.values()) > 0:
            row = []
            for k in nm.keys():
                if nm[k] > 0:
                    row.append(k)
                    nm[k] -= 1
            res += [row]
        return res
