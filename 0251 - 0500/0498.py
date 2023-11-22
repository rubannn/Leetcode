class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diags = dict()
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if (i + j) % 2:
                    diags[i + j] = diags.get(i + j, []) + [mat[i][j]]
                else:
                    diags[i + j] = [mat[i][j]] + diags.get(i + j, [])

        res = []
        for k in sorted(diags.keys()):
            res += diags[k]
        return res
