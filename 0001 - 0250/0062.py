# variant 1
def uniquePaths(m: int, n: int) -> int:
    board = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        board[0][i] = 1
    for i in range(m):
        board[i][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            board[i][j] = board[i - 1][j] + board[i][j - 1]
    return board[m-1][n-1]

# variant 2
def uniquePaths(self, m: int, n: int) -> int:
    board = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            board[i][j] = board[i - 1][j] + board[i][j - 1]
    return board[m-1][n-1]


print(uniquePaths(13, 13))
