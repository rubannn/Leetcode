class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for x in asteroids[1:]:
            if stack and stack[-1] > 0 and x < 0 and abs(x) > stack[-1]:
                stack[-1] = x
            else:
                stack.append(x)
            while len(stack) > 1 and (stack[-2] > 0 and stack[-1] < 0):
                if abs(stack[-1]) > stack[-2]:
                    x = stack.pop()
                    stack[-1] = x
                elif abs(stack[-1]) == stack[-2]:
                    stack.pop()
                    stack.pop()
                else:
                    stack.pop()

        return stack
