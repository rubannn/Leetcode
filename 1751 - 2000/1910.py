class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part = list(part)
        n = len(part)
        for c in s:
            stack += [c]
            if stack and stack[-n:] == part:
                stack = stack[:-n]
        return "".join(stack)
