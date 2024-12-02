class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) > 1:
            return True
        s = set(arr)
        for x in s:
            if x % 2 == 0 and x // 2 in s and x != 0:
                return True
        return False
