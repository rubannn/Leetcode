class Solution:
    def totalNQueens(self, n: int) -> int:
        def queens(n, x = 1, coords = [], combs = 0):
            for y in range(1, n + 1):
                check = True
                for cell in coords:
                    a, b = cell
                    if a == x or b == y or abs(a - x) == abs(b - y):
                        check = False
                        break
                if check:
                    if x == n:
                        return combs + 1
                    else:
                        coords_copy = coords.copy()
                        coords_copy.append([x, y])
                        combs = queens(n, x + 1, coords_copy, combs)
            return combs
        return queens(n)
