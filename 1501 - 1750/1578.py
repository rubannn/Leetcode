class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        stack_c, stack_t = [], []
        for c, t in zip(colors, neededTime):
            if not stack_c or c == stack_c[-1]:
                stack_c.append(c)
                stack_t.append(t)
            else:
                res += sum(stack_t) - max(stack_t)
                stack_c = [c]
                stack_t = [t]
        if len(stack_c) > 1:
            res += sum(stack_t) - max(stack_t)
        return res
