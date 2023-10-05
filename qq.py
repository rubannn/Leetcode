# https://leetcode.com/problems/n-queens/
# https://leetcode.com/problems/n-queens-ii/

def queen_coords(n, x = 1, coords = [], combs = 0):
    for y in range(1, n + 1):
        check = True
        for cell in coords:
            a, b = cell
            if a == x or b == y or abs(a - x) == abs(b - y):
                check = False
                break
        if check:
            if x == n:
                # print(coords + [[x, y]])
                return combs + 1
            else:
                coords_copy = coords.copy()
                coords_copy.append([x, y])
                combs = queen_coords(n, x + 1, coords_copy, combs)
    return combs

# k = 6
# for i in range(k, k+1):
for i in range(1, 10):
  print('N = ', i, ': ', queen_coords(i), sep='')
