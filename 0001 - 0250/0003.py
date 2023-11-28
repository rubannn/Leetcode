class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_symb = dict()
        start = 0
        len_substr = 0

        for i, c in enumerate(s):
            if (c in last_symb) and (last_symb[c] >= start):
                start = last_symb[c] + 1
            else:
                len_substr = max(len_substr, i - start + 1)
            last_symb[c] = i
        return len_substr
