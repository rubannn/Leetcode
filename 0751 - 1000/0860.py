class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dc = {5: 0, 10: 0, 20: 0}
        for c in bills:
            dc[c] += 1
            c -= 5
            for m in [10, 5]:
                while c >= m and dc[m] > 0:
                    dc[m] -= 1
                    c -= m
            if c != 0:
                return False
        return True
