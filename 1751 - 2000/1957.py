class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) > 1 and stack[-1] == stack[-2] == c:
                continue
            else:
                stack.append(c)
        return "".join(stack)
