class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        op = ["Push", "Pop"]
        res = []
        num, p = 1, 0
        while p < len(target) and target[p] <= n:
            if p < len(target) and num == target[p]:
                res.append(op[0])
                num += 1
            elif p < len(target):
                if p - 1 < 0:
                    res += op * (target[p] - 1)
                else:
                    res += op * (target[p] - target[p - 1] - 1)
                res += [op[0]]
                num = target[p]
            p += 1
        return res
