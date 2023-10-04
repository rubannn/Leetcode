class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mn = min(len(w) for w in strs)
        prefix = ''
        for i in range(mn):
            char = strs[0][i]
            if all(char == st[i] for st in strs):
                prefix += char
            else:
                return prefix
        return prefix
