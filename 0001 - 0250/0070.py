def climbStairs(self, n: int) -> int:
    step = [1, 2]
    for i in range(2, n):
        step.append(step[i-2] + step[i-1])
    return step[n-1]
