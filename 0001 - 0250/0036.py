class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits = '123456789'
        # Check rows
        for row in board:
            dgt = [x for x in row if x in digits]
            if len(set(dgt)) != len(dgt):
                return False

        # Check columns
        for col in range(9):
            dgt = [board[i][col] for i in range(9) if board[i][col] in digits]
            if len(set(dgt)) != len(dgt):
                return False

        # Check boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                dgt = [board[i][j] for i in range(row, row+3) for j in range(col, col+3) if board[i][j] in digits]
                if len(set(dgt)) != len(dgt):
                    return False
        return True
