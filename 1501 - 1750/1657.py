class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        c1 = Counter(word1)
        c2 = Counter(word2)
        v1 = sorted(c1.values())
        v2 = sorted(c2.values())
        return v1 == v2 and sorted(c1.keys()) == sorted(c2.keys())
