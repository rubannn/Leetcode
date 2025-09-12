class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = len([c for c in s if c in "aeiou"])
        return vowels > 0
