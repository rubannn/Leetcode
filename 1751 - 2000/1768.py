from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(f'{x}{y}' for x, y in zip_longest(word1, word2, fillvalue=''))
