def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    for x in range(m):
        for y in range(n):
            if x + y + obstacleGrid[x][y] == 0:
                obstacleGrid[x][y] = 1
            elif obstacleGrid[x][y] == 1:
                obstacleGrid[x][y] = '*'
            elif x == 0:
                if y > 0:
                    if obstacleGrid[x][y-1] == '*':
                        obstacleGrid[x][y] = 0
                    else:
                        obstacleGrid[x][y] = obstacleGrid[x][y-1]
            elif y == 0:
                if x > 0:
                    if obstacleGrid[x-1][y] == '*':
                        obstacleGrid[x][y] = 0
                    else:
                        obstacleGrid[x][y] = obstacleGrid[x-1][y]

    for x in range(1, m):
        for y in range(1, n):
            if obstacleGrid[x][y] != '*':
                a = 0 if obstacleGrid[x-1][y] == '*' else obstacleGrid[x-1][y]
                b = 0 if obstacleGrid[x][y-1] == '*' else obstacleGrid[x][y-1]
                obstacleGrid[x][y] = a + b
    return obstacleGrid[m-1][n-1] if obstacleGrid[m-1][n-1] != '*' and obstacleGrid[0][0] != '*' else 0
