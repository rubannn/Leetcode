def spiralMatrixIII(rows: int,  cols: int,  rStart: int,  cStart: int) -> list[list[int]]:
    v = ((0,  1),  (1,  0),  (0,  -1),  (-1,  0))
    x,  y = rStart,  cStart
    res = [[x,  y]]
    p,  step = 0,  1
    while len(res) < rows * cols:
        for _ in range(2):
            for _ in range(step):
                vx,  vy = v[p]
                x += vx
                y += vy
                if (0 <= x < rows) and (0 <= y < cols):
                    res.append([x,  y])
            p = (p + 1) % 4
        step += 1
    return res


r = 1
c = 4
rS = 0
cS = 0
out = [[0, 0], [0, 1], [0, 2], [0, 3]]
print(spiralMatrixIII(r,  c,  rS,  cS) == out)

r = 5
c = 6
rS = 1
cS = 4
out = [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5],
       [3, 5], [3, 4], [3, 3], [3, 2], [2, 2], [1, 2], [0, 2], [4, 5], [4, 4],
       [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [4, 0], [3, 0],
       [2, 0], [1, 0], [0, 0]]
print(spiralMatrixIII(r,  c,  rS,  cS) == out)
