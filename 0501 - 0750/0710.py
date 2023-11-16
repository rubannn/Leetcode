import random

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.whitelist = dict()
        self.N = n - len(blacklist)
        mx = n - 1
        for x in blacklist:
            if x >= self.N:
                continue
            while mx in blacklist:
                mx -= 1
            self.whitelist[x] = mx
            mx -= 1

    def pick(self) -> int:
        v = random.randint(0, self.N-1)
        return self.whitelist.get(v, v)
