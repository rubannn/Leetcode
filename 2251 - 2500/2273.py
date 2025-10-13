from typing import List
from collections import Counter


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        p = 0
        cp = Counter(words[p])
        for i in range(1, len(words)):
            if cp == Counter(words[i]):
                continue
            p = i
            cp = Counter(words[p])
            result.append(words[p])
        return result

    def removeAnagrams2(self, words: List[str]) -> List[str]:
        hashwords = [sorted(w) for w in words]
        result = [words[0]]
        for i in range(len(words) - 1):
            if hashwords[i] != hashwords[i + 1]:
                result.append(words[i + 1])
        return result
