class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        tr, tc = len(mat), len(mat[0])
        if tr * tc == r * c:
            tmp = [y for x in mat for y in x]
            return [tmp[i * c: (i + 1) * c] for i in range(r)]
        return mat
