class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        res = 0
        for c in s:
            if c == "(":
                stack.append("(")
            elif c == ")":
                res = max(res, len(stack))
                stack = stack[:-1]
        return res
