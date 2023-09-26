class Solution:
    def isValid(self, s: str) -> bool:
        L, R = "({[", ")}]"
        stack = []
        for c in s:
            if c in L:
                stack.append(c)
            elif stack and L.find(stack[-1]) == R.find(c):
                stack = stack[:-1]
            else:
                return False
        return stack == []
