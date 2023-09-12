class Solution:
    def minDeletions(self, s: str) -> int:
        count_list = sorted([s.count(c) for c in set(s)])
        count_set = set()
        res = 0
        for c in count_list:
            while c in count_set and c > 0:
                c -= 1
                res += 1
            count_set.add(c)
        return res


sol = Solution

s = "aab"
res = 0
print(sol.minDeletions(sol, s) == res)

s = "aaabbbcc"
res = 2
print(sol.minDeletions(sol, s) == res)

s = "ceabaacb"
res = 2
print(sol.minDeletions(sol, s) == res)
