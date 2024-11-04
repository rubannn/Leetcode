class Solution:
    def compressedString(self, word: str) -> str:
        stack = []
        res = ""
        for c in word:
            if stack and stack[-1] != c:
                d, m = divmod(len(stack), 9)
                rest = f"{m}{stack[-1]}" if m > 0 else ""
                res += f"9{stack[-1]}" * d + rest
                stack = [c]
            else:
                stack += [c]

        if stack:
            d, m = divmod(len(stack), 9)
            rest = f"{m}{stack[-1]}" if m > 0 else ""
            res += f"9{stack[-1]}" * d + rest
        return res


tests = [
    ("abcde", "1a1b1c1d1e"),
    ("aaaaaaaaaaaaaabb", "9a5a2b"),
    ("aaaaaaaaay", "9a1y"),
]
sol = Solution()
for t, ans in tests:
    print(sol.compressedString(t) == ans)
