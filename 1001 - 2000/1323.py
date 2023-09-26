class Solution:
    def maximum69Number (self, num: int) -> int:
        snum = [x for x in list(str(num))]
        res = []
        for x in range(len(snum)):
            t = snum[:]
            t[x] = '6' if snum[x] == '9' else '9'
            res.append(int(''.join(t)))
        return num if str(num).count('6') == 0 else max(res)
