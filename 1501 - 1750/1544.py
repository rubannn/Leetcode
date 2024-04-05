class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
                stack = stack[:-1]
            else:
                stack.append(c)
        return "".join(stack)
