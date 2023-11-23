class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        mx = (R - L) * min(height[L], height[R])
        while L < R:
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
            mx = max(mx, (R - L) * min(height[L], height[R]))
        return  mx
