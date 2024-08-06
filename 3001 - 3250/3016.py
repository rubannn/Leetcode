from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        dc = sorted(Counter(word).values(), reverse=True)
        res, price = 0, 1
        while dc:
            res += sum(dc[:8]) * price
            price += 1
            dc = dc[8:]
        return res
