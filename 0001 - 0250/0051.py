# https://oeis.org/A000170

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def queens(n, boards, x = 1, coords = []):
            for y in range(1, n + 1):
                check = True
                for cell in coords:
                    a, b = cell
                    if a == x or b == y or abs(a - x) == abs(b - y):
                        check = False
                        break
                if check:
                    if x == n:
                        boards.append(coords + [[x, y]])
                        return boards
                    else:
                        coords_copy = coords.copy()
                        coords_copy.append([x, y])
                        queens(n, boards, x + 1, coords_copy)
            return boards
        boards, res = [], []
        for board in queens(n, boards):
            res.append([''.join('Q' if i == y - 1 else '.' for i in range(n)) for _, y in board])
        return res
