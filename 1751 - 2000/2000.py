class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            index = list(word).index(ch) + 1
            return word[:index][::-1] + word[index:]
        return word
