class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def erase_ship(r, c, grid):
            if (r < 0 or r > len(board)-1) or (c < 0 or c > len(board[0])-1)\
                or board[r][c] != 'X':
                return
            grid[r][c] = '.'
            erase_ship(r + 1, c, board)
            erase_ship(r - 1, c, board)
            erase_ship(r, c + 1, board)
            erase_ship(r, c - 1, board)

        res = 0
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'X':
                    res += 1
                    erase_ship(x, y, board)
        return res
