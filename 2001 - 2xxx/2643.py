class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        arr = [sum(x) for x in mat]
        return [arr.index(max(arr)), max(arr)]
