class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x - z) == abs(y - z):
            return 0
        elif abs(x - z) > abs(y - z):
            return 2
        return 1
