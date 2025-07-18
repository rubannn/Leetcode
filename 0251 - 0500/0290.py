from collections import Counter


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w = s.split()
        if sorted(Counter(pattern).values()) != sorted(Counter(w).values()):
            return False

        dc = dict()
        for i, c in enumerate(pattern):
            if c in dc.keys():
                if dc[c] != w[i]:
                    return False
            else:
                dc[c] = w[i]
        return True


tests = [
    ("abba", "dog cat cat dog", True),
    ("abba", "dog cat cat fish", False),
    ("aaaa", "dog cat cat dog", False),
    ("aba", "dog cat cat", False),
    ("abab", "dog cat cat dog", False),
    ("abba", "dog dog dog dog", False),
    ("aba", "cat cat cat dog", False),
]

sol = Solution()
for pattern, s, ans in tests:
    print(pattern, s, ans == sol.wordPattern(pattern, s))
