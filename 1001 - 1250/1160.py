from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        res = 0
        for w in words:
            dc_w = Counter(w)
            if all(k in chars and dc_w[k] <= chars[k] for k in dc_w):
                res += len(w)
        return res
