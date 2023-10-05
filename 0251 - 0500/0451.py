class Solution:
    def frequencySort(self, s: str) -> str:
        s = sorted([(x, y) for x, y in Counter(s).items()], key=lambda x: -x[1])
        return ''.join(t[0]*t[1] for t in s)
