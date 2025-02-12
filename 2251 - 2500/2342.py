class Solution(object):
    def maximumSum(self, nums):
        dc = defaultdict(list)
        for n in nums:
            sm = sum(int(d) for d in str(n))
            dc[sm].append(n)
        mx = -1
        for v in dc.values():
            if len(v) > 1:
                v.sort(reverse=True)
                mx = max(mx, sum(v[:2]))
        return mx
