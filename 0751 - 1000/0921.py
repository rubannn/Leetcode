class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            if stack:
                if stack[-1] == "(" and c == ")":
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return len(stack)
