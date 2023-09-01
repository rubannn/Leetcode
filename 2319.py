def checkXMatrix(grid: list[list[int]]) -> bool:
    n = len(grid)
    diags = notdiags = True
    for i in range(n):
        for j in range(n):
            if (i == j) or (i + j == n - 1):
                diags = diags and (grid[i][j] != 0)
            else:
                notdiags = notdiags and (grid[i][j] == 0)
    return diags and notdiags
