from string import ascii_lowercase, digits


class Solution:
    def isValid(self, word: str) -> bool:
        vowels = set("aeiou")
        consonant = set(ascii_lowercase) - vowels
        one_vowels = any(c in vowels for c in word.lower())
        one_consonant = any(c in consonant for c in word.lower())
        all_correct = all(
            c in ascii_lowercase or c in vowels or c in digits for c in word.lower()
        )
        return (len(word) > 2) and all_correct and one_vowels and one_consonant

    def isValid2(self, word: str) -> bool:
        vowels = "aeiou"
        v = c = 0
        for symb in word.lower():
            if symb.isalpha():
                if symb in vowels:
                    v += 1
                else:
                    c += 1
            elif not symb.isdigit():
                return False
        return v > 0 and c > 0 and len(word) > 2


tests = [
    ("234Adas", True),
    ("b3", False),
    ("a3$e", False),
    ("Ya$", False),
    ("IS", False),
]

sol = Solution()
for t, ans in tests:
    print(f"{t} --> {ans ==  sol.isValid2(t)}")
