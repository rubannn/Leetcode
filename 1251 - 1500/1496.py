class Solution:
    def isPathCrossing(self, path: str) -> bool:
        p = {(0, 0)}
        x = y = 0
        for c in path:
            if c == "N":
                y += 1
            elif c == "S":
                y -= 1
            elif c == "E":
                x += 1
            else:
                x -= 1
            if (x, y) in p:
                return True
            p.add((x, y))
        return False
