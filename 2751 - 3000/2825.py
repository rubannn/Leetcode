class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        for x in str1:
            nx = "a" if x == "z" else chr(ord(x) + 1)
            if i < len(str2) and str2[i] in (x, nx):
                i += 1
        return i == len(str2)


sol = Solution()
tests = [("abc", "ad", True), ("zc", "ad", True), ("ab", "d", False)]
for s1, s2, ans in tests:
    print(sol.canMakeSubsequence(s1, s2) == ans)
