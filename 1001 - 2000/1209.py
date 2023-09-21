class Solution:
    # variant 1. Time = 95 ms, Memory = 28.8 MB
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1].get(c, 0) > 0:
                stack[-1][c] += 1
                if stack[-1][c] == k: stack.pop()
            else:
                stack.append({c : 1})
        return ''.join(k*v for s in stack for k, v in s.items())

    # variant 2. Time = 6766 ms, Memory = 18.3 MB
    def removeDuplicates2(self, s: str, k: int) -> str:
        stack = ['~'] * k
        for c in s:
            if stack and c == stack[-1] and stack[-k+1:] == [c]*(k-1):
                stack = stack[:-k+1]
            else:
                stack.append(c)
        return ''.join(stack)[k:]
