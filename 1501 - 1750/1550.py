class Solution:
    # variant 1
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] % 2 == arr[i + 1] % 2 == arr[i + 2] % 2 == 1:
                return True
        return False

    # variant 2
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd = 0
        for x in arr:
            if x % 2 == 1:
                odd += 1
                if odd == 3:
                    return True
            else:
                odd = 0
        return False
