from collections import Counter
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = []
        dc = Counter(digits)
        for x in range(100, 999, 2):
            check = True
            for k, v in Counter(map(int, str(x))).items():
                check = check and dc.get(k, 0) >= v
            if check:
                result.append(x)
        return result
