import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [x for x in itertools.combinations(range(1, n + 1), k)]
