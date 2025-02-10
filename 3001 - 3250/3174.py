class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                stack = stack[:-1]
            else:
                stack.append(c)
        return "".join(stack)
