class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = sorted(s, key=lambda x: order.index(x) if x in order else -1)
        return "".join(res)
