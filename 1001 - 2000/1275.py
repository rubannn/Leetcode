class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[0 for _ in range(3)] for _ in range(3)]
        for i, p in enumerate(moves):
            board[p[0]][p[1]] = [1, -1][i % 2]
        sol = [sum(x) for x in board] + [sum(x) for x in zip(*board)] + \
            [sum(board[i][i] for i in range(3)), sum(board[i][2-i] for i in range(3))]
        if 3 in sol:
            return 'A'
        elif -3 in sol:
            return 'B'
        elif len(moves) < 9:
            return 'Pending'
        return 'Draw'
