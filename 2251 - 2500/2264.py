class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = []
        stack = ['']
        for c in num:
            if stack[-1] != c:
                stack = [c]
            else:
                stack.append(c)
                if len(stack) == 3:
                    good.append(''.join(stack))
                    stack = ['']
        return sorted(good)[-1] if good else ''
