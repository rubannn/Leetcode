class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        k = 0
        tmat = list(zip(*mat))
        for a in mat:
            if sum(a) == 1:
                for i, el in enumerate(a):
                    if el == 1 == sum(tmat[i]):
                        k += 1
        return k
