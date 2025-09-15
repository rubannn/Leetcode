class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        for w in text.split():
            check = True
            for b in brokenLetters:
                if b in w:
                    check = False
                    break
            count += int(check)
        return count
